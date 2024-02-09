use iced::{Element, Sandbox, Settings};
use iced::widget::text;

fn main() -> iced::Result {
    Editor::run(Settings::default())
}

struct Editor;

#[derive(Debug)]
enum Message {}

impl Sandbox for Editor {
    type Message = Message; // Define the type of messages
    fn new() -> Self {
        Self
    }

    fn title(&self) -> String {
        String::from("A text editor")
    }

    fn update(&mut self, message: Message) {
        // Handle messages here
        match message {}
    }

    fn view(&self) -> Element<'_, Message> {
        // Create the user interface here
        text("Hello, world!").into()
    }
}
