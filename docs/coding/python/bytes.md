# Python中的字节类型

Python中的字节类型包括字节流与字符串。

字符串是由字符组成的序列。字符是组成字符串的基本单位，对字符串的切片等操作以字符为单位进行。一个字符由两个部分进行定义：

* 码位，即字符的字节数值。
* 编码方式，即字节数值与字符的对应关系。

通过编码与解码操作，可以实现字符串与字节序列之间的转换：

```python
>>> "abc".encode() 
b'abc'
>>> b"abc".decode()
'abc'
>>>
```

Python提供了两种字节对象，即`bytes`与`bytearray`，两者都是由无符号字节（取值范围为0~255）为单位组成的序列。`bytes`是不可变序列。

```python
>>> b"\xff\xff"[0]
255
>>> bytes(3)[0]=1   
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
TypeError: 'bytes' object does not support item assignment
>>>
```

!!! update "New in version 3.5"
    `bytes`对象与`bytearray`对象添加了`hex`方法，返回字节的十六进制表示形式。该函数与`bytes`对象的`fromhex`方法相反。

    ```python
    >>> import random
    >>> seq = random.randbytes(8) # New in Python 3.9
    >>> seq.hex()
    'f04be4376519e9ce'
    >>>
    ```

!!! update "Changed in version 3.8"
    `hex`方法新增了可选的`sep`参数与`bytes_per_sep`参数。

    * `sep`参数指定区段间的连接字符串；
    * `bytes_per_sep`参数用于划分连续的字节段，**字节段从右往左进行划分**。

    ```python
    # Following the previous example
    >>> seq.hex('-')
    'f0-4b-e4-37-65-19-e9-ce'
    >>> seq.hex('-', 2)
    'f04b-e437-6519-e9ce'
    >>> seq.hex('-', 3)
    'f04b-e43765-19e9ce'
    >>>
    ```

字节序列中的字节有三种表示方式：

* ASCII中规定的可打印字符，使用该字符本身
* 制表符、换行符、回车符与反斜杠使用对应的转义序列表示，即`\t, \n, \r, \\`
* 所有字节都可以使用十六进制转义序列表示，如`\x00`

```python
>>> b"\t" == b"\x09"
True
>>>
```

字符串与字节序列的区别在于：字符串的索引与切片操作返回的对象都是字符串类型；而字节序列的索引操作返回`int`类型，切片操作返回一个字节序列。

## 构造

字符串的构造非常简单，此处不做讨论。在字符串前加`r`可以取消字符串内部的转义，如：

```python
>>> print(r"ab\n") 
ab\n
>>>
```

在字符串前加`b`可以构造一个字节序列。字符串中只能包含ASCII可打印字符。

除此之外，字节序列还有如下构造方式：

* 指定一个字符串和对应的编码方式，将该字符串编码为字节序列
* 一个仅包含`0~255`内数值的可迭代对象
* 一个实现缓冲协议的对象，将该对象中的字节序列复制到新的字节序列中（可能涉及类型转换）
* 一个整数，创建对应长度的空字节对象

如，从`array.array`对象创建字节序列：

