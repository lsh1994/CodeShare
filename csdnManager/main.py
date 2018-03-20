import sys
import ui
from PyQt5.QtWidgets import QApplication, QWidget,QMainWindow

import warnings
warnings.filterwarnings("ignore")

if __name__ == '__main__':
    app = QApplication(sys.argv)

    MainWindow = QMainWindow()
    ui = ui.Ui_MainWindow()
    ui.setupUi(MainWindow)
    ui.init_data()
    MainWindow.show()

    sys.exit(app.exec_())