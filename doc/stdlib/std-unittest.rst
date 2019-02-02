########
unittest
########

:mod:`unittest` 提供了:

    -   :class:`unittest.TestCase`
    -   :class:`unittest.TestSuite`
    -   :class:`unittest.TestLoader`
    -   :class:`unittest.TextTestRunner`

四个类.

分别用于

    -   定义测试单元
    -   整合测试单元
    -   向 Suite 中加载 Case
    -   运行 Suite, 并以文本格式显示测试结果

TestCase
========

:class:`unittest.TestCase` 的使用,
需要定义一个继承该类的类, 在其中添加测试用例::

    import unittest

    class ExampleTest(unittest.TestCase):
        def test_one(self):
            print("进行一次测试")
        def test_two(self):
            print("第二个测试")


每一个以 ``test`` 开头的方法, 都是一条 case.
只有以 ``test`` 开头, 才会被识别为测试用例,
虽然可以使用其他名称,
但是在后面使用 :class:`unittest.TestLoader` 向 :class:`unittest.TestSuite` 整合时,
命名不符合这个规范的分支不会被加载.

定义了一组测试用例后,
可以简单地调用 :func:`unittest.main` 来运行该文件的测试(不需要实例化).

环境配置
--------

在一组测试用例中, 每一次测试开始或结束,
一般需要配置程序运行的上下文::

    import unittest

    class ExampleTest(unittest.TestCase):


        @classmethod
        def setUpClass(cls):
            print("所有测试的前置条件")

        @classmethod
        def tearDownClass(cls):
            print("所有测试的后置条件")

        def setUp(self):
            print("一条 case 的前置条件")

        def tearDown(self):
            print("一条 case 的后置条件")

        def test_one(self):
            print("一个测试 case")

        def test_two(self):
            print("第二个测试 case")

使用 :meth:`unittest.TestCase.setUp`,
:meth:`unittest.TestCase.tearDown`,
:meth:`unittest.TestCase.setUpClass`,
:meth:`unittest.TestCase.tearDownClass`
分别定义在该类中的每一条 case 运行前后的代码,
以及该类中所有 case 开始或结束的代码.

测试断言
--------

在每一条 case 中,
用到测试断言来判断输出是否与预期相符.

这会用到 ``unittest.TestCase.assert*`` 等方法:

=============================== ================================
断言                            含义
------------------------------- --------------------------------
``assertEqual(a, b)``           ``a == b``
``assertMultiLineEqual(a, b)``  相同的 strings
``assertSequenceEqual(a, b)``   相同的 sequences
``assertListEqual(a, b)``       相同的 lists
``assertTupleEqual(a, b)``      相同的 tuples
``assertSetEqual(a, b)``        相同的 sets or frozensets
``assertDictEqual(a, b)``       相同的 dicts
``assertNotEqual(a, b)``        ``a != b``
``assertTrue(x)``               ``bool(x) is True``
``assertFalse(x)``              ``bool(x) is False``
``assertIs(a, b)``              ``a is b``
``assertIsNot(a, b)``           ``a is not b``
``assertIsNone(x)``             ``x is None``
``assertIsNotNone(x)``          ``x is not None``
``assertIn(a, b)``              ``a in b``
``assertNotIn(a, b)``           ``a not in b``
``assertIsInstance(a, b)``      ``isinstance(a, b)``
``assertNotIsInstance(a, b)``   ``not isinstance(a, b)``
``assertAlmostEqual(a, b)``     ``round(a-b, 7) == 0``
``assertNotAlmostEqual(a, b)``  ``round(a-b, 7) != 0``
``assertGreater(a, b)``         ``a > b``
``assertGreaterEqual(a, b)``    ``a >= b``
``assertLess(a, b)``            ``a < b``
``assertLessEqual(a, b)``       ``a <= b``
``assertRegex(s, r)``           ``r.search(s)``
``assertNotRegex(s, r)``        ``not r.search(s)``
``assertCountEqual(a, b)``      a,b 含有相同的元素; 忽略顺序.
=============================== ================================

+--------------------------------------------------+--------------------------------------+
| 断言                                             | 含义                                 |
+--------------------------------------------------+--------------------------------------+
| assertRaises(exc, fun, \*args, \*\*kwds)         | fun(\*args, \*\*kwds) 抛出 exc 异常  |
+--------------------------------------------------+--------------------------------------+
| assertRaisesRegex(exc, r, fun, \*args, \*\*kwds) | fun(\*args, \*\*kwds) 抛出 exc 异常, |
|                                                  | 并且消息匹配 r (正则表达式)          |
+--------------------------------------------------+--------------------------------------+
| assertWarns(warn, fun, \*args, \*\*kwds)         | fun(\*args, \*\*kwds) 抛出 warn 异常 |
+--------------------------------------------------+--------------------------------------+
| assertWarnsRegex(warn, r, fun, \*args, \*\*kwds) | fun(\*args, \*\*kwds) 抛出 warn 异常 |
|                                                  | 并且消息匹配 r (正则表达式)          |
+--------------------------------------------------+--------------------------------------+
| assertLogs(logger, level)                        | The with block logs on logger        |
|                                                  | with minimum level                   |
+--------------------------------------------------+--------------------------------------+

