# 装饰器

装饰器是一个可调用对象，接受一个函数作为参数并返回一个函数，如下定义了一个装饰器：

```python
>>> def decorator(x):
...     print(x)
...     return x
...
>>>
```

装饰器在函数定义前使用，`@`标记一个装饰器：

```python
>>> @decorator    
... def target(x):
...     return x + 1
... 
<function target at ...>
>>>
```

`@decorator`等价于如下代码，函数被装饰器返回的函数替换

```python
>>> def target(x):
...     return x + 1
... 
>>> target = decorator(target)
<function target at ...>
>>>
```

装饰器在被修饰的函数定义后立即运行。因此，当导入模块时，装饰器函数会立即执行，而被装饰的函数只会调用执行。

```python
>>> src = """def decorator(_):
...     print(_)
...     return _
... print("Before A")
... @decorator
... def a():
...     return 1
... print("Before B")
... @decorator  
... def b():
...     return 1
... print("After B")
... """
>>> exec(src)
Before A
<function a at ...>
Before B
<function b at ...>
After B
>>>
```

## 变量的作用域

Python会自动判断函数代码中的变量是否为局部变量。所有在函数代码内出现的变量被视为局部变量。

```python
>>> b = 2
>>> def A():
...     print(b)
... 
>>> def B():
...     print(b)
...     b = 2
... 
>>> A()
2
>>> B()
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
  File "<stdin>", line 2, in B
UnboundLocalError: local variable 'b' referenced before assignment
>>>
```

因此，如果需要在函数内部访问全局变量，需要使用`global`关键字声明。

```python
>>> def C():
...     global b
...     print(b)
...     b = 3
... 
>>> b
2
>>> C()
2
>>> b
3
>>>
```

检查编译后的字节码，发现`global`关键字声明变量由`LOAD_FAST`与`STORE_FAST`改为了`LOAD_GLOBAL`与`STORE_GLOBAL`：

## 闭包

闭包是扩展了函数作用域的函数，可以访问函数定义之外的局部变量。以下通过不同方式实现滑动平均值的计算：

* 使用类
  
  ```python
  >>> class avg1():
  ...     def __init__(self):
  ...             self.values = []
  ...     def __call__(self, value):
  ...             self.values.append(value)
  ...             return sum(self.values) / len(self.values)
  ... 
  >>> avg = avg1()
  >>> avg(10)
  10.0
  >>> avg(11)
  10.5
  >>>
  ```

* 使用高阶函数

  ```python
  >>> def avg2():
  ...     values = []
  ...     def avg(value): 
  ...             values.append(value)
  ...             return sum(values) / len(values)
  ...     return avg
  >>> 
  >>> avg = avg2()
  >>> avg(10)
  10.0
  >>> avg(11)
  10.5
  >>>
  ```

在`avg2`函数结束后，局部变量`values`原有的作用域消失，成为自由变量。自由变量指没有在本地作用域中绑定的变量。`values`变量的引用存储在`avg`函数的`__closure__`属性中。即使`avg2`函数已经结束执行，`avg`函数仍然能访问`values`变量。
