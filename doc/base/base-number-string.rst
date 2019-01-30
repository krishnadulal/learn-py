############
数字与字符串
############

基本数据类型
============

整数-int
--------

Python 中的整数与长整数没有什么区别 (Python3).
因为 Python3会自动地处理整数的存储方式,
将整型与长整型互换.
从理论上讲,
Python中的整数的位数可以是无限长,
但实际上,
会受到内存空间的限制.

整数的相关信息可以从 :data:`sys.int_info` 获得

.. code:: py

    import sys
    print(sys.int_info)

.. parsed-literal::

    sys.int_info(           # 长整数是普通整数的组合
        bits_per_digit=30,    # 每个整数占用 30 个 bit.
        sizeof_digit=4        # 每个整数占用 4 个 byte (32 bit) 的内存空间.
        )

布尔数-bool
~~~~~~~~~~~

布尔数是整数的一个子集. 它其实就是只有一个 bit 的整数. 其取值只有 ``0``,
``1`` (二进制). 在 Python 中, 还可以用 ``True`` (1) ``False`` (0)
来表示它们.

浮点数-float
------------

所谓的浮点数, 就是一种表示小数或按科学记数法记录的数字的数据类型.
计算机处理它和整数的方法有很大的区别.

-   首先, 浮点数的位数不可能无限. 或者说, 浮点数的分布不是稠密的.
    它不能和数学上的实数等价.
-   其次, 浮点数的存储方法依然是二进制,
    因此, 浮点数在表现数字的时候,
    总是会有无法避免的误差,
    导致错误的四舍五入.
    例如,
    可以试一试将一个超出浮点数存储范围的小数赋值给一个变量,
    会发现超出的部分直接消失了;
    若将一个无法用二进制表示的十进制数赋值给变量, 会发现莫名的误差.

.. code:: ipython3

    a = 1.0000000000000006;a

.. parsed-literal::

    1.0000000000000007

.. code:: ipython3

    a = 1.00000000000000006;a

.. parsed-literal::

    1.0

浮点数的相关信息可以从 :data:`sys.float_info` 对象获得.

`Python 官方文档 对 sys.float_info
的解释 <https://docs.python.org/3/library/sys.html#sys.float_info>`__

.. code:: ipython3

    import sys
    sys.float_info

.. parsed-literal::

    sys.float_info(
    max=1.7976931348623157e+308,
    max_exp=1024,
    max_10_exp=308,
    min=2.2250738585072014e-308,
    min_exp=-1021,
    min_10_exp=-307,
    dig=15,
    mant_dig=53,
    epsilon=2.220446049250313e-16,
    radix=2,
    rounds=1
    )



以下是经过整理的输出信息

浮点数是以 2 进制储存的, 在需要时与 10 进制互相转换.

+-----------------------------------+-----------------------------------+
| 结果                              | 注解                              |
+===================================+===================================+
| ``max=1.7976931348623157e+308``   | 可表示的最大正数                  |
+-----------------------------------+-----------------------------------+
| ``max_exp=1024``                  | :math:`< 2^{1024}`                |
+-----------------------------------+-----------------------------------+
| ``max_10_exp=308``                | 十进制时可正常处理的最大指数      |
+-----------------------------------+-----------------------------------+
| ``min=2.2250738585072014e-308``   | 可表示的最小正数                  |
+-----------------------------------+-----------------------------------+
| ``min_exp=-1021``                 | :math:`> 2^{-1021}`               |
+-----------------------------------+-----------------------------------+
| ``min_10_exp=-307``               | 十进制时可正常处理的最小指数      |
+-----------------------------------+-----------------------------------+
| ``dig=15``                        | 十进制下可正常处理的最大小数位数  |
+-----------------------------------+-----------------------------------+
| ``mant_dig=53``                   | 浮动精度, 二进制下表示有效数字的  |
|                                   | bit 位数.                         |
+-----------------------------------+-----------------------------------+
| ``epsilon=2.220446049250313e-16`` | 十进制下 与 1 “相邻” 的浮点数与 1 |
|                                   | 的差. (浮点数的数量级不同,        |
|                                   | 这个值也不同, 详情…)              |
+-----------------------------------+-----------------------------------+
| ``radix=2``                       | “基数” 即指数部分的 “底数”.       |
+-----------------------------------+-----------------------------------+
| ``rounds=1``                      | 用于表示算术运算的舍入模式,       |
|                                   | 详情参见 C99 标准的5.2.4.2.2节    |
+-----------------------------------+-----------------------------------+

