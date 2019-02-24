#######
logging
#######

logging 模块在导入后, 需要设置一下::

    import logging
    logging.basicConfig(filename="program.log", level=logging.DEBUG)

.. function:: basicConfig(filename, filemode, format, datefmt, style, level, stream, handlers)

    basicConfig 的参数都应使用命名参数的方式传入.

    :param level: 设置日志的输出等级

    level 共有 5 个等级: CRITICAL > ERROR > WARNING > INFO > DEBUG > NOTSET
    对应了 :func:`logging.critical`, :func:`logging.error` 等函数.
    当函数的等级高于设定等级时, 才会输出.

    :param str format: 设置日志输出的格式
    :param str datefmt: 设置日期格式, 格式需要被 :func:`time.strftime` 接受
    :param str style: 设置格式字符

    当 format 指定时, datefmt 和 style 才会生效.

    format 可用

    -   python3 format 函数语法: ``{message}``
    -   python2 % 语法: ``%(message)s``
    -   $ 语法: ``${message}``

    可用的命名字符串有:

    -   message 输入的消息
    -   asctime :func:`time.asctime` 格式的时间戳

    使用了对应的语法, 需要对 style 进行对应的设置,
    可选: ``%``, ``{``, ``$``.

    日期格式 datefmt 可以设置为通用的时间格式字符串:

    %Y-%m-%d %H:%M:%S

    -   %Y 公元年份
    -   %m 数字格式的月份
    -   %d 按月计算的天数
    -   %H 二十四小时制的小时数
    -   %M 分钟数
    -   %S 秒数
    -   %y yy-mm-dd 格式的日期
    -   %D dd/mm/yy 格式的日期
    -   %h 单词格式的月份
    -   %s Unix 时间戳

    :param stream: 输出目标, 可以为一个打开的可写文件或者 stdout, stderr
    :param handlers: 一组添加到 root logger 的 handler.
    :param str filename: 将日志保存至文件
    :param str filemode: 如果 filename 被定义, 才定义此参数,
        定义文件的打开方式, 默认为 'a'

然后, 可以使用对应函数在程序中输出日志::

    logging.info("程序启动")
    logging.debug("xxxx 当前值为 yyyy")
    logging.warning("zxc == NULL")
    logging.error("isinstance(z, float)")

在什么时候使用 logging, 官方文档给出了一个参考意见:

https://docs.python.org/3/howto/logging.html#when-to-use-logging

+----------------------------------+----------------------------------------+
| 你想要做什么                     | 你的选择                               |
+----------------------------------+----------------------------------------+
| 在控制台显示一些信息             | :func:`print`                          |
+----------------------------------+----------------------------------------+
| 报告在程序正常运行期间发生的事件 | :func:`logging.info` 或者              |
| (例如, 用于状态监视或故障调查)   | 输出更详细的信息 :func:`logging.debug` |
+----------------------------------+----------------------------------------+
| 发送有关特定事件的警告           | :func:`logging.warnning`               |
+----------------------------------+----------------------------------------+
| 报告有关特定事件的错误           | raise 一个异常                         |
+----------------------------------+----------------------------------------+
| 报告一个不会导致异常的错误       | :func:`logging.error`                  |
|                                  | :func:`logging.exception`              |
|                                  | 或者 :func:`logging.critical`          |
+----------------------------------+----------------------------------------+
