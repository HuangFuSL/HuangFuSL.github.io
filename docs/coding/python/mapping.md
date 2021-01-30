# Python中的映射类型

Python中最常见的映射类型是字典。本文将从字典入手对Python中的映射类型进行探讨。

## 字典

字典类型`dict`对应的抽象基类为`MutableMapping`。而`MutableMapping`是`Mapping`的子类。

`dict`中的数据组织为键-值对的形式，字典对值的类型没有要求，但要求键的类型必须可散列（hashable）。由此可见，字典结构的底层实现类似散列表，以加快字典内元素的访问速度。字典的执行效率远高于列表。

Python 3.6及以后，`dict`类型在实现上是有序的，键的顺序取决于添加顺序，但标准并没有规定`dict`类型的有序性。因此两个键顺序不同的字典被视为相同。

```python
>>> a = {1: 2, 2: 1}
>>> b = {2: 1, 1: 2}
>>> a == b
True
>>>
```

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

映射类型通常是可修改的，使用`types.MappingProxyType`会创建一个原映射的视图。对原映射的任何修改都会反映在视图中，但不能对视图进行任何直接的修改。此方法间接地创建一个不可修改的映射类型。

```python
>>> from types import MappingProxyType
>>> a = {1: 2, 3: 4}
>>> b = MappingProxyType(a)
>>> b
mappingproxy({1: 2, 3: 4})
>>> a.update({1: 5})
>>> b
mappingproxy({1: 5, 3: 4})
>>> b[1] = 2
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
TypeError: 'mappingproxy' object does not support item assignment
>>>
```

### 可散列类型

满足如下条件的对象称为可散列对象：

1. 如果该对象可散列，则在其生命周期中，该散列值不变
2. 对象实现了`__hash__()`与`__eq__()`方法（没有实现`__eq__()`方法的对象不应实现`__hash__()`方法）
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

注：若一个自定义类型定义了`__eq__`，且没有定义`__hash__`，`__hash__`会被设为`None`。可散列的自定义对象必须有`__hash__`方法。

