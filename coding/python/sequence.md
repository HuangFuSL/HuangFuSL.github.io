# Python中的序列类型

序列指可以存储多个数据的数据结构。

按照存储的数据类型可以分为：

* 容器可以存储不同类型的数据，这部分类型有`list`、`tuple`、`collections.deque`
* 扁平序列只能存储某种类型的数据，这部分类型有`str`、`bytes`、`bytearray`、`memoryview`、`array.array`

按照序列是否可以修改可以分为

* 可变序列：`list`、`bytearray`、`array.array`、`collections.deque`、`memoryview`
* 不可变序列：`tuple`、`str`、`bytes`

## 列表

列表是可以修改的序列，可以存储多种不同类型的数据结构。如下着重讨论列表推导的书写形式。

列表推导可用于从一个列表生成新的列表，相比于for循环加`append()`方法，列表推导的写法有更好的可读性。

列表推导示例：

```python
a = [1, 2, 3]
b = [_ ** 2 for _ in a]
```

Python 3.x中的列表推导不会产生变量泄露的问题，如下：

```python
x = 'ABC'
y = [x for x in x]
print(x)
```

输出为`ABC`，说明列表推导变量`x`的值没有传递到外部。

列表推导等价于`map`与`filter`的结合。`map`函数接收两个参数。第一个参数为函数，第二个参数为可迭代对象。`map`函数迭代地将函数作用于可迭代对象，从而得到结果。

列表推导可以用于计算列表的笛卡尔积，如下列代码：

```python
[(x, y) for x in range(10) for y in range(11, 20)]
```

循环的顺序与`for`循环一致，先执行外层的循环，再执行内层的循环。

将列表推导的方括号圆括号，即为生成器表达式。如果生成器表达式是函数调用的唯一参数，圆括号可以省略。

## 元组

元组是不可变的序列，可以理解为字段的集合，对应数据表中的某一行。如下着重讨论元组解包的内容。

平行赋值可以将一个可迭代对象中的元素复制到一组变量中。可迭代对象不要求是元组。如：

```python
a, b = (1, 2)
c, d = [3, 4]
e, f = {1: 2, 3: 4} # 按照key的取值进行分配
```

`*`运算符可以用于解包元组中的值作为函数参数，如：

```python
print(*(1, 2))
```

`*`运算符可以用于从函数中获取可变数量的参数，常见用法为`*args`与`**kwargs`。

`*`运算符还可以用于平行赋值中，但平行赋值中的一组变量只能出现一个`*`运算符。带`*`的变量解包后成为列表。

```python
a, b, c, *d = range(5) # d = [3, 4]
a, b, *c, d = range(5) # c = [2, 3]
```

当待解包的元组本身是元组时，可以使用括号解包，如：

```python
a, (b, c), d = (1, (2, 3), 4)
```

元组不支持列表的`append`、`clear`、`copy`、`extend`、`insert`、`pop`、`remove`、`reverse`等方法。

### 具名元组

`collections.namedtuple`提供了用于创建具名元组类型的方法，其参数列表如下：

```python
collections.namedtuple(typename, field_names, *, rename=False, defaults=None, module=None)
```

* `typename`指类型的名称，该变量被写入`__repr__`方法中。该参数的取值与代码中类型被实际分配的名称无关。
* `field_names`是元组中字段的名称
* 当`rename`为`True`重复或与关键字冲突的字段名称会被自动处理，否则会抛出`ValueError`
* `defaults`为字段的默认值，该列表与字段名称列表按右对齐进行匹配。
* 若提供了`module`参数，该值会被写入`__module__`属性中。

`namedtuple`返回可以用于创建对象的类型。

```python
>>> from collections import namedtuple
>>> Point = namedtuple('Point', ["x", "y"], defaults=[1, 2]) 
>>> Point()
Point(x=1, y=2)
>>> Point(2)
Point(x=2, y=2)
>>> Point(2, 3)
Point(x=2, y=3)
>>>
```

## 切片

