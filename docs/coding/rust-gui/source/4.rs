use std::io;
use std::path::Path;
use std::sync::Arc;

use iced::{executor, Application, Command, Element, Length, Settings, Theme};
use iced::widget::{column, container, horizontal_space, row, text, text_editor};

fn main() -> iced::Result {
    Editor::run(Settings::default())
}

struct Editor {
    content: text_editor::Content,
    error: Option<io::ErrorKind>
}

#[derive(Debug, Clone)]
enum Message {
    EditorEdit(text_editor::Action),
    FileOpened(Result<Arc<String>, io::ErrorKind>)
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
                error: None
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
                self.content.edit(action);
            },
            Message::FileOpened(Ok(result)) => {
                self.content = text_editor::Content::with(&result);
            },
            Message::FileOpened(Err(error)) => {
                self.error = Some(error);
            }
        };

        Command::none()
    }

    fn view(&self) -> Element<'_, Message> {
        // Create the user interface here
        let editor = text_editor(&self.content).on_edit(Message::EditorEdit);

        // Query cursor position
        let cursor_indicator = {
            let (line, column) = self.content.cursor_position();

            text(format!("Line: {}, Column: {}", line + 1, column + 1))
        };
        let status_bar = row![horizontal_space(Length::Fill), cursor_indicator];

        container(column![editor, status_bar].spacing(10)).padding(10).into()
    }

    fn theme(&self) -> Theme {
        Theme::Dark
    }
}

async fn load_file(path: impl AsRef<Path>) -> Result<Arc<String>, io::ErrorKind> {
    tokio::fs::read_to_string(path)
        .await
        .map(Arc::new)
        .map_err(|err| err.kind())
}
