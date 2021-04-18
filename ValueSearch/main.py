#-- coding: utf-8 --


from system_hotkey import SystemHotkey
from PyQt5.QtWidgets import QApplication, QWidget, QDialog, QMainWindow
from PyQt5.QtCore import QObject, pyqtSignal
from main_fram import Ui_main_form, main_fram
import sys
import common_component as cc
from key import KeyBorder
import time
import win32clipboard as clipboard
import win32con




# 这里之所以继承QObject是因为要使用自定义信号(PyQt5要求)
class common_ipc(QObject, Ui_main_form):
    # 定义一个热键信号
    sig_keyhot = pyqtSignal(str)

    def __init__(self):
        # 1. 简单的绘制一个窗口
        super(common_ipc, self).__init__()

        self.item_fram = QMainWindow()

        self.setupUi(self.item_fram)
        self.update_tbrow.setText("检测到新版本，请去 https://github.com/Setless7/PathOfTrade 下载")
        self.price_lwidget = cc.price_lwidget()
        self.price_lwidget.addprice_lwidget(self.item_fram)
        self.item_fram.show()
        # self.ui.elder_lab.setText('fewgfe')
        self.price_lwidget.add_item(('40 chaos', '100', '1小时前'))
        self.keyBorder = KeyBorder()

        # 2. 设置我们的自定义热键响应函数
        self.sig_keyhot.connect(self.MKey_pressEvent)
        # 3. 初始化两个热键
        self.hk_start, self.hk_stop = SystemHotkey(), SystemHotkey()
        # 4. 绑定快捷键和对应的信号发送函数
        self.hk_start.register(('control', 'd'), callback=lambda x: self.send_key_event("start"))
        self.hk_stop.register(('control', '2'), callback=lambda x: self.send_key_event("stop"))

    # 热键处理函数

    def MKey_pressEvent(self, i_str):
        time.sleep(0.05)
        self.keyBorder.key_up('d')
        time.sleep(0.05)
        self.keyBorder.key_up('ctrl')
        time.sleep(0.05)
        self.keyBorder.key_down_up_team('ctrl', 'c')
        self.item_fram.l
        self.item_fram.showMinimized()
        self.item_fram.showNormal()

    # 热键信号发送函数(将外部信号，转化成qt信号)
    def send_key_event(self, i_str):
        self.sig_keyhot.emit(i_str)

    def get_clipboard_text(self):
        clipboard.OpenClipboard()
        text = clipboard.GetClipboardData(win32con.CF_TEXT)
        clipboard.CloseClipboard()
        return text.decode('GBK')




# ui = c_demo()
app = QApplication(sys.argv)

common_ipc()


sys.exit(app.exec_())


# See PyCharm help at https://www.jetbrains.com/help/pycharm/