```python
>>> import array  
>>> import random
>>> a = array.array("H", [51417, 45016, 65120, 9976])
>>> b = bytes(a)
>>> b
b'\xd9\xc8\xd8\xaf`\xfe\xf8&'
>>>
```

## 结构体

`struct`模块提供了将字节序列转换为不同类型字段的元组，类似于C语言结构体的功能。

### 结构定义

结构定义包含两个部分，即字节顺序与字段。`struct`模块允许多种字节顺序

|字符|字节顺序|大小|对齐方式|
|:-:|:-:|:-:|:-:|
|`@`|native|native|native|
|`=`|native|standard|none|
|`<`|little-endian|standard|none|
|`>`|big-endian|standard|none|
|`!`|network (= big-endian)|standard|none|

默认的字节顺序为`@`。

`struct`模块的字段定义如下，所有的字段在C语言中都有对应的类型：

|字符|C 类型|Python 类型|字宽||
|:-:|:-:|:-:|:-:|:-:|
|`x`|（填充字节）|N/A|
|`c`|`char`|长度为1的字节|1|
|`b`|`signed char`|`int`|1|
|`B`|`unsigned char`|`int`|1|
|`?`|`_Bool`|`bool`|1|
|`h`|`short`|`int`|2|
|`H`|`unsigned short`|`int`|2|
|`i`|`int`|`int`|4|
|`I`|`unsigned int`|`int`|4|
|`l`|`long`|`int`|4|
|`L`|`unsigned long`|`int`|4|
|`q`|`long long`|`int`|8|
|`Q`|`unsigned long long`|`int`|8|
|`n`|`ssize_t`|`int`|（仅适用于默认或`@`字节顺序）|
|`N`|`size_t`|`int`|（仅适用于默认或`@`字节顺序）|
|`e`|（半精度）|`float`|2|
|`f`|`float`|`float`|4|
|`d`|`double`|`float`|8|
|`s`|`char[]`|`bytes`|与字符串长度有关|
|`p`|`char[]`|`bytes`|与字符串长度有关|
|`P`|`void *`|`int`|

当试图将非整数对象打包为整数类型时，会调用对象的`__index__`方法。

一个结构体的定义是一个字符串，按照如下结构组织：

1. 第一个字符表示字节顺序
2. 此后的字符串表示结构体中的字段类型
3. 除`s`和`p`以外，字母前的数字表明该字段重复出现的次数
4. `s`、`p`前的数字表明字符串的长度

结构体字符串可以创建一个`struct.Struct`对象，两者实现相同的功能。

### 结构操作

对于一个定义的结构体，可以将数据按照结构体进行打包，或将结构体中的数据解包，也可以显示结构体的大小。

```python
>>> import struct   
>>> struct.pack('<hhf', 1, 2, 3)
b'\x01\x00\x02\x00\x00\x00@@'
>>> struct.unpack('<hhf', b'\x01\x00\x02\x00\x00\x00@@')
(1, 2, 3.0)
>>>
```

!!! update "New in version 3.4"
  `struct`对象新增了`iter_unpack`对象，不同于`unpack`函数，`iter_unpack`函数返回一个迭代器。

`struct`模块不会对字节顺序进行检测，因此对于同一个字节序列，不同的结构体定义在解包后会有不同的结果：

```python
>>> struct.unpack('>hhf', b'\x01\x00\x02\x00\x00\x00@@') 
(256, 512, 2.304855714121459e-41)
>>>
```

每个字段都有范围限制，当传入的参数超过字段所允许的范围，则会抛出异常：

```python
>>> struct.pack('<hhf', 32768, -32769, 3)
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
struct.error: short format requires (-32768) <= number <= 32767
>>>
```

当解包的字节长度与结构体的长度不对应时，也会抛出异常：

```python
>>> struct.unpack('>hhf', b'\x01\x00\x02\x00\x00\x00@')  
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
struct.error: unpack requires a buffer of 8 bytes
>>>
```

对于任何结构体，`struct`模块提供了`calcsize`方法用于检查结构体长度。

## 内存视图

内存视图提供了在不同对象间共享内存的方式。

有关内存视图的内容，请参见[序列类型](sequence.md)的内存视图部分。

## 字符串

此处着重讨论字符串的相关问题

### 编码与解码

如前所述，`str.encode`方法提供了从字符串到字节序列的转换方式，`encoding`参数指明了所使用的编码器。

```python
>>> "测试".encode("utf-8") 
b'\xe6\xb5\x8b\xe8\xaf\x95'
>>> "测试".encode("utf-16")
b'\xff\xfeKm\xd5\x8b'
>>> "测试".encode("gb2312")  
b'\xb2\xe2\xca\xd4'
>>>
```

当编码过程出现错误，如编码器无法识别字符串中的字符时，会抛出`UnicodeEncodeError`异常。

```python
>>> "测试".encode("latin-1")
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
UnicodeEncodeError: 'latin-1' codec can't encode characters in position 0-1: ordinal not in range(256)
>>>
```

出现错误时，有以下解决方式，可以通过`errors`参数指定：

* `ignore`：跳过无法编码的字符
* `replace`：将无法编码的字符替换为`?`
* `xmlcharrefreplace`：将无法编码的字符替换为`xml`实体（即XML中所使用的字符转换方式）

```python
>>> "测试".encode("latin-1", errors="ignore")
b''
>>> "测试".encode("latin-1", errors="replace")
b'??'
>>> "测试".encode("latin-1", errors="xmlcharrefreplace")
b'&#27979;&#35797;'
>>>
```

对应地，解码器无法识别字节序列的字节时会产生`UnicodeDecodeError`异常。但不抛出异常不代表解码成功，解码得到的数据可能是无用数据。`errors`参数指定了解码器在出错时的行为，`replace`将无法编码的字符替换为`�`。

`chardet`是一个基于Python的字符编码检测工具，可以通过二进制序列对原始字符串的编码方式进行推断。不过推断仅适用于较长的字符串，因为任何字符串会有多个编码方式适用于同一个字符串的情况，所以无法完全确定字符串的编码方式。

### BOM

BOM是字节序标记，对应的Unicode字符为`U+FEFF`（不存在`U+FFFE`字符，因此该字符可以用于推断字节顺序）

在UTF-16编码的字节序列开头会写入BOM，如果开头是`b'\xff\xfe'`两个字节，指明编码时使用little endian字节编码顺序。如果是`b'\xfe\xff'`两个字节，说明编码时使用的是big endian字节顺序。如果指明UTF-16所使用的字节顺序，如UTF-16LE或UTF-16BE，则不会生成BOM。

BOM仅用于推断字节顺序而不会出现在最终解码的字符串。

### 文本文件

使用`open`函数以文本模式打开一个文件时，最好指定文件的编码方式。

不要使用二进制方式打开文本文件。

### Unicode规范化

考虑如下两个字符串：

```python
>>> a = 'café'
>>> b = 'cafe\u0301'             
>>> print(a, b)
café café
>>> a == b
False
>>>
```

相同的打印结果，却对应不同的字符串，原因在于字符串`b`使用了`U+0301`字符作为重音标记（组合字符），多使用了一个字节。对于Python而言，这一段字符串的字节序列并不相同，因此认为`a != b`。

```python
>>> a.encode("utf-8")     
b'caf\xc3\xa9'
>>> b.encode("utf-8") 
b'cafe\xcc\x81'
>>>
```

`unicodedata`模块中的`normalize`函数提供了Unicode规范化的功能，该函数接收如下参数用于确定转换标准：

* `'NFC'`：使用最少码位构成等价的字符串
* `'NFD'`：将组合字符分解为基字符与单独的组合字符（如`U+0301`），可以用于去除字符串中的变音符号
* `NFKC`、`NFKD`会额外将兼容字符分解为一个或多个兼容分解，会导致数据损失，如下所示：

```python
>>> from unicodedata import normalize
>>> normalize('NFKC', '㍿') 
'株式会社'
>>>
```

`NKFC`、`NFKD`规范化可能会导致字符串的原意变化，但可以用于搜索引擎。

`str.casefold`函数提供了另一种规范化方式，即将字符串中的所有大写字母转为小写。与`str.lower`不同，部分字符会被替换成新的字符。

### 字符串排序

字符串的排序与其他数据的排序方式相同，都是按照码位升序排序。对于非`ASCII`字符可能会导致一些问题，如：

```python
>>> sorted(['café', 'cafu'])       
['cafu', 'café']
>>>
```

模块`locale`提供了`strxfrm`函数，用于按照区域设置对字符串进行排序。如果操作系统支持，区域设置可以在`setlocale`函数中全局指定。

```python
>>> import locale
>>> locale.setlocale(locale.LC_COLLATE, "en_GB.UTF-8")
'en_GB.UTF-8'
>>> sorted(['café', 'cafu'], key=locale.strxfrm)
['café', 'cafu']
>>>
```

## API

部分涉及到字符串的一些函数可以输入字符串或字节序列。

### re模块

不同于使用字符串构造的正则表达式，使用字节序列构造的正则表达式，`\d`与`\w`只能匹配ASCII字符。

### os模块

`os`模块中的所有字符串参数都可以使用字节序列替换。对于字符串，函数会使用`sys.getfilesystemencoding()`函数取得合适的编码器。此外，`os`模块提供`fsencode`与`fsdecode`函数用于手动进行编码与解码操作。