> 以下内容来自于Python文档
> <iframe srcdoc="&lt;link href=&quot;https://docs.python.org/3/_static/classic.css&quot; rel=&quot;stylesheet&quot; type=&quot;text/css&quot;/&gt;&lt;link href=&quot;https://docs.python.org/3/_static/basic.css&quot; rel=&quot;stylesheet&quot; type=&quot;text/css&quot;/&gt;&lt;link href=&quot;https://docs.python.org/3/_static/pydoctheme.css&quot; rel=&quot;stylesheet&quot; type=&quot;text/css&quot;/&gt;&lt;p&gt;If a class does not define an &lt;a class=&quot;reference internal&quot; target=&quot;_blank&quot; href=&quot;https://docs.python.org/3/reference/datamodel.html#object.__eq__&quot; title=&quot;object.__eq__&quot;&gt;&lt;code class=&quot;xref py py-meth docutils literal notranslate&quot;&gt;&lt;span class=&quot;pre&quot;&gt;__eq__()&lt;/span&gt;&lt;/code&gt;&lt;/a&gt; method it should not define a&lt;a class=&quot;reference internal&quot; target=&quot;_blank&quot; href=&quot;https://docs.python.org/3/reference/datamodel.html#object.__hash__&quot; title=&quot;object.__hash__&quot;&gt;&lt;code class=&quot;xref py py-meth docutils literal notranslate&quot;&gt;&lt;span class=&quot;pre&quot;&gt;__hash__()&lt;/span&gt;&lt;/code&gt;&lt;/a&gt; operation either; if it defines &lt;a class=&quot;reference internal&quot; target=&quot;_blank&quot; href=&quot;https://docs.python.org/3/reference/datamodel.html#object.__eq__&quot; title=&quot;object.__eq__&quot;&gt;&lt;code class=&quot;xref py py-meth docutils literal notranslate&quot;&gt;&lt;span class=&quot;pre&quot;&gt;__eq__()&lt;/span&gt;&lt;/code&gt;&lt;/a&gt; but not&lt;a class=&quot;reference internal&quot; target=&quot;_blank&quot; href=&quot;https://docs.python.org/3/reference/datamodel.html#object.__hash__&quot; title=&quot;object.__hash__&quot;&gt;&lt;code class=&quot;xref py py-meth docutils literal notranslate&quot;&gt;&lt;span class=&quot;pre&quot;&gt;__hash__()&lt;/span&gt;&lt;/code&gt;&lt;/a&gt;, its instances will not be usable as items in hashablecollections.  If a class defines mutable objects and implements an&lt;a class=&quot;reference internal&quot; target=&quot;_blank&quot; href=&quot;https://docs.python.org/3/reference/datamodel.html#object.__eq__&quot; title=&quot;object.__eq__&quot;&gt;&lt;code class=&quot;xref py py-meth docutils literal notranslate&quot;&gt;&lt;span class=&quot;pre&quot;&gt;__eq__()&lt;/span&gt;&lt;/code&gt;&lt;/a&gt; method, it should not implement &lt;a class=&quot;reference internal&quot; target=&quot;_blank&quot; href=&quot;https://docs.python.org/3/reference/datamodel.html#object.__hash__&quot; title=&quot;object.__hash__&quot;&gt;&lt;code class=&quot;xref py py-meth docutils literal notranslate&quot;&gt;&lt;span class=&quot;pre&quot;&gt;__hash__()&lt;/span&gt;&lt;/code&gt;&lt;/a&gt;, since theimplementation of hashable collections requires that a key’s hash value isimmutable (if the object’s hash value changes, it will be in the wrong hashbucket).&lt;/p&gt;&lt;p&gt;User-defined classes have &lt;a class=&quot;reference internal&quot; target=&quot;_blank&quot; href=&quot;https://docs.python.org/3/reference/datamodel.html#object.__eq__&quot; title=&quot;object.__eq__&quot;&gt;&lt;code class=&quot;xref py py-meth docutils literal notranslate&quot;&gt;&lt;span class=&quot;pre&quot;&gt;__eq__()&lt;/span&gt;&lt;/code&gt;&lt;/a&gt; and &lt;a class=&quot;reference internal&quot; target=&quot;_blank&quot; href=&quot;https://docs.python.org/3/reference/datamodel.html#object.__hash__&quot; title=&quot;object.__hash__&quot;&gt;&lt;code class=&quot;xref py py-meth docutils literal notranslate&quot;&gt;&lt;span class=&quot;pre&quot;&gt;__hash__()&lt;/span&gt;&lt;/code&gt;&lt;/a&gt; methodsby default; with them, all objects compare unequal (except with themselves)and &lt;code class=&quot;docutils literal notranslate&quot;&gt;&lt;span class=&quot;pre&quot;&gt;x.__hash__()&lt;/span&gt;&lt;/code&gt; returns an appropriate value such that &lt;code class=&quot;docutils literal notranslate&quot;&gt;&lt;span class=&quot;pre&quot;&gt;x&lt;/span&gt; &lt;span class=&quot;pre&quot;&gt;==&lt;/span&gt; &lt;span class=&quot;pre&quot;&gt;y&lt;/span&gt;&lt;/code&gt;implies both that &lt;code class=&quot;docutils literal notranslate&quot;&gt;&lt;span class=&quot;pre&quot;&gt;x&lt;/span&gt; &lt;span class=&quot;pre&quot;&gt;is&lt;/span&gt; &lt;span class=&quot;pre&quot;&gt;y&lt;/span&gt;&lt;/code&gt; and &lt;code class=&quot;docutils literal notranslate&quot;&gt;&lt;span class=&quot;pre&quot;&gt;hash(x)&lt;/span&gt; &lt;span class=&quot;pre&quot;&gt;==&lt;/span&gt; &lt;span class=&quot;pre&quot;&gt;hash(y)&lt;/span&gt;&lt;/code&gt;.&lt;/p&gt;&lt;p&gt;A class that overrides &lt;a class=&quot;reference internal&quot; target=&quot;_blank&quot; href=&quot;https://docs.python.org/3/reference/datamodel.html#object.__eq__&quot; title=&quot;object.__eq__&quot;&gt;&lt;code class=&quot;xref py py-meth docutils literal notranslate&quot;&gt;&lt;span class=&quot;pre&quot;&gt;__eq__()&lt;/span&gt;&lt;/code&gt;&lt;/a&gt; and does not define &lt;a class=&quot;reference internal&quot; target=&quot;_blank&quot; href=&quot;https://docs.python.org/3/reference/datamodel.html#object.__hash__&quot; title=&quot;object.__hash__&quot;&gt;&lt;code class=&quot;xref py py-meth docutils literal notranslate&quot;&gt;&lt;span class=&quot;pre&quot;&gt;__hash__()&lt;/span&gt;&lt;/code&gt;&lt;/a&gt;will have its &lt;a class=&quot;reference internal&quot; target=&quot;_blank&quot; href=&quot;https://docs.python.org/3/reference/datamodel.html#object.__hash__&quot; title=&quot;object.__hash__&quot;&gt;&lt;code class=&quot;xref py py-meth docutils literal notranslate&quot;&gt;&lt;span class=&quot;pre&quot;&gt;__hash__()&lt;/span&gt;&lt;/code&gt;&lt;/a&gt; implicitly set to &lt;code class=&quot;docutils literal notranslate&quot;&gt;&lt;span class=&quot;pre&quot;&gt;None&lt;/span&gt;&lt;/code&gt;.  When the&lt;a class=&quot;reference internal&quot; target=&quot;_blank&quot; href=&quot;https://docs.python.org/3/reference/datamodel.html#object.__hash__&quot; title=&quot;object.__hash__&quot;&gt;&lt;code class=&quot;xref py py-meth docutils literal notranslate&quot;&gt;&lt;span class=&quot;pre&quot;&gt;__hash__()&lt;/span&gt;&lt;/code&gt;&lt;/a&gt; method of a class is &lt;code class=&quot;docutils literal notranslate&quot;&gt;&lt;span class=&quot;pre&quot;&gt;None&lt;/span&gt;&lt;/code&gt;, instances of the class willraise an appropriate &lt;a class=&quot;reference internal&quot; target=&quot;_blank&quot; href=&quot;https://docs.python.org/3/library/exceptions.html#TypeError&quot; title=&quot;TypeError&quot;&gt;&lt;code class=&quot;xref py py-exc docutils literal notranslate&quot;&gt;&lt;span class=&quot;pre&quot;&gt;TypeError&lt;/span&gt;&lt;/code&gt;&lt;/a&gt; when a program attempts to retrievetheir hash value, and will also be correctly identified as unhashable whenchecking &lt;code class=&quot;docutils literal notranslate&quot;&gt;&lt;span class=&quot;pre&quot;&gt;isinstance(obj,&lt;/span&gt; &lt;span class=&quot;pre&quot;&gt;collections.abc.Hashable)&lt;/span&gt;&lt;/code&gt;.&lt;/p&gt;&lt;p&gt;If a class that overrides &lt;a class=&quot;reference internal&quot; target=&quot;_blank&quot; href=&quot;https://docs.python.org/3/reference/datamodel.html#object.__eq__&quot; title=&quot;object.__eq__&quot;&gt;&lt;code class=&quot;xref py py-meth docutils literal notranslate&quot;&gt;&lt;span class=&quot;pre&quot;&gt;__eq__()&lt;/span&gt;&lt;/code&gt;&lt;/a&gt; needs to retain the implementationof &lt;a class=&quot;reference internal&quot; target=&quot;_blank&quot; href=&quot;https://docs.python.org/3/reference/datamodel.html#object.__hash__&quot; title=&quot;object.__hash__&quot;&gt;&lt;code class=&quot;xref py py-meth docutils literal notranslate&quot;&gt;&lt;span class=&quot;pre&quot;&gt;__hash__()&lt;/span&gt;&lt;/code&gt;&lt;/a&gt; from a parent class, the interpreter must be told thisexplicitly by setting &lt;code class=&quot;docutils literal notranslate&quot;&gt;&lt;span class=&quot;pre&quot;&gt;__hash__&lt;/span&gt; &lt;span class=&quot;pre&quot;&gt;=&lt;/span&gt; &lt;span class=&quot;pre&quot;&gt;&lt;ParentClass&gt;.__hash__&lt;/span&gt;&lt;/code&gt;.&lt;/p&gt;&lt;p&gt;If a class that does not override &lt;a class=&quot;reference internal&quot; target=&quot;_blank&quot; href=&quot;https://docs.python.org/3/reference/datamodel.html#object.__eq__&quot; title=&quot;object.__eq__&quot;&gt;&lt;code class=&quot;xref py py-meth docutils literal notranslate&quot;&gt;&lt;span class=&quot;pre&quot;&gt;__eq__()&lt;/span&gt;&lt;/code&gt;&lt;/a&gt; wishes to suppress hashsupport, it should include &lt;code class=&quot;docutils literal notranslate&quot;&gt;&lt;span class=&quot;pre&quot;&gt;__hash__&lt;/span&gt; &lt;span class=&quot;pre&quot;&gt;=&lt;/span&gt; &lt;span class=&quot;pre&quot;&gt;None&lt;/span&gt;&lt;/code&gt; in the class definition.A class which defines its own &lt;a class=&quot;reference internal&quot; target=&quot;_blank&quot; href=&quot;https://docs.python.org/3/reference/datamodel.html#object.__hash__&quot; title=&quot;object.__hash__&quot;&gt;&lt;code class=&quot;xref py py-meth docutils literal notranslate&quot;&gt;&lt;span class=&quot;pre&quot;&gt;__hash__()&lt;/span&gt;&lt;/code&gt;&lt;/a&gt; that explicitly raisesa &lt;a class=&quot;reference internal&quot; target=&quot;_blank&quot; href=&quot;https://docs.python.org/3/library/exceptions.html#TypeError&quot; title=&quot;TypeError&quot;&gt;&lt;code class=&quot;xref py py-exc docutils literal notranslate&quot;&gt;&lt;span class=&quot;pre&quot;&gt;TypeError&lt;/span&gt;&lt;/code&gt;&lt;/a&gt; would be incorrectly identified as hashable byan &lt;code class=&quot;docutils literal notranslate&quot;&gt;&lt;span class=&quot;pre&quot;&gt;isinstance(obj,&lt;/span&gt; &lt;span class=&quot;pre&quot;&gt;collections.abc.Hashable)&lt;/span&gt;&lt;/code&gt; call.&lt;/p&gt;" style="border-width: 0px; display: block;" width="100%" height="300px"></iframe>

