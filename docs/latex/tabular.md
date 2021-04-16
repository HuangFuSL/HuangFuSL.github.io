# tabular环境

`tabular`环境是$\LaTeX{}$用于创建表格的环境。

## 基本使用

如下代码演示了`tabular`语句的使用方法,生成一个3行3列的表格。

!!! tldr "tabular基本使用"
    === "tex代码"
        ```tex
        \begin{tabular}{|c|c|c|}
            \hline 2    & 9     & 4     \\
            \hline 7    & 5     & 3     \\
            \hline 6    & 1     & 8     \\
            \hline
        \end{tabular}
        ```

    === "渲染结果"
        ![tabular](img/tabular/tabular-1.svg)

### 导言区

`\begin{tabular}`其后紧跟的一对括号内是导言区，导言区规定了单元格的纵向边框和单元格内元素的对齐方式。

* `l`、`c`、`r`分别对应左对齐，居中，右对齐
* `|`、`||`对应表格纵向框线类型（单线或双线）
* `@{exp}`指定插入到列中的文本
* `*{n}{pre}`指重复`pre`内容`n`次
* `p{len}`将对应的列放入一个parbox中

根据如上表述，导言区`{|c|c|c|}`等价于`{*{3}{|c}|}`

!!! tldr "导言区"
    === "tex代码"
        ```tex
        \begin{tabular}{||l|c|r||}
            \hline 2    & 91    & 4     \\
            \hline 71   & 5     & 32    \\
            \hline 652  & 251   & 89    \\
            \hline
        \end{tabular}
        ```

    === "渲染结果"
        ![tabular](img/tabular/tabular-2.svg)

### 合并单元格

横向合并单元格可以使用`\multicolumn`命令，纵向合并单元格需要使用`multirow`宏包中的`\multirow`命令：

* `\multicolumn`命令的第一个参数指定合并列的数量，第二个参数是合并后单元格的导言列
* `\multirow`命令的第一个参数指定合并行的数量，第二个参数指定LaTeX自行设置宽度，第三个参数为单元格内容

{% raw %}
!!! tldr "合并单元格"
    === "tex代码"
        ```tex
        \begin{tabular}{|ccc|}
            \hline
            2   & 9     & 4\\
            7   & \multicolumn{2}{c|} {\multirow{2}*{{?}}} \\
            6   &       &\\
            \hline
        \end{tabular}
        ```

    === "渲染结果"
        ![tabular](img/tabular/tabular-2-1.svg)
{% endraw %}

## 三线表

LaTeX中使用三线表需要用到`booktabs`宏包，加入宏包后可以使用`\toprule`、`\midrule`与`\bottomrule`画线（不应再使用`\hline`命令）。

!!! tldr "三线表"
    === "tex代码"
        ```tex
        \begin{tabular}{ccc}
            \toprule
            2   & 91    & 4     \\
            \midrule
            71  & 5     & 32    \\
            652 & 251   & 89    \\
            \bottomrule
        \end{tabular}
        ```

    === "渲染结果"
        ![tabular](img/tabular/tabular-3.svg)

## 颜色填充

颜色填充需要使用`colortbl`宏包，使用`\rowcolor`命令指定行的填充颜色，或`\cellcolor`命令指定单元格的填充颜色。填充颜色可以选择灰度`[gray]`或彩色`[rgb]`。

!!! tldr "颜色填充"
    === "tex代码"
        ```tex
        \begin{tabular}{ccc}
            \rowcolor[gray]{0.6} 2    & 9     & 4     \\
            \rowcolor[gray]{0.7} 7    & 5     & 3     \\
            \rowcolor[gray]{0.8} 6    & 1     & 8     \\
        \end{tabular}
        ```

    === "渲染结果"
        ![tabular](img/tabular/tabular-4.svg)

## 斜线表头

斜线表头由`diagbox`宏包提供，使用方法如下：

!!! tldr "斜线表头"
    === "tex代码"
        ```tex
        \begin{tabular}{|l|ccc|}
            \hline
            \diagbox{Time}{Room}{Day} & Mon & Tue & Wed \\
            \hline
            Morning & used & used & \\
            Afternoon & & used & used \\
            \hline
        \end{tabular}
        ```

    === "渲染结果"
        ![tabular](img/tabular/tabular-5.svg)