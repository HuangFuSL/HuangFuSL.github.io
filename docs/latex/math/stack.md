# LaTeX 符号堆叠

## 符号上下加文本

部分大型运算符（参见[数学符号](symbols.md)）可以加入上下标。对于行间公式，运算符的上下标有两种位置选择：

* 上下标在符号上下两侧，如
  $$
  \sum_{i=0}^\infty
  $$
* 上下标在符号右侧，如
  $$
  \int_0^\infty
  $$

行内公式默认所有的上下标都在符号右侧，如$\sum_{i=0}^\infty$。使用`\limits`可以强制上下标出现在运算符上下两侧，如

!!! tldr "`\limits`命令"
    === "LaTeX代码"
        ```tex
        $\sum\limits_{i=0}^\infty$
        ```

    === "渲染结果"
        $\sum\limits_{i=0}^\infty$

`\overset`、`\underset`可以实现在符号上下插入符号。`\stackrel`也可以实现与`\overset`相同的功能。

!!! tldr "`\overset`命令与`\underset`命令"
    === "LaTeX代码"
        ```tex
        \begin{equation*}
            \begin{aligned}
                &\overset{above}{\rightarrow} \\
                &\underset{below}{\rightarrow} \\
            \end{aligned}
        \end{\equation*}
        ```

    === "渲染结果"
        $$
        \begin{aligned}
            &\overset{above}{\rightarrow} \\
            &\underset{below}{\rightarrow} \\
        \end{aligned}
        $$

如果需要换行，可以使用`\substack`命令：

!!! tldr "`\substack`命令"
    === "LaTeX代码"
        ```tex
        \begin{equation*}
            \begin{aligned}
                &\overset{\substack{above1 \\ above2}}{\rightarrow} \\
                &\underset{\substack{below1 \\ below2}}{\rightarrow} \\
            \end{aligned}
        \end{\equation*}
        ```

    === "渲染结果"
        $$
        \begin{aligned}
            &\overset{\substack{above1 \\ above2}}{\rightarrow} \\
            &\underset{\substack{below1 \\ below2}}{\rightarrow} \\
        \end{aligned}
        $$

## 箭头上下加文本

`\overset`、`\stackrel`与`\underset`只能实现箭头上下加文本，箭头的长度不能随文本长度自动调整。`amsmath`宏包提供了`\xleftarrow`与`\xrightarrow`，可以实现箭头上下加文本，同时箭头会自动适应文本的长度。示例如下：

!!! tldr "`\xrightarrow`命令"
    === "LaTeX代码"
        ```tex
        \begin{itemize}
            \item $\xrightarrow[\text{below}]{\text{above}}$
            \item $\xrightarrow[\text{very very long below}]{\text{very very long above}}$
        \end{itemize}
        ```

    === "渲染结果"
        {{ latex_image('img/stack-1.tex', 'xrightarrow') }}

定义符号$\triangleq$可以直接使用`\triangleq`输入。
