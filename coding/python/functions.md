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

### 函数内省

函数对象特有的属性提供了有关函数的信息：

|属性名|属性类型|属性说明|
|:-:|:-:|:-:|
|`__annotations__`|`dict`|函数参数和函数返回值的类型注解，键为参数名，值为参数类型|
|`__call__`|`method-wrapper`|实现可调用对象的调用方法|
|`__closure__`|`tuple`|函数闭包，参见相关章节|
|`__code__`|`code`|编译成二进制格式的函数元数据和定义体|
|`__defaults__`|`tuple`|形参的默认值列表|
|`__get__`|`method-wrapper`|实现只读描述符协议|
|`__globals__`|`dict`|函数所在模块中的全局变量|
|`__kwdefaults__`|`dict`|限定关键字形式访问的形参默认值|
|`__name__`|`str`|函数名称|
|`__qualname__`|`str`|函数的限定名称|

```python
>>> def dummy(a, b: int, c = 10, *args, d, e=50, **kwargs):
...     return (a, b, c, args, d, e, kwargs) 
... 
>>> dummy.__annotations__
{'b': <class 'int'>}
>>> dummy.__defaults__
(10,)
>>> dummy.__kwdefaults__
{'e': 50}
>>>
```

函数的参数列表与数量存储在`__code__`属性中：

```python
>>> dummy.__code__.co_varnames
('a', 'b', 'c', 'd', 'e', 'args', 'kwargs')
>>> dummy.__code__.co_argcount
3
>>>
```

`inspect`模块提供了检查函数参数信息的工具。

```python
>>> import inspect
>>> inspect.signature(dummy)
<Signature (a, b: int, c=10, *args, d, e=50, **kwargs)>
>>> sig = inspect.signature(dummy) 
>>> sig.parameters
mappingproxy(OrderedDict([('a', <Parameter "a">), ('b', <Parameter "b: int">), ('c', <Parameter "c=10">), ('args', <Parameter "*args">), ('d', <Parameter "d">), ('e', <Parameter "e=50">), ('kwargs', <Parameter "**kwargs">)]))
>>>
```

`parameters`存储了参数名与参数信息的映射关系。每个`Parameter`对象有`name`、`default`和`kind`属性。`dummy`函数各个参数的属性信息如下，`inspect._empty`表示参数没有默认值：

```python
>>> par = sig.parameters 
>>> for parName in par:
...     print(par[parName].name, par[parName].default, par[parName].kind)
... 
a <class 'inspect._empty'> POSITIONAL_OR_KEYWORD
b <class 'inspect._empty'> POSITIONAL_OR_KEYWORD
c 10 POSITIONAL_OR_KEYWORD
args <class 'inspect._empty'> VAR_POSITIONAL
d <class 'inspect._empty'> KEYWORD_ONLY
e 50 KEYWORD_ONLY
kwargs <class 'inspect._empty'> VAR_KEYWORD
>>>
```

从输出中可以看出，`dummy`共有四种类型的参数，即：

* `POSITIONAL_OR_KEYWORD`，可以通过定位参数或关键字参数传入
* `VAR_POSITIONAL`，多余的定位参数组成的元组
* `KEYWORD_ONLY`，只能通过关键字参数传入
* `VAR_KEYWORD`，多余的关键字参数组成的字典

另一种参数类型是只能通过定位参数传入的参数，即`POSITIONAL_ONLY`，Python语法不支持声明这种类型的参数，在C语言API中可能出现。

### 参数的类型限制

Python中对函数参数的类型检查以函数注解的形式实现。函数注解规定了函数可以接受的参数类型。

函数注解可以为类型，也可以为一个字符串。`:`用于对参数的注解，`->`表示对返回值的注解：

```python
>>> def another_dummy(x: int) -> int:       
...     return -x
... 
>>>
```

注意，注解并不会导致Python对传入参数的类型进行检查。

```python
>>> another_dummy(0.5)         
-0.5
>>>
```

所有的注解存储在函数的`__annotations__`属性中。

## 函数式编程

### operator模块

`operator`模块提供了Python中部分运算符或操作的函数式实现。

```python
>>> import operator
>>> operator.add(5, 3)
8
>>>
```

此外，`__getitem__`、`__getattribute__`方法在`operator`模块中也有对应实现，为`itemgetter`、`attrgetter`。`methodcaller`可以用于调用对象内的某个方法。

### functools模块

functools提供了与函数式编程相关的一系列函数工具。

`partial`用于锁定函数的一部分参数。其余参数可以在调用时指定（定位参数只能按顺序指定，关键字参数可以任意指定）：

```python
>>> from functools import partial
>>> part = partial(divmod, 3) 
>>> part(2)
(1, 1)
>>>
```

`reduce`将接受两个参数的函数应用到一个序列上，得到一个结果。借助`operator`模块中提供的运算符，`reduce`模块可以实现阶乘等需要循环才能实现的运算操作：

```python
>>> from functools import reduce
>>> def fact(x: int):
...     return reduce(operator.mul, range(1, x + 1))
... 
>>> fact(5)
120
>>>
```