用法是在每一条 case 中调用方法::

    self.assertXXX(a,b)

和普通的 :keyword:`assert` 不同,
如果有一条 ``TestCase.assert`` 失败,
程序不会终止,
而是跑完所有测试.

在一条 case 中, 可以使用多个断言, 只有所有断言都成立,
这条 case 才会标记为 OK.

跳过某 case
-----------

在一条需要跳过的分支上, 使用 :py:func:`unittest.skip` 跳过该分支:

.. py:decorator:: unittest.skip(reason)

    无条件地跳过一个 case.

    :param str reason: 跳过的理由

也可以使用条件判断:

.. py:decorator:: unittest.skipIf(condition, reason)

    当条件满足时, 跳过该分支

    :param condition: 条件
    :param str reason: 理由

.. py:decorator:: unittest.skipUnless(condition, reason)

    当条件不满足时, 跳过该分支

    :param condition: 条件
    :param str reason: 理由

.. py:method:: unittest.TestCase.skipTest(reason)

    用在一个 case 内. 跳过该 case.

    :param str reason: 理由

失败就对了
----------

验证一些不合法代码

.. py:decorator:: uniitest.expectedFailure

    如果此分支的断言不成立, 判断此分支 OK,
    如果断言成立, 说明一些不合法的操作被通过, 判断为 Failure.

TestSuite
=========

:class:`unittest.TestSuite` 可以将多个 :class:`unittest.TestCase` 整合到一起.

可以使用方法 :meth:`unittest.TestSuite.addTest` 添加一个分支::

    suite = unittest.TestSuite()

    suite.addTest(MyTest('test_one'))

这个方法只能添加 ``MyTest`` 中的一个命名为 ``test_one`` 的测试分支.

也可以使用方法 :meth:`unittest.TestSuite.addTests` 添加一组分支::

    suite = unittest.TestSuite()

    suite.addTests(
    [MyTest("test_one"), MyTest("test_two")]
    )

这会添加一组测试分支, 也可以传入一个 TestSuite,
将其中包含的分支都添加进去::

    suite_1 = unittest.TestSuite()

    suite_1.addTests(
    [MyTest("test_one"), MyTest("test_two")]
    )


    suite_2 = unittest.TestSuite()
    suite_2.addTests(suite_1)

或者使用 :class:`unittest.TestLoader` 批量添加分支::

    suite = unittest.TestSuite()
    loader = unittest.TestLoader()

    suite.addTests(
        loader.loadTestsFromTestCase(
            MyTest      # 注意, 不传入实例
        )
    )

这会载入所有以 ``test*`` 开头的测试分支.

TestLoader
==========

:class:`unittest.TestLoader` 用于加载一个 TestCase 或者 一个模块 中的测试分支.

.. py:class:: TestLoader

    .. py:method:: loadTestsFromTestCase( TestCaseClass )

        从 TestCaseClass 中加载所有以 "test*" 开头的测试分支.

        :param TestCaseClass: TestCase 类 (不是实例!)

TestRunner
==========

一个 ``TestSuite`` 不直接运行, 而是通过 ``TestRunner`` 运行.

unittest 模块提供了类 :class:`unittest.TextTestRunner` 作为 runner.
测试结果是以文本方式显示的.

.. py:class:: TextTestRunner(stream=None, descriptions=True, verbosity=1, failfast=False, buffer=False, resultclass=None, warnings=None, *, tb_locals=False)

    用于运行一个 TestSuite 实例. 一般使用只需要在乎 stream 与 verbosity 两个参数.

    :param stream: 报告信息的输出目标, 默认(None)为 stderr
    :param int verbosity: 报告信息的详细程度, 0,1,2 三个级别, 3 最详细.

例子::

    suite = unittest.TestSuite()

    runner = unittest.TextTestRunner(
        verbosity=2
    )
    runner.run(suite)

如果要输出到指定文件, 用::

    with open("test-report.txt", "wt", encoding="utf-8") as report:
        runner = unittest.TextTestRunner(
            stream=report,
            verbosity=2
        )
        runner.run(suite)
