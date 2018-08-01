"""
@Time    : 2018/7/24 14:25
@Author  : Lishihang
@File    : dedupfileThread.py
@Software: PyCharm
@desc:
"""
import hashlib
import os

from PyQt5.QtCore import QThread, pyqtSignal
from PyQt5.QtWidgets import QFileDialog, QApplication, QMainWindow


def GetFileMd5(filename):
    if not os.path.isfile(filename):
        return
    myhash = hashlib.md5()
    f = open(filename, 'rb')
    while True:
        b = f.read(8096)
        if not b:
            break
        myhash.update(b)
    f.close()
    return myhash.hexdigest()


class dpThread(QThread):
    _signal = pyqtSignal(str)
    _sig_changepro = pyqtSignal(int)

    def __init__(self, path):
        super(dpThread, self).__init__()
        self.path = path

    def run(self):
        path = self.path
        self._signal.emit("Remove duplicate folder paths: %s\r\n" % path)
        self._sig_changepro.emit(0)

        count = 0
        for root, dirs, files in os.walk(path):  # 目录
            count += len(files)

        self._signal.emit("count: %d\r\n " % count)

        li = {}
        i = 0
        pro=0
        for root, dirs, files in os.walk(path):  # 目录

            for f in files:
                p = os.path.join(root, f)

                # self._signal.emit("deal : %s\r\n" % p)
                pro+=1
                self._sig_changepro.emit(int(pro*100.0/count))

                md5 = GetFileMd5(p)
                r = li.get(md5, None)
                if r:
                    os.remove(p)
                    i += 1
                    self._signal.emit("%d del: %s for : %s\r\n" % (i, p, r))
                else:
                    li[md5] = p

        count = 0
        for root, dirs, files in os.walk(path):  # 目录
            count += len(files)

        self._signal.emit("count: %d \r\n" % count)
        self._signal.emit("finish.\r\n\r\n")