切片是在序列上执行的操作，切片操作得到一个新的序列。切片以`s[a:b:c]`的形式指定，`a`为起始下标、`b`为终止下标（不包含）、`c`为步长（可以为负）。

* `s[::-1]`等价于反转`s`中的元素
* 切片并没有创建新的对象，对切片的修改会反映到原序列中。但对切片的修改必须满足元素数量相同的条件，否则会抛出`ValueError`。

另一种切片的方式为`s[slice(a, b, c)]`，省略的参数使用`None`表示。因此`s[::-1]`等价于`s[slice(None, None, -1)]`。事实上，Python在处理形如`s[a:b:c]`的切片时会调用`s.__getitem__(slice(start, stop, step))`

在NumPy数组的切片中有时会出现省略的情况，此时可以使用`...`。`...`符号会被Python解释为`EllipsisType`类型的常量。

## 序列运算

序列通常支持`+`运算与`*`运算。与切片不同，这两个运算直接创建一个新的序列。

```python
>>> a = [1]
>>> b = [2] 
>>> c = a + b
>>> c is a
False
>>>
```

`+`运算局限于相同类型，对于`list`等可变类型，`a + b`等价于`a.extend(b)`。但`a.extend(b)`方法对`b`的类型无要求，仅需要`b`可迭代。

`*`运算符的第二个操作数`y`必须为整数，表示将序列重复`y`次。若`y<=0`，则返回空列表

**注意**，`*`运算符得到的列表中，列表多次重复的部分以引用的形式存储，如下所示：

```python
>>> b = [[]] * 3
>>> b[0].append(1)
>>> b
[[1], [1], [1]]
>>>
```

`append`处理可变对象的方式同样是复制引用而不是复制值，因此也会造成相同的问题：

```python
>>> a = []
>>> b = []
>>> for i in range(3):
...     a.append(b)
... 
>>> a[0].append(1)
>>> a
[[1], [1], [1]]
>>>
```

因此要避免使用`*`运算符处理包含可变对象的列表。建议使用列表推导创建嵌套列表。

与序列的运算不同，（可变）序列的增量运算`+=`、`*=`是在原序列的基础上进行的，不会创建新的序列对象。不可变序列不支持增量运算。

***

考虑如下代码：

```python
>>> a = [1, 2, 3]
>>> a[2] += 5
>>> a
[1, 2, 8]
>>>
```

可变序列通过`__setitem__`方法实现了切片的修改。若`a`为不可变序列，执行结果应为何？

对于不可变序列，其本身不支持对元素进行的修改，因此序列本身的值不会改变。

```python
>>> a = (1, 2, 3)
>>> a[2] += 5
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
TypeError: 'tuple' object does not support item assignment
>>> a
(1, 2, 3)
>>>
```

但如果要修改的元素本身是引用，如一个可变序列，此时对可变序列的修改不会影响到引用本身，因此`+=`运算仍会正常作用。增量操作不是原子操作。

```python
>>> t = (1, 2, [30, 40])
>>> t[2] += [50, 60]
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
TypeError: 'tuple' object does not support item assignment
>>> t
(1, 2, [30, 40, 50, 60])
>>>
```

如果使用`append`或`extend`方法，则可以避免异常的产生。可变序列被 **正常修改** 。为保证数据不被错误地修改，应避免在不可变序列中容纳可变对象。

## 排序

`list.sort`方法作用与列表本身而不返回（返回值为`None`）。要产生一个新的已排序列表而不影响原列表，可以使用`sorted()`内置函数。

```python
>>> a = [6, 3, 2, 1]
>>> b = sorted(a)
>>> b is a
False
>>>
```

`sorted`与`list.sort`支持按照其他规则对序列进行排序，即`key`参数。`key`参数为只有一个参数的函数，如`key=len`即为对字符串长度升序排序，`key=lower`即为忽略字符串大小写进行升序排序。

Python的`bisect`模块提供了对二分查找的支持。`bisect.bisect`为二分查找函数，返回在目标数组中大于待查元素的第一个值的位置。`bisect.insort`为插入函数，在`bisect`函数查询位置插入元素。