根据如上规则可以判断一些内置数据结构是否为可散列对象

* 可变序列在生命周期中序列的内容可能发生变化，因此可变序列（如`list`、`set`等）不是可散列对象。
* 原子不可变数据类型满足如上所有条件，是可散列对象
* 容器`frozenset`要求其中的所有元素均为可散列对象，并且其中内容在整个生命周期中不会发生变化，因此是可散列对象
* 容器`tuple`中可以容纳不可散列对象，因此`tuple`不是可散列对象，但不含可散列对象的元组是可散列对象。

```python
>>> t1 = hash((1, 2))
>>> t2 = hash((1, [2]))
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
TypeError: unhashable type: 'list'
>>>
```

使用`hash`函数可以取得可散列对象的散列值。为了避免DOS攻击，在计算散列值时会加上一个随机的噪声。噪声的值仅在同一Python实例中相同。对于一个整数，若它的值小于散列值所允许的最大值（即可以被放进散列值所限定的空间内），则散列的值就是该整数的值。

散列表的使用是“空间换时间”策略的典型体现。为了尽可能减少冲突，散列表必须有较低的装填因子，这意味着散列表会占用更多的内存空间。

### 构造

字典提供了多种构造方式，如下构造字典`{'a': 1, 'b': 2}`

1. 花括号构造，如`{'a': 1, 'b': 2}`
2. 通过类构造函数，如`dict(a=1, b=2)`
3. 通过元组/列表（只需是长度为2的可迭代对象）构造，如`dict([('a', 1), ['b', 2]])`
4. 通过`zip`打包构造，如`dict(zip(['a', 'b'], [1, 2]))`
5. 通过字典推导构造，如`{chr(97 + _): _ + 1 for _ in range(2)}`

