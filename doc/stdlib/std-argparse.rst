########
argparse
########

基本使用方法
============

::

    import argparse

    ## 创建一个解析器实例
    parser = argparse.ArgumentParser(
        prog="这个程序叫什么名字",
        description="这是一个怎样的程序",

        # 在没有对应参数传入时, 不向结果中添加对应属性.
        # 不设置此项, 则会设为 None
        argument_default=argparse.SUPPRESS
    )

    ## 为解析器添加解析项目
    # 位置参数, 按照添加顺序解析, 一般是必填项
    parser.add_argument(
        "position", help="对此条目进行说明"
    )

    # 选项
    parser.add_argument(
        "-o", "--option", help="选项是可选的, 并且可携带其他参数"
    )

    # 解析项目, 获得 namespace
    args = parser.parse_args()

之后, 可通过访问 ``args.xxx`` 来获取对应的属性.

argparse 会解析命令行中输入的参数,
也可以向 :meth:`argparse.ArgumentParser.parse_args`
传入一个形式和 :data:`sys.argv` 一致的列表,
那样的话, argparse 则会解析传入的列表.
默认传入 :data:`None`, 从而解析 ``sys.argv[1:]``

解析器实例化
------------

.. class:: argparse.ArgumentParser

    .. method:: __init__(prog=None, usage=None, description=None, epilog=None, parents=[], formatter_class='argparse.HelpFormatter', prefix_chars='-', fromfile_prefix_chars=None, argument_default=None, conflict_handler='error', add_help=True, allow_abbrev=True)

        :param str prog: 该程序的名字, 预设为 None,
            在后续设置 ``add_argument()`` 的 ``help`` 参数时,
            可以使用 ``%(prog)s`` 作为格式化占位符.
        :param str usage: 帮助信息中第一行的 ``Usage: ...`` 信息, 预设为 ``None``,
            将自动生成(根据参数设置而不同)
        :param str description: 描述, 只有单行. 预设为 ``None``
        :param epilog: 在帮助信息最底部的额外说明. 预设为 ``None``
        :param list parents: 该解析器的父解析器,
            与后续的 `subparser`_ 有关. 预设为空列表 ``[]``
        :param formatter_class: 帮助信息的渲染格式,
            预设为 :class:`argparse.HelpFormatter`
        :type formatter_class: :class:`argparse.HelpFormatter`
        :param str prefix_chars: 用于标识可选参数的前缀字符, 预设为 ``-``.
            当该项设置为多余一个字符的字符串时,
            其中的每一个字符都可以当前缀使用.
        :param str fromfile_prefix_chars: 从文件读取参数! 预设为 ``None``
            定义此项后, 例如 ``@``,
            那么在命令行中输入参数 ``prog.py @file.args``
            将会从文本文件 ``file.args`` 中读取参数,
            其他命令行参数会被忽略.
            文件中的参数必须一项一行. 其他要求详见 `从文件读取参数`_
        :param argument_default: 每一条项目的默认值. 预设为 ``None``

            -   ``argparse.SUPPRESS`` 当命令行中没有传入对应参数时,
                不向解析结果中添加对应属性
            -   ``None`` 当命令行中没有传入对应参数时,
                将解析结果中对应属性的值设为 None
            -   ``其他 Python 对象`` 当命令行中没有传入对应参数时,
                将解析结果中对应属性的值设为该值(和 ``None`` 的表现一致)

        :param str conflict_handler: 对冲突的处理方案, 预设为 ``"error"``

            -   ``error`` 不允许参数重复
            -   ``resolve`` 参数重复将导致覆写

        :param bool add_help: 允许内置 ``-h/--help`` 选项, 预设为 ``True``
        :param bool allow_abbrev: 允许长选项的缩写, 预设为 ``True``
            例如, 在无歧义时,
            ``--target`` 可以简写为 ``--t`` 或 ``--ta`` 或 ``--tar`` ...

添加解析规则
------------

argparse 可解析的参数分为 位置参数 与 选项 两种.
在定义时, 位置参数前没有前缀 ``-`` 符号::

    parser.add_argument('pos_arg')

而选项则用 ``-`` 标识::

    parser.add_argument('-t', '--target',
        help="定位目标"
    )

选项可以有短选项形式或长选项形式, 也可以同时为一个选项设置两种形式.
argparse 对选项的两种形式都是一样处理的.

位置参数在命令行中一般是必填项目,
它的值将直接传递给相应的命名.
多个位置参数在命令行中的相对位置应当和定义时一致.