复数-complex
------------

-   复数的概念与数学上的一致, 由 ``实部+虚部j`` 表示.
    但是这里虚数单位的表示法是 ``j`` 不是 ``i`` , 需要注意别搞混淆了.
-   复数的实部与虚部都是浮点数.
-   可以使用 ``complex.real`` 和 ``complex.imag``
    分别取出复数的实部与虚部. (这里的 complex
    是一个类型为复数的变量的变量名)

.. code:: ipython3

    test = 1.0 + 89.0j

.. code:: ipython3

    test




.. parsed-literal::

    (1+89j)



.. code:: ipython3

    test.real




.. parsed-literal::

    1.0



.. code:: ipython3

    test.imag




.. parsed-literal::

    89.0



字符串-str
----------

-   Python 字符串用 ``"字符串"`` 引号括起来,
    可以使用双引号也可以使用单引号. 双引号中可以嵌套单引号, 反过来也一样.
    但如果要在双引号中表示双引号, 需要用 ``\`` 反斜杠转义 ``\"``.

    -   如果需要在字符串中表示反斜杠, 可以使用 ``\\`` 对反斜杠转义,
        也可以使用 ``r"不用\转义的原始字符串"`` 在引号外使用字母 ``r``. 被
        ``r`` 标识的字符串称为 “原始字符串”, 此字符串不会接受 Python
        的转义, 但是在被其他模块处理时, 仍按照对应的转义规律转义. 例如,
        在一个正则表达式 (re模块) 中, 使用 ``r"\\`` 作为一个 pattern,
        最终此 pattern 被正则引擎转义后将会匹配一个反斜杠 ``\``,
        但如果没有标识为原始字符串, 将需要经历 Python 与 正则的两次转义,
        要匹配一个反斜杠, 需要输入 ``\\\\``.
    -   如果需要在字符串中使用 Unicode 编码插入 Unicode 字符,
        可以在引号外使用字母 ``u``. ``u"这是一个\u0020字符"``
        (``\u0020``\ 是空格).
    -   如果要将字符串转化为 ``byte-like`` 对象, 在引号外使用字母 ``b``.

-   Python 的字符串也可以使用成对的三引号\ ``"""超级多的字符"""``.
    这种方法标识的字符串中可以包含换行, 指标符和其他特殊字符.

.. code:: ipython3

    string = """测试三引号
    包裹的字符
        是啥样的?
    """
    print(string)

.. parsed-literal::

    测试三引号
    包裹的字符
        是啥样的?

可以看到, 特殊字符(换行符等)被按照其本意解释了.

-   Python 没有单独的 “字符” 类型, 只有字符串. 但字符串中可以只有 1
    个甚至 0 个字符.
-   Python 字符串是只读的. 要更改, 可以创建并赋值一个新的字符串变量.
-   Python 可用 ``%`` 符号表示格式化字符串.
    **其右侧本质上是一个元组(tuple)**

    -   现在, 更建议使用字符串的 :meth:`str.format` 方法格式化字符串.

格式化字符串
~~~~~~~~~~~~

====== ==================================
格式符 含义
====== ==================================
``%c`` 字符及其 ASCII 码
``%s`` 字符串
``%d`` 整数
``%o`` 八进制整数
``%x`` 十六进制整数
``%X`` 十六进制整数(字母大写)
``%f`` 小数表示的浮点数
``%e`` 科学记数法表示的浮点数
``%E`` 科学记数法表示的浮点数(字母大写)
``%g`` 从 ``%e`` 和 ``%f`` 中选择输出短的
``%G`` 从 ``%E`` 和 ``%F`` 中选择输出短的
====== ==================================

