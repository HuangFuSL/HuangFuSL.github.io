# 特殊技巧

## 公式内中文

使用命令`\text`或`\mbox`可以在公式中加入中文文本。如果使用`\mathrm`，则不会显示中文。

## 隐形字符

`\phantom`命令可以创建一个占据一定空间的空白，空白的长宽由参数的尺寸决定：

$$
\begin{aligned}
    \bbox[border: 2px solid magenta]{\phantom{\int_0^1 x\mathrm dx}} \; & \bbox[border: 2px solid magenta]{\int_0^1 x\mathrm dx} \\
    \bbox[border: 2px solid magenta]{\int_0^1 x\mathrm dx} \; &
\end{aligned}
$$

此外，`\phantom`有两个变种`\vphantom`与`\hphantom`，前者创造一个宽度为0，高度为指定高度的空白；后者创造一个高度为0，宽度为指定宽度的空白。在尺寸根据内容而变的容器中，`\phantom`等一系列命令可以用于控制容器的大小。

!!! example "`\vphantom`使用场景"

    在`\left`、`\right`等命令只能在一行上控制左右两侧括号的大小，而当公式中出现跨行，`\left`、`\right`则无法正确匹配。此时可以使用`\vphantom`命令将括号撑开。

    === "不使用`\vphantom`"

        ```tex
        \begin{equation}
            \begin{aligned}
                \frac{\partial ^2\Pi(x, t)}{\partial x\partial t} =
                & -(p-s)\mathbb E_{Q, B, L}\left[D(t)|Q(t)\leq x\right]f_{Q(t)}(x) \\
                & + h\mathbb P(t < B + L) - h\mathbb E_{B, L} \\
                & \times \left[\int_{t}^\mathbb{B+L}\mathbb E_Q\left[D(t)|Q(t) - Q(\tau)\leq x, B\leq t, L\right]\right. \\
                & \color{magenta} \times \left. f_{Q(t) - Q(\tau) | B\leq t}(x)\mathbb P(B\leq t)\mathrm d \tau\right]
            \end{aligned}
        \end{equation}
        ```

        $$
        \begin{aligned}
            \frac{\partial ^2\Pi(x, t)}{\partial x\partial t} =
            & -(p-s)\mathbb E_{Q, B, L}\left[D(t)|Q(t)\leq x\right]f_{Q(t)}(x) \\
            & + h\mathbb P(t < B + L) - h\mathbb E_{B, L} \\
            & \times \left[\int_{t}^\mathbb{B+L}\mathbb E_Q\left[D(t)|Q(t) - Q(\tau)\leq x, B\leq t, L\right]\right. \\
            & \color{magenta} \times \left. f_{Q(t) - Q(\tau) | B\leq t}(x)\mathbb P(B\leq t)\mathrm d \tau\right]
        \end{aligned}
        $$

    === "使用`\vphantom`"

        ```tex
        \begin{equation}
            \begin{aligned}
                \frac{\partial ^2\Pi(x, t)}{\partial x\partial t} =
                & -(p-s)\mathbb E_{Q, B, L}\left[D(t)|Q(t)\leq x\right]f_{Q(t)}(x) \\
                & + h\mathbb P(t < B + L) - h\mathbb E_{B, L} \\
                & \times \left[\int_{t}^\mathbb{B+L}\mathbb E_Q\left[D(t)|Q(t) - Q(\tau)\leq x, B\leq t, L\right]\right. \\
                & \color{magenta} \times \left.\vphantom{\int_t^{B+L}} f_{Q(t) - Q(\tau) | B\leq t}(x)\mathbb P(B\leq t)\mathrm d \tau\right]
            \end{aligned}
        \end{equation}
        ```

        $$
        \begin{aligned}
            \frac{\partial ^2\Pi(x, t)}{\partial x\partial t} =
            & -(p-s)\mathbb E_{Q, B, L}\left[D(t)|Q(t)\leq x\right]f_{Q(t)}(x) \\
            & + h\mathbb P(t < B + L) - h\mathbb E_{B, L} \\
            & \times \left[\int_{t}^\mathbb{B+L}\mathbb E_Q\left[D(t)|Q(t) - Q(\tau)\leq x, B\leq t, L\right]\right. \\
            & \color{magenta} \times \left.\vphantom{\int_t^{B+L}} f_{Q(t) - Q(\tau) | B\leq t}(x)\mathbb P(B\leq t)\mathrm d \tau\right]
        \end{aligned}
        $$
