# 递归

LaTeX中的递归可以通过`\def`命令实现，在定义的宏中包含自身即可。

```tex
\def\recursion#1{
    \ifx#1\relax
        \relax
    \else
        do something
        \expandafter\recursion
    \fi
}
```

在宏第一次展开后，如果`#1`不是`\relax`，则会转入`\else`语句进行第二次展开。

* 宏定义中引用的宏名称前必须加`\expandafter`，表示在展开当前宏后才展开`\recursion`；
* `\relax`是宏的终止条件，输入序列需要以`\relax`结尾。
