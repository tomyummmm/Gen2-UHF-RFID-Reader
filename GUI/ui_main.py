# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'ui_main.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(880, 600)
        MainWindow.setMinimumSize(QSize(880, 600))
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.drop_shadow_layout = QVBoxLayout(self.centralwidget)
        self.drop_shadow_layout.setSpacing(0)
        self.drop_shadow_layout.setObjectName(u"drop_shadow_layout")
        self.drop_shadow_layout.setContentsMargins(10, 10, 10, 10)
        self.drop_shadow_frame = QFrame(self.centralwidget)
        self.drop_shadow_frame.setObjectName(u"drop_shadow_frame")
        self.drop_shadow_frame.setStyleSheet(u"background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1, stop:0 rgba(42, 44, 111, 255), stop:0.521368 rgba(28, 29, 73, 255));\n"
"border-radius: 10px;")
        self.drop_shadow_frame.setFrameShape(QFrame.NoFrame)
        self.drop_shadow_frame.setFrameShadow(QFrame.Raised)
        self.verticalLayout = QVBoxLayout(self.drop_shadow_frame)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.title_bar = QFrame(self.drop_shadow_frame)
        self.title_bar.setObjectName(u"title_bar")
        self.title_bar.setMaximumSize(QSize(16777215, 50))
        self.title_bar.setStyleSheet(u"background-color: none;")
        self.title_bar.setFrameShape(QFrame.NoFrame)
        self.title_bar.setFrameShadow(QFrame.Raised)
        self.horizontalLayout = QHBoxLayout(self.title_bar)
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.frame_title = QFrame(self.title_bar)
        self.frame_title.setObjectName(u"frame_title")
        self.frame_title.setMinimumSize(QSize(0, 50))
        font = QFont()
        font.setFamily(u"Roboto Condensed Light")
        font.setPointSize(14)
        self.frame_title.setFont(font)
        self.frame_title.setFrameShape(QFrame.StyledPanel)
        self.frame_title.setFrameShadow(QFrame.Raised)
        self.verticalLayout_2 = QVBoxLayout(self.frame_title)
        self.verticalLayout_2.setSpacing(0)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(15, 0, 0, 0)
        self.label_title = QLabel(self.frame_title)
        self.label_title.setObjectName(u"label_title")
        font1 = QFont()
        font1.setFamily(u"Roboto")
        font1.setPointSize(14)
        self.label_title.setFont(font1)
        self.label_title.setStyleSheet(u"color: rgb(60, 231, 195);")

        self.verticalLayout_2.addWidget(self.label_title)


        self.horizontalLayout.addWidget(self.frame_title)

        self.frame_btns = QFrame(self.title_bar)
        self.frame_btns.setObjectName(u"frame_btns")
        self.frame_btns.setMaximumSize(QSize(100, 16777215))
        self.frame_btns.setFrameShape(QFrame.StyledPanel)
        self.frame_btns.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_3 = QHBoxLayout(self.frame_btns)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.btn_minimize = QPushButton(self.frame_btns)
        self.btn_minimize.setObjectName(u"btn_minimize")
        self.btn_minimize.setMinimumSize(QSize(16, 16))
        self.btn_minimize.setMaximumSize(QSize(17, 17))
        self.btn_minimize.setStyleSheet(u"QPushButton {\n"
"	border: none;\n"
"	border-radius: 8px;		\n"
"	background-color: rgb(255, 170, 0);\n"
"}\n"
"QPushButton:hover {	\n"
"	background-color: rgba(255, 170, 0, 150);\n"
"}")

        self.horizontalLayout_3.addWidget(self.btn_minimize)

        self.btn_maximize = QPushButton(self.frame_btns)
        self.btn_maximize.setObjectName(u"btn_maximize")
        self.btn_maximize.setMinimumSize(QSize(16, 16))
        self.btn_maximize.setMaximumSize(QSize(17, 17))
        self.btn_maximize.setStyleSheet(u"QPushButton {\n"
"	border: none;\n"
"	border-radius: 8px;	\n"
"	background-color: rgb(85, 255, 127);\n"
"}\n"
"QPushButton:hover {	\n"
"	background-color: rgba(85, 255, 127, 150);\n"
"}")

        self.horizontalLayout_3.addWidget(self.btn_maximize)

        self.btn_close = QPushButton(self.frame_btns)
        self.btn_close.setObjectName(u"btn_close")
        self.btn_close.setMinimumSize(QSize(16, 16))
        self.btn_close.setMaximumSize(QSize(17, 17))
        self.btn_close.setStyleSheet(u"QPushButton {\n"
"	border: none;\n"
"	border-radius: 8px;		\n"
"	background-color: rgb(255, 0, 0);\n"
"}\n"
"QPushButton:hover {		\n"
"	background-color: rgba(255, 0, 0, 150);\n"
"}")

        self.horizontalLayout_3.addWidget(self.btn_close)


        self.horizontalLayout.addWidget(self.frame_btns)


        self.verticalLayout.addWidget(self.title_bar)

        self.content_bar = QFrame(self.drop_shadow_frame)
        self.content_bar.setObjectName(u"content_bar")
        self.content_bar.setStyleSheet(u"background-color: none;")
        self.content_bar.setFrameShape(QFrame.StyledPanel)
        self.content_bar.setFrameShadow(QFrame.Raised)
        self.verticalLayout_4 = QVBoxLayout(self.content_bar)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.stackedWidget = QStackedWidget(self.content_bar)
        self.stackedWidget.setObjectName(u"stackedWidget")
        self.stackedWidget.setStyleSheet(u"background-color: none;")
        self.page_home = QWidget()
        self.page_home.setObjectName(u"page_home")
        self.verticalLayout_5 = QVBoxLayout(self.page_home)
        self.verticalLayout_5.setSpacing(0)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.verticalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.frame_content_home = QFrame(self.page_home)
        self.frame_content_home.setObjectName(u"frame_content_home")
        self.frame_content_home.setFrameShape(QFrame.StyledPanel)
        self.frame_content_home.setFrameShadow(QFrame.Raised)
        self.verticalLayout_9 = QVBoxLayout(self.frame_content_home)
        self.verticalLayout_9.setObjectName(u"verticalLayout_9")
        self.frame_infos = QFrame(self.frame_content_home)
        self.frame_infos.setObjectName(u"frame_infos")
        self.frame_infos.setEnabled(True)
        sizePolicy = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.frame_infos.sizePolicy().hasHeightForWidth())
        self.frame_infos.setSizePolicy(sizePolicy)
        self.frame_infos.setFrameShape(QFrame.StyledPanel)
        self.frame_infos.setFrameShadow(QFrame.Raised)
        self.formLayout = QFormLayout(self.frame_infos)
        self.formLayout.setObjectName(u"formLayout")
        self.formLayout.setHorizontalSpacing(10)
        self.formLayout.setVerticalSpacing(6)
        self.formLayout.setContentsMargins(-1, -1, -1, 9)
        self.label_Manufacturer = QLabel(self.frame_infos)
        self.label_Manufacturer.setObjectName(u"label_Manufacturer")
        self.label_Manufacturer.setMinimumSize(QSize(65, 16))
        font2 = QFont()
        font2.setPointSize(10)
        self.label_Manufacturer.setFont(font2)
        self.label_Manufacturer.setAutoFillBackground(False)
        self.label_Manufacturer.setStyleSheet(u"color: rgb(255, 255, 255);")
        self.label_Manufacturer.setFrameShape(QFrame.NoFrame)
        self.label_Manufacturer.setLineWidth(1)
        self.label_Manufacturer.setMargin(0)
        self.label_Manufacturer.setIndent(-1)

        self.formLayout.setWidget(0, QFormLayout.LabelRole, self.label_Manufacturer)

        self.line_Manfacturer = QLineEdit(self.frame_infos)
        self.line_Manfacturer.setObjectName(u"line_Manfacturer")
        self.line_Manfacturer.setFont(font2)
        self.line_Manfacturer.setClearButtonEnabled(False)

        self.formLayout.setWidget(0, QFormLayout.FieldRole, self.line_Manfacturer)

        self.label_Category = QLabel(self.frame_infos)
        self.label_Category.setObjectName(u"label_Category")
        self.label_Category.setMinimumSize(QSize(45, 16))
        self.label_Category.setFont(font2)
        self.label_Category.setAutoFillBackground(False)
        self.label_Category.setStyleSheet(u"color: rgb(255, 255, 255);")
        self.label_Category.setFrameShape(QFrame.NoFrame)
        self.label_Category.setLineWidth(1)
        self.label_Category.setMargin(0)
        self.label_Category.setIndent(-1)

        self.formLayout.setWidget(1, QFormLayout.LabelRole, self.label_Category)

        self.line_Category = QLineEdit(self.frame_infos)
        self.line_Category.setObjectName(u"line_Category")
        self.line_Category.setFont(font2)
        self.line_Category.setClearButtonEnabled(False)

        self.formLayout.setWidget(1, QFormLayout.FieldRole, self.line_Category)

        self.label_Product = QLabel(self.frame_infos)
        self.label_Product.setObjectName(u"label_Product")
        self.label_Product.setMinimumSize(QSize(37, 16))
        self.label_Product.setFont(font2)
        self.label_Product.setAutoFillBackground(False)
        self.label_Product.setStyleSheet(u"color: rgb(255, 255, 255);")
        self.label_Product.setFrameShape(QFrame.NoFrame)
        self.label_Product.setLineWidth(1)
        self.label_Product.setMargin(0)
        self.label_Product.setIndent(-1)

        self.formLayout.setWidget(2, QFormLayout.LabelRole, self.label_Product)

        self.line_Product = QLineEdit(self.frame_infos)
        self.line_Product.setObjectName(u"line_Product")
        self.line_Product.setFont(font2)
        self.line_Product.setClearButtonEnabled(False)

        self.formLayout.setWidget(2, QFormLayout.FieldRole, self.line_Product)

        self.label_UID = QLabel(self.frame_infos)
        self.label_UID.setObjectName(u"label_UID")
        self.label_UID.setMinimumSize(QSize(18, 16))
        self.label_UID.setFont(font2)
        self.label_UID.setAutoFillBackground(False)
        self.label_UID.setStyleSheet(u"color: rgb(255, 255, 255);")
        self.label_UID.setFrameShape(QFrame.NoFrame)
        self.label_UID.setLineWidth(1)
        self.label_UID.setMargin(0)
        self.label_UID.setIndent(-1)

        self.formLayout.setWidget(3, QFormLayout.LabelRole, self.label_UID)

        self.line_UID = QLineEdit(self.frame_infos)
        self.line_UID.setObjectName(u"line_UID")
        self.line_UID.setFont(font2)
        self.line_UID.setClearButtonEnabled(False)

        self.formLayout.setWidget(3, QFormLayout.FieldRole, self.line_UID)

        self.label_Timedate = QLabel(self.frame_infos)
        self.label_Timedate.setObjectName(u"label_Timedate")
        self.label_Timedate.setMinimumSize(QSize(47, 16))
        self.label_Timedate.setFont(font2)
        self.label_Timedate.setAutoFillBackground(False)
        self.label_Timedate.setStyleSheet(u"color: rgb(255, 255, 255);")
        self.label_Timedate.setFrameShape(QFrame.NoFrame)
        self.label_Timedate.setLineWidth(1)
        self.label_Timedate.setMargin(0)
        self.label_Timedate.setIndent(-1)

        self.formLayout.setWidget(4, QFormLayout.LabelRole, self.label_Timedate)

        self.line_Datetime = QLineEdit(self.frame_infos)
        self.line_Datetime.setObjectName(u"line_Datetime")
        self.line_Datetime.setFont(font2)
        self.line_Datetime.setClearButtonEnabled(False)

        self.formLayout.setWidget(4, QFormLayout.FieldRole, self.line_Datetime)


        self.verticalLayout_9.addWidget(self.frame_infos)

        self.simulate_ZMQ = QPushButton(self.frame_content_home)
        self.simulate_ZMQ.setObjectName(u"simulate_ZMQ")
        self.simulate_ZMQ.setFont(font2)
        self.simulate_ZMQ.setAutoFillBackground(False)
        self.simulate_ZMQ.setStyleSheet(u"background-color: yellow")

        self.verticalLayout_9.addWidget(self.simulate_ZMQ)

        self.search_db = QLineEdit(self.frame_content_home)
        self.search_db.setObjectName(u"search_db")
        sizePolicy1 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Fixed)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.search_db.sizePolicy().hasHeightForWidth())
        self.search_db.setSizePolicy(sizePolicy1)
        self.search_db.setFont(font2)
        self.search_db.setAlignment(Qt.AlignCenter)

        self.verticalLayout_9.addWidget(self.search_db)

        self.tableView = QTableView(self.frame_content_home)
        self.tableView.setObjectName(u"tableView")
        sizePolicy2 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.tableView.sizePolicy().hasHeightForWidth())
        self.tableView.setSizePolicy(sizePolicy2)
        self.tableView.setFont(font2)
        self.tableView.setSizeAdjustPolicy(QAbstractScrollArea.AdjustToContents)
        self.tableView.setAlternatingRowColors(True)
        self.tableView.setShowGrid(True)
        self.tableView.setWordWrap(True)

        self.verticalLayout_9.addWidget(self.tableView)

        self.remove_row = QPushButton(self.frame_content_home)
        self.remove_row.setObjectName(u"remove_row")
        self.remove_row.setStyleSheet(u"background-color: white")

        self.verticalLayout_9.addWidget(self.remove_row)

        self.tableView.raise_()
        self.search_db.raise_()
        self.simulate_ZMQ.raise_()
        self.frame_infos.raise_()
        self.remove_row.raise_()

        self.verticalLayout_5.addWidget(self.frame_content_home)

        self.stackedWidget.addWidget(self.page_home)
        self.page_credits = QWidget()
        self.page_credits.setObjectName(u"page_credits")
        self.frame_content_credits = QFrame(self.page_credits)
        self.frame_content_credits.setObjectName(u"frame_content_credits")
        self.frame_content_credits.setGeometry(QRect(90, 70, 120, 80))
        self.frame_content_credits.setFrameShape(QFrame.StyledPanel)
        self.frame_content_credits.setFrameShadow(QFrame.Raised)
        self.stackedWidget.addWidget(self.page_credits)

        self.verticalLayout_4.addWidget(self.stackedWidget)


        self.verticalLayout.addWidget(self.content_bar)

        self.credits_bar = QFrame(self.drop_shadow_frame)
        self.credits_bar.setObjectName(u"credits_bar")
        self.credits_bar.setMaximumSize(QSize(16777215, 30))
        self.credits_bar.setStyleSheet(u"background-color: rgb(33, 33, 75);")
        self.credits_bar.setFrameShape(QFrame.NoFrame)
        self.credits_bar.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_2 = QHBoxLayout(self.credits_bar)
        self.horizontalLayout_2.setSpacing(0)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.frame_label_credits = QFrame(self.credits_bar)
        self.frame_label_credits.setObjectName(u"frame_label_credits")
        self.frame_label_credits.setFrameShape(QFrame.StyledPanel)
        self.frame_label_credits.setFrameShadow(QFrame.Raised)
        self.verticalLayout_3 = QVBoxLayout(self.frame_label_credits)
        self.verticalLayout_3.setSpacing(0)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalLayout_3.setContentsMargins(15, 0, 0, 0)
        self.label_credits = QLabel(self.frame_label_credits)
        self.label_credits.setObjectName(u"label_credits")
        font3 = QFont()
        font3.setFamily(u"Roboto")
        self.label_credits.setFont(font3)
        self.label_credits.setStyleSheet(u"color: rgb(128, 102, 168);")

        self.verticalLayout_3.addWidget(self.label_credits)


        self.horizontalLayout_2.addWidget(self.frame_label_credits)

        self.frame_grip = QFrame(self.credits_bar)
        self.frame_grip.setObjectName(u"frame_grip")
        self.frame_grip.setMinimumSize(QSize(30, 30))
        self.frame_grip.setMaximumSize(QSize(30, 30))
        self.frame_grip.setStyleSheet(u"padding: 5px;")
        self.frame_grip.setFrameShape(QFrame.StyledPanel)
        self.frame_grip.setFrameShadow(QFrame.Raised)

        self.horizontalLayout_2.addWidget(self.frame_grip)


        self.verticalLayout.addWidget(self.credits_bar)


        self.drop_shadow_layout.addWidget(self.drop_shadow_frame)

        MainWindow.setCentralWidget(self.centralwidget)
        QWidget.setTabOrder(self.btn_minimize, self.btn_maximize)
        QWidget.setTabOrder(self.btn_maximize, self.btn_close)
        QWidget.setTabOrder(self.btn_close, self.line_Manfacturer)
        QWidget.setTabOrder(self.line_Manfacturer, self.line_Category)
        QWidget.setTabOrder(self.line_Category, self.line_Product)
        QWidget.setTabOrder(self.line_Product, self.line_UID)
        QWidget.setTabOrder(self.line_UID, self.line_Datetime)
        QWidget.setTabOrder(self.line_Datetime, self.simulate_ZMQ)
        QWidget.setTabOrder(self.simulate_ZMQ, self.search_db)
        QWidget.setTabOrder(self.search_db, self.tableView)

        self.retranslateUi(MainWindow)

        self.stackedWidget.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.label_title.setText(QCoreApplication.translate("MainWindow", u"GUI database test", None))
