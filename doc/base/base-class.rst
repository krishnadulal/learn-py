########
面对对象
########

.. _data-model: https://docs.python.org/3/reference/datamodel.html

命令式编程
    这中编程思维所想的是:

    1.  首先, 打造一条流水线
    2.  把数据放进流水线的起点
    3.  在流水线中, 根据数据的各种性质的不同, 进行不同的处理.
    4.  在流水线的终点, 将结果返回.

    也就是说, 命令式编程, 着重的是 "命令", 是 "要干什么"
面对对象编程
    面对对象编程, 则是先设计一个 "类", 它有什么性质, 它能做什么动作,
    再用这些设计好的类来模拟一个世界:

    1.  "封装" 一个类

        -   定义一个类
        -   描述这个类有哪些数据成员, 拥有哪些数据特征
        -   描述这个类有哪些函数成员, 能完成什么动作

    2.  类的 "继承" 关系

        以一个封装好的类为祖宗, 让一系列子类继承他.
        继承者复制了父类的所有公开的成员.
        但是又能对其进行修改, 这被称为 "重载"(overload).
        也能添加新的成员.

    3.  类的 "多态" 性质

        通过继承, 得到的父子类间, 可以通过重载来实现 "多态".
        即, 根据实例所属类的不同, 同一个方法完成不同的动作.
        如果子类未重载方法, 则会调用父类的方法.
        如果子类重载, 则会调用重载的方法.
        在 Python 中, 更是可以使用 :func:`super` 函数,
        在重载方法中调用父类方法, 再方便地进行修改.

    4.  创建类的实例

        "类" 是一个模板, 而实例才是真正在程序中运行的实体.
        创建了实例后, 可以为实例的属性单独进行赋值,
        调用实例的方法等等.

    5.  对象间的交流

        创建了多个不同类或同类的实例, 让他们在程序中交流.
        在这一点, 似乎又回到了 "命令式编程" 的地步,
        但是, 由于面对对象的 "封装", "继承", "多态" 性质,
        流水线的长度大大缩短了, 且逻辑上也更容易使人理解.

定义类
======

::

    class ClassName:
        class_attr = "静态成员"

        def __init__(self):
            self.instance_attr = "实例成员"

        def method(self, *args, **kwargs):
            """定义类的方法
            """
            pass

在 Python 中, 可以使用 :keyword:`class` 定义一个类,
在增加一层缩进后, 可以为这个类添加成员.
类的方法, 其实就是一个函数,
不过这个函数需要传入类的实例作为第一个参数罢了.

值得一提的是, 类中以双下划线开头与结尾的成员往往有着特殊作用,
可以查询官方文档 `data-model`_ 或本站的 :doc:`base-magics`.
后者主要是从应用方面介绍的.

类与实例
========

类与实例之间, 存在着 "类属性", "实例属性",
"类方法", "实例方法" 以及 "静态方法" 的区别.

实例和类拥有相对独立的命名空间.
其特点在于, 当获取实例的属性时,
优先查找该实例的命名空间,
找不到则查找类的命名空间.

类的命名空间中的属性, 所有实例共享;
实例命名空间中的属性, 为实例独有.

.. ipython::

    In [1]: class NameSpace:
       ...:     overwrited = "重名的属性"
       ...:     no_overwrited = "类属性"
       ...:     def __init__(self):
       ...:         self.overwrited = "实例中重名的属性"
       ...:         self.no_overwrited_attr = "实例属性"

    In [2]: x = NameSpace()

    In [3]: x.overwrited
    Out[3]: '实例中重名的属性'

    In [4]: x.no_overwrited_attr
    Out[4]: '实例属性'

    In [5]: x.no_overwrited
    Out[5]: '类属性'

    In [6]: NameSpace.overwrited
    Out[6]: '重名的属性'

    In [7]: NameSpace.no_overwrited
    Out[7]: '类属性'

    In [8]: x.__class__ is NameSpace
    Out[8]: True

利用这个性质, 可以为一个类添加 "计数器" 的功能:

.. ipython::

    In [1]: class Count:
       ...:     amount = 0
       ...:     def __init__(self, name):
       ...:         self.name = name
       ...:         self.__class__.amount += 1

    In [2]: x = Count("x")

    In [3]: y = Count("y")

    In [4]: x.amount
    Out[4]: 2

    In [5]: Count.amount
    Out[5]: 2

在 ``__init__`` 方法中, 为 ``self`` 变量添加的属性,
属于这个实例.
而 ``self.__class__`` 则指向实例所处的类.

至于实例方法, 类方法与静态方法,
则是以执行时默认所传入的对象为区分的.

普通的没有任何装饰的方法定义, 则是实例方法的定义::

    def method(self, *args, **kwargs):
        pass

这样的方法, 传入的第一个参数为当前实例.

使用 :func:`classmethod` 定义的方法为类方法::

    @classmethod
    def method(cls, *args, **kwargs):
        pass

传入的第一个参数为实例的类.

使用 :func:`staticmethod` 定义的方法为静态方法::

    @staticmethod
    def method(*args, **kwargs):
        pass

静态方法不传入实例或类, 就类似于普通函数一般.

实例方法与类方法中的 ``self``, ``cls`` 并不是语法要求,
仅仅是习惯命名. 如果起一个其他的名字, 也是可以运行的,
它只要求是第一个参数即可.

用以下例子, 来说明实例方法, 类方法以及静态方法在调用时的区别:

.. ipython::

    In [1]: class NameSpace:
       ...:     a = "重名的属性"
       ...:     b = "类属性"
       ...:     def __init__(self):
       ...:         self.a = "实例中重名的属性"
       ...:         self.c = "实例属性"
       ...:
       ...:     def get(self):
       ...:         print(
       ...:             self.a,
       ...:             self.b,
       ...:             self.c,
       ...:             sep="\n"
       ...:         )
       ...:
       ...:     @classmethod
       ...:     def get_cls(cls):
       ...:         print(
       ...:             cls.a,
       ...:             cls.b,
       ...:             # cls.c,
       ...:             sep="\n"
       ...:         )
       ...:
       ...:     @staticmethod
       ...:     def get_static(*args, **kwargs):
       ...:         print(
       ...:             *args,
       ...:             kwargs.items(),
       ...:             sep="\n"
       ...:         )
       ...:

    In [2]: x = NameSpace()

    In [3]: x.get()
    实例中重名的属性
    类属性
    实例属性

    In [4]: x.get_cls()
    重名的属性
    类属性

    In [5]: x.get_static(1,2,3, name=123)
    1
    2
    3
    dict_items([('name', 123)])


:func:`super`
=============

:func:`super` 是