### 变种

`collections`提供了字典的两个变种，即`defaultdict`与`OrderDict`

#### defaultdict

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

#### OrderedDict

`OrderedDict`是严格（在任何版本中）保持顺序的字典。在迭代过程中键的顺序保持一致。

`OrderedDict`新增了`popitem`方法，默认移除并返回字典中最后添加的一个元素。如果手动指定`last`参数为`False`，则移除并返回字典中第一个添加的元素。同时，`move_to_end`是与之配合的移动方法，可以将字典中的键值对（由`key`参数指定）移动到字典一端（由`last`参数指定）。

#### ChainMap

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

#### Counter

`Counter`提供了对一系列值的统计方法。可以使用可迭代对象初始化`Counter`类型，`Counter`会自动统计可迭代对象中每个值的出现顺序。

> `Counter`不会对输入的值进行检查，如果使用字典初始化并提供非整数类型的值，在调用`Counter.most_common()`方法或迭代`Counter.elements()`的返回值时会抛出`TypeError`异常。
> ```python
> >>> from collections import Counter
> >>> a = Counter({'0': '0'})
> >>> for i in a.elements():
> ...     pass
> ...
> Traceback (most recent call last):
>   File "<stdin>", line 1, in <module>
> TypeError: 'str' object cannot be interpreted as an integer
> ```
> 
> 这一点在Python文档中有相应说明：
>
> <iframe style="border-width: 0px;" width="100%" height="360px" scrolling="no" srcdoc="&lt;link rel=&quot;stylesheet&quot; type=&quot;text/css&quot; href=&quot;https://docs.python.org/3/_static/classic.css&quot; /&gt;&lt;link rel=&quot;stylesheet&quot; type=&quot;text/css&quot; href=&quot;https://docs.python.org/3/_static/basic.css&quot; /&gt;&lt;link rel=&quot;stylesheet&quot; type=&quot;text/css&quot; href=&quot;https://docs.python.org/3/_static/pydoctheme.css&quot; /&gt;&lt;div class=&quot;admonition note&quot;&gt;&lt;p class=&quot;admonition-title&quot;&gt;Note&lt;/p&gt;&lt;p&gt;&lt;span class=&quot;highlighted&quot;&gt;Counter&lt;/span&gt;s were primarily designed to work with positive integers to represent running counts; however, care was taken to not unnecessarily preclude use cases needing other types or negative values.  To help with those use cases, this section documents the minimum range and type restrictions.&lt;/p&gt;&lt;ul class=&quot;simple&quot;&gt;&lt;li&gt;&lt;p&gt;The &lt;a class=&quot;reference internal&quot; target=&quot;_blank&quot; href=&quot;https://docs.python.org/3/library/collections.html#collections.Counter&quot; title=&quot;collections.Counter&quot;&gt;&lt;code class=&quot;xref py py-class docutils literal notranslate&quot;&gt;&lt;span class=&quot;pre&quot;&gt;&lt;span class=&quot;highlighted&quot;&gt;Counter&lt;/span&gt;&lt;/span&gt;&lt;/code&gt;&lt;/a&gt; class itself is a dictionary subclass with no restrictions on its keys and values.  The values are intended to be numbers representing counts, but you &lt;em&gt;could&lt;/em&gt; store anything in the value field.&lt;/p&gt;&lt;/li&gt;&lt;li&gt;&lt;p&gt;The &lt;a class=&quot;reference internal&quot; target=&quot;_blank&quot; href=&quot;https://docs.python.org/3/library/collections.html#collections.Counter.most_common&quot; title=&quot;collections.Counter.most_common&quot;&gt;&lt;code class=&quot;xref py py-meth docutils literal notranslate&quot;&gt;&lt;span class=&quot;pre&quot;&gt;most_common()&lt;/span&gt;&lt;/code&gt;&lt;/a&gt; method requires only that the values be orderable.&lt;/p&gt;&lt;/li&gt;&lt;li&gt;&lt;p&gt;For in-place operations such as &lt;code class=&quot;docutils literal notranslate&quot;&gt;&lt;span class=&quot;pre&quot;&gt;c[key]&lt;/span&gt; &lt;span class=&quot;pre&quot;&gt;+=&lt;/span&gt; &lt;span class=&quot;pre&quot;&gt;1&lt;/span&gt;&lt;/code&gt;, the value type need only support addition and subtraction.  So fractions, floats, and decimals would work and negative values are supported.  The same is also true for&lt;a class=&quot;reference internal&quot; href=&quot;https://docs.python.org/3/library/collections.html#collections.Counter.update&quot; title=&quot;collections.Counter.update&quot;&gt;&lt;code class=&quot;xref py py-meth docutils literal notranslate&quot;&gt;&lt;span class=&quot;pre&quot;&gt;update()&lt;/span&gt;&lt;/code&gt;&lt;/a&gt; and &lt;a class=&quot;reference internal&quot; target=&quot;_blank&quot; href=&quot;https://docs.python.org/3/library/collections.html#collections.Counter.update&quot; title=&quot;collections.Counter.subtract&quot;&gt;&lt;code class=&quot;xref py py-meth docutils literal notranslate&quot;&gt;&lt;span class=&quot;pre&quot;&gt;subtract()&lt;/span&gt;&lt;/code&gt;&lt;/a&gt; which allow negative and zero values for both inputs and outputs.&lt;/p&gt;&lt;/li&gt;&lt;li&gt;&lt;p&gt;The multiset methods are designed only for use cases with positive values. The inputs may be negative or zero, but only outputs with positive values are created.  There are no type restrictions, but the value type needs to support addition, subtraction, and comparison.&lt;/p&gt;&lt;/li&gt;&lt;li&gt;&lt;p&gt;The &lt;a class=&quot;reference internal&quot; target=&quot;_blank&quot; href=&quot;https://docs.python.org/3/library/collections.html#collections.Counter.update&quot; title=&quot;collections.Counter.elements&quot;&gt;&lt;code class=&quot;xref py py-meth docutils literal notranslate&quot;&gt;&lt;span class=&quot;pre&quot;&gt;elements()&lt;/span&gt;&lt;/code&gt;&lt;/a&gt; method requires integer counts.  It ignores zero and negative counts.&lt;/p&gt;&lt;/li&gt;&lt;/ul&gt;&lt;/div&gt;&lt;script type=&quot;text/javascript&quot; src=&quot;../_static/switchers.js&quot;&gt;&lt;/script&gt;"></iframe>

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

