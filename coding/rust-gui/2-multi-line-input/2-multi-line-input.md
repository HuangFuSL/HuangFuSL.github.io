# Add Multi-line Input

Keywords: `iced::widget::text_editor`, `iced::widget::container`.

本节我们将`text`控件替换为`text_editor`控件，以实现多行文本的输入。

!!! warning "iced库版本"

    `text_editor`控件尚未在正式版本中发布，需要使用`git`仓库中的代码。

    ```toml
    [dependencies]
    iced = { git = "https://github.com/iced-rs/iced.git", rev = "refs/tags/text-editor" }
    ```

首先，将引入的`iced::widget::text`替换为`iced::widget::text_editor`。`text_editor`是有状态的，需要在`new`中初始化空间状态，并且在`view`中根据状态更新控件内容。

```rust
struct Editor {
    content: text_editor::Content
}

// ...

impl Sandbox for Editor {
    type Message = Message;

    fn new() -> Self {
        Editor {
            content: text_editor::Content::new() // Initialize the content
        }
    }

    // ...

    fn view(&self) -> Element<'_, Message> {
        text_editor(&self.content).into() // Link the content state
    }
}
```

默认情况下，`into`方法会使控件充满整个窗口，我们可以使用`container`包围`text_editor`控件辅助布局。

```rust
use iced::widget::container;

// ...

impl Sandbox for Editor {
    // ...
    fn view(&self) -> Element<'_, Message> {
        let editor = text_editor(&self.content);
        container(editor).padding(10).into() // Add padding and wrap the editor
    }
}
```

此时，多行文本输入框的布局已经完成。但由于输入框没有绑定事件处理，因此目前无法输入文本。`text_editor`控件支持的事件有

```rust hl_lines="6"
pub enum Action {
    Move(Motion),
    Select(Motion),
    SelectWord,
    SelectLine,
    Edit(Edit),
    Click(Point),
    Drag(Point),
    Scroll { lines: i32 },
}
```

我们需要将`Edit`事件在`update`和`view`中进行处理，同时更新`Message`枚举类型。

```rust
#[derive(Debug, Clone)]
enum Message {
    EditorEdit(text_editor::Action)
}

// ...

impl Sandbox for Editor {
    // ...
    fn update(&mut self, message: Message) {
        match message {
            Message::EditorEdit(action) => {
                self.content = self.content.edit(action);
            }
        }
    }

    fn view(&self) -> Element<'_, Message> {
        let editor = text_editor(&self.content).on_edit(Message::EditorEdit); // Bind the edit event
        container(editor).padding(10).into() // Add padding and wrap the editor
    }
}
```

以下为完整的`main.rs`文件内容：

{{ read_code_from_file('docs/coding/rust-gui/source/2.rs') }}
