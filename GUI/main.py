################################################################################
##
## BY: WANDERSON M.PIMENTA
## PROJECT MADE WITH: Qt Designer and PySide2
## V: 1.0.0
##
################################################################################

import sys
import platform
from PySide2 import QtCore, QtGui, QtWidgets
from PySide2.QtCore import (QCoreApplication, QPropertyAnimation, QDate, QDateTime, QMetaObject, QObject, QPoint, QRect, QSize, QTime, QUrl, Qt, QEvent, QSortFilterProxyModel)
from PySide2.QtGui import (QBrush, QColor, QConicalGradient, QCursor, QFont, QFontDatabase, QIcon, QKeySequence, QLinearGradient, QPalette, QPainter, QPixmap, QRadialGradient)
from PySide2.QtWidgets import *
from os.path import exists
from PySide2.QtSql import *


# GUI FILE
from ui_main import Ui_MainWindow

# IMPORT FUNCTIONS
from ui_functions import *

if not exists("projects.db"):
	print("File projects.db does not exist. Please run initdb.py.")
	sys.exit()



class MainWindow(QMainWindow):
	def __init__(self):
		QMainWindow.__init__(self)
		self.ui = Ui_MainWindow()
		self.ui.setupUi(self)

		# Connect to SQL database
		self.db = QSqlDatabase.addDatabase("QSQLITE")
		self.db.setDatabaseName("projects.db")
		self.db.open()

		# Setup QSqlTableModel for easy read / write access to db
		self.model = QSqlTableModel(self)
		self.model.setTable("projects")
		self.model.setEditStrategy(QSqlTableModel.OnFieldChange)
		self.model.select()
		# self.model.setHeaderData(0, Qt.Horizontal, "Manufacturer")
		# self.model.setHeaderData(1, Qt.Horizontal, "Category")
		# self.model.setHeaderData(2, Qt.Horizontal, "Product")
		# self.model.setHeaderData(3, Qt.Horizontal, "UID")
		# self.model.setHeaderData(4, Qt.Horizontal, "Date & Time")

		# Update tableView as QSqlTableModel
		self.ui.tableView.setModel(self.model)
		self.ui.tableView.resizeColumnsToContents()

		# Setup QSortFilterProxyModel to enable search through QSqlTableModel
		self.filter_proxy_model = QSortFilterProxyModel()
		self.filter_proxy_model.setSourceModel(self.model)
		self.filter_proxy_model.setFilterCaseSensitivity(Qt.CaseInsensitive)
		# setFilterKeyColumn default 0, -1 to search all columns
		self.filter_proxy_model.setFilterKeyColumn(-1)
		# Start search when text is entered into the QLineEdit search_db
		self.ui.search_db.textChanged.connect(self.filter_proxy_model.setFilterRegExp)
		self.ui.tableView.setModel(self.filter_proxy_model)

		# Trigger ZMQ Simulation
		self.ui.simulate_ZMQ.clicked.connect(self.ZMQ_simulation)

		# Trigger db row removal
		self.ui.remove_row.clicked.connect(self.DeleteRow)

		# MOVE WINDOW
		def moveWindow(event):
			# RESTORE BEFORE MOVE
			if UIFunctions.returnStatus() == 1:
				UIFunctions.maximize_restore(self)

			# IF LEFT CLICK MOVE WINDOW
			if event.buttons() == Qt.LeftButton:
				self.move(self.pos() + event.globalPos() - self.dragPos)
				self.dragPos = event.globalPos()
				event.accept()

		# SET TITLE BAR
		self.ui.title_bar.mouseMoveEvent = moveWindow

		## ==> SET UI DEFINITIONS
		UIFunctions.uiDefinitions(self)


		## SHOW ==> MAIN WINDOW
		########################################################################
		self.show()

	## APP EVENTS
	########################################################################
	def mousePressEvent(self, event):
		self.dragPos = event.globalPos()

	# def closeEvent(self, event: PySide2.QtGui.QCloseEvent) -> None:
	def closeEvent(self, event):
		self.db.close()
		return super().closeEvent(event)

	def ZMQ_simulation(self):
		self.ui.line_Manfacturer.setText('EPCglobal')
		self.ui.line_Category.setText('Class 1 Gen 2')
		self.ui.line_Product.setText('Tag')
		self.ui.line_UID.setText('189256')
		datetime = QDateTime.currentDateTime()
		self.ui.line_Datetime.setText(datetime.toString('d.M.yy hh:mm:ss AP'))

		# Append new data to table
		self.rec = self.model.record()
		# Update each field's record
		data = [self.ui.line_Manfacturer.text(), self.ui.line_Category.text(), \
			self.ui.line_Product.text(), int(self.ui.line_UID.text()), self.ui.line_Datetime.text()]
		for i in range(5):
			self.rec.setValue(self.rec.field(i).name(), data[i])
		self.model.insertRecord(-1, self.rec)

	def DeleteRow(self):
		self.model.removeRow(self.ui.tableView.currentIndex().row())

if __name__ == "__main__":
	app = QApplication(sys.argv)
	window = MainWindow()
	sys.exit(app.exec_())
