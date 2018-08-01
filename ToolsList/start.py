import sys

from PyQt5.QtWidgets import QApplication
from ToolsList import maingui


if __name__ == '__main__':

    app=QApplication(sys.argv)

    gui = maingui.Ui_MainWindow()

    gui.show()
    sys.exit(app.exec_())

    # pyinstaller -F -w ToolsList\start.py