传递多个格式化字符串需要使用 ``()`` 圆括号将参数括起来. 然后在内部用
``,`` 逗号划分各参数. 也就是一个 **元组**

.. code:: ipython3

    test1 = "hello"
    test2 = "HELLO"
    test3 = "WoRlD"
    print("%s(%s) %s!"%(test1,test2,test3))

.. parsed-literal::

    hello(HELLO) WoRlD!


对格式化字符可以使用修饰符

+---------+-------------------------------------------------+
| 修饰符  | 含义                                            |
+---------+-------------------------------------------------+
| ``#``   | 十六进制前添\ ``0x``, 八进制前添\ ``0``         |
+---------+-------------------------------------------------+
| ``+``   | 在数字前添加正负号                              |
+---------+-------------------------------------------------+
| ``m.n`` | ``m``\ 表示显示数字的总位数(整数部分+小数部分); |
|         | ``n`` 表示保留小数点的位数,                     |
|         | 若 ``m`` 的条件已达到,                          |
|         | 则 ``n`` 将被忽略.                              |
+---------+-------------------------------------------------+
| ``0``   | 数字前填0, 默认空格                             |
+---------+-------------------------------------------------+
| ``-``   | 左对齐, 默认右对齐                              |
+---------+-------------------------------------------------+

另一种格式化方法为 ``"{}{}".format(a,b)`` 对字符串调用 ``format()``
方法.

.. code:: ipython3

    test1 = 1
    test2 = 3.14
    test3 = '哈哈哈'
    # 按顺序
    print("按顺序:{},{},{}".format(test1,test2,test3))
    # 按索引号
    print("按索引号:{2},{1},{0}".format(test1,test2,test3))
    # 按参数名
    print("按参数名:{a},{c},{b}".format(a=test1, b=test2, c=test3))


.. parsed-literal::

    按顺序:1,3.14,哈哈哈
    按索引号:哈哈哈,3.14,1
    按参数名:1,哈哈哈,3.14


字符串的截取与分段(切片)
~~~~~~~~~~~~~~~~~~~~~~~~

一个字符串变量, 实质上可以视作一个由字符拼接起来的 “元组”,
可以在变量名后用 ``[index]`` 提取其中的一个元素, 或者使用
``[index1:index2]`` 提取其中一段, 注意有一个 **要头不要腚** 的规则.

   我突然想到用这个字符串来做例子也许会更形象…

   .. code:: py

      "_(:з」∠)_"    # 要头不要腚

.. code:: ipython3

    str = "abcdefg"
    for i in range(7): # i = 0,1,2,3,4,5,6
        print(str[i], end=':index(%d)|'%(i))
    print() # 换行
    print(str[0:2]) # 打印 'ab\n'  (文雅点说"宁左毋右"吧).


.. parsed-literal::

    a:index(0)|b:index(1)|c:index(2)|d:index(3)|e:index(4)|f:index(5)|g:index(6)|
    ab


index 号可以为非负数, 代表从左到右的索引号; 也可以为负数,
代表从右到左的索引号.

::

   str     a  b  c  d  e  f  g
   +       0  1  2  3  4  5  6
   -      -7 -6 -5 -4 -3 -2 -1

index 可以留空一个, 表示从另一个开始一直取到末尾(或头部).

.. code:: ipython3

    print(str[2:]) # 打印 'cdefg\n' 从c开始向末尾
    print(str[:4]) # 打印 'abcd\n'  从d开始向头部 (仍然不要腚)


.. parsed-literal::

    cdefg
    abcd


无论正负, index 都是一个对字符位置的索引号而已.
所以它的大小关系和一般整数无关. 因此, 以下这些输出都是一样的.

