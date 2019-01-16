##############
win32clipboard
##############

这是 pywin32 的一部分, 用于操作 Windows 系统的剪贴板.

常用操作
========

对剪贴板进行操作, 都需要先打开, 操作完成后必须关闭, 就和操作文件一样. 如果需要将内容放入其中, 则必须要清空当前的剪贴板::

    import win32clipboard as c
    def main():
        # 打开剪贴板
        c.OpenClipboard()

        # 获取内容, 获取 CF_TEXT 内容时, 返回一个 bytes 类型, 需要解码为字符串,
        # 这里用 gbk 字符集解码是因为 Windows 中文版的默认字符集就是它
        string = c.GetClipboardData(c.CF_TEXT).decode('gbk')
        # 也可以读取 CF_UNICODETEXT 内容, 是按照 Unicode 编码保存的 str 类型.
        string = c.GetClipboardData(c.CF_UNICODETEXT)

        # 在写入内容之前需要清空
        c.EmptyClipboard()
        c.SetClipboardData

.. error::
    需要注意的是, PowerShell 的管道将文本视作内置的字符串对象, 但是又处理不好编码, 会导致文本通过管道传递后变成乱码. 只有 PowerShell 的函数或编写的脚本不会出现这种错误.

    PowerShell 提供了 cmdlet ``Set-Clipboard`` 与 ``Get-Clipboard`` 读写剪贴板, 当它们通过管道接收非 PowerShell 程序传递的文本时, 不会乱码, 但是当它们通过管道向其他程序传递文本时, 仍然乱码.

win32clipboard 模块提供的函数一览
=================================

