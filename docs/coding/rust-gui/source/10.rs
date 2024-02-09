use std::io;
use std::path::{Path, PathBuf};
use std::sync::Arc;

use iced::{executor, keyboard, theme, Application, Command, Element, Font, Length, Settings, Subscription, Theme};
use iced::highlighter::{self, Highlighter};
use iced::widget::{button, column, container, horizontal_space, pick_list, row, text, text_editor, tooltip};

fn main() -> iced::Result {
    Editor::run(Settings {
        fonts: vec![include_bytes!("../fonts/editor-icon.ttf").as_slice().into()],
        ..Default::default()
    })
}

struct Editor {
    path: Option<PathBuf>,
    content: text_editor::Content,
    modified: bool,
    error: Option<Error>,
    theme: highlighter::Theme
}

#[derive(Debug, Clone)]
enum Message {
    EditorEdit(text_editor::Action),
    FileOpened(Result<(PathBuf, Arc<String>), Error>),
    FileSaved(Result<PathBuf, Error>),
    ThemeChanged(highlighter::Theme),
    NewButtonPressed,
    OpenButtonPressed,
    SaveButtonPressed
}

impl Application for Editor {
    type Message = Message; // Define the type of messages
    type Theme = Theme;
    type Executor = executor::Default; // Engine for running async tasks
    type Flags = ();

    fn new(_flags: Self::Flags) -> (Self, Command<Message>) {
        (
            Self {
                content: text_editor::Content::new(),
                error: None,
                modified: false,
                path: None,
                theme: highlighter::Theme::SolarizedDark
            },
            Command::perform(
            load_file(format!("{}/src/main.rs", env!("CARGO_MANIFEST_DIR"))),
            Message::FileOpened
            )
        )
    }

    fn title(&self) -> String {
        let path_text = match &self.path {
            None => String::from("New file"),
            Some(path) => path.to_string_lossy().to_string()
        };
        let suffix = if self.modified { "*" } else { "" };
        format!("{}{}", path_text, suffix)
    }

    fn subscription(&self) -> Subscription<Message> {
        keyboard::on_key_press(|keycode, modifier| {
            match (keycode, modifier) {
                (keyboard::KeyCode::S, keyboard::Modifiers::COMMAND) => {
                    Some(Message::SaveButtonPressed)
                },
                (keyboard::KeyCode::O, keyboard::Modifiers::COMMAND) => {
                    Some(Message::OpenButtonPressed)
                },
                (keyboard::KeyCode::N, keyboard::Modifiers::COMMAND) => {
                    Some(Message::NewButtonPressed)
                },
                _ => None
            }
        })
    }

    fn update(&mut self, message: Message) -> Command<Message> {
        // Handle messages here
        match message {
            Message::EditorEdit(action) => {
                match &action {
                    text_editor::Action::Edit(_) => self.modified = true,
                    _ => {}
                }
                self.content.edit(action);
                Command::none()
            },
            Message::FileOpened(Ok((path, result))) => {
                self.path = Some(path);
                self.modified = false;
                self.content = text_editor::Content::with(&result);
                Command::none()
            },
            Message::FileSaved(Ok(path)) => {
                self.path = Some(path);
                self.modified = false;
                Command::none()
            },
            Message::FileOpened(Err(error)) | Message::FileSaved(Err(error)) => {
                self.error = Some(error);
                Command::none()
            },
            Message::ThemeChanged(theme) => {
                self.theme = theme;
                Command::none()
            },
            Message::NewButtonPressed => {
                self.content = text_editor::Content::new();
                self.error = None;
                self.path = None;
                self.modified = false;
                Command::none()
            },
            Message::OpenButtonPressed => {
                self.modified = false;
                Command::perform(pick_file(), Message::FileOpened)
            },
            Message::SaveButtonPressed => {
                let content = self.content.text();
                match self.modified {
                    false => Command::none(),
                    true => Command::perform(
                        save_file(self.path.clone(), content),
                        Message::FileSaved
                    )
                }
            }
        }
    }

