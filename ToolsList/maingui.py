import os
import re
import sys

from PyQt5 import QtGui, QtWidgets
from PyQt5.QtCore import QObject, pyqtSignal, Qt
from PyQt5.QtGui import QIcon, QTextOption
from PyQt5.QtWidgets import QTextEdit, QVBoxLayout, QHBoxLayout, QPushButton, QMainWindow, qApp, QFileDialog, \
    QApplication, QProgressBar
import excfiledlg
import excfileThread
import dedupfileThread as dpT


class EmittingStream(QObject):
    textWritten = pyqtSignal(str)  # 定义一个发送str的信号

    def write(self, text):
        self.textWritten.emit(str(text))


class Ui_MainWindow(QMainWindow):

    def __init__(self):
        super().__init__()
        self.resize(850, 550)
        self.setWindowTitle("Tool Lists")
        self.setMinimumSize(300, 200)
        self.setWindowIcon(QIcon("res/favicon.ico"))

        self.centralwidget = QtWidgets.QWidget()
        self.setCentralWidget(self.centralwidget)

        self.menubar = self.menuBar()
        self.menufile = QtWidgets.QMenu("文件")
        self.menutools = QtWidgets.QMenu("工具")
        self.menutools_dirs = QtWidgets.QMenu("文件夹处理")
        self.menuhelp = QtWidgets.QMenu("帮助")
        self.menuview = QtWidgets.QMenu("视图")

        self.excfile = QtWidgets.QAction("提取文件")
        self.excfile.setStatusTip("深度提取文件夹中的所有文件到指定文件夹，"
                                  "文件命名： 原文件名 <_copy>*n.")
        self.excfile.triggered.connect(self.excfilemethod)
        self.dedupfile = QtWidgets.QAction("移除重复")
        self.dedupfile.setStatusTip(
            "深度移除文件夹MD5重复的文件")
        self.dedupfile.triggered.connect(self.dedupfilemethod)
        self.printdirs = QtWidgets.QAction("打印文件")
        self.printdirs.setStatusTip("深度打印文件夹中的文件")
        self.printdirs.triggered.connect(self.printdirsmethod)

        self.version = QtWidgets.QAction("版本")

        self.exit = QtWidgets.QAction("退出")
        self.exit.setShortcut("Ctrl+Q")
        self.exit.triggered.connect(qApp.exit)

        self.menubar.addMenu(self.menufile)
        self.menubar.addMenu(self.menutools)
        self.menubar.addMenu(self.menuview)
        self.menubar.addMenu(self.menuhelp)

        self.menufile.addAction(self.exit)
        self.menutools.addMenu(self.menutools_dirs)
        self.menutools_dirs.addAction(self.excfile)
        self.menutools_dirs.addAction(self.dedupfile)
        self.menutools_dirs.addAction(self.printdirs)

        self.statusbar = self.statusBar()

        self.changeUI()

    def changeUI(self):
        self.textedit = QTextEdit()
        # self.textedit.setEnabled(False)
        # self.textedit.setFocusPolicy(Qt.NoFocus)
        self.textedit.setWordWrapMode(QTextOption.NoWrap)
        vbox = QVBoxLayout()

        hbox = QHBoxLayout()
        self.progress = QProgressBar()
        self.progress.setMinimumWidth(200)
        clearbtn = QPushButton(" 清屏 ")
        clearbtn.clicked.connect(self.textedit.clear)
        hbox.addWidget(self.progress)
        hbox.addStretch(1)
        hbox.addWidget(clearbtn)

        vbox.addLayout(hbox)
        vbox.addWidget(self.textedit)
        self.centralwidget.setLayout(vbox)

        sys.stdout = EmittingStream(textWritten=self.outputWritten)
        sys.stderr = EmittingStream(textWritten=self.outputWritten)

    def outputWritten(self, text):
        cursor = self.textedit.textCursor()
        cursor.movePosition(QtGui.QTextCursor.End)
        cursor.insertText(text)
        self.textedit.setTextCursor(cursor)
        self.textedit.ensureCursorVisible()

    def excfilemethod(self):
        dlg = excfiledlg.ExcfileDlg()
        dlg.show()
        dlg._signal.connect(self.excfilemethod2)
        dlg.exec_()

    def excfilemethod2(self, path, dir,deleter=False):
        self.thread = excfileThread.excThread(path, dir,deleter)
        self.thread._signal.connect(self.outputWritten)
        self.thread._sig_changepro.connect(self.progress.setValue)
        self.thread.start()

    def closeEvent(self, a0: QtGui.QCloseEvent):
        a0.accept()
        qApp.exit()

    def dedupfilemethod(self):

        print("remove duplicate dirs file...")
        QApplication.processEvents()

        path = QFileDialog.getExistingDirectory(caption="Remove duplicate folder paths",
                                                directory="../")
        if path == "" or path is None or not os.path.isdir(path):
            return

        self.t = dpT.dpThread(path=path)
        self.t._signal.connect(self.outputWritten)
        self.t._sig_changepro.connect(self.progress.setValue)
        self.t.start()

    def printdirsmethod(self):
        print("print dirs file...")
        QApplication.processEvents()
        path = QFileDialog.getExistingDirectory(
            self, "print folder files", "../")
        if path == "" or path is None or not os.path.isdir(path):
            return

        count = 0
        for root, dirs, files in os.walk(path):  # 目录
            for f in files:
                count += 1
                print(count, os.path.join(root, f))
                QApplication.processEvents()
        print("finish.\r\n")
        QApplication.processEvents()