见 `MSDN Clipboard Functions 页面 <https://docs.microsoft.com/zh-cn/windows/desktop/dataxchg/clipboard-functions>`_, 虽然此文档是 C++ 版本, 但是函数名/参数位置是相同的::

    OpenClipboard() -> None
    """打开剪贴板, 并防止其他程序修改剪贴板.
    除非调用EmptyClipboard函数, 否则由 hWnd 参数标识的窗口不会成为剪贴板所有者."""
    CloseClipboard() -> None
    """关闭剪贴板."""
    EmptyClipboard() -> None
    """清空剪贴板并释放剪贴板中数据的句柄.
    然后, 该函数将剪贴板的所有权分配给当前打开剪贴板的窗口.
    注意, 此函数会清除所有类型的剪贴板内容"""

    # 以上对剪贴板的操作不需要指定参数, 因为剪贴板对象在系统中有且仅有一个.

    # 获取内容部分
    GetClipboardData(format) -> str
    """函数以指定的格式从剪贴板检索数据.
    必须先打开剪贴板.
    请注意, 并非所有数据格式都受支持, 并且可以使用 win32clipboard.GetClipboardDataHandle() 检索基础句柄.
    根据 format 的不同, 返回值类型如下:
    ================
    CF_HDROP	        一个存放文件路径的元组.
    CF_UNICODETEXT	    使用 Unicode 编码的字符串对象.
    CF_OEMTEXT	        一个字节流对象, 使用系统默认编码.
    CF_TEXT	            一个字节流对象, 使用系统默认编码.
    CF_ENHMETAFILE	    A string with binary data obtained from GetEnhMetaFileBits
    CF_METAFILEPICT	    A string with binary data obtained from GetMetaFileBitsEx (currently broken)
    CF_BITMAP	        An integer handle to the bitmap.
    All other formats	A string with binary data obtained directly from the global memory referenced by the handle.
    """

    GetClipboardDataHandle(format) -> int
    """以指定数据格式检索剪贴板, 并返回数据的整数句柄."""

    GetClipboardFormatName() -> str
    """函数从剪贴板检索指定的注册格式的名称.
    返回包含格式的字符串"""

    GetClipboardOwner() -> int
    """函数检索剪贴板当前所有者的窗口句柄
    即使当前没有剪贴板, 剪贴板仍然可以包含数据.
    通常, 剪贴板所有者是最后在剪贴板中放置数据的窗口. EmptyClipboard 函数指定剪贴板所有权."""

    GetClipboardSequenceNumber() -> int
    """函数返回当前剪贴板 windows station 的序列号
    系统为每个窗口站的剪贴板保留一个 32 位序列号. 只要剪贴板的内容发生变化或剪贴板清空, 该数字就会递增.
    您可以跟踪此值以确定剪贴板内容是否已更改并优化创建 DataObjects.
    如果剪贴板渲染延迟, 则序列号不会递增, 直到呈现更改为止."""

    GetClipboardViewer() -> int
    """函数检索剪贴板查看器链中第一个窗口的句柄."""

    GetGlobalMemory(hglobal) -> str
    """返回指定的全局内存对象的内容."""

    GetOpenClipboardWindow() -> int
    """GetOpenClipboardWindow 函数检索当前打开剪贴板的窗口的句柄.
    如果应用程序或动态链接库(DLL)在调用 OpenClipboard 函数时指定 NULL 窗口句柄, 则剪贴板将打开但不与窗口关联.
    在这种情况下, GetOpenClipboardWindow 返回 NULL."""

    # 设定(写入)内容部分
    SetClipboardData(format, content) -> int
    """SetClipboardData 函数以指定的剪贴板格式将数据放在剪贴板上.
    该窗口必须是当前剪贴板所有者, 并且应用程序必须已调用 OpenClipboard 函数.
    在响应 WM_RENDERFORMAT 和 WM_RENDERALLFORMATS 消息时, 剪贴板所有者在调用 SetClipboardData 之前不得调用 OpenClipboard.

    format: int
        指定一个剪贴板格式.
    hMem:   int/buffer
        指定格式的数据的整数句柄, 或字符串, unicode 或支持缓冲区接口的任何对象.
    分配全局内存对象, 并将对象的缓冲区复制到新内存.
    此参数可以为 0, 表示窗口根据请求以指定的剪贴板格式(呈现格式)提供数据.
    如果窗口延迟渲染, 则必须处理 WM_RENDERFORMAT 和 WM_RENDERALLFORMATS 消息.
    调用 SetClipboardData 后, 系统拥有 hMem 参数标识的对象.

    应用程序可以读取数据, 但不能释放句柄或将其锁定. 如果 hMem 参数标识了内存对象, 则必须使用带有 GMEM_MOVEABLE 和 GMEM_DDESHARE 标志的 GlobalAlloc 函数分配该对象.
    """

    SetClipboardText(text, format) -> int
    """使用文本时调用 SetClipboardData 的便捷功能.

    text: str/unicode
        写入剪贴板的文本
    format=CF_TEXT: int
        使用的剪贴板格式, 只能是 CF_TEXT 或 CF_UNICODETEXT

        可以将字符串/字节对象传递给此函数, 但是根据 format 参数的值, 它可以转换为该参数的适当类型.
    许多应用程序需要调用此函数两次, 指定相同的字符串, 但 CF_UNICODETEXT 指定第二个.
    """

    PyHANDLE = SetClipboardViewer(hWndNewViewer) -> PyHANDLE
    """SetClipboardViewer 函数将指定的窗口添加到剪贴板查看器链.
    每当剪贴板的内容发生更改时, 剪贴板查看器窗口都会收到 WM_DRAWCLIPBOARD 消息.

    hWndNewViewer: PyHANDLE
        要添加到剪贴板链的窗口的整数句柄

        作为剪贴板查看器链的一部分的窗口(称为剪贴板查看器窗口)必须处理剪贴板消息 WM_CHANGECBCHAIN 和 WM_DRAWCLIPBOARD. 每个剪贴板查看器窗口都调用 SendMessage 函数将这些消息传递到剪贴板查看器链中的下一个窗口.
    剪贴板查看器窗口最终必须通过调用 ChangeClipboardChain 函数从剪贴板查看器链中删除自身 - 例如, 响应 WM_DESTROY 消息。"""

    # 配置部分
    ChangeClipboardChain(...)
    CountClipboardFormats(...)

    EnumClipboardFormats(format) -> int
    """EnumClipboardFormats 函数枚举剪贴板上当前可用的数据格式.

    format=0: int
        指定已知可用的剪贴板格式.
    要启动剪贴板格式的枚举, 请将 format 设置为零. 当 format 为零时, 该函数检索第一个可用的剪贴板格式. 对于枚举期间的后续调用, 请将 format 设置为上一个 EnumClipboardFormat 调用的结果.

        剪贴板数据格式存储在有序列表中. 要执行剪贴板数据格式的枚举, 您需要对 EnumClipboardFormats 函数进行一系列调用. 对于每个调用, format参数指定可用的剪贴板格式, 该函数返回下一个可用的剪贴板格式.
    必须在枚举其格式之前打开剪贴板. 使用 OpenClipboard 函数打开剪贴板. 如果剪贴板未打开, 则 EnumClipboardFormats 函数将失败.
    EnumClipboardFormats 函数按照放置在剪贴板上的顺序枚举格式. 如果要将信息复制到剪贴板, 请按照从最具描述性的剪贴板格式到最不具描述性的剪贴板格式的顺序添加剪贴板对象. 如果要从剪贴板粘贴信息, 请检索可以处理的第一个剪贴板格式. 这将是您可以处理的最具描述性的剪贴板格式.
    系统为某些剪贴板格式提供自动类型转换. 在这种格式的情况下, 此函数枚举指定的格式, 然后枚举可以转换的格式. 有关更多信息, 请参阅标准剪贴板格式和合成剪贴板格式."""

    GetPriorityClipboardFormat(...)
    IsClipboardFormatAvailable(...)
    RegisterClipboardFormat(...)

