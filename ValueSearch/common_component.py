# -- coding: utf-8 --

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QApplication, QWidget, QDialog, QMainWindow

label = {
    'white': {
        'text': '白孔:',
        'width': '60',
        'height': '10',
        'rich_text': False
    },
    'item_level': {
        'text': '物品等级:',
        'width': '60',
        'height': '10',
        'rich_text': False
    },
    'elder': {
        'text': '裂界者',
        'width': '60',
        'height': '10',
        'rich_text': True,
        'image': 'url(:/pic/power_image/crusader-symbol.png);'
    }
}


class price_lwidget:
    def addprice_lwidget(self, main_form):
        self.price_lwidget = QtWidgets.QListWidget(main_form)
        self.price_lwidget.setGeometry(QtCore.QRect(10, 560, 341, 461))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.price_lwidget.sizePolicy().hasHeightForWidth())
        self.price_lwidget.setSizePolicy(sizePolicy)
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(51, 86, 118))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(59, 99, 136))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.AlternateBase, brush)
        brush = QtGui.QBrush(QtGui.QColor(51, 86, 118))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(59, 99, 136))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.AlternateBase, brush)
        brush = QtGui.QBrush(QtGui.QColor(240, 240, 240))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(59, 99, 136))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.AlternateBase, brush)
        self.price_lwidget.setPalette(palette)
        self.price_lwidget.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.price_lwidget.setAlternatingRowColors(True)
        self.price_lwidget.setObjectName("price_lwidget")
        # _translate = QtCore.QCoreApplication.translate
        self.add_item(('价格', '物品等级', '上架时间'))

    def add_item(self, text_tuple):
        templet = ''
        for text in text_tuple:
            templet += '%s\t'

        item = QtWidgets.QListWidgetItem()
        item.setText(templet % text_tuple)
        self.price_lwidget.addItem(item)

    def is_Chinese(self, ch):
        if '\u4e00' <= ch <= '\u9fff':
            return True
        return False

    # __sortingEnabled = self.price_lwidget.isSortingEnabled()
    # self.price_lwidget.setSortingEnabled(False)
    # item = self.price_lwidget.item(0)
    # item.setText(_translate("main_form", "价格           物品等级          上架时间"))
    # item = self.price_lwidget.item(1)
    # item.setText(_translate("main_form", "调查撒"))
    # item = self.price_lwidget.item(2)
    # item.setText(_translate("main_form", "调查撒"))
    # item = self.price_lwidget.item(3)
    # item.setText(_translate("main_form", "大地"))
    # self.price_lwidget.setSortingEnabled(__sortingEnabled)


class base_attr_fram:
    def __init__(self, main_form):
        self.base_attr_fram = QtWidgets.QFrame(main_form)
        self.base_attr_fram.setGeometry(QtCore.QRect(10, 90, 341, 61))
        self.base_attr_fram.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.base_attr_fram.setFrameShadow(QtWidgets.QFrame.Raised)
        self.base_attr_fram.setObjectName("base_attr_fram")
        self.base_attr_fram.setWindowOpacity(0)
        self.x = 5
        self.y = 5
        self.label = {}

    def add_label(self, label_name):
        self.label[label_name] = QtWidgets.QLabel(self.base_attr_fram)
        width = label[label_name]['width']
        height = label[label_name]['height']
        self.label[label_name].setGeometry(QtCore.QRect(self.x, self.y, width, height))
        setStyleSheet = "border-radius: 6px;  border:1px solid white;color:white;background:rgb(31, 52, 71);" \
                        "font: 9pt \"微软雅黑\";"
        if label[label_name]['rich_text']:
            setStyleSheet += "background-image: %s;\n" % (label[label_name]['image'])
        self.label[label_name].setStyleSheet(setStyleSheet)
        self.label[label_name].setAlignment(QtCore.Qt.AlignCenter)
        self.label[label_name].setObjectName("item_level_lab")
