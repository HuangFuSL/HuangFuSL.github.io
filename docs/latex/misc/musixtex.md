---
todo: true
---

# 乐谱排版

`musixtex`是LaTeX中用来排版乐谱的宏包。以下内容针对鼓谱排版。

```tex
\usepackage{musixtex}
\input{musixper} % 加入了鼓谱排版的一些内容
```

## 音高对照表

从左向右依次为A-Q

{{ latex_image('imgs/musixtex/notes-pitch.tex') }}

## 基本使用

`musixtex`中添加了`music`环境，在`music`环境中可以对乐谱进行设置。然后在命令`\startextract`和`\zendextract`之间输入音符。

```tex
\begin{music}
    \instrumentnumber{1}        % 乐器
    \setclefsymbol1\empty       % 谱号
    \nobarnumbers               % 取消小节编号
    \generalmeter{\meterfrac44} % 节拍
    \startextract
        % Enter notes here
    \zendextract
\end{music}
```

在本小节中，`p`表示音符对应的音高。

### 确定音符分布间距

使用`\notes`的不同大小写形式来确定音符的分布间距。

```tex
\notes ... \en % Suitable for sixteenth notes
\Notes ... \en % Suitable for eighth notes
\NOtes ... \en % Suitable for quarter notes
```

=== "`\notes`"

    {{ latex_image('imgs/musixtex/notes-sixteenth.tex') }}

=== "`\Notes`"

    {{ latex_image('imgs/musixtex/notes-eighth.tex') }}

=== "`\NOtes`"

    {{ latex_image('imgs/musixtex/notes-quarter.tex') }}

### 音符

音符命令由两部分组成：时值+方向。不同音符的时值对应的命令如下表所示

|时值|全音符|二分|四分|八分|十六分|
|:-:|:-:|:-:|:-:|:-:|:-:|
|命令|`w`|`h`|`q`|`c`|`cc`|

`u`表示向上的音符，`l`表示向下的音符，`a`表示自动设置音符方向。如`\qu{p}`表示一个向上的四分音符。如果不加方向，则没有音符的“杆”。

在方向后面加上`p`表示附点，`pp`表示双附点。

每输入一个音符，下一个命令输入的位置便会向后移动。如果要输入和弦，需要在最后一个音符之前，使用`z`+时值表示这个音符不向后移动输入位置。

如果两个音符离得过近，使用`l`将音符向左移动一个音符的位置，`r`将音符向右移动一个音符的位置。

```\tex
\NOtes \zq d\qu g\rq g\qu f\zq e\qu h\zq f\qu k \en
```

{{ latex_image('imgs/musixtex/notes-chord.tex') }}

### 符杠

如果八分或更短的音符连续出现，这些音符之间使用符杠相连，通常每四个音符连成一组。符杠的定义格式如下

```tex
% 上方
\ibu{n}{p}{s} <notes-under-beam> \tbu{n} <the-last-note>
% 下方
\ibl{n}{p}{s} <notes-under-beam> \tbl{n} <the-last-note>
```

其中`n`为编号，`p`为开始的音符高度，`s`为斜度。命令里`b`的个数等于显示的符杠数。与符杠相连的音符标记为时值+`b`+编号，如果同一位置有多个音符，需要在时值前面加`z`。注意音符之间不要加空格。

```tex
\Notes\ibu0j0\qb0j\qb0j\qb0j\tbu0\qb0j\en
\notes\ibbu0j0\qb0j\qb0j\qb0j\tbu0\qb0j\en
\NOtes\qu j\en
```

{{ latex_image('imgs/musixtex/beam-basic.tex') }}

`\tbu{n}\qb{n}{p}`可以缩写为`\tqu{n}{p}`，`\tbl{n}{p}\qb{n}{p}`可以缩写为`\tql{n}{p}`，`\tbu{n}\zqb{n}{p}`可以缩写为`\zqu{n}{p}`，`\tbl{n}{p}\zqb{n}{p}`可以缩写为`\zql{n}{p}`

`\ibu`中需要手动确定斜率，可以用对应的`\Ibu`命令自动确定：

```tex
\Ibu{n}{p1}{p2}{np}
```

其中`{n}`为编号，`p1`为第一个音符高度，`p2`为最后一个音符高度，`np`为音符个数。

```tex
\Notes\Ibu0dk4\qb0d\qb0h\qb0f\tbu0\qb0k\en
\Notes\Ibu0kd4\qb0k\qb0f\qb0h\tbu0\qb0d\en
```

{{ latex_image('imgs/musixtex/beam-slope.tex') }}

当不包含和弦时，可以用`D`、`T`、`Q`快速输入包含2、3、4个音符的符杠。

```tex
\Notes\Qqbu dhfk\en
\notes\Qqbbu kfhd\Qqbbl dhfk\en
```

{{ latex_image('imgs/musixtex/beam-shortcut.tex') }}

当在符杠中需要改变等级时，使用`\nbu`将等级增加到`b`的个数对应的级数，使用`\ibu`将等级减少到`b`的个数减一对应的级数。

```tex
\Notes\ibu0k0\qb0j\en\notes\nbbu0\qb0j\tbu0\qb0j\en
\notes\ibbu0j0\qb0j\tbbu0\qb0j\en\Notes\tbu0\qb0j\en
```

使用`\roff{}`在当前音符右侧添加一个对应等级的短杠，当`\tbbu`配合更高等级输入时，在当前音符左侧位置添加一个对应等级短杠，可以用来输入切分音。

```tex
\notes\ibbu0j0\qb0j\tbbu0\qb0j\en
\Notes\tbu0\qb0j\en

\notes\ibbu0j0\roff{\tbbu0}\qb0j\en
\Notes\qb0j\tbbu0\en
\notes\tbu0\qb0j\en
```

{{ latex_image('imgs/musixtex/beam-roff.tex') }}

### 休止符

休止符的命令为

|时值|全音符|二分|四分|八分|十六分|
|:-:|:-:|:-:|:-:|:-:|:-:|
|命令|`\pause`|`\hp`|`\qp`|`\ds`|`\qs`|

在命令前使用`\raise`调整休止符高度，`\Interligne`表示线间距；使用`\rlap`使下一个音符停留在原位。

{{ latex_image('imgs/musixtex/rest.tex') }}
