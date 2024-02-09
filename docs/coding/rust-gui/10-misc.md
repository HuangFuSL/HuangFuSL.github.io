# Miscellaneous

本节添加一些额外功能。

首先，当文件没有被修改时，可以设置禁用保存按钮。这样可以避免用户误操作。在`on_press_maybe`中传入`None`即可。同时，可以根据文件的修改情况设置按钮的样式。

```rust hl_lines="10 15 16 17 18 19 20 21"
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
```

同时修改`toolbar_button`的调用。

```rust hl_lines="5"
// ... In `view` function
let controls = row![
    toolbar_button("New", Some(Message::NewButtonPressed)),
    toolbar_button("Open", Some(Message::OpenButtonPressed)),
    toolbar_button("Save", if self.modified { Some(Message::SaveButtonPressed) } else { None }),
    horizontal_space(Length::Fill),
    pick_list(highlighter::Theme::ALL, Some(self.theme), Message::ThemeChanged)
].spacing(10);
```

我们可以添加不同的快捷键，以方便用户操作。

```rust
// In `impl Application for Editor`
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
```

这样，用户可以使用`Command + S`来保存文件，`Command + O`来打开文件，`Command + N`来新建文件。

文件的标题栏通常显示文件路径，可以和左下角的状态栏保持同步。

```rust
// ... In `impl Application for Editor`
fn title(&self) -> String {
    let path_text = match &self.path {
        None => String::from("New file"),
        Some(path) => path.to_string_lossy().to_string()
    };
    let suffix = if self.modified { "*" } else { "" };
    format!("{}{}", path_text, suffix)
}

// ... In `view` function
let path_indicator = if let Some(error) = &self.error {
    match error {
        Error::DialogClosed => text("Dialog closed"),
        Error::IO(kind) => text(format!("I/O error: {:?}", kind))
    }
} else {
    text(self.title())
};
```

以下为完整的`main.rs`文件内容：

{{ read_code_from_file('docs/coding/rust-gui/source/10.rs') }}
