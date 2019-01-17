#################
Python 文件扩展名
#################

编写 Python 程序, 一般都是将其保存在 ``.py`` 后缀的文本文件之中, 这是通常所看到的 Python 代码文件.

与 Python 相关的文件后缀还有 ``.pyw``, ``.pyc``, ``.pyo``, ``.pyx``, ``.pyd``, ``.pyz`` 等等, 以下是详细介绍.

py pyw
======

``.py``, ``.pyw`` 其实都是 Python 源代码. Python 提供了两种解释器: ``python`` 或 ``pythonw``, 前者是命令行解释器, 会弹出一个控制台窗口, 而后者是常用于图形界面程序的解释器, 除了程序的主窗口之外, 不会弹出额外的控制台窗口.

而 ``.py`` 与 ``.pyw`` 则是在这方面进行区分. ``.pyw`` 被约定作为图形界面程序的后缀名. 实际上, Python 解释器根本不挑剔后缀名, 哪怕代码文件根本没有后缀名, 只要作为参数传递给解释器, 也是可以运行的.

这个两个后缀名的区别是为了方便人类区分.

pyc pyo
=======

Python 是一门动态语言, 是用 PVM (Python Vitual Machine) 来动态解释源代码执行的. 在执行时, 会将人类可读的源代码 (.py 文件) 先编译为字节码 bytes code, 然后交给 PVM 执行. 对于不同的解释器, 不同的版本, 字节码的格式可能不一样.

运行单模块时, 也就是运行 ``python xxx.py`` 这样的命令时, 生成的字节码只会作为 ``PyCodeObject`` 存在内存中, 当程序结束后便会清除. 而当程序中存在 ``import`` 语句时, Python 则会在当前工作目录下创建 ``__pycache__`` 目录, 将 import 的模块生成的字节码保存在其中. ``.pyc`` 就是 Python 自动保存的字节码文件使用的后缀名. 当 Python 运行一个模块时, 首先寻找它的 ``.pyc`` 文件, 找到了就直接载入, 否则就重新编译, 运行结束后保存. 如果 .pyc 文件的最后修改时间早于对应的 .py 文件, 那么也会重新编译. [#ref_1]_

.. [#ref_1] 参考了 `<https://michaelyou.github.io/2016/01/23/pyc文件和python程序的执行过程/>`_

``.pyc`` 是一个二进制文件. 它的命名方式为::

    <模块名>.<解释器版本>.<优化等级>.pyc

如果优化等级为 0, 那么这一项是不在文件名中表达的. 并且, 在每个文件的头部, 都有相同的 magic number: ``42 0D 0D 0A 00 00 00 00``.

编译 pyc
--------

除了 ``import`` 之外, 可以手动调用标准库 :mod:`py_compile` 来将指定模块编译为字节码保存::

    python -m py_compile hello.py

会自动保存在工作目录的 ``__pycache__`` 下.

或者, 可以在一个脚本中完成以上工作::

    import py_compile

    py_compile.compile("D:/_Playground/py/hello.py")
    # 需要绝对路径

.. function:: py_compile.compile(file, cfile=None, dfile=None, doraise=False, optimize=-1, invalidation_mode=<PycInvalidationMode.TIMESTAMP: 1>)

    :param file: 源代码文件路径.
    :param cfile: 编译的目标文件名. 如果不指定(默认为 None) 则按照 PEP 3147/PEP 488 的规定命名.
    :param dfile: 声称的文件名, 即出现在错误警告中的文件名, 默认为源文件名.
    :param doraise: 指示在找到编译错误时是否应引发异常的标志. 如果发生异常并且此标志设置为 False, 则将打印一个指示异常性质的字符串, 该函数将返回给调用者. 如果发生异常并且此标志设置为 True，则将抛出 PyCompileError 异常.
    :param optimize: 设置编译的优化等级. 可用的值有 -1,0,1,2. -1 表示使用解释器设定的优化等级, 即使用命令行参数 ``-O`` 设定的等级.
    :param invalidation_mode: 未找到文档
    :return: 生成的文件的路径

    .. note:: 所有的参数都是位置参数, 不支持命名参数.

如果要批量地编译, 使用 :mod:`compileall` 模块编译整个目录下的所有模块::

    python -m compileall /path/to/src/dir

详见 https://docs.python.org/3/library/compileall.html .

``.pyo`` 则是优化编译的字节码, 和 ``.pyc`` 是一样的作用, 只不过设置了优化选项::

    python -m py_compile -O hello.py    # 1 级优化, 移除断言以及其他调试信息
    python -m py_compile -OO hello.py   # 2 级优化, 在 1 级优化之后再移除文档字符串

这里的优化并不涉及到程序逻辑.

.. important::
    .pyo 是 Python2 使用的命名方式, Python3 使用 module.cpython-37.opt-1.pyc 这样的命名.

运行 pyc
--------

``.pyc`` 文件可以使用 ``python hello.cpython-37.pyc`` 直接运行.

反编译 pyc
----------

可以使用工具 `<https://github.com/rocky/python-uncompyle6>`_

pyd
====

``.pyd`` 是使用其他语言编写并编译给 Python 使用的动态链接库. 本质上就是一个 ``.dll`` (Windows) 或 ``.so`` (Linux).

在 import 时, ``.pyd`` 的表现和普通的 ``.py`` 模块一致, 可以将其等同于一个 ``.py`` 来使用, 只不过无法查看或修改源代码.

pyx
===

``.pyx`` 是使用 Cython 语言为 Python 编写 C/C++ 扩展时约定使用的源代码文件后缀名.

pyz
===

Python3.5 之后, 可以使用标准库 :mod:`zipapp` 将 Python 模块打包成一个可执行的 .zip 压缩包, 并使用 ``.pyz`` 后缀名. zipapp 的用法见本站 :ref:`zipapp`.