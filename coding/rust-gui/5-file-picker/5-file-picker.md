# File Picker

Keywords: `iced::widget::button`, `rfd::AsyncFileDialog`

本节在窗口上添加一个按钮，点击后弹出文件选择对话框，选择文件后将文件内容显示在窗口上。首先需要添加`rfd`库的依赖，用于文件选择对话框。

```bash
cargo add rfd
```

首先需要编写用于显示文件选择窗口的函数。注意`rfd::AsyncFileDialog`会返回一个异常，因此需要自定义异常类型。

```rust
#[derive(Debug, Clone)]
enum Error {
    DialogClosed,
    IO(io::ErrorKind)
}

async fn pick_file() -> Result<Arc<String>, Error> {
    let handler = rfd::AsyncFileDialog::new()
        .set_title("Choose a text file...")
        .pick_file()
        .await
        .ok_or(Error::DialogClosed)?; // If error, return DialogClosed error
    load_file(handler.path()).await
}
```

调整窗口布局，在窗口上添加一个按钮。

```rust
impl Application for Editor {
    // ...

    fn view(&self) -> Element<'_, Message> {
        let controls = row![button("Open")];
        // ...
        container(column![controls, editor, status_bar].spacing(10)).padding(10).into()
    }
}
```

之后需要添加按钮的点击事件处理，调用`pick_file`函数。

```rust
enum Message {
    // ...
    OpenButtonPressed
}

impl Application for Editor {
    // ...

    fn update(&mut self, message: Message) -> Command<Message> {
        // Handle messages here
        match message {
            // ...
            Message::OpenButtonPressed => {
                Command::perform(pick_file(), Message::FileOpened)
            }
        }
    }

    fn view(&self) -> Element<'_, Message> {
        let controls = row![button("Open").on_press(Message::OpenButtonPressed)];
        // ...
    }
}
```

以下为完整的`main.rs`文件内容：

{{ read_code_from_file('docs/coding/rust-gui/source/5.rs') }}
