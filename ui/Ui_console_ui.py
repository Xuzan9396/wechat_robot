# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'console_ui.ui'
##
## Created by: Qt User Interface Compiler version 6.5.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QFrame, QGridLayout, QGroupBox,
    QHBoxLayout, QLabel, QLineEdit, QMainWindow,
    QPlainTextEdit, QPushButton, QSizePolicy, QSpacerItem,
    QVBoxLayout, QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(1102, 692)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.verticalLayout = QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalFrame = QFrame(self.centralwidget)
        self.verticalFrame.setObjectName(u"verticalFrame")
        self.verticalLayout_2 = QVBoxLayout(self.verticalFrame)
        self.verticalLayout_2.setSpacing(1)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.frame = QFrame(self.verticalFrame)
        self.frame.setObjectName(u"frame")
        self.frame.setFrameShape(QFrame.NoFrame)
        self.frame.setFrameShadow(QFrame.Raised)
        self.verticalLayout_3 = QVBoxLayout(self.frame)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.horizontalLayout_4 = QHBoxLayout()
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.groupBox_0 = QGroupBox(self.frame)
        self.groupBox_0.setObjectName(u"groupBox_0")
        font = QFont()
        font.setPointSize(20)
        self.groupBox_0.setFont(font)
        self.verticalLayout_4 = QVBoxLayout(self.groupBox_0)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.verticalSpacer_2 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_4.addItem(self.verticalSpacer_2)

        self.gridLayout_3 = QGridLayout()
        self.gridLayout_3.setObjectName(u"gridLayout_3")
        self.gridLayout_3.setContentsMargins(-1, -1, -1, 12)
        self.label_2 = QLabel(self.groupBox_0)
        self.label_2.setObjectName(u"label_2")
        font1 = QFont()
        font1.setPointSize(17)
        font1.setBold(False)
        self.label_2.setFont(font1)
        self.label_2.setLayoutDirection(Qt.RightToLeft)
        self.label_2.setAlignment(Qt.AlignCenter)
        self.label_2.setMargin(1)

        self.gridLayout_3.addWidget(self.label_2, 0, 0, 1, 1)

        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout_3.addItem(self.horizontalSpacer, 0, 2, 1, 1)

        self.label_5 = QLabel(self.groupBox_0)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setAlignment(Qt.AlignCenter)

        self.gridLayout_3.addWidget(self.label_5, 1, 0, 1, 1)

        self.ws_port = QLineEdit(self.groupBox_0)
        self.ws_port.setObjectName(u"ws_port")
        self.ws_port.setMaximumSize(QSize(200, 16777215))

        self.gridLayout_3.addWidget(self.ws_port, 0, 1, 1, 1)

        self.ws_token = QLineEdit(self.groupBox_0)
        self.ws_token.setObjectName(u"ws_token")

        self.gridLayout_3.addWidget(self.ws_token, 1, 1, 1, 1)

        self.start_button = QPushButton(self.groupBox_0)
        self.start_button.setObjectName(u"start_button")
        self.start_button.setMaximumSize(QSize(100, 16777215))
        font2 = QFont()
        font2.setPointSize(18)
        self.start_button.setFont(font2)
        self.start_button.setStyleSheet(u"text-align:left;")

        self.gridLayout_3.addWidget(self.start_button, 3, 1, 1, 1)

        self.ws_path = QLineEdit(self.groupBox_0)
        self.ws_path.setObjectName(u"ws_path")

        self.gridLayout_3.addWidget(self.ws_path, 2, 1, 1, 1)

        self.label_6 = QLabel(self.groupBox_0)
        self.label_6.setObjectName(u"label_6")
        self.label_6.setAlignment(Qt.AlignCenter)

        self.gridLayout_3.addWidget(self.label_6, 2, 0, 1, 1)

        self.gridLayout_3.setColumnStretch(0, 3)
        self.gridLayout_3.setColumnStretch(1, 4)
        self.gridLayout_3.setColumnStretch(2, 2)

        self.verticalLayout_4.addLayout(self.gridLayout_3)

        self.verticalSpacer = QSpacerItem(20, 3, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_4.addItem(self.verticalSpacer)

        self.verticalLayout_4.setStretch(0, 10)
        self.verticalLayout_4.setStretch(2, 30)

        self.horizontalLayout_4.addWidget(self.groupBox_0)

        self.groupBox = QGroupBox(self.frame)
        self.groupBox.setObjectName(u"groupBox")
        self.groupBox.setFont(font)
        self.verticalLayout_5 = QVBoxLayout(self.groupBox)
#ifndef Q_OS_MAC
        self.verticalLayout_5.setSpacing(-1)
#endif
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.gridLayout_2 = QGridLayout()
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.gridLayout_2.setHorizontalSpacing(14)
        self.gridLayout_2.setVerticalSpacing(13)
        self.gridLayout_2.setContentsMargins(-1, 8, 0, -1)
        self.msg_button = QPushButton(self.groupBox)
        self.msg_button.setObjectName(u"msg_button")
        self.msg_button.setMaximumSize(QSize(150, 16777215))

        self.gridLayout_2.addWidget(self.msg_button, 3, 1, 1, 1)

        self.send_msg_text = QPlainTextEdit(self.groupBox)
        self.send_msg_text.setObjectName(u"send_msg_text")

        self.gridLayout_2.addWidget(self.send_msg_text, 2, 1, 1, 1)

        self.label_3 = QLabel(self.groupBox)
        self.label_3.setObjectName(u"label_3")

        self.gridLayout_2.addWidget(self.label_3, 2, 0, 1, 1)

        self.label_4 = QLabel(self.groupBox)
        self.label_4.setObjectName(u"label_4")

        self.gridLayout_2.addWidget(self.label_4, 0, 0, 1, 1)

        self.send_wxid = QLineEdit(self.groupBox)
        self.send_wxid.setObjectName(u"send_wxid")

        self.gridLayout_2.addWidget(self.send_wxid, 0, 1, 1, 1)


        self.verticalLayout_5.addLayout(self.gridLayout_2)


        self.horizontalLayout_4.addWidget(self.groupBox)


        self.verticalLayout_3.addLayout(self.horizontalLayout_4)


        self.verticalLayout_2.addWidget(self.frame)

        self.label = QLabel(self.verticalFrame)
        self.label.setObjectName(u"label")
        sizePolicy = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label.sizePolicy().hasHeightForWidth())
        self.label.setSizePolicy(sizePolicy)

        self.verticalLayout_2.addWidget(self.label)

        self.console_text = QPlainTextEdit(self.verticalFrame)
        self.console_text.setObjectName(u"console_text")

        self.verticalLayout_2.addWidget(self.console_text)

        self.verticalLayout_2.setStretch(0, 65)
        self.verticalLayout_2.setStretch(1, 1)
        self.verticalLayout_2.setStretch(2, 35)

        self.verticalLayout.addWidget(self.verticalFrame)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"wechat-hook", None))
        self.groupBox_0.setTitle(QCoreApplication.translate("MainWindow", u"\u542f\u52a8", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"ws\u76d1\u542c\u7aef\u53e3", None))
        self.label_5.setText(QCoreApplication.translate("MainWindow", u"ws token", None))
        self.ws_port.setText(QCoreApplication.translate("MainWindow", u"12725", None))
        self.ws_token.setText(QCoreApplication.translate("MainWindow", u"auth123", None))
        self.start_button.setText(QCoreApplication.translate("MainWindow", u"\u542f\u52a8\u670d\u52a1", None))
        self.ws_path.setText(QCoreApplication.translate("MainWindow", u"/", None))
        self.label_6.setText(QCoreApplication.translate("MainWindow", u"ws path", None))
        self.groupBox.setTitle(QCoreApplication.translate("MainWindow", u"\u6d88\u606f", None))
        self.msg_button.setText(QCoreApplication.translate("MainWindow", u"\u53d1\u9001\u6d88\u606f", None))
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"\u53d1\u9001\u4ebawxid", None))
        self.label_4.setText(QCoreApplication.translate("MainWindow", u"\u53d1\u9001\u5185\u5bb9", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"\u65e5\u5fd7\u8f93\u51fa", None))
    # retranslateUi

