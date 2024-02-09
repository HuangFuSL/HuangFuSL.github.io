# New and Save

本节添加新建和保存文件的功能。

首先，在`EditorEdit`消息处理中检查是否对文件进行了修改，并且记录文件的修改状态。

```rust hl_lines="3 7 8 9 10 16 22"
struct Editor {
    // ...
    modified: bool
}
// ... In `update` function
            Message::EditorEdit(action) => {
                match &action {
                    text_editor::Action::Edit(_) => self.modified = true,
                    _ => {}
                }
                self.content.edit(action);
                Command::none()
            },
            Message::FileOpened(Ok((path, result))) => {
                self.path = Some(path);
                self.modified = false;
                self.content = text_editor::Content::with(&result);
                Command::none()
            },
            // ...
            Message::OpenButtonPressed => {
                self.modified = false;
                Command::perform(pick_file(), Message::FileOpened)
            },
```

其次，调整文件路径控件的不同显示状态：

1. 当文件路径为空时，为新文件，显示“New File”。
2. 当打开一个文件时，显示文件路径。
3. 当文件被修改后，文件路径后加上“*”。
4. 当打开文件出错时，显示错误信息。

```rust
let path_indicator = if let Some(error) = &self.error {
    match error {
        Error::DialogClosed => text("Dialog closed"),
        Error::IO(kind) => text(format!("I/O error: {:?}", kind))
    }
} else {
    let path_text = match &self.path {
        None => String::from("New file"),
        Some(path) => path.to_string_lossy().to_string()
    };
    let suffix = if self.modified { "*" } else { "" };
    text(format!("{}{}", path_text, suffix))
};
```

在创建文件时，需要清空文件路径和内容，以及清空错误信息。加入一个新的消息类型`NewButtonPressed`，由一个按钮触发，在`update`函数中执行这个逻辑。

=== "消息类型声明"

    ```rust hl_lines="4"
    enum Message {
        EditorEdit(text_editor::Action),
        FileOpened(Result<(PathBuf, Arc<String>), Error>),
        NewButtonPressed,
        OpenButtonPressed
    }
    ```

=== "消息触发"

    ```rust hl_lines="3"
    // ... In `view` function
    let controls = row![
        button("New").on_press(Message::NewButtonPressed),
        button("Open").on_press(Message::OpenButtonPressed)
    ];
    ```

=== "执行逻辑"

    ```rust
    // ... In matching logic in `update` function
    Message::NewButtonPressed => {
        self.content = text_editor::Content::new();
        self.error = None;
        self.path = None;
        self.modified = false;
        Command::none()
    },
    // ...
    ```

接下来处理保存文件的逻辑，当存在文件路径时，保存文件，否则打开文件选择对话框。

```rust
async fn save_file(path: Option<PathBuf>, content: String) -> Result<PathBuf, Error> {
    let path = if let Some(path) = path {
        path
    } else {
        rfd::AsyncFileDialog::new()
            .set_title("Save the file to...")
            .save_file()
            .await
            .ok_or(Error::DialogClosed)?
            .path()
            .to_path_buf()
    };
    tokio::fs::write(&path, content)
        .await
        .map_err(|err| err.kind())
        .map_err(Error::IO)
        .map(|_| path)
}
```

在保存文件时，需要

1. 检查文件的修改状态，如果文件没有修改，不执行保存操作。
2. 检查文件路径是否为空，如果为空，打开文件选择对话框，否则直接保存文件。
3. 加入一个新的消息类型`SaveButtonPressed`，由一个按钮触发，在`update`函数中执行这个逻辑。

=== "消息类型声明"

    ```rust hl_lines="4 7"
    enum Message {
        EditorEdit(text_editor::Action),
        FileOpened(Result<(PathBuf, Arc<String>), Error>),
        FileSaved(Result<PathBuf, Error>),
        NewButtonPressed,
        OpenButtonPressed,
        SaveButtonPressed
    }
    ```

=== "消息触发"

    ```rust hl_lines="5"
    // ... In `view` function
    let controls = row![
        button("New").on_press(Message::NewButtonPressed),
        button("Open").on_press(Message::OpenButtonPressed),
        button("Save").on_press(Message::SaveButtonPressed)
    ];
    ```

=== "执行逻辑"

    ```rust
    // ... In matching logic in `update` function
    Message::FileSaved(Ok(path)) => {
        self.path = Some(path);
        self.modified = false;
        Command::none()
    },
    Message::FileOpened(Err(error)) | Message::FileSaved(Err(error)) => {
        self.error = Some(error);
        Command::none()
    },
    // ...
    Message::SaveButtonPressed => {
        let content = self.content.text();
        match self.modified {
            false => Command::none(),
            true => Command::perform(
                save_file(self.path.clone(), content),
                Message::FileSaved
            )
        }
    }
    ```

最后，调整三个按钮之间的间距

```rust hl_lines="5"
let controls = row![
    button("New").on_press(Message::NewButtonPressed),
    button("Open").on_press(Message::OpenButtonPressed),
    button("Save").on_press(Message::SaveButtonPressed)
].spacing(10);
```

以下为完整的`main.rs`文件内容：

{{ read_code_from_file('docs/coding/rust-gui/source/7.rs') }}