.. code:: ipython3

    # 对照着上面那个表看
    print(str[1:6])
    print(str[-6:6])
    print(str[1:-1])
    # 都打印 'bcdef\n'

    print(str[0:5])
    print(str[:5])
    print(str[:-2])
    # 都打印 'abcde\n'
    # ... 以此类推


.. parsed-literal::

    bcdef
    bcdef
    bcdef
    abcde
    abcde
    abcde


字符串切片可以指定递进级别, 默认为 1.

.. code:: ipython3

    STR = "abcdefg"

.. code:: ipython3

    STR[::1]

.. parsed-literal::

    'abcdefg'

.. code:: ipython3

    STR[::2]    # 每两个索引提取一个

.. parsed-literal::

    'aceg'

.. code:: ipython3

    STR[::-1]   # 逆序, 每一个索引提取一个

.. parsed-literal::

    'gfedcba'

.. code:: ipython3

    STR[1:-1:-1]    # 逆序时, 设定的起点与终点也得反过来

.. parsed-literal::

    ''

.. code:: ipython3

    STR[-1::-1]

.. parsed-literal::

    'gfedcba'

字符串的“运算”
~~~~~~~~~~~~~~

Python 中的字符串参与运算:

-  ``"str1" + "str2"`` 拼接一个新的字符串 ``"str1str2"``.
-  ``"str"*int`` 重复一个字符串 ``int`` 次. 例如 ``"str"*3`` ==
   ``"strstrstr"``

