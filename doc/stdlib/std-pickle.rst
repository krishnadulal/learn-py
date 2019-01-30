######
pickle
######

.. highlight:: ipython3

pickle 是用于将 Python 对象保存至文件或字符串的工具. 提供了 ``load``, ``loads``, ``dump``, ``dumps`` 四个函数给用户使用.

pickle 的保存与加载操作只能用于一个对象, 不能将多个对象连接在一起. 保存非内建对象也是可以的, 只是在加载时必须 import 相同的库.

``dump``, ``load`` 操作文件, 必须是可写/可读的二进制方式打开的文件流.

::

    x = 10

    with open("test.pickle", "ab") as file:
        pickle.dump(x, file)

        y = pickle.load(file)

``dumps``, ``loads`` 则是返回/读取一个 pickle 处理的字节.

::

    In [10]: pickle.dumps([1,2,3,4,])
    Out[10]: b'\x80\x03]q\x00(K\x01K\x02K\x03K\x04e.'

    In [11]: pickle.loads(b'\x80\x03]q\x00(K\x01K\x02K\x03K\x04e.')
    Out[11]: [1, 2, 3, 4]