而选项的填写则相对自由,
选项一般是可填可不填的, 对位置排列也没有要求.
选项的输入,
呈现 ``--name value`` 或 ``--name=value`` 的形式.
选项还有更多可调整的属性.

.. class:: argparse.ArgumentParser

    .. method:: add_argument(*args, **kwargs)

        :param args: ``name`` 或 ``flag``.
            此项设置条目的命名或性质.

            -   传入单个无前缀命名, 则该条目为一个位置参数.
                ``add_argument("name")``
            -   传入带前缀命名, 则该条目为一个选项, 可同时定义长选项与短选项.
                ``add_argument("-o")`` 或 ``add_argument("--option")``
                或 ``add_argument("-o", "--option")``

        :type action: :class:`argparse.Action` or :class:`str`
        :param action: 参数的解析动作, 预设为 ``store``, 存储该值.
            若为字符串, 则调用对应的预设动作,
            也可自定义 Action 类.

        :type nargs: :class:`str` or :class:`int`
        :param nargs: 项目的值容量, 预设为 ``None``, 也就是一个值.

        :param const: 常量, 预设为 ``None``.
            配合 action, nargs 等属性使用.
        :param default: 输入参数的默认值. 预设为 parser 的 ``argument_default`` 值.
            配合 action, nargs 等属性使用.


        :param type: 条目值的类型, 预设为 ``str``.
            实际上, 从命令行读取数据都是以字符串的形式进行的.
            如果不是简单的进行基本类型转换, 例如 int, float 等,
            更建议通过 `自定义 Action`_ 对值进行解析.

        :param list choices: 该条目的值域, 传入值必须在其中.
            预设为 ``None``, 不作要求.

        :param bool required: 只作用于选项, 是该选项为必填项. 预设为 ``False``
        :param str help: 提示信息
        :param str metavar: 传值示例
        :param str dest: 定义该条目的命名

action
~~~~~~

-   ``store`` 保存参数值
-   ``store_const`` 只能用于选项.
    当选项存在时, 保存 ``add_argument()`` 中 ``const`` 参数定义的值.

::

    In [6]: parser.add_argument("--set10", dest="num", action="store_const", const=10)
    Out[6]: _StoreConstAction(option_strings=['--set10'], dest='num', nargs=0, const=10, default=None, type=None, choices=None, help=None, metavar=None)
    In [8]: parser.parse_args(['--set10'])
    Out[8]: Namespace(num=10)

-   ``store_true``,
    ``store_false`` 只能用于选项.
    将参数保存为布尔值.
    对于 ``store_true``, 若参数存在,
    则保存为 ``True``,
    否则 ``False``;``store_false`` 和 ``store_true`` 行为相反.
-   ``append`` 只能用于选项.
    将参数值添加到 list 中,
    若参数重复出现, 则保存多个值.
-   ``append_const`` 只能用于选项.
    当选项出现, 则将 ``const`` 添加到值中.
-   ``count`` 只能用于选项.
    记录此参数的个数, 将数目储存.
    对于短选项, 可以这么用: ``-v`` , ``-vvvv`` = 4.
-   ``help`` 只能用于选项. 打印帮助信息, 然后退出.
-   ``version`` 只能用于选项.
    打印程序的版本信息, 然后退出. 必须同时定义 ``version`` 的值.

::

    parser.add_argument('--version', action='version', version="%(prog)s v0.0")

nargs
~~~~~

``nargs`` 属性设置项目的值的容量. 默认为 ``None``.

0. 当为 ``None`` 时, 该选项只接受一个值.
1. 当为一个整数 n 时, 该选项的值为一个长度为 n 的列表, 并且必须接受同等数目的值
2. 当为 ``?`` 问号时, 需要定义 ``const`` 与 ``default``, 有以下可能:
    -   ``--foo`` 未出现, 则值为 ``const``
    -   ``--foo`` 出现, 但没有指定值, 则值为 ``default``
    -   ``--foo=value`` 则值为 ``value``

::

    parser.add_argument('--foo', nargs='?', const='const', default='default')


3.  ``*``. 将会把从选项所在位置之后的所有值存入列表, 直到下一个选项.
4.  ``+``. 将会把从选项所在位置之后的所有值存入列表, 直到下一个选项. 但至少需要一个值.
5.  ``argparse.REMAINDER`` 储存所有未解析的参数.

从文件读取参数
--------------

当定义了解析器的 ``fromfile_prefix_chars`` 属性时,
可以在命令行中使用::

    example.py @/path/to/argsfile.txt

从文件中读取参数.

文件形式为一个用换行符分隔的列表, 例如::

    -o
    value
    position_arg1
    position_arg2
    --option1
    value
    --many_option
    value1
    value2

