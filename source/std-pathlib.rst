.. _pathlib:

#######
pathlib
#######

pathlib 是对 os 库中关于文件路径的部分的一个替代产物, 秉持了面对对象的基本思想. 封装效果好, 简单易用.

pathlib 中, 提供了 ``Path`` 类作为面向用户的接口, 它的底层实现, 根据操作系统的不同而有所不同, 不过对于使用者来说, 只需要使用 ``Path`` 类即可.

实例化 Path
===========

::

    x = Path("std-pathlib.rst")

``Path`` 并不在实例化时检查该路径是否存在, 也不区分该路径代表一个文件或者目录. 当调用相关方法的时候, 在文件系统中创建了实体, 才会储存相关的属性.

常用方法
========

joinpath()
----------

将路径连接起来.

::

    In [35]: x.joinpath("test")
    Out[35]: WindowsPath('std-pathlib.rst/test')

也可以使用 ``/`` 操作符, 该运算符的行为被重载为 ``joinpath``

::

    In [36]: x / "test"
    Out[36]: WindowsPath('std-pathlib.rst/test')

absolute()
----------

绝对路径. 只有当路径真实存在时, 才能获取绝对路径.

::

    In [25]: x.absolute()
    Out[25]: WindowsPath('D:/Github/my.Tutorials/learn-py/source/std-pathlib.rst')

    In [26]: x
    Out[26]: WindowsPath('std-pathlib.rst')

cwd()
-----

当前工作目录

::

    In [27]: x.cwd()
    Out[27]: WindowsPath('D:/Github/my.Tutorials/learn-py/source')

exists()
--------

存在性

::

    In [28]: x.exists()
    Out[28]: True

home()
------

所属用户的家目录

::

    In [29]: x.home()
    Out[29]: WindowsPath('C:/Users/zom')

open()
------

打开对应文件, 和内建函数 ``open`` 一致, 路径由该 ``Path`` 对象传入.

::

    opened_file = x.open("rt", encoding='utf-8')

    # do something

    opened_file.close()

touch()
-------

创建对应的空文件.

::

    x.touch(mode=438, exist_ok=True)
    # mode 是 Linux 系统的权限参数, 查询 Linux 命令 chmod; Windows 系统下无效.
    # (准确的说是非 ext* 文件系统下无效.)
    # exist_ok 设为 False 则在已存在对应文件时报错; 设为 True 时则不报错, 但是当
    # 已存在对应目录时, 什么也不做. 不会覆盖已有文件.

mkdir()
-------

创建对应目录, 和 ``os.mkdir()`` 一致, 路径由 ``Path`` 对象传入.

::

    x.mkdir()

    # 会在当前路径下创建一个名为 std-pathlib.rst 的文件夹.

    x.mkdir(mode=511, parents=False, exist_ok=False)
    # mode 是 Linux 系统的权限参数, 查询 Linux 命令 chmod; Windows 系统下无效.
    # (准确的说是非 ext* 文件系统下无效.)
    # parents 是
    # exist_ok 设为 False 则在已存在对应目录时报错; 设为 True 时则不报错, 但是当
    # 已存在对应目录时, 什么也不做.

rename()
--------

重命名文件或目录, 但是当改变了上级路径时, 也相当于移动 (mv) 该文件/目录.

::

    x.rename("std-pathlib")

该方法没有返回值, 并且, 当重命名了文件系统中的文件时, 并不会改变实例 ``x``, 如果需要建立 python 中的对象 -> 文件系统中的对象 的映射关系, 需要重新实例化一个 ``Path``.

另一个 ``replace`` 和该方法效果相同.

获取目录下的子对象
==================

iterdir()
---------

返回一个获取该目录下一级子对象的生成器.

glob()
------

返回一个获取该目录下满足通配符的一级子对象的生成器.

rglob()
-------

返回一个递归获取该目录下满足通配符的末端子对象的生成器.