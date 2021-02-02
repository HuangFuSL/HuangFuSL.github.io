# Python中的函数

> “一等对象”指满足如下条件的对象：
>
> * 在程序执行时创建
> * 能够赋值给变量或数据结构中的元素
> * 能作为函数参数与返回值
>
> **Python中的函数是一等对象**

## 函数与高阶函数

函数是一个对象，通常使用`def`关键字定义一个函数：

```python
>>> def constant():  
...     return 1
... 
>>> type(constant)
<class 'function'>
>>>
```

函数可以定义在其他函数内部：

```python
>>> def outer():
...     def inner():
...             return "ok"
...     return inner
... 
>>> func = outer()
>>> func()
'ok'
>>>
```

高阶函数是接受另一个函数作为参数或返回一个函数的函数，如`map`、`filter`等。

除使用`def`关键字定义函数以外，`lambda`提供了另一种创建简单函数的方法，这种方法常用于向高阶函数传递参数。`lambda`表达式只能加入表达式而无法添加控制逻辑：

```python
>>> a = lambda : "ok"  
>>> a()
'ok'
>>>
```

`lambda`表达式可以创建不同参数数量的函数：

* 没有参数，如`lambda : "ok"`
* 给定数量参数，如`lambda x, y : x + y`
* 任意参数，如`lambda *_ : sum(_)`（无名参数）或`lambda **_ : sum(_)`（具名参数）

若`lambda`表达式的右侧是逗号分隔的表达式，生成的是`lambda`对象组成的元组。

使用`dir()`查看函数的内置属性。相比于一般对象，函数有以下的额外属性：

```python
>>> class Obj():    
...     pass
... 
>>> def func(): 
...     pass
... 
>>> sorted(list(set(dir(func)) - set(dir(Obj()))))
['__annotations__', '__call__', '__closure__', '__code__', '__defaults__', '__get__', '__globals__', '__kwdefaults__', '__name__', '__qualname__']
>>>
```

### 广义函数

任何实现了`__call__`方法的对象都是可调用对象，可以使用类似于函数调用的方式进行调用。以下类型为可调用对象：

* 函数或`lambda`表达式
* 内置函数或类型方法
* 类型方法
* 类（相当于一个返回类对象的函数）
* 实现了`__call__`的对象
* 生成器函数

内置函数`callable()`用于检测一个对象是否是可调用对象。

## 函数的参数

Python中，函数的参数可以按照如下方式传递：

* 逗号分隔，按函数声明顺序传入参数
* 关键字参数，即参数名=参数值
* 有默认值的参数可以省略
* `*`解包可迭代对象或`**`解包映射对象

对应地，函数对参数有如下处理方式：

* 按照参数名获取参数
* 其他的无记名参数被`*`参数获取，单个`*`或`*`参数后的普通参数只能按照关键字参数的方式传递
* 其他的记名参数被`**`参数获取

函数声明中出现的单个`*`不会被视为参数，只用于限定此后所有参数的传入方式：

```python
>>> def a(*, a, b):
...     return a + b
... 
>>> a(1, 2) 
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
TypeError: a() takes 0 positional arguments but 2 were given
>>> a(a=1, b=2)
3
>>>
```

函数传参有两种方式，即值传递与引用传递。默认情况下，可变对象按引用传递，不可变对象按值传递：

```python
>>> def argPass(x):
...     x += x      
...           
>>> a = "test"      
>>> b = ["test"]
>>> argPass(a)
>>> argPass(b)
>>> a
'test'
>>> b
['test', 'test']
>>>
```