`Counter.elements()`方法返回一个迭代器，每个元素按照其出现次数重复。`Counter.most_common`方法返回计数器中出现次数最多的元素。

`Counter`类型提供了`+`、`-`、`&`和`|`运算符，分别对应计数器的相加、相减、交和并操作。当`+`、`-`被用作一元运算符时，另一个操作数默认为空计数器。

### 扩展

`collections.UserDict`类是对`dict`的Python实现，可以用于自定义映射类型的实现。

`UserDict`不是`dict`的子类，但`UserDict`中有一个`dict`类型的`data`属性，是`UserDict`存储数据的最终位置。相比于直接对`dict`类型进行扩展，`data`属性保证了`__getitem__`方法不会产生循环递归的情况。

`UserDict`类继承自`_collections_abc.MutableMapping`与`_collections_abc.Mapping`类。`MutableMapping`提供了`update()`方法。方法的内部实现表明，`update()`在内部通过`__setitem__`实现。`Mapping`提供了`get()`方法，该方法在内部通过`__getitem__`实现。

```python
>>> from collections import UserDict
>>> class myDict(UserDict):
...     def __init__(self, *args, **kwargs):
...             super().__init__(*args, **kwargs)  
...     def __setitem__(self, index, value):
...             print("Modification: ", index, ":", value)
...             super().__setitem__(index, value)
... 
>>> a = myDict()
>>> a.update(a=5, b=4)
Modification:  a : 5
Modification:  b : 4
>>>
```

