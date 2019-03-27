# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'mainwindow.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

import csv
import pandas as pd
from PyQt5 import QtCore, QtGui, QtWidgets
import sys
data=[]
class Ui_MainWindow(QtWidgets.QMainWindow):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(658, 394)
        self.centralWidget = QtWidgets.QWidget(MainWindow)
        self.centralWidget.setObjectName("centralWidget")
        self.tableWidget = QtWidgets.QTableWidget(self.centralWidget)
        self.tableWidget.setGeometry(QtCore.QRect(10, 10, 631, 321))
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setColumnCount(1)
        self.tableWidget.setRowCount(1)
        MainWindow.setCentralWidget(self.centralWidget)
        self.menuBar = QtWidgets.QMenuBar(MainWindow)
        self.menuBar.setGeometry(QtCore.QRect(0, 0, 658, 22))
        self.menuBar.setObjectName("menuBar")

        self.menuImport_Data = QtWidgets.QMenu(self.menuBar)
        self.menuImport_Data.setObjectName("menuImport_Data")
        self.menuImport_Data.triggered.connect(self.browse)

        self.menuExport_Table = QtWidgets.QMenu(self.menuBar)
        self.menuExport_Table.setObjectName("menuExport_Table")
        self.menuExport_Table.triggered.connect(self.export)

        self.menuTable_View = QtWidgets.QMenu(self.menuBar)
        self.menuTable_View.setObjectName("menuTable_View")
        self.menuPandas_Data_Frame = QtWidgets.QMenu(self.menuBar)
        self.menuPandas_Data_Frame.setObjectName("menuPandas_Data_Frame")
        MainWindow.setMenuBar(self.menuBar)
        self.mainToolBar = QtWidgets.QToolBar(MainWindow)
        self.mainToolBar.setObjectName("mainToolBar")
        MainWindow.addToolBar(QtCore.Qt.TopToolBarArea, self.mainToolBar)
        self.statusBar = QtWidgets.QStatusBar(MainWindow)
        self.statusBar.setObjectName("statusBar")
        MainWindow.setStatusBar(self.statusBar)
        self.actionfrom_CSV = QtWidgets.QAction(MainWindow)
        self.actionfrom_CSV.setObjectName("actionfrom_CSV")
        self.actionto_CSV = QtWidgets.QAction(MainWindow)
        self.actionto_CSV.setObjectName("actionto_CSV")

        self.actionIncrease_Table = QtWidgets.QAction(MainWindow)
        self.actionIncrease_Table.setObjectName("actionIncrease_Table")
        self.actionIncrease_Table.triggered.connect(self.increaesRow)

        self.actionDecrease_Row = QtWidgets.QAction(MainWindow)
        self.actionDecrease_Row.setObjectName("actionDecrease_Row")
        self.actionDecrease_Row.triggered.connect(self.decreaesRow)

        self.actionIncrease_Column = QtWidgets.QAction(MainWindow)
        self.actionIncrease_Column.setObjectName("actionIncrease_Column")
        self.actionIncrease_Column.triggered.connect(self.increaesColumn)

        self.actionDecrease_Column = QtWidgets.QAction(MainWindow)
        self.actionDecrease_Column.setObjectName("actionDecrease_Column")
        self.actionDecrease_Column.triggered.connect(self.decreaesColumn)

        self.actionCreate_and_Export_as_CSV = QtWidgets.QAction(MainWindow)
        self.actionCreate_and_Export_as_CSV.setObjectName("actionCreate_and_Export_as_CSV")
        self.actionCreate_and_Export_as_CSV.triggered.connect(self.create_pandasDataFrame)

        self.menuImport_Data.addAction(self.actionfrom_CSV)
        self.menuExport_Table.addAction(self.actionto_CSV)
        self.menuTable_View.addAction(self.actionIncrease_Table)
        self.menuTable_View.addAction(self.actionDecrease_Row)
        self.menuTable_View.addAction(self.actionIncrease_Column)
        self.menuTable_View.addAction(self.actionDecrease_Column)
        self.menuPandas_Data_Frame.addAction(self.actionCreate_and_Export_as_CSV)
        self.menuBar.addAction(self.menuImport_Data.menuAction())
        self.menuBar.addAction(self.menuExport_Table.menuAction())
        self.menuBar.addAction(self.menuTable_View.menuAction())
        self.menuBar.addAction(self.menuPandas_Data_Frame.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.menuImport_Data.setTitle(_translate("MainWindow", "Import Data"))
        self.menuExport_Table.setTitle(_translate("MainWindow", "Export Table"))
        self.menuTable_View.setTitle(_translate("MainWindow", "Table View"))
        self.menuPandas_Data_Frame.setTitle(_translate("MainWindow", "Pandas Data Frame"))
        self.actionfrom_CSV.setText(_translate("MainWindow", "from CSV"))
        self.actionto_CSV.setText(_translate("MainWindow", "to CSV"))
        self.actionIncrease_Table.setText(_translate("MainWindow", "Increase Row"))
        self.actionDecrease_Row.setText(_translate("MainWindow", "Decrease Row"))
        self.actionIncrease_Column.setText(_translate("MainWindow", "Increase Column"))
        self.actionDecrease_Column.setText(_translate("MainWindow", "Decrease Column"))
        self.actionCreate_and_Export_as_CSV.setText(_translate("MainWindow", "Create and Export as CSV"))

    def increaesRow(self):
        self.tableWidget.insertRow(self.tableWidget.rowCount())
    def decreaesRow(self):
        self.tableWidget.removeRow(self.tableWidget.rowCount()-1)
    def increaesColumn(self):
        self.tableWidget.insertColumn(self.tableWidget.columnCount())
    def decreaesColumn(self):
        self.tableWidget.removeColumn(self.tableWidget.rowCount()-1)

    def browse(self):
        file = QtWidgets.QFileDialog.getOpenFileName(self, 'Browse File','/home','*.csv')
        if(len(file[0])>0):
            with open(file[0],'rt') as f:
                data = csv.reader(f)
                rows=0
                cols=0
                for row in data:
                    rows+=1
                    cols=len(row)
                self.tableWidget.setRowCount(rows)
                self.tableWidget.setColumnCount(cols)
            with open(file[0],'r') as f:
                data = csv.reader(f)
                i=0
                for row in data:
                    j=0
                    print(1)
                    for val in row:
                        print(val)
                        self.tableWidget.setItem(i,j,QtWidgets.QTableWidgetItem(val))
                        j+=1
                    i+=1

    def export(self):
        file = QtWidgets.QFileDialog.getSaveFileName(self,"Export as CSV", "","(*.csv);;All Files (*)")
        print(file)
        global data
        self.read_data_from_table()

        if(len(file[0])>0):
            with open(file[0], 'w') as writeFile:
                writer = csv.writer(writeFile)
                writer.writerows(data)

    def read_data_from_table(self):
        global data
        data.clear()
        cols=self.tableWidget.columnCount()
        rows=self.tableWidget.rowCount()
        for i in range(rows):
            row=[]
            for j in range(cols):
                item=self.tableWidget.item(i,j)
                print(item)
                if item is not None:
                    row.append(item.text())
            data.append(row)

    def create_pandasDataFrame(self):
        self.export()
        global data
        self.read_data_from_table()
        df=pd.DataFrame(data)
        df.to_csv(index=None, header=True)
        print('\n\n\n______Panda Data Frame______\n',pd.DataFrame(data))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

