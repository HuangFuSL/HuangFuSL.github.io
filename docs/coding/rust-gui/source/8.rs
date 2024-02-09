use std::io;
use std::path::{Path, PathBuf};
use std::sync::Arc;

use iced::{executor, theme, Application, Command, Element, Font, Length, Settings, Theme};
use iced::widget::{button, column, container, horizontal_space, row, text, text_editor, tooltip};

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
    error: Option<Error>
}

#[derive(Debug, Clone)]
enum Message {
    EditorEdit(text_editor::Action),
    FileOpened(Result<(PathBuf, Arc<String>), Error>),
    FileSaved(Result<PathBuf, Error>),
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
                path: None
            },
            Command::perform(
            load_file(format!("{}/src/main.rs", env!("CARGO_MANIFEST_DIR"))),
            Message::FileOpened
            )
        )
    }

    fn title(&self) -> String {
        String::from("A text editor")
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
        let editor = text_editor(&self.content).on_edit(Message::EditorEdit);
        let controls = row![
            toolbar_button("New", Message::NewButtonPressed),
            toolbar_button("Open", Message::OpenButtonPressed),
            toolbar_button("Save", Message::SaveButtonPressed)
        ].spacing(10);

        // Query cursor position
        let path_indicator = if let Some(error) = &self.error {
            match error {
                Error::DialogClosed => text("Dialog closed"),
                Error::IO(kind) => text(format!("I/O error: {:?}", kind))
            }
        } else {
            let path_text = match &self.path {
                None => String::from("New file"),
                Some(path) => path.to_string_lossy().to_string()
            };
            let suffix = if self.modified { "*" } else { "" };
            text(format!("{}{}", path_text, suffix))
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
        Theme::Dark
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

fn toolbar_button<'a>(description: &str, callback: Message) -> Element<'a, Message> {
    let font = Font::with_name("editor-icon");
    let lower = description.to_lowercase();
    let icon = text(match lower.as_str() {
        "new" => '\u{E800}',
        "open" => '\u{F115}',
        "save" => '\u{E801}',
        _ => ' '
    }).font(font);

    tooltip(
        button(container(icon)
            .width(30)  // Set the width of the button
            .center_x() // Center the icon
        ).on_press(callback),
        description, tooltip::Position::FollowCursor
    ).style(theme::Container::Box).into()
}

#[derive(Debug, Clone)]
enum Error {
    DialogClosed,
    IO(io::ErrorKind)
}
