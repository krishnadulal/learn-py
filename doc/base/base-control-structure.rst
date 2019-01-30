########
控制结构
########

Python 中含有 :keyword:`for`, :keyword:`while`, :keyword:`if` 等循环或判断结构.
进入一个结构,
需要使用冒号 ``:`` 并添加一级缩进.
相同缩进表示一个代码块.
(并不使用花括号)

:keyword:`if`
=============

:keyword:`if` 判断结构是 Python 唯一的判断结构.
它的语法如下::

    if True:
        pass
    elif True:
        pass
    else:
        pass

它可以只包含 ``if - else``,
也可以添加多分支 ``if - elif - else``,
只要一个分支中的条件满足,
则执行后将会退出整个 :keyword:`if` 结构.

控制条件是按照顺序判定的.
当所有给出的条件都不满足时,
将会执行 :keyword:`else` 后的语句.

:keyword:`for`
==============

:keyword:`for` 循环语法如下::

    for _ in iterable:
        pass

它可以遍历一个可迭代对象的每一项元素,
得到的元素将会赋值给 :keyword:`in` 前的 ``_`` 变量,
如果得到的元素也是一个集合元素,
那么可以使用 ``a, b, c = iterable`` 进行解包.
当元素遍历完成后,
将退出此结构.

.. warning::

    最好不要在遍历时修改可迭代对象,
    这可能导致某些元素重复取出或跳过.

:keyword:`while`
================

:keyword:`while` 循环::

    while True:
        pass

当条件成立时, 执行循环体.

中断或继续
==========

-   :keyword:`break` 用在循环或判断结构中,
    将会直接退出结构
-   :keyword:`continue` 用在循环结构中,
    将会跳过本次循环,
    进行下一次循环的判定.
