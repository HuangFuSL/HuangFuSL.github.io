# Syntax Highlighting

Keywords: `iced::widget::pick_list`

本节添加代码编辑器的语法高亮功能。

首先，修改编辑器的默认字体为等宽字体，以便更好地显示代码。

```rust hl_lines="3"
// ... In `view` function
let editor = text_editor(&self.content)
    .on_edit(Message::EditorEdit)
    .font(Font::MONOSPACE);
```

接下来，添加高亮处理的逻辑。高亮功能由`iced`的`highlighter`模块提供，需要在`Cargo.toml`中添加依赖。

```toml
[dependencies]
iced = { git = "https://github.com/iced-rs/iced.git", rev = "refs/tags/text-editor", features = [ "highlighter" ] }
```

在文本框的`highlight`方法中设置高亮。`highlight`方法需要指定配色方案`theme`和语法`extension`。`extension`可以根据文件路径的后缀名自动识别，如果没有后缀名，则默认为`rs`。

```rust hl_lines="3 4 5 6 7 8 9 10 11 12 13 14"
let editor = text_editor(&self.content)
    .on_edit(Message::EditorEdit)
    .highlight::<Highlighter>( // use iced::highlighter::Highlighter
        highlighter::Settings {
            theme: highlighter::Theme::SolarizedDark, // Set the theme
            extension: self.path
                .as_ref()
                .and_then(|path| path.extension()?.to_str())
                .unwrap_or("rs") // If extension is not found, use `rs`
                .to_string()
        }, |highlighter, _theme| {
            highlighter.to_format()
        }
    )
    .font(Font::MONOSPACE);
```

接下来添加高亮风格的选择功能。首先在`Editor`中添加`theme`状态作为当前的主题，并且设置初始化状态。

```rust
struct Editor {
    // ...
    theme: highlighter::Theme
}
// ... In `new` function
Self {
    // ...
    theme: highlighter::Theme::SolarizedDark
},
// ... In `view` function
highlighter::Settings {
    theme: self.theme,
    // ...
}
```

添加一个`pick_list`控件用于选择高亮风格，`pick_list`需要设置选项、当前选中项和触发事件。每次更新时都会以选中项为参数触发事件。

```rust hl_lines="6"
let controls = row![
    toolbar_button("New", Message::NewButtonPressed),
    toolbar_button("Open", Message::OpenButtonPressed),
    toolbar_button("Save", Message::SaveButtonPressed),
    horizontal_space(Length::Fill),
    pick_list(highlighter::Theme::ALL, Some(self.theme), Message::ThemeChanged)
].spacing(10);
```

同时更新`ThemeChanged`事件的处理逻辑

```rust
// ... In `update` function
Message::ThemeChanged(theme) => {
    self.theme = theme;
    Command::none()
}
```

内置的部分主题并不是暗色主题，需要添加一个根据主题的亮暗切换窗口配色的功能：

```rust
// ... In `impl Application for Editor`
fn theme(&self) -> Theme {
    if self.theme.is_dark() {
        Theme::Dark
    } else {
        Theme::Light
    }
}
```

以下为完整的`main.rs`文件内容：

{{ read_code_from_file('docs/coding/rust-gui/source/9.rs') }}
