######
random
######

random 简介
===========

在 :mod:`random` 模块中, 提供了三个常用的函数:

-  ``randint(a:int, b:int) -> int`` 返回 :math:`[a,b]` 之间的随机整数, 闭区间.
-  ``random() -> float`` 返回 :math:`[0,1)` 范围内的随机浮点数, 不包括 1.
-  ``seed()`` 设定随机数种子.

随机浮点数
==========

:func:`random.random`
---------------------

``random`` 返回 :math:`[0,1)` 之间的随机浮点数.

.. code:: python

   random() -> float

.. code:: ipython3

    RANDOM = []
    for i in range(32):
        RANDOM.append(random.random())
    showList(RANDOM)


.. parsed-literal::

    0.932145, 0.585761, 0.266209, 0.292376, 0.677802, 0.205647, 0.686904, 0.132223,
    0.073533, 0.878883, 0.624689, 0.999049, 0.963787, 0.507370, 0.708983, 0.449279,
    0.386094, 0.105186, 0.242520, 0.980925, 0.721951, 0.353227, 0.343717, 0.825081,
    0.931163, 0.050479, 0.058426, 0.047659, 0.350502, 0.906636, 0.709760, 0.180347,

    ===END===


:func:`random.uniform`
----------------------

``uniform`` 是对 ``random`` 的一个封装, 接受两个参数 ``min``, ``max`` , 用于生成从 ``min`` 到 ``max`` 的随机浮点数. 本质上是

.. code:: python

   uniform(min, max) == min + (max - min)*random()

.. code:: ipython3

    UNIFORM = []
    for i in range(32):
        UNIFORM.append(random.uniform(100, 200))
    showList(UNIFORM)


.. parsed-literal::

    112.638747, 199.294596, 136.588501, 129.424293, 101.353560, 191.487727, 114.927154, 103.494282,
    157.708606, 181.659964, 177.150655, 141.877326, 188.521830, 145.337710, 140.109476, 117.026358,
    180.602178, 167.703939, 141.257318, 171.280684, 165.434606, 124.803260, 137.109256, 105.323654,
    157.682474, 171.603650, 158.789115, 185.701245, 197.800756, 159.502018, 189.720423, 133.682513,

    ===END===


随机整数
========

:func:`random.randint`
----------------------

``randint`` 需要两个参数, 用于限定返回整数的范围.

.. code:: python

   randint(min, max) -> int

.. code:: ipython3

    RANDINT = []
    for i in range(32):
        RANDINT.append(random.randint(1, 100))
    showList(RANDINT)


.. parsed-literal::

      47,   53,   79,   42,   66,   43,   79,   53,
       7,   23,    6,   47,   72,   11,   76,   53,
      18,   40,   20,   55,   83,   69,   56,   51,
      84,   93,  100,   43,   82,   31,   57,   26,

    ===END===


:func:`random.randrange`
------------------------

``randrange`` 接受两个或三个参数, 当接受两个参数时, 效果与 ``randint`` 相同, 当输入了第三个参数时, 会将其作为步长.

效果相当于从 ``range(min, max, step)`` 生成的序列中随机选取一个.

.. code:: python

   randrange(min, max, step) -> int

.. code:: ipython3

    RANDRANGE1 = []
    RANDRANGE2 = []
    for i in range(32):
        RANDRANGE1.append(random.randrange(1, 100))
        RANDRANGE2.append(random.randrange(0, 100, 10))
    showList(RANDRANGE1)
    showList(RANDRANGE2)


.. parsed-literal::

       5,   28,   59,   91,   66,   49,   45,   27,
      87,   76,   64,   86,   38,   64,   42,   52,
       3,   26,   73,   44,   28,   87,   49,   45,
      63,   31,   93,   11,   22,   69,   35,   77,

    ===END===
      90,   90,   20,   90,    0,   30,   10,   90,
      60,   30,   10,   60,   80,    0,   90,   40,
      20,   50,   20,   60,   40,   10,   80,   80,
      80,   10,    0,   20,   20,   30,   50,   80,

    ===END===


生成器状态
==========

:func:`random.seed`
-------------------

``random()``

每次调用的时候都生成不同的值，并且在它重复任何数字之前有一个很大的周期。这对于生成唯一值及其变体很有用，但有时以不同的方式处理相同的数据集是很有用的。一种技术是用一个程序生成随机数并保存他们以通过单独的步骤进行处理。然而，对于大量数据可能不实用，所以，random 模块包含了 seed() 函数用于初始化伪随机数生成器以生成预期的一组值。

``seed`` 的参数可以是任何可 Hash 对象, 相同的 ``seed`` 会使得随机数生成器产生相同的值.

就算不设置, random 也会自动用 ``/dev/random`` 或 ``/dev/urandom`` (Linux) 或者当地时间来设置 ``seed``

.. code:: ipython3

    SEEDED = []
    random.seed(1)
    for i in range(32):
        SEEDED.append(random.randint(1, 100))
    showList(SEEDED)


