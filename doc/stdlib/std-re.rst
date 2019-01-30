####
re
####

.. highlight:: none

正则表达式简介
==============

正则表达式 (Regex) 是一个强大的文本处理工具.

正则表达式中拥有的元素有:

-   普通字符, 例如一般的 ``abcd`` 和 ``中文字符`` 等等.
-   元字符, 元字符起特殊的控制作用, 如果要匹配元字符本身, 需要使用反斜杠
    ``\`` 转义.

术语解释
========

::

    "[a-zA-Z]{5}" --> "This is a example string with a word which has only 5 letters." --> "which"
        pattern                    string                                                result
    pattern 表示一个          string 表示匹配的目标                                result 表示匹配到的结果.
    用于匹配的正则表达式.

常用函数
========

:mod:`re` 模块中最常用的函数有:

-   :func:`re.compile` 将一个 pattern 编译为 :class:`re.Pattern` 对象, 以提升匹配效率.
-   :func:`re.split` 用于切分字符串, 与内建的 :meth:`str.split` 不同的是,
    它使用正则表达式作为分隔符.
-   :func:`re.search` 搜索整个字符串中匹配的表达式.
-   :func:`re.match` 用于检测目标字符串是否能被正则表达式匹配.
-   :meth:`re.Match.group` 用于提取匹配到的捕获组.
-   :func:`re.findall` 用于搜索目标字符串中能被正则表达式匹配的内容,
    并存储到一个列表中返回.

compile()
---------

.. code:: py

    compile(pattern, flags) --> re.Pattern

在每次使用正则表达式匹配 pattern 的时候都有::

    pattern(str) --编译--> re.Pattern ----> 用于匹配

的过程.

对于同一个表达式需要使用多次的情况, 用 :func:`re.compile` 函数将 pattern
编译, 之后使用编译后的 :class:`re.Pattern` 进行匹配, 可以提高效率.

split()
-------

.. code:: py

    split(pattern, string) --> list(cut_string)

例如:

.. code:: ipython3

    In [0]: import re
    In [1]: STRING = "a, b, c,  ,d,e f"
    In [2]: STRING.split(", ")
    Out[2]: ['a', 'b', 'c', ' ,d,e f']      # 未能正确处理错误的情况
    In [3]: re.split("[, ]+", STRING)
    Out[3]: ['a', 'b', 'c', 'd', 'e', 'f']

search()
--------

.. code:: py

    search(pattern, string, flags=0) --> re.Match

``search()`` 将在整段 string 中搜索 pattern 匹配的字符串, 如果匹配成功,
则返回一个 ``Match`` 对象, 否则返回 ``None``.

match()
-------

.. code:: py

    match(pattern, string, flags=0) --> re.Match

``match()`` 会尝试在字符串的开头匹配 pattern, 返回一个 ``Match`` 对象.
找不到匹配项时返回 ``None``. 与 ``search`` 不同之处在于, ``match``
不会扫描整个字符串, 它只从给定字符串的开头进行匹配.

一般来讲, ``match`` 常用于检测输入是否合法,
或者用于从一个整理好的字符串中提取捕获组.

group()
-------

.. code:: py

    re.Match.group(index) --> str

``group()`` 常与 ``search`` 或 ``match`` 连用, 对于其返回的 ``Match``
对象, 可用 ``group`` 方法取出匹配到的捕获组内容.

.. code:: ipython3

    In [1]: import re
    In [2]: Match_object = re.match("This is (\S+), Hello!","This is Mike, Hello!")
    In [3]: Match_object.group(0)
    Out[3]: 'This is Mike, Hello!'
    In [4]: Match_object.group(1)
    Out[4]: 'Mike'

``group(0)`` 为表达式自身, ``group(1)`` 开始则按顺序为对应的捕获组.

要提取命名捕获组, 向 ``group()`` 中传递对应命名的字符串即可.

findall()
---------

.. code:: py

    findall(pattern, string, flags=0)
        --> list(matched)
        --> list(tuple(matched groups))

``findall()`` 函数会以列表的形式返回 string 中所有与 pattern
向匹配的字符串. 如果在 pattern 中定义了捕获组,
则将会返回以元组的形式组织起来的捕获组匹配项列表.

sub() 与 subn()
---------------

.. code:: py

    sub(pattern, repl, string, count=0, flags=0)
     --> str(替换后字符串)
    subn(pattern, repl, string, count=0, flags=0)
     --> tuple(str(替换后字符串), int(替换次数))

``sub()`` 函数用于搜索替换字符串. 它将 ``string`` 中被 ``pattern``
匹配到的部分用 ``repl`` 替换. 在 ``pattern`` 中匹配的捕获组可被 ``repl``
取用.

``count`` 参数决定替换次数, 若为 0 则会全部替换.

以下为实例:

.. code:: ipython3

    In [1]: import re
        ...: FROM = """\
        ...: Name:           Mike Donald
        ...: Age:            18
        ...: Address:        Earth
        ...: """
        ...:
        ...: pattern = r"Name:\s*([\S ]+)\s*Age:\s*([ \S]+)\s*Address:\s*([\S ]+)"
        ...: repl    = r"""姓名: \1
        ...: 年龄: \2
        ...: 地址: \3
        ...: """
        ...:
        ...: TO = re.sub(pattern, repl, FROM)
        ...:
        ...: print(TO)
        ...:
        ...:
    姓名: Mike Donald
    年龄: 18
    地址: Earth

TODO: 另外还有一些函数, 留待日后讲解.

::

   escape(pattern)
       """转义除了 ASCII 字母, 数字, 与下划线 `_` 之外的所有字符."""

   finditer(pattern, string, flags=0)
       """类似于 findall, 但是返回的是生成器. 空匹配也包含在内."""

   fullmatch(pattern, string, flags=0)
       """将 pattern 用于整个字符串"""

   purge()
       """清除正则表达式缓存"""

   template(pattern, flags=0)
       """编译模板 pattern, 返回 Pattern 实例"""

re.flags
--------

对于 :mod:`re` 模块中的一些函数, 有一个可选参数为 ``flags``,
该参数用于决定函数解析表达式时的一些策略, 其值的含义如下.

这些参数都是 re 模块下的一级数据. ``import re`` 的情况下以 ``re.X``
的方式使用, ``from re import *`` 的情况下以 ``X`` 的方式使用.

::

    A           = <RegexFlag.ASCII: 256>
    ASCII       = <RegexFlag.ASCII: 256>
    DOTALL      = <RegexFlag.DOTALL: 16>
    I           = <RegexFlag.IGNORECASE: 2> # 忽略大小写
    IGNORECASE  = <RegexFlag.IGNORECASE: 2>
    L           = <RegexFlag.LOCALE: 4>
    LOCALE      = <RegexFlag.LOCALE: 4>     # 使用本地化时间日期表示法
    M           = <RegexFlag.MULTILINE: 8>
    MULTILINE   = <RegexFlag.MULTILINE: 8>  # 多行模式
    S           = <RegexFlag.DOTALL: 16>
    U           = <RegexFlag.UNICODE: 32>   # 使用 Unicode 识别
    UNICODE     = <RegexFlag.UNICODE: 32>
    VERBOSE     = <RegexFlag.VERBOSE: 64>
    X           = <RegexFlag.VERBOSE: 64>

----

.. include:: ../_static/rst/regex.rst
