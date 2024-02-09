# Asynchronous File Loading

Keywords: `iced::Application`, `iced::Command`, `iced::executor`, `std::io`, `std::path::Path`, `std::sync::Arc`, `tokio::fs::read_to_string`

为了实现异步文件加载，我们需要使用`tokio`库

```toml
[dependencies]
tokio = { version = "1.32", features = ["fs"] }
```

`Sandbox`不能直接执行异步函数，需要用`Application`。相比于`Sandbox`，`Application`需要额外实现如下类型

```rust
impl Application for Editor {
    // ...
    type Theme; // Color theme
    type Executor; // Engine for running async tasks
    type Flags; // Initial state
}
```

此处，`Theme`和`Flags`类型不需要额外实现，可以分别用`iced::Theme`和`()`代替。默认情况下，`Executor`类型需要用`iced::executor::Default`代替。

在修改为`Application`后，`new`和`update`方法的返回值标签也需要修改，`new`方法返回`(Self, Command<Message>)`，`update`方法返回`Command<Message>`。其中`Command<Message>`是一个异步任务，在执行完毕后会发送一个对应类型的`Message`。

```rust
impl Application for Editor {
    // ...

    fn new(_flags: ()) -> (Self, Command<Message>) {
        (
            Self {
                // ...
            },
            Command::none(),
        )
    }

    fn update(&mut self, message: Message) -> Command<Message> {
        match message {
            // ...
        }

        Command::none()
    }
}
```

此后，我们需要编写用于读取文件的函数。

```rust
use std::io;
use std::path::Path;
use std::sync::Arc;

async fn load_file<T>(path: T) -> Result<Arc<String>, io::ErrorKind>
    where T: AsRef<Path>
{
    tokio::fs::read_to_string(path)
        .await
        .map(Arc::new)
        .map_err(|e| e.kind())
}
```

在`new`方法中，我们可以使用`Command`来调用`load_file`函数。

```rust

enum Message {
    EditorEdit(text_editor::Action),
    FileOpened(Result<Arc<String>, io::ErrorKind>)
}

impl Application for Editor {
    // ...

    fn new(_flags: ()) -> (Self, Command<Message>) {
        let path = "path/to/file.txt";
        let file = load_file(path);

        (
            Self {
                // ...
            },
            Command::perform(
                load_file(format!("{}/main.rs", env!("CARGO_MANIFEST_DIR"))),
                Message::FileLoaded,
            ),
        )
    }
}
```

读取文件时可能会发生错误，需要对异常消息进行处理。在`load_file`函数中已经通过`Result`返回了对应的错误类型，只需要在`update`方法中处理`Message::FileOpened`即可。

```rust
struct Editor {
    // ...
    error: Option<io::ErrorKind>, // Use Option to store error
}

// ...

impl Application for Editor {
    // ...

    fn new(_flags: ()) -> (Self, Command<Message>) {
        (
            Self {
                // ...
                error: None, // Initialize error as None
            },
            // ...
        )
    }

    fn update(&mut self, message: Message) -> Command<Message> {
        // ...
        match message {
            // ...
            Message::FileOpened(Error(e)) => {
                self.error = Some(e); // Store error
            }
        }
        // ...
    }
}
```

以下为完整的`main.rs`文件内容：

{{ read_code_from_file('docs/coding/rust-gui/source/3.rs') }}
