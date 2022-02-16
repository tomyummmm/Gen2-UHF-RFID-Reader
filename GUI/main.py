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


class MainWindow(QMainWindow):
	def __init__(self):
		QMainWindow.__init__(self)
		self.ui = Ui_MainWindow()
		self.ui.setupUi(self)

		# Connect to SQL database
		self.db = QSqlDatabase.addDatabase("QSQLITE")
		self.db.setDatabaseName("projects.db")
		if not exists("projects.db"):
			self.db.open()
			print("File projects.db does not exist. Creating empty table.")
			query = QSqlQuery()
			query.exec_("""
						CREATE TABLE projects
						(EPC TEXT PRIMARY KEY, Category TEXT, Read_Count INTEGER, Last_Read_From TEXT, First_Seen TEXT, Last_Seen TEXT, Time_Since_Last_Seen INTEGER, Last_RSSI INTEGER, RSSI_Avg INTEGER, RSSI_Max INTEGER, RSSI_Min INTEGER, Power INTEGER, Phase_Angle INTEGER, Doppler_Freq INTEGER)
						""")
			query.exec_("""INSERT INTO projects VALUES 
							('912391239123912391239123', 'Classic', 0, '127.0.0.1', '2022-01-01 12:00:00.001', '2022-01-02 12:00:00.001', 2678400, -50.30, -48.8, -45.2, -54.6, 30.00, NULL, NULL),
							('845684568456845684568456', 'Class 1', 1, '127.0.0.1', '2022-02-01 3:00:00.001', '2022-02-02 12:00:00.001', 2678400, -50.30, -48.8, -45.2, -54.6, 30.00, NULL, NULL),
							('789078907890789078907890', '18000-6C', 0, '127.0.0.1', '2022-02-01 5:00:00.001', '2022-02-03 12:00:00.001', 2764800, -50.30, -48.8, -45.2, -54.6, 30.00, NULL, NULL)
							""")
			self.db.close()

		self.db.open()

		# Setup QSqlTableModel for easy read / write access to db
		self.model = QSqlTableModel(self)
		self.model.setTable("projects")
		self.model.setEditStrategy(QSqlTableModel.OnFieldChange)
		# self.model.setEditStrategy(QSqlTableModel.OnManualSubmit)
		self.model.select()
		self.model.setHeaderData(0, Qt.Horizontal, "EPC")
		self.model.setHeaderData(1, Qt.Horizontal, "Category")
		self.model.setHeaderData(2, Qt.Horizontal, "Read Count")
		self.model.setHeaderData(3, Qt.Horizontal, "Last Read From")
		self.model.setHeaderData(4, Qt.Horizontal, "First Seen (Y-M-D H:M:S)")
		self.model.setHeaderData(5, Qt.Horizontal, "Last Seen")
		self.model.setHeaderData(6, Qt.Horizontal, "Time Since Last Seen (Sec)")
		self.model.setHeaderData(7, Qt.Horizontal, "Last RSSI")
		self.model.setHeaderData(8, Qt.Horizontal, "RSSI Avg")
		self.model.setHeaderData(9, Qt.Horizontal, "RSSI Max")
		self.model.setHeaderData(10, Qt.Horizontal, "RSSI Min")
		self.model.setHeaderData(11, Qt.Horizontal, "Power")
		self.model.setHeaderData(12, Qt.Horizontal, "Phase Angle")
		self.model.setHeaderData(13, Qt.Horizontal, "Doppler Frequency")

		# Update tableView as QSqlTableModel
		self.ui.tableView.setModel(self.model)
		self.ui.tableView.resizeColumnsToContents()
		# # Set to stretch EPC column so that entire table stays in view regardless of window size
		self.ui.tableView.horizontalHeader().setSectionResizeMode(0, QHeaderView.Stretch)

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
		# Append new data to table
		query = QSqlQuery()

		# EPC TEXT PRIMARY KEY
		# Category TEXT
		# Read_Count INTEGER
		# Last_Read_From TEXT
		# First_Seen TEXT
		# Last_Seen TEXT
		# Time_Since_Last_Seen INTEGER
		# Last_RSSI INTEGER
		# RSSI_Avg INTEGER
		# RSSI_Max INTEGER
		# RSSI_Min INTEGER
		# Power INTEGER
		# Phase_Angle INTEGER
		# Doppler_Freq INTEGER
		# Using SQL UPSERT (https://www.sqlite.org/lang_UPSERT.html). Special syntax addition to INSERT that causes the INSERT to behave as an UPDATE or a no-op if the INSERT would violate a uniqueness constraint. UPSERT is not standard SQL.
		query.exec_("""INSERT INTO projects (EPC, Category, Read_Count, Last_Read_From, First_Seen, Last_Seen, Time_Since_Last_Seen, Last_RSSI, RSSI_Avg, RSSI_Max, RSSI_Min, Power, Phase_Angle, Doppler_Freq)
					VALUES('912391239123912391239123', 'Classic', 0, '127.0.0.1', '2022-01-01 12:00:00.001', '2022-01-02 12:00:00.001', 2678400, -50.30, -48.8, -45.2, -54.6, 30.00, NULL, NULL)
					ON CONFLICT (EPC) DO
					UPDATE SET Read_Count=Read_count+1,
					Time_Since_Last_Seen=(julianday('now') - julianday(Last_Seen)) * 86400,
					Last_Seen=strftime('%Y-%m-%d %H:%M:%f', 'now')
					""")
		self.model.select()
		# self.model.submitAll()

		# self.db.exec_("""INSERT INTO projects (EPC, Category, Read_Count, Last_Read_From, First_Seen, Last_Seen, Time_Since_Last_Seen, Last_RSSI, RSSI_Avg, RSSI_Max, RSSI_Min, Power, Phase_Angle, Doppler_Freq)
		# 			VALUES('912391239123912391239123', 'Classic', 0, '127.0.0.1', '2022-01-01 12:00:00.001', '2022-01-02 12:00:00.001', 2678400, -50.30, -48.8, -45.2, -54.6, 30.00, NULL, NULL)
		# 			ON CONFLICT (EPC) DO UPDATE SET 
		# 			Read_Count=Read_count+1,
		# 			Time_Since_Last_Seen=strftime('%Y-%m-%d %H:%M:%f', 'now') - strftime('%Y-%m-%d %H:%M:%f', Last_Seen),
		# 			Last_Seen=strftime('%Y-%m-%d %H:%M:%f', 'now')
		# 			""")
		# self.model.submitAll()


	def DeleteRow(self):
		self.model.removeRow(self.ui.tableView.currentIndex().row())
		self.model.select()
		# self.model.submitAll()


if __name__ == "__main__":
	app = QApplication(sys.argv)
	window = MainWindow()
	sys.exit(app.exec_())
