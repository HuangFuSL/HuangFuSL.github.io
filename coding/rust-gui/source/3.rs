use iced::{Theme, Element, Sandbox, Settings, Length};
use iced::widget::{column, container, horizontal_space, row, text, text_editor};

fn main() -> iced::Result {
    Editor::run(Settings::default())
}

struct Editor {
    content: text_editor::Content
}

#[derive(Debug, Clone)]
enum Message {
    EditorEdit(text_editor::Action)
}

impl Sandbox for Editor {
    type Message = Message; // Define the type of messages

    fn new() -> Self {
        Self {
            content: text_editor::Content::with(include_str!("main.rs"))
        }
    }

    fn title(&self) -> String {
        String::from("A text editor")
    }

    fn update(&mut self, message: Message) {
        // Handle messages here
        match message {
            Message::EditorEdit(action) => {
                self.content.edit(action);
            }
        }
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
