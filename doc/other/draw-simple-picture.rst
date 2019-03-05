############
绘制简单图形
############

使用 :mod:`PIL` 绘制简单几何图形.
需要用到 Image, ImageDraw, 以及 ImageFont 三个模块.

为了处理像素阵列, 再引入 numpy.

.. code:: ipython3

    import numpy as np
    from PIL import Image, ImageDraw, ImageFont

计算机处理图像时, 坐标系原点位于左上方, xy 正方向则分别是右方与下方.


.. code:: ipython3

    # 生成画布
    canve = np.ndarray(shape=(400, 640, 4), dtype=np.uint8)
    # 这里, shape 的最后一个因子总是为 4, 因为 rgb 三种颜色再加上 alpha 通道
    # 由于想象多维数组时, 总是认为内部是横向排列的, 所以认为高度为 400, 宽度为 640

.. code:: ipython3

    # 将画布初始化, 全部设置为白色 rgb(255, 255, 255), alpha=255 (不透明)
    canve[:,:,:] = 255

.. code:: ipython3

    # PIL 能从数组创建图像
    image = Image.fromarray(canve)

.. code:: ipython3

    # 从 Image 对象创建一个可编辑的 ImageDraw 对象
    drawer = ImageDraw.Draw(image)

ImageDraw.Draw 对象可用的方法
=============================

每个方法都至少需要坐标参数以及颜色参数.

坐标
    可以传入 ``[(a_x, a_y), (b_x, b_y)]`` 或
    ``(a_x, a_y, b_x, b_y)`` 两种格式.
颜色
    可以为整数 rgb (或 rgba) 元祖,
    也可以用字符串 HTML 十六进制颜色编码或 HTML 预设颜色名.
    例如 ``(100, 200, 233, 128)`` 和 ``"#64c8e980"`` 是相同的.

.. function:: point(xy, fill=None)

    xy 为点的坐标, 可以为多个点. fill 决定点的颜色.
    每个点只占一个像素, 实际效果上看不如使用小型的圆来填充.

.. code:: ipython3

    # 绘制点 (只有一个像素, 太小了, 不如用小圆填充)
    drawer.point((500, 300), fill="red")

.. function:: line(xy, fill=None, width=0, joint=None)

    绘制一条线段, xy 为端点坐标, fill 为线段颜色,
    width 则是宽度, joint 是一系列线段序列的联合特征, 作曲线时用到.

    file=None 是默认为白色.

    xy 可以有两个以上端点, 将会做出一条折线,
    可以定义 joint 参数的值, 将折线变为曲线.

.. code:: ipython3

    # 绘制线段
    drawer.line((0, 320, 640, 360), fill=(0, 0, 0, 255), width=1)

.. function:: arc(xy, start, end, fill=None, width=0)

    绘制圆弧, xy 限定了一个矩形区域,
    在此区域中绘制圆弧 start -> end 的部分.

    fill 表示圆弧的颜色, 而非填充内部.

    ::

        | 这里是起点, (a_x, a_y)
        v
        +-----------+-----------+
        |           |           |
        |           |           |
        |           |           |
        |           |           |
        +-----------+---------------> x
        |           |           |
        |           |          || 0 -> 30
        |           |         / |
        |           |           |
        +-----------|-----------+ <--这里是终点, (b_x, b_y)
                    v y

.. code:: ipython3

    # 绘制圆弧
    drawer.arc((200, 200, 300, 300), 0, 120, fill="#444444", width=3)

.. function:: ellipse(xy, fill=None, outline=None, width=0)

    绘制椭圆, fill 填充内部, outline 为边框着色.

    当 xy 所选区域为正方形时, 将做出正圆.

.. code:: ipython3

    # 绘制圆
    drawer.ellipse((100, 0, 200, 100), outline="#000")
    # 绘制椭圆
    drawer.ellipse((200, 0, 350, 100), outline="#000")

.. function:: pieslice(xy, start, end, fill=None, outline=None, width=0)

.. code:: ipython3

    # 绘制饼图
    drawer.pieslice((400, 0, 500, 100), -90,120, fill="#244442", outline="#000", width=3)

.. function:: chord(xy, start, end, fill=None, outline=None, width=0)

    做弓形图, 可以填充内部.

.. code:: ipython3

    # 绘制弦(弓形图)
    drawer.chord((500, 0, 600, 100), -30, 60, fill="#782287")

.. function:: rectangle(xy, fill=None, outline=None, width=0)

    绘制矩形. fill 填充内部, outline 决定边框颜色.

.. code:: ipython3

    # 绘制矩形
    drawer.rectangle((100, 100, 200, 200), fill="#000", outline="blue", width=3)

.. function:: polygon(xy, fill=None, outline=None)

    绘制多边形, xy 输入各个顶点的坐标,
    最后一个顶点会与第一个顶点连接在一起.

    没有 width 参数.

.. code:: ipython3

    # 绘制多边形
    drawer.polygon((0, 0, 50, 50, 50, 0), "#444444", "#000")
