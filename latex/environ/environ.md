# LaTeX语句块（环境）

## 列表环境

在LaTeX中，`enumerate`环境定义了编号列表，`itemize`环境与`description`环境定义了符号列表。所有的列表使用`\item`命令定义列表项。列表可以自定义使用的编号与符号。

当列表被嵌套时，不同层次的列表会使用不同的编号以避免混淆。

### `enumerate`环境

`enumerate`环境的使用方式如下：

```tex
\begin{enumerate}
    \item This is an item.
    \item This is an item.
    \item This is an item.
\end{enumerate}
```

渲染后的效果：

1. This is an item.
2. This is an item.
3. This is an item.

`enumerate`环境默认使用`1. 2. 3. ...`进行编号，自定义编号通过在`\begin{enumerate}`后添加参数实现。

```tex
\begin{enumerate}[A.]
    \item This is an item.
    \item This is an item.
    \item This is an item.
\end{enumerate}
```

渲染后的效果：

A. This is an item.  
B. This is an item.  
C. This is an item.

**自定义编号列表需要引入`enumerate`包**：`\usepackage{enumerate}`

### `itemize`环境

`itemize`环境用于生成符号列表，使用方式如下：

```tex
\begin{itemize}
    \item This is an item.
    \item This is an item.
    \item This is an item.
\end{itemize}
```

渲染后的效果：

* This is an item.
* This is an item.
* This is an item.

`\item`命令可以使用中括号指定当前项使用的符号，如`\item[-]`使用`-`作为符号