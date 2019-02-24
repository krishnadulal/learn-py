####
函数
####

函数, 是程序中一组指令的集合, 是程序功能的一个次级模块.
虽然程序的所有逻辑都可以写在一个函数(或脚本)之中,
但是为了便于修改与扩展,
将程序尽量的模块化,
将关系最紧密的代码布置到一个函数中,
能明显地简化代码.

.. note:: 函数模块化

函数
====

在 Python 中, 可以如此定义一个函数::

    def function(param_1, param_2):

        # do something

        return result

在 :keyword:`def` 一行, 是为函数的函数头,
在这里, 定义了函数的命名与形式参数列表.
之下的 ``# do something`` 与 :keyword:`return` 语句
是函数的函数体.
函数体比函数头多一级缩进,
当缩进结束时, 表示这个函数结束.

函数命名与变量命名遵守相同的规则.
函数定义对参数的数目没有要求, 可以无参数,
也可以支持多个参数, 甚至 `无限参数`_ .

一个函数可以如此调用::

    result = function(arg1, arg2)

按照参数列表的要求, 将需要的参数传入, 经过函数的计算, 得到返回的结果.

关于函数的传参, 可以分 `定义时`_ 和 `调用时`_ 两个阶段来讨论.

定义时
------

默认参数
~~~~~~~~

在定义函数时, 对参数使用赋值语句,
将设置一个默认参数::

>>> def hello(name="Zombie110year")
>>>     print("Hello {}".format(name))

在默认参数被定义时, 调用该函数而不传入此参数,
则将该参数设置为默认值继续运行:

>>> hello()
Hello Zombie110year

而如果传入了参数, 那么则将参数的值设定为传入值.

>>> hello("NIHAO")
Hello NIHAO

.. _无限参数:

集合参数
~~~~~~~~

在定义时使用这样的语法::

>>> def log(*args, **kwargs):
>>>     print(type(args), type(kwargs))

在参数名前添加一个或两个星号,
则这两个参数将作为 :class:`tuple` 或 :class:`dict`
将调用时传入的参数或 `命名参数`_ 存储起来.

一个星号的 args(当然可以取其他命名) 存储直接传值的参数,
两个星号的 kwargs 存储以命名方式传入的参数.

可以用集合参数来承载无限个参数,
并只取用想用的部分.

参数的顺序
~~~~~~~~~~

定义函数时,
形参表中的形式参数需要遵守以下规律:

    普通参数在默认参数之前, 一般参数在集合参数之前.

例如::

    def function(a, b=1, *c, **d):
        pass

调用时
------

位置参数
~~~~~~~~

位置参数, 就是按照顺序直接传值,
会按照定义时的顺序将值赋给对应参数::

    def func(a, b, c):
        pass

    func(1, 2, 3)

    # a = 1, b = 2, c = 3

命名参数
~~~~~~~~

命名参数可以按照形参的命名将值传递给对应形参::

    func(b=1, c=2, a=3)

不过, 命名参数必须在位置参数之后,
并且不能将值传递给已接受位置参数的形参.

解包
~~~~

对于集合变量, 例如列表和元祖, 可以在传参时添加一个星号, 将其解包::

    args = (1, 2, 3)
    func(*args)

    # 等价于 func(1, 2, 3)

对于字典, 可以用两个星号解包::

    kwargs = {"a": 1, "b": 2, "c": 3}
    func(**kwargs)

    # 等价于 func(a=1, b=2, c=3)

传参顺序
~~~~~~~~

位置参数在命名参数之前, 一般参数在解包参数之前::

    func(1, *args, z=1, **kwargs)

函数的返回值
============

一个函数在遇到 :keyword:`return` 语句时, 会终止运行,
并将 return 的变量返回.

在 Python 中, 可以返回一个元祖::

    return 1, 2, 3

可以在调用时使用同等数量的变量来接收,
也可以同样使用星号来解包::

    a = func()
    # a = (1, 2, 3)

    a, b, c = func()
    # a = 1, b = 2, c = 3

    a, *b = func()
    # a = 1, b = [2, 3]

生成器
======

生成器就是将一个函数的 :keyword:`return` 语句替换成 :keyword:`yield`.

一个生成器将会保留上次调用的状态,
所以生成器的函数体一般都处于循环之内,
比如一个自然数生成器::

    def number():
        x = 0
        while True:
            yield x
            x += 1

在调用时, 需要先获得一个生成器实例::

    gen_num = number()

然后, 可以使用 :keyword:`for` 或 :class:`list` 或 :func:`next` 来获取返回值::

    x = next(gen_num)

