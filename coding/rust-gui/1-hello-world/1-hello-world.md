# Hello World App

Keywords: `iced::Sandbox`, `iced::Settings`, `iced::widget::text`

## 创建项目

首先，创建一个新的 Rust 项目，并添加对`iced`库的依赖。

```bash
cargo new text-editor
cd text-editor
cargo add iced
```

此时的`main.rs`文件内容如下：

```rust
fn main() {
    println!("Hello, world!");
}
```

## 创建GUI应用

`iced`的GUI类有`Application`和`Sandbox`两种。其中`Sandbox`是一个简化版的`Application`，提供了一些默认的行为。`Sandbox`特性包含如下方法：

```rust hl_lines="2 3 4 5 6"
pub trait Sandbox {
    type Message: std::fmt::Debug + Send;
    fn new() -> Self;
    fn title(&self) -> String;
    fn update(&mut self, message: Self::Message);
    fn view(&self) -> Element<'_, Self::Message>;
    fn theme(&self) -> Theme {
        Theme::default()
    }
    fn style(&self) -> theme::Application {
        theme::Application::default()
    }
    fn scale_factor(&self) -> f64 {
        1.0
    }
    fn run(settings: Settings<()>) -> Result<(), Error>
    where
        Self: 'static + Sized,
    {
        <Self as Application>::run(settings)
    }
}
```

为了使用`Sandbox`，我们需要实现其中未实现的方法，即`Message`、`new`、`title`、`update`和`view`。

* `Message`是一个枚举类型，用于定义应用会产生的消息类型，需要实现`std::fmt::Debug`和`Send`特性。

    ```rust
    #[derive(Debug)] // Inherit the Debug trait
    enum Message {} // No message required
    ```

* `new`方法用于创建一个新的`Sandbox`实例，初始化实例状态，一般情况下直接返回`Self`即可。

    ```rust
    fn new() -> Self {
        Self
    }
    ```

* `title`方法用于返回GUI窗口的标题。

    ```rust
    fn title(&self) -> String {
        String::from("A text editor")
    }
    ```

* `update`方法和`view`方法共同组成应用的消息循环：`update`方法用于处理消息，更新应用状态，`view`方法用于在状态更新后更新应用界面。此处我们在`view`方法中放置一个文本控件。

    ```rust
    fn update(&mut self, message: Self::Message) {
        match message {
            // No message to handle
        }
    }

    fn view(&self) -> Element<'_, Self::Message> {
        text("Hello, world!").into()
    }
    ```

通过`Sandbox::run`方法启动应用，该方法返回`Result<(), Error>`类型，可以直接作为`main`函数的返回值。

以下为完整的`main.rs`文件内容：

{{ read_code_from_file('docs/coding/rust-gui/source/1.rs') }}
