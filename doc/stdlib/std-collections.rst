###########
collections
###########

:mod:`collections` 提供了一系列常用的集合类型数据结构.

namedtuple
==========

可以为元祖以及其中元素命名::

    from collections import namedtuple

    Point3D = namedtuple("Point3D", ("x", "y", "z"))

    a = Point3D(1, 1, 1)
    a.x
    a.y
    z.z

命名元祖仍然具有元祖的不可变性质.
但是可以通过命名, 以访问成员的性质得到数据.

:func:`namedtuple` 是一个函数, 返回一个类的定义.

.. function:: namedtuple(typename, field_names)

    返回值需要一个标识符来接收,
    命名虽然可以不一致,
    但是为了实例的字符串转化,
    建议标识符命名与命名保持相同.

    :param typename: 类的命名
    :param field_names: 成员的命名, 同时设定了容量
    :return: 类
    :rtype: tuple


deque
=====

内置的 :class:`list` 是用链表实现的.
当检索元素过多, 则对尾端的插入与删除效率就会降低.

:class:`collections.deque` 则是双向链表,
和 list 相比, 在两头都很有效率.

多了 ``appendleft`` 和 ``popleft`` 两种方法,
应用上可以视作与 list 等同.

defaultdict
===========

内置的 :class:`dict` 在读取不存在的键时将会跑出异常.
如果希望返回一个默认值,
则需要使用其 :meth:`dict.get` 方法,
并传入参数.

如果需要整个字典直接支持返回默认值,
可以使用 :class:`collections.defaultdict`::

    from collections import defaultdict

    x = defaultdict(lambda : "NULL")

    x['abc']

    'NULL'

注意, 实例化需要传入一个函数 (称为工厂函数).
可以用 :keyword:`lambda` 表达式,
也可以定义需要的函数再传入. (没有参数)

OrderedDict
===========

有序字典.
添加的元素是按照添加顺序排序的.

ChainMap
========

ChainMap 就是将多个字典组合起来,
当要查找一个元素时,
首先查找第一个字典, 如果存在, 则直接返回值.
否则将依次查找下去, 直到查找完毕,
则抛出异常 :exc:`KeyError`

可以用这个特性准备一个配置组: 默认, 配置文件, 命令行等.

::

    import collections as c

    default = {
        "path": ".",
        "name": "untitled.txt",
        "type": 2,
    }

    config_file = {
        "path": "/",
        "name": "new"
    }

    cli_args = {
        "path": ".."
    }


    chain = c.ChainMap(cli_args, config_file, default)
    chain["path"] # cli
    chain["name"] # file
    chain["path"] # default

Counter
=======

:class:`Counter` 可用作计数器.
当传入一个集合进行实例化时,
将计算集合中重复元素的数目.

不过在之后再写入时, 表现就和普通的 dict 一致了.
