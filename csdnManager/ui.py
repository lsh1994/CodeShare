from PyQt5 import QtCore, QtGui, QtWidgets
import csdnCg
import numpy as np
import pandas as pd

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1100, 560)
        icon = QtGui.QIcon("res/reflush.png")
        MainWindow.setWindowIcon(icon)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName("gridLayout")
        self.tableWidget = QtWidgets.QTableWidget(self.centralwidget)
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setColumnCount(6)
        horizontalHeader = ["标题", "发布日期", "阅读量", "评论量","阅读量增加","评论量增加"]
        self.tableWidget.setHorizontalHeaderLabels(horizontalHeader)
        font = QtGui.QFont('华文新魏', 12)
        # font.setBold(True)  # 设置字体加粗
        self.tableWidget.horizontalHeader().setFont(font)  # 设置表头字体
        self.tableWidget.setColumnWidth(0,325)
        self.tableWidget.setColumnWidth(1, 150)
        self.tableWidget.setRowCount(0)
        self.gridLayout.addWidget(self.tableWidget, 0, 0, 1, 1)
        self.tableWidget.horizontalHeader().setSectionsClickable(True)  # 可以禁止点击表头的列

        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.toolBar = QtWidgets.QToolBar(MainWindow)
        self.toolBar.setObjectName("toolBar")
        MainWindow.addToolBar(QtCore.Qt.TopToolBarArea, self.toolBar)
        self.action_save = QtWidgets.QAction(MainWindow)
        self.action_save.setObjectName("action_save")
        self.action_define_old = QtWidgets.QAction(MainWindow)
        self.action_define_old.setObjectName("action_define_old")
        self.action_update = QtWidgets.QAction(MainWindow)
        self.action_update.setObjectName("action_update")
        self.toolBar.addAction(self.action_save)
        self.toolBar.addAction(self.action_define_old)
        self.toolBar.addAction(self.action_update)
        self.retranslateUi(MainWindow)
        #QtCore.QMetaObject.connectSlotsByName(MainWindow)

        self.label = QtWidgets.QLabel()
        self.statusbar.addWidget(self.label)

        self.action_save.triggered.connect(self.save2file)
        self.action_define_old.triggered.connect(self.define_old)
        self.action_update.triggered.connect(self.reflush_data)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "CSDN博客管理工具"))
        self.toolBar.setWindowTitle(_translate("MainWindow", "toolBar"))

        self.action_save.setText(_translate("MainWindow", "保存到文件"))
        self.action_save.setIcon(QtGui.QIcon('res/save.png'))
        self.action_save.setToolTip("网络状态读取保存到文件")

        self.action_define_old.setText(_translate("MainWindow", "和旧文件比较"))
        self.action_define_old.setIcon(QtGui.QIcon('res/vs.png'))
        self.action_define_old.setToolTip("网络状态读取和保存的旧文件对比")

        self.action_update.setText("更新")
        self.action_update.setIcon(QtGui.QIcon('res/update.png'))
        self.action_update.setToolTip("更新最新的网络状态读取")

    datas=[]

    def reflush_data(self):
        self.tableWidget.setRowCount(0)
        self.tableWidget.clearContents()
        self.init_data()

    def init_data(self):
        self.datas=[]
        total=0
        for dt in csdnCg.getData():
            for i in dt:
                self.tableWidget.insertRow(self.tableWidget.rowCount())
                self.tableWidget.setItem(total,0,QtWidgets.QTableWidgetItem(i[1]))
                self.tableWidget.setItem(total, 1, QtWidgets.QTableWidgetItem(i[2]))
                self.tableWidget.setItem(total, 2, QtWidgets.QTableWidgetItem(i[3]))
                self.tableWidget.setItem(total, 3, QtWidgets.QTableWidgetItem(i[4]))
                total+=1
                self.datas.append(i)


    def save2file(self):
        reply=QtWidgets.QMessageBox.question(self.centralwidget,'确认对话框','确认保存到本地？该操作不可逆',
                                       QtWidgets.QMessageBox.Yes | QtWidgets.QMessageBox.Cancel,QtWidgets.QMessageBox.Cancel)
        if reply == QtWidgets.QMessageBox.Yes:
            df = pd.DataFrame(self.datas)
            df.to_csv(csdnCg.mysite+".txt",encoding='utf8')
            QtWidgets.QMessageBox.information(self.centralwidget,"信息","保存成功")


    def define_old(self):
        try:
            df_old = pd.read_csv(csdnCg.mysite+".txt",encoding='utf8')
        except Exception as e: #读取失败，可能是没有历史文件
            print(e)
            QtWidgets.QMessageBox.information(self.centralwidget, "信息", "读取错误，即将新建备份...")
            self.save2file()
            return
        df_new =pd.DataFrame(self.datas)
        res=[]
        # for url in df_new[0]:
        #     sp = df_old[df_old["0"].isin([url])]
        #     res.append(sp.values[0][-2:])
        # print(res)
        for i in range(df_new.shape[0]):
            p=df_new.iloc[i].values[-2:]
            sp = df_old[df_old["0"].isin([df_new.iloc[i].values[0]])]
            if(len(sp.values)==0):
                sp=[0,0]
            else:
                sp=sp.values[0][-2:]
            res.append([int(p[0])-int(sp[0]),int(p[1])-int(sp[1])])
            # print(np.subtract(p,sp))
        # return res

        for i in range(df_new.shape[0]):
            # print(i,res[i])
            if (res[i][0] == 0 and res[i][1] == 0):
                self.tableWidget.hideRow(i)
                continue
            self.tableWidget.setItem(i, 4, QtWidgets.QTableWidgetItem(str(res[i][0])))
            self.tableWidget.setItem(i, 5, QtWidgets.QTableWidgetItem(str(res[i][1])))

        total=np.sum(res,axis=0)

        self.label.setText("总浏览量增加：%d  总评论增加：%d" % (total[0],total[1]))