帮助信息
--------

``help=argparse.SUPPRESS`` 将会使该条 help 不显示.

在实例化解析器 或者 调用 ``add_argument`` 时, 都可以指定 ``help`` 参数用于编写帮助信息中, 其中可以使用以下格式控制符:

-   ``%(prog)s`` 程序名
-   ``%(default)s`` 只能用于参数. 默认值
-   ``%(type)s`` 只能用于参数. 参数类型
-   ``%(nargs)s``

自定义 Action
=============

可以自定义 Action 类, 需要继承 `argparse.Action`.

::

    class BuiltfulVersion(argparse.Action):
        def __init__(self, option_strings, dest, nargs=None, **kwargs):
            if nargs is not None:
                raise ValueError("nargs not allowed")
            super(BuiltfulVersion, self).__init__(option_strings, dest, **kwargs)
        def __call__(self, parser, namespace, values, option_string=None):
            print("%r %r %r" % (namespace, values, option_string))
            setattr(namespace, self.dest, values)

.. class:: BuiltfulVersion(argparse.Action)

    .. method:: __init__(self, option_strings, dest, nargs=None, **kwargs)

        一般都在 ``__init__`` 方法中对该 argument 的设置进行检查.

        :param option_strings: 其他解析选项
        :param str dest: 该参数的命名,
            :meth:`argparse.ArgumentParser.add_argument` 传入
        :param nargs: :meth:`argparse.ArgumentParser.add_argument` 传入的 ``nargs``

    .. method:: __call__(self, parser, namespace, values, option_string=None):

        在 ``__call__`` 中对 ``values`` 进行处理,
        将其写入 ``namespace`` 命名空间中.

        常用 :func:`getattr` 和 :func:`setattr` 与 namespace 交互.

        一般只操作 namespace 与 values

        :param parser: 该参数所依附的解析器
        :param namespace: 该参数依附的解析器将返回的 :class:`argparse.Namespace`
        :param values: 传入的值, 根据 nargs 和 type 的不同,
            可能是各种独立类型或容器类型.
        :param option_string: 解析选项

subparser
=========

如果一个应用程序需要通过不同的入口,
解析不同的参数,
执行不同的程序.
那么, 一个 subparser 就很有设置的必要了.

首先, 定义一个顶层根解析器,
然后从这个根解析器分支子解析器.

根解析器和子解析器都可以添加解析条目.

在运行时,
调用根解析器的 ``parse_args`` 方法,
得到解析的 namespace.

以下是我编写的 PDF 工具
`pdfwork <https://github.com/zombie110year/pdfwork>`_
中的部分代码::

    parser = ArgumentParser(
        prog="pdfwork", description="处理 PDF 文件",
    )

    # 添加子解析器分组,
    # 相当于在根解析器创建了一个可选的位置参数.
    tools = parser.add_subparsers(
        dest="cmd", title="sub-cmd", help="子命令"
    )

    # 具体的一个子解析器,
    # 自动添加到 tools 的 choice 分组
    # 除了 prog 属性改为 name 属性之外,
    # 其他的和普通 ArgumentParser 一样
    merge = tools.add_parser(
        name="merge", description="合并多个 PDF 文件"
    )

    # 对这个子解析器添加解析条目
    merge.add_argument(
        '-o', '--output', default=Path('merged.pdf'),
        metavar='example.pdf', help='合并输出到 PDF 文件',
        action=SetFilePathAction
    )
    merge.add_argument(
        '-i', dest='files', nargs=2, required=True,
        metavar='page.pdf 100', help='输入文件以及重复次数', type=str,
        action=AppendInputAction
    )

    # 另一个子解析器也是同样的操作
    extract = tools.add_parser(
        name="extract", description="提取 PDF 的一部分, 输出至目标文件中",
    )

    extract.add_argument(
        "origin", help="原文件", metavar="origin.pdf",
        action=SetFilePathAction
    )

    extract.add_argument(
        "-e", "--extract", help="输出文件, 以及抽取的页码, 连续页码用 - 间断页码用 ,. 连续页码为闭区间", metavar="exam.pdf 1-19,2,34",
        nargs=2, action=ParsePagesAction, required=True
    )

    args = parser.parse_args()


由于在上面的代码中,
对子解析器分组 ``tools`` 定义了 ``dest=cmd`` 属性,
因此, 在最后返回的 namespace 中,
就含有 ``args.cmd`` 属性,
这个属性存储了调用的子解析器的命名::

    if args.cmd == 'merge':
        from .merge import merge
        merge(args)
    elif args.cmd == 'extract':
        from .extract import extract
        extract(args)