剪贴板格式参考资料
==================

Windows 系统中的剪贴板格式都是以 ``CF_*`` 开头的常量. 剪贴板就是一个内存空间中的缓冲区, 根据存入数据类型的不同, 划分出不同种类的内存空间. 不同类型的剪贴板空间可以共存, 而同类型的只能同时存在一个.

见 `MSDN 标准剪贴板格式 页面 <https://docs.microsoft.com/zh-cn/windows/desktop/dataxchg/standard-clipboard-formats>`_::

    CF_BITMAP = 2                   # 与设备相关的位图格式
    CF_DIB = 8                      # 与设备无关的位图格式内存块
    CF_DIBV5 = 17                   # 包含 BITMAPV5HEADER 结构的内存对象, 后跟位图颜色空间信息和位图数据.
    CF_DIF = 5                      # 包含数据交换格式 (DIF) 数据的整体内存块
    CF_DSPBITMAP = 130
    CF_DSPENHMETAFILE = 142
    CF_DSPMETAFILEPICT = 131
    CF_DSPTEXT = 129
    CF_ENHMETAFILE = 14             # 增强型 metafile 句柄
    CF_HDROP = 15                   # 用于键入 HDROP 的句柄, 用于标识文件列表. 应用程序可以通过将句柄传递给 DragQueryFile 函数来检索有关文件的信息
    CF_LOCALE = 16                  # 数据是与剪贴板中的文本关联的区域设置标识符的句柄. 当您关闭剪贴板时, 如果它包含 CF_TEXT 数据但没有 CF_LOCALE 数据, 系统会自动将 CF_LOCALE 格式设置为当前输入语言. 您可以使用 CF_LOCALE 格式将不同的区域设置与剪贴板文本相关联
    CF_MAX = 18
    CF_METAFILEPICT = 3             # 以旧的 metafile 格式存放的图片
    CF_OEMTEXT = 7                  # 包含 OEM 字符集中字符的文本格式. 每行以 /r/n 格式结束. 以空字符标识末尾
    CF_OWNERDISPLAY = 128           # Owner-display 格式. 剪贴板所有者必须显示并更新剪贴板浏览窗口. 并且接收 WM_ASKCBFORMATNAME, WM_HSCROLLCLIPBOARD, WM_PAINTCLIPBOARD, WM_SIZECLIPBOARD 和 WM_VSCROLLCLIPBOARD 信息. 并且 hMem 参数的值必须为 NULL.
    CF_PALETTE = 9                  # 调色盘句柄
    CF_PENDATA = 10                 # 与 Windows 的笔式输入扩充功能联合使用
    CF_RIFF = 11                    # 表示比 CF_WAVE 标准波形格式更复杂的音频数据
    CF_SYLK = 4                     # 包含 Microsoft 符号链接数据格式的整体内存块
    CF_TEXT = 1                     # 以 NULL 结尾的 ANSI 字符集字符串
    CF_TIFF = 6                     # 标记图像文件格式
    CF_UNICODETEXT = 13             # 含有 Unicode 编码字节的内存块
    CF_WAVE = 12                    # 标准波形音频文件