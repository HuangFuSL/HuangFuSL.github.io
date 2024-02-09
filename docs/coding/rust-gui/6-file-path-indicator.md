# File Path Indicator

本节在状态栏中添加一个显示文件路径的文本控件。首先需要存储文件路径状态，并在初始化阶段设置为`None`。

```rust
struct Editor {
    path: Option<PathBuf>,
    // ...
}

impl Application for Editor {
    // ...
    fn new() -> (Editor, Command<Message>) {
        (
            Editor {
                path: None,
                // ...
            },
            // ...
        )
    }
    // ...
}
```

!!! warning "Path与PathBuf"
    `std::path::Path`和`std::path::PathBuf`的关系类似于`&str`和`String`的关系。`Path`是一个不可变引用，`PathBuf`是一个可变的对象，因此存储路径状态需要使用`PathBuf`，引用路径可以使用`Path`。


之前的`load_file`函数只返回了文件内容，此处需要将文件的路径一同返回。注意函数不能返回引用，因此需要将路径转换为`PathBuf`类型。`and_then`方法处理`Result`的`Ok`值，在成功读取文件后将`Path`转换为`PathBuf`并返回。调用`load_file`的`pick_file`函数也需要一并修改，同时返回路径和文件内容。

```rust hl_lines="11"
async fn pick_file() -> Result<(PathBuf, Arc<String>), Error> {
    // ...
}

async fn load_file(path: impl AsRef<Path>) -> Result<(PathBuf, Arc<String>), Error> {
    let content = tokio::fs::read_to_string(path.as_ref())
        .await
        .map(Arc::new)
        .map_err(|err| err.kind())
        .map_err(Error::IO);
    content.and_then(|content| Ok((path.as_ref().to_path_buf(), content)))
}
```

在修改读取文件的函数后，需要修改函数回调事件的类型和对应的处理函数


=== "修改后"

    ```rust hl_lines="3 11 12"
    enum Message {
        // ...
        FileOpened(Result<(PathBuf, Arc<String>), Error>),
    }

    impl Application for Editor {
        // ...
        fn update(&mut self, message: Message) -> Command<Message> {
            match message {
                // ...
                Message::FileOpened(Ok((path, result))) => {
                    self.path = Some(path);
                    self.content = text_editor::Content::with(&result);
                    Command::none()
                },
            }
        }
    }
    ```

=== "修改前"

    ```rust
    enum Message {
        // ...
        FileOpened(Result<Arc<String>, Error>),
    }

    impl Application for Editor {
        // ...
        fn update(&mut self, message: Message) -> Command<Message> {
            match message {
                // ...
                Message::FileOpened(Ok(result)) => {
                    self.content = text_editor::Content::with(&result);
                    Command::none()
                },
            }
        }
    }
    ```

最后在状态栏中添加一个文本控件显示文件路径即可。

```rust
impl Application for Editor {
    // ...
    fn view(&mut self) -> Element<Message> {
        // ...
        let path_indicator = match &self.path {
            None => text(""),
            Some(path) => text(path.to_string_lossy())
        };
        let status_bar = row![
            path_indicator, // Add path indicator here
            horizontal_space(Length::Fill),
            cursor_indicator
        ];
        // ...
    }
}
```

以下为完整的`main.rs`文件内容：

{{ read_code_from_file('docs/coding/rust-gui/source/6.rs') }}
