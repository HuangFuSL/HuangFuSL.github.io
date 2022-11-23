# LaTeX中的字体与字号

## 字号

$\LaTeX$中共有`\tiny`、`\scriptsize`、`\footnotesize`、`\small`、`\normalsize`、`\large`、`\Large`、`\LARGE`、`\huge`、`\Huge`等10种相对尺寸的字号设置。每次修改字号后，会对命令后所有的文本生效。如果仅需要修改一部分文字的字号，可以将需要调整字号的部分使用花括号`{}`包围。

!!! tldr "LaTeX中的字号"
    === "tex代码"
        ```tex
        \centering
        \tiny tiny \\
        \scriptsize scriptsize \\
        \footnotesize footnotesize \\
        \small small \\
        \normalsize normalsize \\
        \large large \\
        \Large Large \\
        \LARGE LARGE \\
        \huge huge \\
        \Huge Huge \\
        ```

    === "渲染结果"
        {{ latex_image('img/fonts-1.tex', 'font size') }}