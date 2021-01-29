# Python中的映射类型

Python中最常见的映射类型是字典。本文将从字典入手对Python中的映射类型进行探讨。

## 字典

字典类型`dict`对应的抽象基类为`MutableMapping`。而`MutableMapping`是`Mapping`的子类。

`dict`中的数据组织为键-值对的形式，字典对值的类型没有要求，但要求键的类型必须可散列（hashable）。由此可见，字典结构的底层实现类似散列表，以加快字典内元素的访问速度。

Python 3.6及以后，`dict`类型在实现上是有序的，但标准并没有规定`dict`类型的有序性。

> Python 3.9中，字典对象支持`|`运算符，用于将两个字典合并为一个。当两个字典中出现重复值时右侧字典中的值优先。
> ```python
> >>> import sys 
> >>> ver = sys.version_info
> >>> if ver.major == 3 and ver.minor > 8:
> ...     a = {1: 2}
> ...     b = {3: 4}
> ...     print(a | b)
> ... 
> >>>
> ```

### 可散列类型

满足如下条件的对象称为可散列对象：

1. 如果该对象可散列，则在其生命周期中，该散列值不变
2. 对象实现了`__hash__()`与`__eq__()`方法
3. 如果它和另一个对象相等，则两者有相同的散列值

如：

```python
>>> a = "abc"
>>> b = "".join(["a", "b", "c"])
>>> a is b
False
>>> hash(a) == hash(b)
True
>>>
```

根据如上规则可以判断一些内置数据结构是否为可散列对象

* 可变序列在生命周期中序列的内容可能发生变化，因此可变序列（如`list`）不是可散列对象。
* 原子不可变数据类型满足如上所有条件，是可散列对象
* 容器`frozenset`要求其中的所有元素均为可散列对象，因此本身是可散列对象
* 容器`tuple`中可以容纳不可散列对象，因此`tuple`不是可散列对象，但不含可散列对象的元组是可散列对象。

```python
>>> t1 = hash((1, 2))
>>> t2 = hash((1, [2]))
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
TypeError: unhashable type: 'list'
>>>
```

### 构造

字典提供了多种构造方式，如下构造字典`{'a': 1, 'b': 2}`

1. 花括号构造，如`{'a': 1, 'b': 2}`
2. 通过类构造函数，如`dict(a=1, b=2)`
3. 通过元组/列表（只需是长度为2的可迭代对象）构造，如`dict([('a', 1), ['b', 2]])`
4. 通过`zip`打包构造，如`dict(zip(['a', 'b'], [1, 2]))`
5. 通过字典推导构造，如`{chr(97 + _): _ + 1 for _ in range(2)}`

## 变种

`collections`提供了字典的两个变种，即`defaultdict`与`OrderDict`

### defaultdict

当在一个字典`d`中找不到键`k`时，Python会产生`KeyError`异常。使用`d.get(k, default)`可以为找不到的键设置默认返回值。但`dict.get`函数不会对字典进行更新，插入找不到的键。

`dict.setdefault`提供了另一种从字典中获取值的方法。`setdefault`接收两个参数，第一个参数为`key`，第二个参数为可选的默认值`default`。当字典中找到`key`所对应的元素时，`setdefault`直接返回该值，否则`setdefault`会在字典中添加键值对`key: default`，然后返回`default`。

```python
>>> a = {}
>>> a.setdefault(0, True)
True
>>> a[0] = False
>>> a.setdefault(0, False) 
False
>>>
```

使用`setdefault`从字典中获取值时，可以减少字典的查询次数，提高字典执行的效率：

```python
>>> a = {}
>>> try:
...     a[0].append(True)
... except KeyError:
...     a[0] = []
...     a[0].append(True)
...        
>>> a
{0: [True]}
>>>
```

如上使用`try-except`结构处理字典中找不到值的结果，如果使用`setdefault`函数，则可以有效减少代码长度，增加代码可读性。

```python
>>> a = {}
>>> a.setdefault(0, []).append(True)
>>> a
{0: [True]}
>>>
```

