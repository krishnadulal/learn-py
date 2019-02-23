############
configparser
############

:mod:`configparser` 是一个用于解析 ini 配置文件的库.

一个 ini 文件有着以下结构:

.. code-block:: ini

    [node_name] ; 这是一个 section
    key = value
    key2 = value2

    [another_node_name]

    key3 = value3

所有的值都是以字符串的形式读取到 Python 中的.
整个配置文件都存在一个类似字典的结构当中, 而一个分组则对应一个次级字典::

    {
        "node_name": {
            "key": "value",
            "key2": "value2",
        },
        "another_node_name": {
            "key3": "value3",
        },
    }

ConfigParser
============

要使用 configparser 库,
需要首先引入库中的 :class:`configparser.ConfigParser` 类,
并实例化一个解析器类::

    from configparser import ConfigParser

    parser = ConfigParser()

可以在程序中读取, 设置, 或修改 ``parser`` 的配置::

    parser["name"] = "ConfigParser"
    parser["other"] = {
        "id": None,
        "path": "/",
    }

可以打开一个文件, 将配置写入::

    with open("config.ini", "wt") as file:
        parser.write(file)

也可以直接传入一个路径(或打开这个文件的流)读取配置::

    parser.read("config.ini")

    # with open("config.ini", "rt") as file:
    #    parser.read(file)

确定读取类型
==========

ini 配置文件默认所有数值都是字符串,
ConfigParser 提供了基本的解析功能:

.. function:: get()

    get()
    getboolean()
    getfloat()
    getint()

下面以 ``_static/ini/example.ini`` 为例, 解释功能.

>>> from configparser import ConfigParser
>>> parser = ConfigParser()
>>> parser.read("../_static/ini/example.ini", encoding="utf-8")
>>> parser.get("root", "path")
'/home/zombie110year/exec.bin'
>>> parser.get("root", "age")
'1.2'
>>> parser.getfloat("root", "age")
1.2
>>> parser.get("root", "writable")
'true'
>>> parser.getboolean("root", "writable")
True

以此类推.
