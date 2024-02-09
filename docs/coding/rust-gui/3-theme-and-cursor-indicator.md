# Theme and Cursor Indicator

Keywords: `iced::widget::column`, `iced::widget::row`, `iced::widget::horizontal_space`, `iced::Theme`, `iced::Length`

本节将窗口设置为暗色调，并且通过`text`控件显示光标的位置。

## 设置窗口主题

窗口主题通过`theme`函数设置，定义主题风格的类为`iced::Theme`，`Light`和`Dark`分别表示亮色和暗色调。

```rust
use iced::Theme

// ...

impl Sandbox for Editor {
    // ...

    fn theme(&self) -> iced::Theme {
        iced::Theme::Dark // Set the window theme to dark
    }
}
```

## 读取文件内容

在程序启动时，我们可以设置一个默认的文件内容，此处可以使用`include_str!`宏在编译时读取文件内容并用于初始化文本框的状态。

```rust
impl Sandbox for Editor {
    // ...

    fn new() -> Self {
        Self {
            content: text_editor::Content::with(include_str!("main.rs"))
        }
    }
}
```

## 显示光标位置

文本框的光标位置可以通过`self.content`状态的`cursor_position`方法获取，返回一个包含光标位置（从0开始）的元组，可以根据光标位置创建一个`text`控件用于显示。

* 通过`column!`宏创建一个列布局，上边包含输入文本框，下边包含光标位置显示。
* 通过`row!`宏创建一个行布局，结合`Length::Fill`把光标位置压缩到右侧对齐。

```rust
use iced::widget::{column, row, horizontal_space, text};
use iced::Length;

// ...

impl Sandbox for Editor {
    // ...

    fn view(&self) -> Element<'_, Message> {
        let editor = text_editor(&self.content);
        // Query cursor position
        let cursor_indicator = {
            let (line, column) = self.content.cursor_position();

            text(format!("Line: {}, Column: {}", line + 1, column + 1))
        };
        let status_bar = row![horizontal_space(Length::Fill), cursor_indicator];

        container(column![editor, status_bar].spacing(10)).padding(10).into()
    }
}
```

以下为完整的`main.rs`文件内容：

{{ read_code_from_file('docs/coding/rust-gui/source/3.rs') }}
