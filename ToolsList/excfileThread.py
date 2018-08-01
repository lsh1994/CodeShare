"""
@Time    : 2018/7/24 19:06
@Author  : Lishihang
@File    : excfileThread.py
@Software: PyCharm
@desc:
"""
import os
import shutil

from PyQt5.QtCore import QThread, pyqtSignal
from PyQt5.QtWidgets import QApplication


class excThread(QThread):
    _signal = pyqtSignal(str)
    _sig_changepro = pyqtSignal(int)

    def __init__(self, path, dir, deleter):
        super(excThread, self).__init__()
        self.path = path
        self.dir = dir
        self.deleter = deleter

    def run(self):

        self._sig_changepro.emit(0)

        count = 0
        for root, dirs, files in os.walk(self.path):  # 目录
            count += len(files)

        i = 0
        for root, dirs, files in os.walk(self.path):  # 目录
            for f in files:
                i += 1
                self._sig_changepro.emit(int(i * 100.0 / count))

                p1 = os.path.join(root, f)
                p2 = self.get_new_name(self.dir, f)

                shutil.copy(p1, p2)
                self._signal.emit('Move ： %s To %s\r\n' % (p1, p2))

        if self.deleter:
            shutil.rmtree(self.path)
            self._signal.emit("del source folder.\r\n")

        self._signal.emit("finish.\r\n\r\n")

    def get_new_name(self, d, f):

        if os.path.exists(os.path.join(d, f)):
            self._signal.emit("%s hava exist.\r\n" % os.path.join(d, f))
            s = "%s_%s%s" % (os.path.splitext(
                f)[0], "copy", os.path.splitext(f)[1])
            return self.get_new_name(d, s)
        return os.path.join(d, f)