生成器也可以设置参数::

    def number(start=0, step=1):
        x = start
        while True:
            yield x
            x += step

    gen_odd = number(0, 2)

    odd = next(gen_odd)

闭包
====

由于在 Python 中, 函数与其他对象一样,
都是可修改该的对象.

例如, 可以将一个函数命名赋值给一个变量,
就能如同函数一样调用它:

>>> def hello():
>>>     print("Hello")
>>> var = hello
>>> var()
Hello

甚至, 函数本身也可以作为函数的返回值:

>>> def outer():
>>>     def inner():
>>>         print("this is inner")
>>>     return inner
>>> x = outer()
>>> x()
this is inner

如果在内部定义的函数(称闭包函数)中引用了外部函数的局部变量
(使用 :keyword:`nolocal` 声明)
那么, 当外部函数 return 了,
而由于闭包函数还引用了局部变量,
导致局部变量不会被销毁, 而是绑定到了闭包函数中.

利用这个性质, 可以做到一系列需要多组全局变量才能做到的事.
例如一组计数器::

>>> def count(start=0, step=1):
>>>     i = start
>>>     def inner():
>>>         nonlocal i
>>>         i += step
>>>         return i
>>>     return inner
>>> x = count()
>>> x()
>>> # 1
>>> x()
>>> # 2


装饰器
======

类似于闭包, 装饰器也是对函数的高级利用.

一个装饰器同样是返回函数的函数.

假设, 要在运行函数之时打一个 log,
总不可能在每一个函数中调用 ``print`` 吧,
但是, 可以在装饰器中, 给传入的函数加点东西::

>>> from time import asctime
>>> def log(func):
>>>     def wrap():
>>>         print(asctime())
>>>         return func()
>>>     return wrap
>>>
>>> @log
>>> def hello():
>>>     print("Hello")
>>> hello()
Sun Feb 24 23:00:31 2019
Hello

最外层的 ``log`` 函数接受一个 func 参数,
在调用时::

    @log
    def func():
        return

是直接将定义的函数传入, 在装饰之后赋值给同名变量.

``@`` 符号是一个语法糖, 它的本义是::

    def func():
        return
    func = log(func)

如果被装饰的函数需要参数怎么做?
-------------------------------

用上方的 ``log`` 装饰器举例::

    from time import asctime
    def log(func):  # 这里, 定义装饰器的形参
        def wrap(): # 这里, 定义被装饰函数的形参
            print(asctime())
            return func() # 这里, 对需要的形参原样传入
        return wrap

一般情况下, 装饰器都是期望能用于所有函数的, 所以,
一般以 ``*args, **kwargs`` 来当参数::

    from time import asctime
    def log(func):
        def wrap(*args, **kwargs):
            print(asctime())
            return func(*args, **kwargs)
        return wrap
    @log
    def hello(name):
        print("Hello " + name)
    hello("Zombie110year")

    Sun Feb 24 23:07:47 2019
    Hello Zombie110year

如果装饰器需要参数?
-------------------

如果装饰器也需要参数,
那么就不是一层闭包能解决的了,
需要两层闭包:

-   最外层, 也是新加的一层, 用 ``log`` 充当装饰器的命名,
    装饰器需要的参数在这里传入.
-   次外层, 姑且命名为 ``decorator``, 就是原本的装饰器.
-   最内层, 命名为 ``wrap``, 也就是包装函数.

::

    def log(text):
        def decorator(func):
            def wrap(*args, **kwargs):
                print(text)
                return func(*args, **kwargs)
            return wrap
        return decorator

在调用时::

    @log("this is hello")
    def hello():
        print("Hello")

1.  首先, 调用了最外层的 ``log("this is hello")``,
    返回了一个经过修改的装饰器 ``decorator``
2.  然后, 调用了 ``decorator``, 将 ``hello`` 函数传入了进去.
    得到了装饰后的 ``hello`` 函数 (这时候的 hello 其实是 ``wrap`` 函数了)
3.  最后, 可以调用这个 hello 函数, 那么, 就会执行 ``wrap``
    函数. 即, 先调用了 ``print(text)``, 再调用原本的 hello.

匿名函数
========

匿名函数和普通的函数只在与没有函数名这一点上::

    lambda arg1, args2 : return_value

匿名函数一般用于临时使用, 例如在 :func:`filter`
或者 :func:`map` 中传入作为参数使用.

除了没有命名 (实际上会在内部生成机器命名) 之外,
其他和普通函数一样. 只是由于 :keyword:`lambda` 表达式
很简短, 只有形参与返回值两个部分, 所以无法定义复杂逻辑.
