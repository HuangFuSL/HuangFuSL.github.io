use iced::{Element, Sandbox, Settings};
use iced::widget::{text_editor, container};

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
            content: text_editor::Content::new()
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
        container(editor).padding(10).into()
    }
}