## 集合

集合`set`是一种序列类型，集合中的各个元素最多只能出现一次。任何非空集合可以使用字面表示法`{}`进行表示，空集只能用`set()`表示。集合同样适用于与列表推导相似的推导方式。

集合有对应的只读变种`frozenset`。`set`可以通过字面表示法进行构造，或使用可迭代对象进行构造。`frozenset`只能使用可迭代对象构造。

> 可以利用`set`中元素的唯一性去除列表中的重复值：
> 
> ```python
> >>> src_list = [1, 1, 2, 3, 4, 2, 3]
> >>> list(set(src_list))
> [1, 2, 3, 4]
> >>>
> ```
> 
> 另一种方法是通过`collections.Counter`去重。
> 
> ```python
> >>> from collections import Counter
> >>> src_list = [1, 1, 2, 3, 4, 2, 3]
> >>> list(Counter(src_list).keys())
> [1, 2, 3, 4]
> >>>
> ```

和字典的键一样，集合中的元素必须是可散列的。`set`类型本身不可散列，`frozenset`类型可散列。

### 运算

集合有如下运算，由于集合的底层数据结构是散列表，这些运算方法有较高的计算效率。

* 交集、并集、差集、对称差，即`&`、`|`、`-`与`^`；
* 子集、真子集、超集、真超集，即`<=`、`<`、`>=`与`>`；
* 属于，即`in`

以`in`操作为例，`set`可以直接查询散列表获取结果，但`list`必须扫描一遍列表才能获取结果。对于含有许多元素的序列，两者在执行速度上有明显的差别。

`set`还支持`add`、`clear`、`copy`、`pop`、`remove`等方法。
