# Button Prettify

在本节中，我们把按钮的文本替换为图标，并且添加文本悬浮提示。

首先需要创建包含图标的字体，可以在[Fontello](https://fontello.com/)上选择图标，然后下载字体文件。将`ttf`版本的字体存放在项目下的`fonts/editor-icon.ttf`中。

然后在代码中加载字体文件，在`iced::Settings`中添加字体：

```rust
fn main() -> iced::Result {
    Editor::run(Settings {
        fonts: vec![include_bytes!("../fonts/editor-icon.ttf").as_slice().into()],
        ..Default::default() // Expand the default settings
    })
}
```

加载字体后，可以将按钮的输入文本替换为图标，使用`text`控件创建图标。在网页中可以读取到对应新建、打开、保存的Unicode编码分别为`\u{E800}`、`\u{F115}`、`\u{E801}`。

```rust
fn toolbar_button<'a>(description: &str, callback: Message) -> Element<'a, Message> {
    let font = Font::with_name("editor-icon");

    let icon = text(match description {
        "new" => '\u{E800}',
        "open" => '\u{F115}',
        "save" => '\u{E801}',
        _ => ' '
    }).font(font);

    button(container(icon)
        .width(30)  // Set the width of the button
        .center_x() // Center the icon
    ).on_press(callback).into()
}
```

使用`button_icon`函数替换按钮原本的输入

```rust
// ... In `view` function
let controls = row![
    toolbar_button("new", Message::NewButtonPressed),
    toolbar_button("open", Message::OpenButtonPressed),
    toolbar_button("save", Message::SaveButtonPressed)
].spacing(10);
```

最后，实现悬浮提示，使用`Tooltip`控件包裹按钮即可。为了美观，可以通过`style`方法设置提示框的样式。

```rust
// ... In `view` function
let controls = row![
    toolbar_button("New", Message::NewButtonPressed),
    toolbar_button("Open", Message::OpenButtonPressed),
    toolbar_button("Save", Message::SaveButtonPressed)
].spacing(10);

// ... In the outer scope
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
    ).style(theme::Container::Box).into() // Set the style of the tooltip
}
```

以下为完整的`main.rs`文件内容：

{{ read_code_from_file('docs/coding/rust-gui/source/8.rs') }}
