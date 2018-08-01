import hashlib
import os
from time import sleep

from PyQt5.QtCore import pyqtSignal
from PyQt5.QtWidgets import QDialog, QVBoxLayout, QLabel, QPushButton,  QFileDialog, \
    QGridLayout,  QCheckBox




class ExcfileDlg(QDialog):

    _signal = pyqtSignal(str,str,bool)

    def __init__(self):

        super().__init__()

        self.label = QLabel("原文件夹...")
        self.label.setObjectName("label")
        button = QPushButton("选择1")
        button.clicked.connect(self.getdir)

        self.label2 = QLabel("新文件夹...")
        button2 = QPushButton("选择2")
        button2.clicked.connect(self.getdir)

        self.button3 = QPushButton("开始")
        self.button3.clicked.connect(self.sure)

        self.deleter = QCheckBox("处理后删除原文件夹")
        self.closedw = QCheckBox("确定后关闭本对话框")
        self.closedw.setChecked(True)

        grid = QGridLayout()
        grid.setSpacing(20)
        grid.addWidget(self.label, 0, 0)
        grid.addWidget(button, 0, 1)
        grid.addWidget(self.label2, 1, 0)
        grid.addWidget(button2, 1, 1)
        grid.addWidget(self.button3, 2, 1)

        vbox = QVBoxLayout()
        vbox.setSpacing(20)
        vbox.addStretch(1)
        vbox.addWidget(self.deleter)
        vbox.addWidget(self.closedw)
        vbox.addStretch(1)
        vbox.addLayout(grid)
        vbox.addStretch(1)
        self.setLayout(vbox)
        self.resize(500, 200)
        self.setWindowTitle("文件处理对话框")

    def getdir(self):
        s = QFileDialog.getExistingDirectory(self, "get src", "../")
        if s == "":
            return
        sender = self.sender().text()
        if sender == "选择1":
            self.label.setText(s)
        if sender == "选择2":
            self.label2.setText(s)

    def sure(self):
        path = self.label.text()
        dir = self.label2.text()

        if not os.path.isdir(path) or not os.path.isdir(dir):
            return

        deleter=False
        if self.deleter.isChecked():
            deleter=True

        self._signal.emit(path,dir,deleter)

        if self.closedw.isChecked():
            self.close()


