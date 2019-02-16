####################
打包你的 Python 项目
####################

:mod:`setuptools` 提供了 Python 项目的打包工具.

该模块提供了 :func:`setuptools.setup` 函数作为启动入口.
打包所需的所有信息都作为参数传入此函数中.

添加数据文件
============

如果用以上的方法直接打包, 那么, 只有 Python 代码( .py 后缀的文件) 才会被装进库中.
要想包装一些数据文件, 比如一些文本模板, 图片, 等等,
需要在 setup.py 中传入参数::

    include_package_data=True

并且, 在 ``MANIFEST.in`` 文件中,
使用 ``include`` 语句用相对或绝对路径指出需要包含的特殊文件.

setup.py 支持的一些指令
=======================

基本指令

======================= ============================================================
----------------------- ------------------------------------------------------------
``build``               build 所有需要安装的东西 (存储在 build 目录下)
``build_py``            "build" 纯 Python 模块 (只是复制到 build 目录下)
``build_ext``           build C/C++ 和 Cython 扩展 (编译并链接, 放入 build 目录)
``build_clib``          build Python 扩展用到的 C/C++ 库
``build_scripts``       "build" 脚本 (复制并加上 shebang #!)
``clean``               清理 build 目录下的临时文件 (Windows 系统无效)
``install``             从 build 目录安装到当前环境下的 Lib/site-packages 目录
``install_lib``         安装所有 Python 模块 (扩展与纯 Python)
``install_headers``     安装 C/C++ 头文件
``install_scripts``     安装脚本 (Python 或 其他)
``install_data``        安装数据文件
``sdist``               创建一个源代码的分发包 ( tar, zip 或其他)
``register``            在 PyPI 上注册此项目
``bdist``               创建一个二进制分发包
``bdist_dumb``          创建一个 "dumb" 构建分发包
``bdist_rpm``           创建一个 RPM 分发包
``bdist_wininst``       创建一个 MS Windows 分发包(一个具有图形界面的 exe 安装程序)
``check``               对包做一些检查
``upload``              将二进制包上传至 PyPI
======================= ============================================================

额外指令

======================= ============================================================
指令                    功能
----------------------- ------------------------------------------------------------
``bdist_wheel``         创建 wheel 分发包
``bdist_sphinx``        构建 Sphinx 文档
``alias``               定义一个快捷方式来调用一个或多个指令
``bdist_egg``           创建一个 "egg" 分发包
``develop``             在 开发者模式 安装包
``dist_info``           创建一个 .dist-info 目录
``easy_install``        发现/获取/安装 Python 包
``egg_info``            创建一个分发包的 .egg-info 目录
``install_egg_info``    为这个包安装 .egg-info 目录
``rotate``              删除旧得分发包, 保持 N 最新的文件
``saveopts``            保存提供的选项到 setup.cfg 或其他配置文件
``setopt``              设置一个选项到 setup.cfg 或其他配置文件
``test``                在 build 之后运行单元测试
``upload_docs``         上传文档到 PyPI
``isort``               对在 setuptools 中注册的模块运行 isort
``compile_catalog``     编译 message catalog 到二进制 MO 文件
``extract_messages``    从项目代码中提取可本地化的字符串
``init_catalog``        基于 POT 文件创建一个新的 catalog
``update_catalog``      从 POT 文件更新 message catalogs
======================= ============================================================

参考链接
========

-   如何打包你的Python代码,
    https://python-packaging-zh.readthedocs.io/zh_CN/latest/non-code-files.html