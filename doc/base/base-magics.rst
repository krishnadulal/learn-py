########
魔法属性
########

Python 中的 "魔法属性" 指的是那些总是被双下划线包围, 例如 ``__init__``, ``__del__`` 等等, 的内置变量/方法.

它们在 Python 的解释运行中起到了较深层次的作用, 能改变一个对象的行为:

- 初始化方法
- 运算符重载
- 上下文管理

等等功能, 都可以通过这些魔法属性来进行控制. 甚至只有学会了这些方法, 才能对对象进行深度的控制.

    本文介绍的内容对应官方文档 https://docs.python.org/3/reference/datamodel.html

    同时参考了 https://pycoders-weekly-chinese.readthedocs.io/en/latest/issue6/a-guide-to-pythons-magic-methods.html

实例的初始化
============

在定义类时, 定义 :meth:`object.__init__` 方法::

    class Example:
        def __init__(self, *args):
            self.args = args

对于将在其他方法中用到的数据成员, 最好在此方法中赋值一个初值.

限制实例的数据成员
==================

在类中定义一个名为 :data:`object.__slots__` 的属性, 这个属性应当为一个 :class:`tuple`, 而且其中以 :class:`str` 的形式输入允许出现的数据成员名. 那么, 该实例只能添加在此之中的成员:

1. 可以定义名称在此元组之外的方法, 但是不能定义在此之内的方法.
2. 可以在后续运行时动态定义 :keyword:`lambda` 匿名函数, 并赋值给在此元组之内的成员.
3. 添加的数据成员必须在此元组之内, 无论是公共数据还是私有数据 ( ``_name`` ) 都不允许超出范围.

>>> class SlotsExample:
>>>     __slots__ = ("a", "b")
>>>     def __init__(self):
>>>         self.a = "a"
>>>     def c(self):
>>>         print("{}{}".format(self.a, self.b()))
>>> x = SlotsExample()
>>> x.b = lambda : "b"
>>> x.c()
ab

这个属性的定义会影响 Python 底层创建实例的数据结构, 关闭其数据成员的可扩展性.

继承对 ``__slots__`` 的影响
---------------------------

- 如果子类 **没有** 定义 ``__slots__``, 那么子类相当于没有 ``__slots__``.
- 如果子类也 **定义了** ``__slots__``, 那么子类的实际 ``__slots__`` 就是子类定义的 ``__slots__`` 与父类定义的 ``__slots__`` 的并集.

运算符重载
==========

定义以下方法, 将会影响运算符的行为::

    class Test:

        # 关系运算
        def __eq__(self, other):
            "self == other"
        def __ne__(self, other):
            "self != other"
        def __lt__(self, other):
            "self <  other"
        def __gt__(self, other):
            "self >  other"
        def __le__(self, other):
            "self <= other"
        def __ge__(self, other):
            "self >= other"

        # 单目运算
        def __pos__(self):
            " + self"
        def __neg__(self):
            " - self"
        def __abs__(self):
            "abs(self)"

        # 算术运算
        def __add__(self, other):
            "self + other"
        def __sub__(self, other):
            "self - other"
        def __mul__(self, other):
            "self * other"
        def __floordiv__(self, other):
            "self // other"
        def __div__(self, other):
            "self / other"
        def __mod__(self, other):
            "self % other"
        def __divmod__(self, other):
            "divmod(self, other)"
        def __pow__(self, other):
            "self ** other"
        def __invert__(self):
            "~ self"
        def __lshift__(self, other):
            "self << other"
        def __rshift__(self, other):
            "self >> other"
        def __and__(self, other):
            "self & other"
        def __or__(self, other):
            "self | other"
        def __xor__(self, other0:
            "self ^ other"

        # 对于以上算术或位运算操作符, 都有 __r*__ 格式, 对应反序计算, 例如
        # __radd__(self, other) -> other + self
        # 也有 __i*__ 格式, 对应复合赋值表达式
        # __iadd__(self, other) -> self += other

将对象转化为字符串
==================

一个对象可以用 :class:`str` 或 :func:`repr` 来转化为一个可读的字符串. 分别调用了 :meth:`object.__str__`, :meth:`object.__repr__` 两个方法. 这两个方法虽然效果比较类似, 不过目的不一样:

- :meth:`object.__str__` 是将该对象转化为人类可读的字符串, 用于向人类展示
- :meth:`object.__repr__` 则是将该对象转化为一个可被 Python 执行的语句, 可用于创建一个相同的实例

例如, 对于一个二维向量, :meth:`object.__str__` 可以返回一个类似于 ``(x, y)`` 的向量表达形式, 或者对应的 LaTeX 代码 ``\begin{bmatrix} x \\ y \end{bmatrix}`` 等等. 而 :meth:`object.__repr__` 则需要保证, 返回的字符串可以再被执行, 并且能实例化一个相同的对象: ``Vector(x, y)``::

    class Vector:
        def __init__(self, x, y):
            self._x = x
            self._y = y

        def __str__(self):
            return "\begin{bmatrix} {} \\ {} \end{bmatrix}".format(self._x, self._y)

        def __repr__(self):
            return "Vector({}, {})".format(self._x, self._y)

以上只是使用这两个方法的原则, 就算实际上没有这么做, Python 也不会报错, 不过遵守这个原则总是有利的.

另外, 如果 :meth:`object.__str__` 方法没有定义, 那么默认与 :meth:`object.__repr__` 相同. 两者都不定义的话, 会显示该对象的模块路径关系与 ID, 就像这样: ``'<__main__.Vector object at 0x00000269573E1898>'``.

:func:`print` 在打印一个对象前, 会先调用它的 :meth:`object.__str__` 方法.

让你的对象可被调用
==================

要让一个对象表现出函数的性质, 需要定义 :meth:`object.__call__` 方法:

>>> class Func:
>>>     def __call__(self):
>>>         return "我可以被调用"
>>> x = Func()
>>> x()
'我可以被调用'

你可以在 :meth:`object.__call__` 中定义这个对象被调用时怎么根据参数行动.

设置上下文管理器
================

让一个对象在 :keyword:`with` 语句中可用, 需要定义 :meth:`object.__enter__` 和 :meth:`object.__exit__` 方法, 前者用于定义进入时的动作, 需要一个返回值, 用于赋值给 ``with xxx as yyy:`` 中的 ``yyy``, 而后者定义退出时动作, 一般用于关闭打开的文件与缓冲区, 释放堆上的数据等等:

>>> from io import BytesIO
>>> class Buffer:
>>>     def __enter__(self):
>>>         self._pointer = BytesIO()
>>>         print("打开一个二进制流")
>>>         return self._pointer
>>>     def __exit__(self, exception_type, exception_val, trace):
>>>         try:
>>>             self._pointer.close()
>>>             print("退出, 流已关闭")
>>>         except:
>>>             print("遇到错误")
>>> with Buffer() as b:
>>>     pass
打开一个二进制流
退出, 流已关闭

- :meth:`object.__enter__` 不需要额外的参数, 也不应该有额外参数.
- :meth:`object.__exit__` 需要三个额外参数, 分别是在 :keyword:`with` 语句中发生的异常类型, 异常变量, 错误追踪. 而在 :meth:`object.__exit__` 之中, 也应当根据异常的不同进行错误处理.