`defaultdict`可以用于处理字典中缺失的键。准确地说，`defaultdict`在创建时需要提供一个可调用对象作为参数，字典中找不到键时，`defaultdict`会通过调用这个可调用对象来得到该键对应的默认值。

```python
>>> from collections import defaultdict
>>> a = defaultdict(list)
>>> a
defaultdict(<class 'list'>, {})
>>> a[False] = {}
>>> a[False]
{}
>>> a[True]
[]
>>> a
defaultdict(<class 'list'>, {False: {}, True: []})
>>>
```

如果创建`defaultdict`时没有指定参数，访问不存在的键时仍会抛出`KeyError`。

事实上，`__getitem__`通过特殊方法`__missing__`处理字典中缺失的键。手动调用`__missing__`方法能实现相同的效果：

```python
>>> from collections import defaultdict 
>>> a = defaultdict(list)
>>> a 
defaultdict(<class 'list'>, {})
>>> a.__missing__(0)  
[]
>>> a
defaultdict(<class 'list'>, {0: []})
>>>
```

`__missing__`方法的参数为`self, key`，其中`key`为缺失的键。即使`__missing__`正常执行，返回值也不会被添加到字典中。

```python
>>> class NumDict(dict):
...     def __init__(self, *args, **kwargs):
...             super().__init__(*args, **kwargs)
...     def __missing__(self, key):
...             if isinstance(key, int):
...                     return 0
...             else:
...                     raise KeyError(key)
...
>>> a = NumDict([(1, 2), ("a", "b")])
>>> a
{1: 2, 'a': 'b'}
>>> a[0]
0
>>> a['b']
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
  File "<stdin>", line 8, in __missing__
KeyError: 'b'
>>> a
{1: 2, 'a': 'b'}
>>>
```

### OrderedDict

`OrderedDict`是严格（在任何版本中）保持顺序的字典。在迭代过程中键的顺序保持一致。

`OrderedDict`新增了`popitem`方法，默认移除并返回字典中最后添加的一个元素。如果手动指定`last`参数为`False`，则移除并返回字典中第一个添加的元素。同时，`move_to_end`是与之配合的移动方法，可以将字典中的键值对（由`key`参数指定）移动到字典一端（由`last`参数指定）。

### ChainMap

`ChainMap`可以视为一种容纳映射的序列。相比于使用`dict.update()`或`|`运算符逐个合并映射，`ChainMap`有更高的效率。

`ChainMap`也可以被视为映射，当在`ChainMap`对象中查询时，`ChainMap`会逐个查询其中的映射。当同一个键出现在不同的映射中时，`ChainMap`返回查询到的第一个结果。

```python
>>> from collections import ChainMap
>>> a = ChainMap({'a': 1, 'b': 2}, {'a': 3, 'b': 4})
>>> a['b']
2
>>> a['a']
1
>>>
```

存储的映射在`ChainMap.maps`属性中，对该属性的修改会同时反映在`ChainMap`对象中。`parents`是一个通过属性方式访问的方法，返回去除原`ChainMap`中的第一个映射后的新`ChainMap`，原`ChainMap`保持不变。

`new_child`提供了向`ChainMap`中添加映射的方法。新的映射被添加到`ChainMap`的开头，如果没有提供映射，则添加一个空字典。

`ChainMap`并没有合并原有的映射，因此迭代`ChainMap`对象或对`ChainMap`对象调用`dict()`时只会应用到其中包含的第一个映射。

```python
>>> dict(a)
{'a': 1, 'b': 2}
>>>
```

### Counter

`Counter`提供了对一系列值的统计方法。可以使用可迭代对象初始化`Counter`类型，`Counter`会自动统计可迭代对象中每个值的出现顺序。

```python
>>> from collections import Counter 
>>> a = Counter([1, 1, 1, 2, 2, 3])          
>>> a
Counter({1: 3, 2: 2, 3: 1})
>>>
```

更新`Counter`对象时，计数器会相应地更新：

```python
>>> a.update([3, 3, 3, 2, 2, 1])
>>> a
Counter({1: 4, 2: 4, 3: 4})
>>>
```