`bisect`与`insort`函数有变种`bisect_left`与`insort_left`。`bisect_left`返回在目标数组中不大于待查元素的最后一个值的位置。

## 其他序列类型

### 数组

`array`模块提供了数组结构的支持。数组是只能存储一种类型元素的可变序列，支持`list`的多数方法。同时数组提供了`fromfile, tofile`与`frombytes, tobytes`，从而支持直接读写文件或比特流。

在创建数组时需要指定类型码，即数组中存储的数据类型。每一个类型码对应的类型只占用有限的内存空间。在存储大量数据时优于列表等其他可变序列。

|类型码|C 类型|Python 类型|字宽|
|:-:|:-:|:-:|:-:|
|`'b'`|`signed char`|`int`|1|
|`'B'`|`unsigned char`|`int`|1|
|`'u'`|`wchar_t`|Unicode character|2|
|`'h'`|`signed short`|`int`|2|
|`'H'`|`unsigned short`|`int`|2|
|`'i'`|`signed int`|`int`|2|
|`'I'`|`unsigned int`|`int`|2|
|`'l'`|`signed long`|`int`|4|
|`'L'`|`unsigned long`|`int`|4|
|`'q'`|`signed long long`|`int`|8|
|`'Q'`|`unsigned long long`|`int`|8|
|`'f'`|`float`|`float`|4|
|`'d'`|`double`|`float`|8|

数组不支持列表的如下方法：

* `clear`
* `copy`
* `sort`

但数组支持从列表添加对象，即`fromlist`方法。当列表中一个元素在添加过程中出错，则所有的添加都会被回滚。

```python
>>> import array
>>> a = array.array('f')
>>> b = [1.0, 2.0, 'a']
>>> a
array('f')
>>> a.fromlist(b)
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
TypeError: must be real number, not str
>>> a
array('f')
>>>
```

数组是bytes-like object，因此可以用于内存视图中。

### 内存视图

`memoryview`允许使用不同的方式读写同一块内存的数据。

如下创建一个映射到字节序列的`memoryview`，在不执行操作时，`memory`的数据内容与原序列的数据内容相同。

```python
>>> a = [1, 2, 3, 4]
>>> b = memoryview(array.array('i', a))
>>> b[0]
1
>>>
```

使用`memoryview.cast`方法可以将`memoryview`映射的内存区域以不同的方式进行解释。

```python
>>> c = b.cast('B')
>>> list(c)
[1, 0, 0, 0, 2, 0, 0, 0, 3, 0, 0, 0, 4, 0, 0, 0]
>>>
```

`memoryview`的可变性取决于其所映射内存区域的性质，若使用不可变序列创建`memoryview`，则`memoryview`为不可变序列。

```python
>>> d = memoryview(b"abc") 
>>> d[0] = "d"
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
TypeError: cannot modify read-only memory
>>>
```

作为可变序列的`memoryview`可以被修改，再转换为原来的解释方式，即可实现对序列中某个特定字节的修改。

```python
>>> c[1] = 1 
>>> b = c.cast("i")
>>> list(b)
[257, 2, 3, 4]
>>>
```

`memoryview`的切片是一个新的`memoryview`对象（基于原字节序列）

### 队列

列表的`append`与`pop`方法组合使用可以实现对栈或队列的模拟。`collection.deque`提供了队列的更高效的实现，并且满足线程安全的条件。

在创建队列时，可选提供队列的最大长度`maxlen`。该参数只能在构造函数中指定，在对象中只读。

队列提供如下方法：

* `rotate`，当参数`n > 0`时将队列右侧的`n`个元素移动到队列左侧，反之将队列左侧的`n`个元素移动到队列右侧
* `appendleft`，在队列的左侧添加元素（当超出队列长度时，会从队列另一侧删除）
* `extendleft`，在队列的左侧添加一组元素（当超出队列长度时，会从队列另一侧删除）
* 队列支持列表的大多数方法，除`copy`、`sort`、`insert`、`index`等方法，队列仅支持`+=`运算符的作用。