但是, 在拼接大量字符串时, 最好不要使用 ``string += other`` 这样的语法.
由于 Python 中字符串是 “不可变对象”, 每一次拼接,
都会在内存中创建一个新的字符串(假设原字符串为 A, B,
那么拼接时是这样的过程:

1. 有字符串 A,B
2. 创建一个字符串 C
3. C = A + B
4. 若 A,B 已经没有引用了, 则删除 A,B

因此, 如果有几百, 几千个, 那么上面的步骤就会重复几百, 几千次, 每一次过后
C 就会越来越大, 内存中就越来越难找到能存放下 C 的连续空间. 导致效率降低.

因此, 采用这样的语法是很合适的:

.. code:: python

    strings = []
    strings.append("string1")
    strings.append("string2")
    ...

    C = ''.join(strings)

和字符串相比, 列表是可变对象, 它的修改不需要新建一个实例.
因此, 只会在最后 ``join`` 时产生一个大字符串.

数据类型转换
============

:class:`int`
------------

.. code-block:: none

   class int(object)
    |  int([x]) -> integer
    |  int(x, base=10) -> integer
    |
    |  Convert a number or string to an integer, or return 0 if no arguments
    |  are given.  If x is a number, return x.__int__().  For floating point
    |  numbers, this truncates towards zero.
    |
    |  If x is not a number or if base is given, then x must be a string,
    |  bytes, or bytearray instance representing an integer literal in the
    |  given base.  The literal can be preceded by '+' or '-' and be surrounded
    |  by whitespace.  The base defaults to 10.  Valid bases are 0 and 2-36.
    |  Base 0 means to interpret the base from the string as an integer literal.

-  :class:`int` 可接受的参数有:

   -  ``x`` 表示被转换的对象, 此参数未命名,
      所以需要将对应实参放在参数表第一位.
   -  ``base`` 表示转换时依据的进制基数, 默认 10 进制.

-  若 ``x`` 是一个整数, 返回其自身.
-  若 ``x`` 是一个浮点数, 其小数部分会被砍掉.
-  若 ``x`` 是一个字符串,
   会将字符串中的字符依据定义的基数转换为对应的整数.
   且该字符串中不能有基数表示范围以外的字符.

   -  默认基数为 ``base=10``, 可接受的基数值为 0 或 从 2 到 36.

      -  就是说 10 进制下只能有 ``0123456789``, 十六进制下可以有
         ``0123456789abcdef``, 最高可以在 36 进制下用 ``z`` 表示 ``35``.
      -  ``base=0`` 的情况下, 根据字符串内容猜测进制. 但适用情况较少:

         -  ``0x10`` 会被识别为 16 进制的 ``16``.
         -  ``f`` 会被识别为 16 进制的 ``15``.
         -  ``0o10`` 会被识别为 8 进制的 ``8``. (零后面是小写的字母O)
         -  ``29134`` 会被识别为 10 进制.
         -  ``01423`` 会被识别为 10 进制, 尽管没有任何大于 7 的数字,
            在最前方也有个 ``0``.
         -  只能从 ``16`` ``8`` ``10`` 中猜测.

   -  字符串中可以在前面有 ``+ -`` 正负号. 也可以在两侧有空格.
   -  **规定了基数 ``base`` 时, 必须输入字符串.**

:class:`float`
--------------

.. code:: none

   class float(object)
    |  float(x=0, /)
    |
    |  Convert a string or number to a floating point number, if possible.

文档说得这么简洁, 我也没啥好说的… 只能用多了再来说说感受了…

-   :meth:`float.hex` 返回一个用 16 进制表示的浮点数.
-   :meth:`float.fromhex` 从字符串转换一个 16 进制的浮点数.
    形式为 ``0xf.fp+1``, 用 ``p`` 表示 16 为底的指数.

:class:`complex`
----------------

.. code:: none

   class complex(object)
    |  complex(real=0, imag=0)
    |
    |  Create a complex number from a real part and an optional imaginary part.
    |
    |  This is equivalent to (real + imag*1j) where imag defaults to 0.

:class:`str`
------------

.. code:: none

   class str(object)
    |  str(object='') -> str
    |  str(bytes_or_buffer[, encoding[, errors]]) -> str
    |
    |  Create a new string object from the given object. If encoding or
    |  errors is specified, then the object must expose a data buffer
    |  that will be decoded using the given encoding and error handler.
    |  Otherwise, returns the result of object.__str__() (if defined)
    |  or repr(object).
    |  encoding defaults to sys.getdefaultencoding().
    |  errors defaults to 'strict'.

大意是说:

-  从给定对象创建一个新的字符串对象. 如果指定了 ``encoding`` 或
   ``errors``, 则必须公开 ``bytes_or_buffer``
   来编码字符串和处理错误信息.
-  ``str()`` 可接受的参数有:

   -  ``object`` 被转换的对象.
   -  ``bytes_or_buffer`` 字节或缓冲区.
   -  ``encoding`` 字符编码, 默认值由 ``sys.getdefaultencoding()`` 获得,
      一般为 ``utf-8``
   -  ``errors`` 错误策略. 默认为 ``strict``.

其他
----

-  :func:`hex` 将整数转换为其 16 进制形式的字符串.
-  :func:`oct` 将整数转换未其 8 进制形式的字符串.
-  :func:`chr` 将整数按 ASCII 转换为字符. 若整数值超出了 255 , 则按
   Unicode 转换. 整数可以是 10, 8, 16 进制. 范围为 ``0<=i<=0x10ffff``.
-  :func:`ord()` 将字符 (单字符的字符串)转换为对应的 10 进制整数. 支持
   Unicode .
-  :func:`repr` 类似 :func:`str` 但返回的是一个字符串表达式. 可以在
   :func:`eval` 中运行.

小数与分数
==========

在模块 :mod:`decimal` 与 :mod:`fractions` 中定义了小数与分数类型.

:mod:`fractions` 中的 :class:`fractions.Decimal` 与 :class:`decimal.Decimal` 是相同的,
因此,
要用到小数与分数,
只需要::

    from fractions import Decimal, Fraction

即可.

小数是用字符串模拟的, 分数则是将分子与分母分开存储.

例如::

    Decimal("0.12321839879182448971498732")
    Fraction(1, 3) # 1/3

不过它们与其他类型算术运算, 将得到浮点数.