###############
multiprocessing
###############

:mod:`multiprocessing` 是一个跨平台的多进程支持.

基本使用
========

实例化 :class:`multiprocessing.Process`::

    from multiprocessing import Process

    # 一个进程将会执行一个函数
    def echo(x):
        print(x)
        return x

    def main():
        # 创建一个进程, 但是并没有运行
        p = Process(target=echo, args=(1,))
        # 运行一个进程, 运行是非阻塞的
        p.start()
        # 阻塞式等待, 直到该进程运行完毕才继续下一步
        p.join()

多进程间不能像函数调用那样交流.

.. note::

    进程的位置参数通过 ``args`` 传入,
    命名参数通过 ``kwargs`` 传入.

进程池
======

如果要一次性创建多个进程,
那么, 使用进程池 :class:`multiprocessing.Pool` 比较方便::

    from multiprocessing import Pool
    from time import sleep
    from random import randint

    def echo(x=0):
        sleep(randint(1, 3))
        print(x)
        return x

    def main():
        pool = Pool()
        for i in range(10):
            pool.apply_async(func=echo, args=(i,))

        # 关闭进程池, 之后无法继续添加新的进程,
        # 并且, 进程池中的进程开始运行
        pool.close()

        # 等待, 在所有进程运行完毕后, 继续下一步
        pool.join()

    if __name__ == "__main__":
        main()[<ForkProcess(ForkPoo...d daemon)>, <ForkProcess(ForkPoo...d daemon)>, <ForkProcess(ForkPoo...d daemon)>, <ForkProcess(ForkPoo...d daemon)>]


:class:`multiprocess.Pool` 可以分别使用
:meth:`multiprocessing.Pool.apply` 和
:meth:`multiprocessing.Pool.apply_async`
两种方法添加进程.
他们接受的参数命名与 Process 是一致的.

前者添加的进程是同步的,
当前一进程结束才运行下一进程.
后者是异步的, 将会同时运行允许的最大进程数.
并且, 不会暂停等待结果.
最大进程数是在创建 Pool 实例时设定的.
可以自己设定::

    pool = Pool(100)

默认值为 CPU 核心数, 一般不建议修改,
因为就算设置再高, 物理运行时仍然收到 CPU 的限制.

.. warning::

    在使用 :meth:`multiprocessing.Pool.apply_async`
    添加进程后, 才需要使用 :meth:`multiprocessing.Pool.join`
    方法.
    否则程序将会继续执行, 并不会等待进程池.
    如果在进程池运行完毕前, 程序就结束了,
    那么很有可能丢失部分或全部运行信息.

    而 :meth:`multiprocessing.Pool.apply` 添加的进程是同步的.
    倒是不需要 join.

进程间通信
==========

常用的通信手段有队列或管道.

队列就是一个先进先出的集合,
multiprocessing 已经提供了
:class:`multiprocessing.Queue` 作为实现.

需要注意的是, Queue 只能通过继承的方式传递.
它不能通过参数传递.
