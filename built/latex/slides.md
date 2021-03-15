# 使用LaTeX创建幻灯片

首先，需要指定`documentclass`为`beamer`类型：

```tex
\documentclass{beamer}
```

每一张幻灯片使用`frame`环境，如下代码创建一个新的空白幻灯片：

```tex
\begin{frame}
\end{frame}
```

第一页PPT通常显示PPT的标题、作者的个人信息等内容：

```tex
\title{标题}
\subtitle{副标题}
\author{作者}
\institute{组织}
\date{\today}  % 显示日期
\titlepage
```