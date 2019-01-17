.. _zipapp:

######
zipapp
######

:mod:`zipapp` 是一个管理可被 Python 解释器执行的包含 Python 代码的 zip 归档的工具.

从命令行创建
============

假设, 现在有一个 Python 包, 其目录结构如下:

.. code-block:: none

    example/
        __init__.py
        something.py

在 ``something.py`` 模块中, 有一个函数 ``sayHello``, 其作用就是输出一句 "Hello World".

运行以下命令创建一个 ``.pyz`` 后缀的归档:

.. code-block:: sh

    python -m zipapp -m "something:sayHello" example

- ``python -m zipapp`` 是调用 zipapp 标准库的入口函数, 可以视作一个命令, 后面的 ``-m`` 选项不要与这里的 ``-m`` 混淆.
- ``-m "something:sayHello`` 指定了归档的程序入口, 语法类似 "模块路径:函数名".
- 最后的 ``example`` 则是指定这个包在文件系统中的位置.

然后会在当前目录下生成名为 ``example.pyz`` 的归档. 可以使用 ``python example.pyz`` 来运行. 将会在 stdout 上输出 ``Hello World``.

将该 .pyz 文件以 .zip 文件的方式打开, 看到其中就是对原 Package 的压缩打包 (但是压缩率为 0...), 只不过多了一个 ``__main__.py`` 模块, 其中出现了以下语句::

    # -*- coding: utf-8 -*-
    import something
    something.sayHello()

关于入口路径
------------

在指定 ``-m "something:sayHello`` 时, 发现以下几个要点:

1. 不需要指定最外层包

如果传入 ``-m "example.something:sayHello"``, 虽然能生成对应的压缩包, 但是在执行时会报错 ``ModuleNotFoundError: No module named 'example'``. 因为归档内创建 ``__main__.py`` 模块时, 生成的是以下语句::

    # -*- coding: utf-8 -*-
    import example.something
    example.something.sayHello()

2. 不能使用相对路径

如果传入 ``-m ".something:sayHello"``, 在生成时便报错: ``__main__.ZipAppError: Invalid entry point: .something:sayHello``

3. 以类的静态方法作为入口

修改了 ``something.py`` 中的内容::

    class 人类():
        @staticmethod
        def 本质():
            while True:
                print(input())

然后通过 ``-m "something:人类.本质"`` 参数, 成功地创建了 .pyz 归档, 并且成功运行, 明白了人类的本质 😀.

命令行选项
==========

+-----------------+------------------------------------------------------+
| ``-o/--output`` | 指定目标文件路径,                                    |
|                 | 例如 ``-o test.zip`` 则会创建一个 test.zip 文件      |
+-----------------+------------------------------------------------------+
| ``-m/--main``   | 指定程序入口                                         |
+-----------------+------------------------------------------------------+
| ``-p/--python`` | 指定 shebang, 可用 python 或 pythonw.                |
|                 | 当在 Unix-like 系统中, 此选项将允许归档(.pyz) 能够以 |
|                 | ``./example.pyz`` 的方式执行.                        |
+-----------------+------------------------------------------------------+
| ``--info``      | 显示目标归档的 shebang 信息                          |
|                 |                                                      |
|                 | .. code-block:: sh                                   |
|                 |                                                      |
|                 |     $ python -m zipapp --info example.pyz            |
|                 |     Interpreter: <none>                              |
+-----------------+------------------------------------------------------+

API
===

程序提供了创建 pyz 文档的 API

.. function:: zipapp.create_archive(source, target=None, interpreter=None, main=None)

    从 ``source`` 创建一个 .pyz 归档, 到 target 指定的路径.

    :param source: 创建归档的源, 应当为:

        -   一个 Python 包的路径或者指向该包的 :class:`pathlib.Path` 对象.
        -   也可以为一个已有的 .pyz 归档, 将会复制它到一个新的归档. (一般来讲, 都是用此方法修改这个归档的 shebang).
        -   以 ``"rb"`` 模式读取的归档文件. 并且读指针应处于文件头部.

    :param target: 指定写入的目标归档, 可以为:

        - 一个文件名称或 :class:`pathlib.Path`, 将会写入指定的文件
        - 一个以 ``"wb"`` 模式打开的文件, 将会写入该文件
        - ``None`` (默认值), 同时 ``source`` 必须为一个目录, 生成的文件将会是 ``目录名.pyz``

    :param interpreter: 写入 shebang 的解释器路径. 在 Unix-like 系统中, 由系统解析, 并使归档可用 ``./example.pyz`` 方式执行; 在 Windows 系统, 则是由 Python 启动器处理.

    :param main: 指定用作归档的主程序的可调用名. 应当在 ``source`` 是目录且不包含 ``__main__`` 模块时指定. 采用 ``"pkg.module:callable"`` 的形式, 并且无法直接传递参数, 必须通过 :data:`sys.argv` 传参.

    :type source: str, pathlib.Path
    :type target: str, pathlib.Path
    :type interpreter: str
    :type main: str