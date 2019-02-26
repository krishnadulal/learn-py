#############
Ellipsis 对象
#############

在看一些 Python 源码的时候, 发现了个 ``...`` 的语法.

这竟然还是一个 Python 对象:

>>> type(...)
<class 'ellipsis'>

从网上看的一些资料, 这东西其实就表达一个 省略号 的意思.
单独使用时, 作用和 :keyword:`pass` 差不多.

它只有一个实例, 且不可修改.

又因为它是一个对象, 也可以用作参数传入函数中使用.

其他的一些讨论见

-   https://farer.org/2017/11/29/python-ellipsis-object/
-   https://www.keakon.net/2014/12/05/Python装逼篇之Ellipsis