#if QT_CONFIG(tooltip)
        self.btn_minimize.setToolTip(QCoreApplication.translate("MainWindow", u"Minimize", None))
#endif // QT_CONFIG(tooltip)
        self.btn_minimize.setText("")
#if QT_CONFIG(tooltip)
        self.btn_maximize.setToolTip(QCoreApplication.translate("MainWindow", u"Maximize", None))
#endif // QT_CONFIG(tooltip)
        self.btn_maximize.setText("")
#if QT_CONFIG(tooltip)
        self.btn_close.setToolTip(QCoreApplication.translate("MainWindow", u"Close", None))
#endif // QT_CONFIG(tooltip)
        self.btn_close.setText("")
        self.label_Manufacturer.setText(QCoreApplication.translate("MainWindow", u"Manufacturer", None))
        self.label_Category.setText(QCoreApplication.translate("MainWindow", u"Category", None))
        self.label_Product.setText(QCoreApplication.translate("MainWindow", u"Product", None))
        self.label_UID.setText(QCoreApplication.translate("MainWindow", u"UID", None))
        self.label_Timedate.setText(QCoreApplication.translate("MainWindow", u"Date & Time", None))
        self.simulate_ZMQ.setText(QCoreApplication.translate("MainWindow", u"Simulate ZMQ data", None))
        self.search_db.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Search", None))
        self.remove_row.setText(QCoreApplication.translate("MainWindow", u"Remove Row", None))
        self.label_credits.setText(QCoreApplication.translate("MainWindow", u"By: Mervin", None))
    # retranslateUi