.. parsed-literal::

      18,   73,   98,    9,   33,   16,   64,   98,
      58,   61,   84,   49,   27,   13,   63,    4,
      50,   56,   78,   98,   99,    1,   90,   58,
      35,   93,   30,   76,   14,   41,    4,    3,

    ===END===


:func:`random.getstate`, :func:`random.setstate`
------------------------------------------------

``getstate()`` 与 ``setstate()`` 函数分别用于 保存 与 载入 生成器状态.

``random.getstate()`` 函数返回当前随机数生成器的状态,
应当用一个变量去接收它,

随后, 可以使用 ``random.setstate(x)`` 将随机数状态设置为 x 所指量.

用于避免多次运行同一程序时产生重复数据.

.. code:: ipython3

    STATE = []
    for i in range(32):
        STATE.append(random.random())
    showList(STATE)


.. parsed-literal::

    0.025446, 0.541412, 0.939149, 0.381204, 0.216599, 0.422117, 0.029041, 0.221692,
    0.437888, 0.495812, 0.233084, 0.230867, 0.218781, 0.459603, 0.289782, 0.021490,
    0.837578, 0.556454, 0.642294, 0.185906, 0.992543, 0.859947, 0.120890, 0.332695,
    0.721484, 0.711192, 0.936441, 0.422107, 0.830036, 0.670306, 0.303369, 0.587581,

    ===END===


.. code:: ipython3

    r_state = random.getstate()

.. code:: ipython3

    STATE_a = []
    random.setstate(r_state)
    for i in range(32):
        STATE_a.append(random.random())
    showList(STATE_a)


.. parsed-literal::

    0.882479, 0.846197, 0.505284, 0.589002, 0.034526, 0.242740, 0.797404, 0.414314,
    0.173007, 0.548799, 0.703041, 0.674486, 0.374703, 0.438962, 0.508426, 0.778443,
    0.520938, 0.393255, 0.489694, 0.029575, 0.043487, 0.703382, 0.983188, 0.593184,
    0.393600, 0.170349, 0.502239, 0.982077, 0.770523, 0.539617, 0.860290, 0.232176,

    ===END===


   可以通过 pickle 将这个状态量写入文件或从文件读取.

操作序列
========

从序列中随机抽取
----------------

:func:`random.choice` 函数接收一个参数, 从传入的序列中随机选择一个值返回.

.. code:: python

   random.choice(iterable)

.. code:: ipython3

    outcomes = {
        'heads': 0,
        'tails': 0,
    }
    sides = list(outcomes.keys())

    for i in range(10000):
        outcomes[random.choice(sides)] += 1

    print('Heads:', outcomes['heads'])
    print('Tails:', outcomes['tails'])


.. parsed-literal::

    Heads: 5052
    Tails: 4948


不重复地从序列中选择
--------------------

:func:`random.choice` 函数可能会重复地抽取同一元素, 而 ``shuffle`` 的作用是将该序列打乱顺序, 并赋值给原变量.

随机采样
--------

:func:`random.shuffle` 将原序列打乱, 而 ``sample`` 只会返回新的序列, 原序列不会改变.

.. code:: python

   sample(sep, counts) -> iter
   "输入一个序列, 返回此序列随机采样, counts 控制采样数"

random 类
=========

``random`` 库中提供了 :class:`random.SystemRandom` 类用于自定义随机数生成器.

在实例化后, 都可以对它们执行模块级函数对应的方法.

一些操作系统提供了一个随机数字生成器，它可以访问随机数生成器引入的更多熵源。random 通过 SystemRandom 暴露了这个功能，它和 Random 有相同的 API，但是使用 os.urandom() 生成构成其它算法基础的值。

SystemRandom 生成的序列是不可预测的，因为随机性来源于系统，而不是软件（实际上，seed() 和 setstate() 对它都没有影响）。

概率与统计模拟器
================

``random`` 库提供了一些概率分布的生成函数. 上述的模块级方法会生成均匀分布的随机数.

正态分布
--------

:func:`random.normalvariate` 和 :func:`random.gauss` (更快).

指数分布
--------

:func:`random.expovariate` 和 :func:`random.paretovariate`

近似分布
--------

三角分布用于小样本量的近似分布。三角形分布的曲线在已知的最小和最大值处具有低点，并且在模式处具有高点，其基于最可能的结果（由 triangular() 的模式参数反映）。

Angular
-------

Von Mises 或者 圆形正态分布（由 :func:`random.vonmisesvariate` 生成）用于计算循环值的概率，日历T天数和时间。

大小
----

:func:`random.betavariate` 使用 Beta 分布生成值，这通常用于贝叶斯统计和应用程序（如任务持续时间建模）。

:func:`random.gammavariate` 产生的 Gamma 分布用于模拟诸如等待时间，降雨量和计算误差之类事物的大小。

由 :func:`random.weibullvariate` 计算的 Weibull 分布用于故障分析，工业工程和天气预报。它描述了粒子或者其他离散对象的分布。