    fn view(&self) -> Element<'_, Message> {
        // Create the user interface here
        let editor = text_editor(&self.content)
            .on_edit(Message::EditorEdit)
            .highlight::<Highlighter>(
                highlighter::Settings {
                    theme: self.theme,
                    extension: self.path
                        .as_ref()
                        .and_then(|path| path.extension()?.to_str())
                        .unwrap_or("rs")
                        .to_string()
                }, |highlighter, _theme| {
                    highlighter.to_format()
                }
            )
            .font(Font::MONOSPACE);
        let controls = row![
            toolbar_button("New", Some(Message::NewButtonPressed)),
            toolbar_button("Open", Some(Message::OpenButtonPressed)),
            toolbar_button("Save", if self.modified { Some(Message::SaveButtonPressed) } else { None }),
            horizontal_space(Length::Fill),
            pick_list(highlighter::Theme::ALL, Some(self.theme), Message::ThemeChanged)
        ].spacing(10);

        // Query cursor position
        let path_indicator = if let Some(error) = &self.error {
            match error {
                Error::DialogClosed => text("Dialog closed"),
                Error::IO(kind) => text(format!("I/O error: {:?}", kind))
            }
        } else {
            text(self.title())
        };
        let cursor_indicator = {
            let (line, column) = self.content.cursor_position();

            text(format!("Line: {}, Column: {}", line + 1, column + 1))
        };
        let status_bar = row![
            path_indicator,
            horizontal_space(Length::Fill),
            cursor_indicator
        ];

        container(column![controls, editor, status_bar].spacing(10)).padding(10).into()
    }

    fn theme(&self) -> Theme {
        if self.theme.is_dark() {
            Theme::Dark
        } else {
            Theme::Light
        }
    }
}

async fn pick_file() -> Result<(PathBuf, Arc<String>), Error> {
    let file_handle = rfd::AsyncFileDialog::new()
        .set_title("Choose a text file...")
        .pick_file()
        .await
        .ok_or(Error::DialogClosed)?;
    load_file(file_handle.path()).await
}

async fn load_file(path: impl AsRef<Path>) -> Result<(PathBuf, Arc<String>), Error> {
    let content = tokio::fs::read_to_string(path.as_ref())
        .await
        .map(Arc::new)
        .map_err(|err| err.kind())
        .map_err(Error::IO);
    content.and_then(|content| Ok((path.as_ref().to_path_buf(), content)))
}

async fn save_file(path: Option<PathBuf>, content: String) -> Result<PathBuf, Error> {
    let path = if let Some(path) = path {
        path
    } else {
        rfd::AsyncFileDialog::new()
            .set_title("Save the file to...")
            .save_file()
            .await
            .ok_or(Error::DialogClosed)?
            .path()
            .to_path_buf()
    };
    tokio::fs::write(&path, content)
        .await
        .map_err(|err| err.kind())
        .map_err(Error::IO)
        .map(|_| path)
}

fn toolbar_button<'a>(description: &str, callback: Option<Message>) -> Element<'a, Message> {
    let font = Font::with_name("editor-icon");
    let lower = description.to_lowercase();
    let icon = text(match lower.as_str() {
        "new" => '\u{E800}',
        "open" => '\u{F115}',
        "save" => '\u{E801}',
        _ => ' '
    }).font(font);
    let is_disabled = callback.is_none();
    tooltip(
        button(container(icon)
            .width(30)  // Set the width of the button
            .center_x() // Center the icon
        ).on_press_maybe(callback).style(
            if is_disabled {
                theme::Button::Secondary
            } else {
                theme::Button::Primary
            }
        ),
        description, tooltip::Position::FollowCursor
    ).style(theme::Container::Box).into()
}

#[derive(Debug, Clone)]
enum Error {
    DialogClosed,
    IO(io::ErrorKind)
}
