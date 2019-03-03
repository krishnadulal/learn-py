#############
IPython Shell
#############

`IPython <https://ipython.org>`_
是一个比原生交互式解释器更好用的版本.

这些特性是我认为它好用的原因:

自动补全
    按下 :kbd:`Tab` 键, 可以自动补全标识符以及文件路径.
基于 Cell 而非 Line
    原版的 Python Shell 是以行为单位的,
    因此, 如果按上方向键, 出现的是上一行内容.
    如果要修改上次创建的类或函数, 这就十分不便了.

    而 IPython 则是以 Cell 为单位,
    一个函数, 类, 或跨行语句都会被归于一个 Cell 中,
    作为基本单元, 可以全部调出.
内置一些方便的指令(magic commands)
    例如测试 Cell 运行时间的 ``%%time`` 与 ``%%timeit``,
    查询内置文档的 ``?`` 指令等等.
能显示多媒体内容
    在终端里看图片怕不怕?
直接执行终端命令
    在命令前加 ``!`` 就会向系统 Shell 传递指令了.


一些好用的 magic commands
=========================

https://ipython.readthedocs.io/en/stable/interactive/magics.html

.. function:: ?

    ``?`` 查看可获取到的文档,
    ``??`` 则还会查看源代码(如果有的话).

    用法::

        someobj?
        someobj??

.. function:: %lsmagic

    查看所有可用的 IPython 魔法指令.

.. function:: %run path.py

    运行 ``path.py`` 脚本,
    运行完成后, 全局变量会保存在当前会话中.

.. function:: %load path.py

    将 ``path.py`` 的内容加载到当前 Cell 中.

.. function:: %who type

    查询当前会话中属于 ``type`` 类型的变量.

.. function:: %debug [-b file:line]

    以调试模式运行当前 Cell.
    有两种方式:

    1.  不带后面的参数,
        则是以调试模式运行当前 Cell,
        当发生异常后将进入 debug 环节,
        可以检查当前堆栈帧.
    2.  使用 ``-b file:line`` 参数
        为 file 文件第 line 行添加断点.
        当当前 Cell 调用目标模块,
        运行到断点位置的语句时,
        则会暂停运行, IPython 将充当 Debug Console.

.. function:: %edit [-options] [args]

    调用编辑器编辑, 结束后将代码导入此 Cell 中运行.
    默认调用环境变量 ``EDITOR`` 设置的编辑器.

    支持的选项:

    -n  <number>                设置编辑器打开时光标所在行号.
    -p                          打开上次编辑的文件
    -x                          退出编辑器后不执行代码

    当参数为以下形式时, 将执行对应动作:

    filename                    一个文件路径格式的参数,
                                将使 %edit 指令打开并编辑对应文件, 编辑结束后,
                                使用 :func:`execfile` 执行.
    history number              类似 1-3 这样的数字序列, 将被认为是历史编号.
                                将打开当前会话的 ``In[begin]`` 到 ``In[end]``
                                之间的 Cell 内容进行编辑.
    object                      一个 Python 中的标识符.
                                将会检测该对象的源代码, 找到定义这个对象的文件.
                                并跳转到对应位置进行编辑. 结束后自动执行.

.. function:: %save [-options] filename [ranges]

    将当前会话的 ranges 规定的范围保存到文件 filename 当中.
    filename 自动添加后缀名.

    -r                          默认保存经过处理的输入, IPython 中的一些语法将被
                                转化为 Python 函数. 设置此选项, 则保留原始输入,
                                即 IPython 中的输入.
    -f                          覆盖模式.
    -a                          追加模式.

    ranges 为用空格分割的 ``begin-end`` 序列, 如::

        %save ipython.py 1 2 3 5-11 13

.. function:: timeit

    可以用作单行模式 ``%timeit``, 也可用作 Cell 模式 ``%%timeit``.

    执行之后的语句, 并测试它们的运行耗时.

    -n <loop>                   每一轮测试的循环次数, 默认由 IPython 自动决定.
    -r <cycle>                  测试轮次. 默认为 7.
    -c                          测试 CPU clock 时间.
    -t                          使用计时器时间.
    -p <number>                 结果的显示精度.

    单行无参数的情况下可以使用 ``%time`` 代替.
