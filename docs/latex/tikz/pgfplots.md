# pgfplots

借助宏包`pgfplots`，可以使用TikZ绘制折线图，如下所示。

!!! tldr "pgfplots绘制折线图"
    === "tex代码"
        ```tex
        \begin{figure}[htbp]
            \begin{tikzpicture}
                \begin{axis}[sharp plot]
                    \addplot coordinates{(0, 5)(1, 9)(2, 7)(3, 4)(4, 10)};
                \end{axis}
            \end{tikzpicture}
        \end{figure}
        ```

    === "渲染结果"
        {{ latex_image('img/pgfplots-1.tex', 'pgfplots') }}

`axis`控制一个图像，`\begin{axis}`后可以加一对方括号，用于设定图片的参数。`addplot`控制图像中的一个序列，其后同样可以加一对方括号用于控制参数。

## `axis`环境

`axis`环境可用的参数如下所列：

* `[sharp plot, smooth]`等，表明折线图的曲线是否经过平滑
* `xlabel`与`ylabel`，控制坐标轴的标注。
* `title`控制图像的标题
* `xmode`与`ymode`控制坐标轴是线性坐标轴（`normal`）还是对数坐标轴（`log`）
* `xtick distance`与`ytick distance`控制坐标轴刻度大小
* `xmin, xmax`与`ymin, ymax`控制坐标轴的范围
    * 当指定坐标轴范围时，如果`enlargelimits`指定为`true`，则坐标轴会自动放大以符合输入数据

如下创建一个空的图像，x坐标轴为线性，y坐标轴为对数：

!!! tldr "axis参数示例"
    === "tex代码"
        ```tex
        \begin{figure}[htbp]
            \begin{tikzpicture}
                \begin{axis}[
                    xlabel=Year,
                    ylabel=Inventory,
                    xmin=2019, xmax=2021,
                    ymin=100, ymax=1000,
                    xtick distance=1,
                    title=Inventory Graph,
                    xmode=normal, ymode=log
                ]
                \end{axis}
            \end{tikzpicture}
        \end{figure}
        ```

    === "渲染结果"
        {{ latex_image('img/pgfplots-2.tex', 'pgfplots') }}

有关更多参数，请参见[pgfplots 手册](http://mirrors.ctan.org/graphics/pgf/contrib/pgfplots/doc/pgfplots.pdf)

## `\addplot`

`\addplot`命令可以向图像中添加折线图或函数。

1. `\addplot coordinates{}` 用于绘制折线图，其中`coordinates`中的坐标用圆括号括起
2. `\addplot [smooth] {f(x)}` 用于绘制平滑的折线图，其中`f(x)`为函数表达式

!!! tldr "axis参数示例"
    === "tex代码"
        ```tex
        \begin{figure}[htbp]
            \begin{tikzpicture}
                \begin{axis}[
                    xlabel=$x$ variable,
                    ylabel=$y$ variable,
                    xmin=0, xmax=7,
                    title=Regression Example,
                ]
                    \addplot coordinates{(0, 5)(1, 9)(2, 7)(3, 4)(4, 10)};
                    \addlegendentry{\small Data}
                    \addplot [smooth, red]{0.5*x + 6};
                    \addlegendentry{\small Regressor}
                \end{axis}
            \end{tikzpicture}
        \end{figure}
        ```

    === "渲染结果"
        {{ latex_image('img/pgfplots-3.tex', 'pgfplots') }}

`\addplot`有如下参数：

* `smooth`如果存在，绘制不包含点坐标的平滑图像
* `[color]`设置颜色。
