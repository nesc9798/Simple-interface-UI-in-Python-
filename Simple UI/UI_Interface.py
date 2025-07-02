# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'UI_Interface.ui'
##
## Created by: Qt User Interface Compiler version 6.9.0
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
from PySide6.QtWidgets import (QApplication, QFrame, QHBoxLayout, QLabel,
    QLineEdit, QMainWindow, QPushButton, QSizePolicy,
    QStackedWidget, QVBoxLayout, QWidget)
import icons_rc

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(1037, 604)
        self.stylesheet = QWidget(MainWindow)
        self.stylesheet.setObjectName(u"stylesheet")
        self.stylesheet.setStyleSheet(u"QWidget {\n"
"    background-color: #282a36;\n"
"    color: #f8f8f2;\n"
"    font-family: \"Segoe UI\", Arial, sans-serif;\n"
"    font-size: 12pt;\n"
"	selection-color:white;\n"
"	border:none;\n"
"	border-radius: 1px;\n"
"}\n"
"QPushButton {\n"
"    background-color: #6272a4;\n"
"    color: #f8f8f2;\n"
"    border: 1px solid #44475a;\n"
"    border-radius: 4px;\n"
"    padding: 5px;\n"
"    min-width: 80px;\n"
"}")
        self.horizontalLayout = QHBoxLayout(self.stylesheet)
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.SIDE_MENU_CONTAINER = QFrame(self.stylesheet)
        self.SIDE_MENU_CONTAINER.setObjectName(u"SIDE_MENU_CONTAINER")
        self.SIDE_MENU_CONTAINER.setMinimumSize(QSize(0, 0))
        self.SIDE_MENU_CONTAINER.setMaximumSize(QSize(0, 16777215))
        self.SIDE_MENU_CONTAINER.setFrameShape(QFrame.StyledPanel)
        self.SIDE_MENU_CONTAINER.setFrameShadow(QFrame.Raised)
        self.verticalLayout = QVBoxLayout(self.SIDE_MENU_CONTAINER)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.side_menu = QFrame(self.SIDE_MENU_CONTAINER)
        self.side_menu.setObjectName(u"side_menu")
        self.side_menu.setMinimumSize(QSize(200, 0))
        self.side_menu.setMaximumSize(QSize(200, 16777215))
        self.side_menu.setFrameShape(QFrame.StyledPanel)
        self.side_menu.setFrameShadow(QFrame.Raised)
        self.verticalLayout_2 = QVBoxLayout(self.side_menu)
        self.verticalLayout_2.setSpacing(0)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.header_menu = QFrame(self.side_menu)
        self.header_menu.setObjectName(u"header_menu")
        self.header_menu.setFrameShape(QFrame.StyledPanel)
        self.header_menu.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_2 = QHBoxLayout(self.header_menu)
        self.horizontalLayout_2.setSpacing(0)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.label = QLabel(self.header_menu)
        self.label.setObjectName(u"label")
        self.label.setStyleSheet(u"font-size:20px;")

        self.horizontalLayout_2.addWidget(self.label, 0, Qt.AlignLeft|Qt.AlignTop)

        self.label_2 = QLabel(self.header_menu)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setStyleSheet(u"font-size:20px;")

        self.horizontalLayout_2.addWidget(self.label_2, 0, Qt.AlignLeft|Qt.AlignTop)


        self.verticalLayout_2.addWidget(self.header_menu, 0, Qt.AlignTop)

        self.menus_menu = QFrame(self.side_menu)
        self.menus_menu.setObjectName(u"menus_menu")
        self.menus_menu.setFrameShape(QFrame.StyledPanel)
        self.menus_menu.setFrameShadow(QFrame.Raised)
        self.verticalLayout_3 = QVBoxLayout(self.menus_menu)
        self.verticalLayout_3.setSpacing(0)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.interface_btn = QPushButton(self.menus_menu)
        self.interface_btn.setObjectName(u"interface_btn")
        icon = QIcon()
        icon.addFile(u":/icons/box.svg", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.interface_btn.setIcon(icon)

        self.verticalLayout_3.addWidget(self.interface_btn)

        self.pushButton_3 = QPushButton(self.menus_menu)
        self.pushButton_3.setObjectName(u"pushButton_3")

        self.verticalLayout_3.addWidget(self.pushButton_3)

        self.settings_btn = QPushButton(self.menus_menu)
        self.settings_btn.setObjectName(u"settings_btn")
        icon1 = QIcon()
        icon1.addFile(u":/icons/settings.svg", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.settings_btn.setIcon(icon1)

        self.verticalLayout_3.addWidget(self.settings_btn)

        self.about_btn = QPushButton(self.menus_menu)
        self.about_btn.setObjectName(u"about_btn")
        icon2 = QIcon()
        icon2.addFile(u":/icons/github.svg", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.about_btn.setIcon(icon2)

        self.verticalLayout_3.addWidget(self.about_btn)


        self.verticalLayout_2.addWidget(self.menus_menu)

        self.rooter_menu = QFrame(self.side_menu)
        self.rooter_menu.setObjectName(u"rooter_menu")
        self.rooter_menu.setFrameShape(QFrame.StyledPanel)
        self.rooter_menu.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_3 = QHBoxLayout(self.rooter_menu)
        self.horizontalLayout_3.setSpacing(0)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.horizontalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.exit_side_menu_btn = QPushButton(self.rooter_menu)
        self.exit_side_menu_btn.setObjectName(u"exit_side_menu_btn")

        self.horizontalLayout_3.addWidget(self.exit_side_menu_btn, 0, Qt.AlignLeft)


        self.verticalLayout_2.addWidget(self.rooter_menu, 0, Qt.AlignBottom)


        self.verticalLayout.addWidget(self.side_menu)


        self.horizontalLayout.addWidget(self.SIDE_MENU_CONTAINER, 0, Qt.AlignLeft)

        self.BODY = QFrame(self.stylesheet)
        self.BODY.setObjectName(u"BODY")
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.BODY.sizePolicy().hasHeightForWidth())
        self.BODY.setSizePolicy(sizePolicy)
        self.BODY.setFrameShape(QFrame.StyledPanel)
        self.BODY.setFrameShadow(QFrame.Raised)
        self.verticalLayout_4 = QVBoxLayout(self.BODY)
        self.verticalLayout_4.setSpacing(0)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.verticalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.header = QFrame(self.BODY)
        self.header.setObjectName(u"header")
        self.header.setFrameShape(QFrame.StyledPanel)
        self.header.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_4 = QHBoxLayout(self.header)
        self.horizontalLayout_4.setSpacing(0)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.horizontalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.frame_4 = QFrame(self.header)
        self.frame_4.setObjectName(u"frame_4")
        self.frame_4.setFrameShape(QFrame.StyledPanel)
        self.frame_4.setFrameShadow(QFrame.Raised)
        self.verticalLayout_6 = QVBoxLayout(self.frame_4)
        self.verticalLayout_6.setSpacing(0)
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.verticalLayout_6.setContentsMargins(0, 0, 0, 0)
        self.size_menu_btn = QPushButton(self.frame_4)
        self.size_menu_btn.setObjectName(u"size_menu_btn")
        icon3 = QIcon()
        icon3.addFile(u":/icons/align-justify(2).svg", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.size_menu_btn.setIcon(icon3)
        self.size_menu_btn.setIconSize(QSize(32, 32))

        self.verticalLayout_6.addWidget(self.size_menu_btn)


        self.horizontalLayout_4.addWidget(self.frame_4, 0, Qt.AlignLeft|Qt.AlignTop)

        self.search = QFrame(self.header)
        self.search.setObjectName(u"search")
        self.search.setFrameShape(QFrame.StyledPanel)
        self.search.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_7 = QHBoxLayout(self.search)
        self.horizontalLayout_7.setSpacing(0)
        self.horizontalLayout_7.setObjectName(u"horizontalLayout_7")
        self.horizontalLayout_7.setContentsMargins(5, 0, 5, 0)
        self.lineEdit = QLineEdit(self.search)
        self.lineEdit.setObjectName(u"lineEdit")
        self.lineEdit.setMinimumSize(QSize(135, 0))
        font = QFont()
        font.setFamilies([u"Segoe UI,Arial,sans-serif"])
        font.setPointSize(12)
        self.lineEdit.setFont(font)

        self.horizontalLayout_7.addWidget(self.lineEdit, 0, Qt.AlignLeft)

        self.pushButton_11 = QPushButton(self.search)
        self.pushButton_11.setObjectName(u"pushButton_11")
        icon4 = QIcon()
        icon4.addFile(u":/icons/search.svg", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.pushButton_11.setIcon(icon4)

        self.horizontalLayout_7.addWidget(self.pushButton_11, 0, Qt.AlignLeft)


        self.horizontalLayout_4.addWidget(self.search, 0, Qt.AlignLeft|Qt.AlignTop)

        self.frame_3 = QFrame(self.header)
        self.frame_3.setObjectName(u"frame_3")
        self.frame_3.setFrameShape(QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_6 = QHBoxLayout(self.frame_3)
        self.horizontalLayout_6.setSpacing(0)
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.horizontalLayout_6.setContentsMargins(5, 0, 5, 0)
        self.pushButton_10 = QPushButton(self.frame_3)
        self.pushButton_10.setObjectName(u"pushButton_10")
        icon5 = QIcon()
        icon5.addFile(u":/icons/user(1).svg", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.pushButton_10.setIcon(icon5)

        self.horizontalLayout_6.addWidget(self.pushButton_10)

        self.pushButton_9 = QPushButton(self.frame_3)
        self.pushButton_9.setObjectName(u"pushButton_9")
        icon6 = QIcon()
        icon6.addFile(u":/icons/archive.svg", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.pushButton_9.setIcon(icon6)

        self.horizontalLayout_6.addWidget(self.pushButton_9)


        self.horizontalLayout_4.addWidget(self.frame_3, 0, Qt.AlignHCenter|Qt.AlignTop)

        self.frame_2 = QFrame(self.header)
        self.frame_2.setObjectName(u"frame_2")
        self.frame_2.setFrameShape(QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_5 = QHBoxLayout(self.frame_2)
        self.horizontalLayout_5.setSpacing(0)
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.horizontalLayout_5.setContentsMargins(5, 0, 5, 0)
        self.minin_window = QPushButton(self.frame_2)
        self.minin_window.setObjectName(u"minin_window")
        icon7 = QIcon()
        icon7.addFile(u":/icons/arrow-down-left.svg", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.minin_window.setIcon(icon7)

        self.horizontalLayout_5.addWidget(self.minin_window)

        self.max_window = QPushButton(self.frame_2)
        self.max_window.setObjectName(u"max_window")
        icon8 = QIcon()
        icon8.addFile(u":/icons/maximize-2.svg", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.max_window.setIcon(icon8)

        self.horizontalLayout_5.addWidget(self.max_window)

        self.exit_window = QPushButton(self.frame_2)
        self.exit_window.setObjectName(u"exit_window")
        icon9 = QIcon()
        icon9.addFile(u":/icons/x(1).svg", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.exit_window.setIcon(icon9)

        self.horizontalLayout_5.addWidget(self.exit_window)


        self.horizontalLayout_4.addWidget(self.frame_2, 0, Qt.AlignLeft|Qt.AlignTop)


        self.verticalLayout_4.addWidget(self.header)

        self.stackedWidget = QStackedWidget(self.BODY)
        self.stackedWidget.setObjectName(u"stackedWidget")
        self.NEXT_PG = QWidget()
        self.NEXT_PG.setObjectName(u"NEXT_PG")
        self.verticalLayout_10 = QVBoxLayout(self.NEXT_PG)
        self.verticalLayout_10.setObjectName(u"verticalLayout_10")
        self.frame = QFrame(self.NEXT_PG)
        self.frame.setObjectName(u"frame")
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.verticalLayout_11 = QVBoxLayout(self.frame)
        self.verticalLayout_11.setObjectName(u"verticalLayout_11")
        self.label_6 = QLabel(self.frame)
        self.label_6.setObjectName(u"label_6")
        self.label_6.setStyleSheet(u"font-size: 40px;")

        self.verticalLayout_11.addWidget(self.label_6, 0, Qt.AlignHCenter)


        self.verticalLayout_10.addWidget(self.frame)

        self.stackedWidget.addWidget(self.NEXT_PG)
        self.ABOUT_PG = QWidget()
        self.ABOUT_PG.setObjectName(u"ABOUT_PG")
        self.verticalLayout_12 = QVBoxLayout(self.ABOUT_PG)
        self.verticalLayout_12.setObjectName(u"verticalLayout_12")
        self.frame_5 = QFrame(self.ABOUT_PG)
        self.frame_5.setObjectName(u"frame_5")
        self.frame_5.setFrameShape(QFrame.StyledPanel)
        self.frame_5.setFrameShadow(QFrame.Raised)
        self.verticalLayout_13 = QVBoxLayout(self.frame_5)
        self.verticalLayout_13.setObjectName(u"verticalLayout_13")
        self.frame_6 = QFrame(self.frame_5)
        self.frame_6.setObjectName(u"frame_6")
        self.frame_6.setFrameShape(QFrame.StyledPanel)
        self.frame_6.setFrameShadow(QFrame.Raised)
        self.verticalLayout_14 = QVBoxLayout(self.frame_6)
        self.verticalLayout_14.setSpacing(0)
        self.verticalLayout_14.setObjectName(u"verticalLayout_14")
        self.verticalLayout_14.setContentsMargins(0, 0, 0, 0)
        self.label_8 = QLabel(self.frame_6)
        self.label_8.setObjectName(u"label_8")
        self.label_8.setStyleSheet(u"color:rgb(255, 170, 0);\n"
"font-size: 20px;")

        self.verticalLayout_14.addWidget(self.label_8, 0, Qt.AlignHCenter|Qt.AlignBottom)

        self.label_7 = QLabel(self.frame_6)
        self.label_7.setObjectName(u"label_7")
        self.label_7.setStyleSheet(u"")

        self.verticalLayout_14.addWidget(self.label_7, 0, Qt.AlignHCenter|Qt.AlignBottom)


        self.verticalLayout_13.addWidget(self.frame_6)

        self.frame_7 = QFrame(self.frame_5)
        self.frame_7.setObjectName(u"frame_7")
        self.frame_7.setFrameShape(QFrame.StyledPanel)
        self.frame_7.setFrameShadow(QFrame.Raised)
        self.verticalLayout_15 = QVBoxLayout(self.frame_7)
        self.verticalLayout_15.setSpacing(0)
        self.verticalLayout_15.setObjectName(u"verticalLayout_15")
        self.verticalLayout_15.setContentsMargins(0, 0, -1, 0)
        self.label_9 = QLabel(self.frame_7)
        self.label_9.setObjectName(u"label_9")

        self.verticalLayout_15.addWidget(self.label_9, 0, Qt.AlignHCenter|Qt.AlignBottom)

        self.frame_8 = QFrame(self.frame_7)
        self.frame_8.setObjectName(u"frame_8")
        self.frame_8.setFrameShape(QFrame.StyledPanel)
        self.frame_8.setFrameShadow(QFrame.Raised)
        self.verticalLayout_16 = QVBoxLayout(self.frame_8)
        self.verticalLayout_16.setSpacing(0)
        self.verticalLayout_16.setObjectName(u"verticalLayout_16")
        self.verticalLayout_16.setContentsMargins(0, 0, 0, 0)
        self.label_10 = QLabel(self.frame_8)
        self.label_10.setObjectName(u"label_10")
        self.label_10.setStyleSheet(u"color:rgb(0, 255, 0)")

        self.verticalLayout_16.addWidget(self.label_10, 0, Qt.AlignHCenter|Qt.AlignTop)


        self.verticalLayout_15.addWidget(self.frame_8)


        self.verticalLayout_13.addWidget(self.frame_7)


        self.verticalLayout_12.addWidget(self.frame_5)

        self.stackedWidget.addWidget(self.ABOUT_PG)
        self.INTERFACE_PG = QWidget()
        self.INTERFACE_PG.setObjectName(u"INTERFACE_PG")
        self.verticalLayout_5 = QVBoxLayout(self.INTERFACE_PG)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.interface_main = QFrame(self.INTERFACE_PG)
        self.interface_main.setObjectName(u"interface_main")
        sizePolicy1 = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Expanding)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.interface_main.sizePolicy().hasHeightForWidth())
        self.interface_main.setSizePolicy(sizePolicy1)
        self.interface_main.setFrameShape(QFrame.StyledPanel)
        self.interface_main.setFrameShadow(QFrame.Raised)
        self.verticalLayout_9 = QVBoxLayout(self.interface_main)
        self.verticalLayout_9.setSpacing(0)
        self.verticalLayout_9.setObjectName(u"verticalLayout_9")
        self.verticalLayout_9.setContentsMargins(0, 0, 0, 0)
        self.label_3 = QLabel(self.interface_main)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setMinimumSize(QSize(10, 10))
        self.label_3.setBaseSize(QSize(0, 0))
        self.label_3.setPixmap(QPixmap(u":/icons/Captura_de_tela_2025-06-16_194120-removebg-preview.png"))

        self.verticalLayout_9.addWidget(self.label_3, 0, Qt.AlignHCenter|Qt.AlignBottom)

        self.label_5 = QLabel(self.interface_main)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setStyleSheet(u"font-size:40px;")

        self.verticalLayout_9.addWidget(self.label_5, 0, Qt.AlignHCenter|Qt.AlignTop)


        self.verticalLayout_5.addWidget(self.interface_main)

        self.FOOTER = QFrame(self.INTERFACE_PG)
        self.FOOTER.setObjectName(u"FOOTER")
        self.FOOTER.setFrameShape(QFrame.StyledPanel)
        self.FOOTER.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_8 = QHBoxLayout(self.FOOTER)
        self.horizontalLayout_8.setSpacing(0)
        self.horizontalLayout_8.setObjectName(u"horizontalLayout_8")
        self.horizontalLayout_8.setContentsMargins(0, 0, 0, 0)
        self.version = QFrame(self.FOOTER)
        self.version.setObjectName(u"version")
        self.version.setFrameShape(QFrame.StyledPanel)
        self.version.setFrameShadow(QFrame.Raised)
        self.verticalLayout_8 = QVBoxLayout(self.version)
        self.verticalLayout_8.setSpacing(0)
        self.verticalLayout_8.setObjectName(u"verticalLayout_8")
        self.verticalLayout_8.setContentsMargins(0, 0, 0, 0)
        self.label_4 = QLabel(self.version)
        self.label_4.setObjectName(u"label_4")

        self.verticalLayout_8.addWidget(self.label_4, 0, Qt.AlignBottom)


        self.horizontalLayout_8.addWidget(self.version, 0, Qt.AlignLeft)

        self.icon_bottom = QFrame(self.FOOTER)
        self.icon_bottom.setObjectName(u"icon_bottom")
        sizePolicy.setHeightForWidth(self.icon_bottom.sizePolicy().hasHeightForWidth())
        self.icon_bottom.setSizePolicy(sizePolicy)
        self.icon_bottom.setFrameShape(QFrame.StyledPanel)
        self.icon_bottom.setFrameShadow(QFrame.Raised)
        self.verticalLayout_7 = QVBoxLayout(self.icon_bottom)
        self.verticalLayout_7.setSpacing(0)
        self.verticalLayout_7.setObjectName(u"verticalLayout_7")
        self.verticalLayout_7.setContentsMargins(0, 0, 0, 0)
        self.pushButton_13 = QPushButton(self.icon_bottom)
        self.pushButton_13.setObjectName(u"pushButton_13")
        self.pushButton_13.setIcon(icon)

        self.verticalLayout_7.addWidget(self.pushButton_13, 0, Qt.AlignBottom)


        self.horizontalLayout_8.addWidget(self.icon_bottom)

        self.size_grip = QFrame(self.FOOTER)
        self.size_grip.setObjectName(u"size_grip")
        self.size_grip.setMinimumSize(QSize(10, 10))
        self.size_grip.setMaximumSize(QSize(10, 10))
        self.size_grip.setFrameShape(QFrame.StyledPanel)
        self.size_grip.setFrameShadow(QFrame.Raised)

        self.horizontalLayout_8.addWidget(self.size_grip, 0, Qt.AlignRight|Qt.AlignBottom)


        self.verticalLayout_5.addWidget(self.FOOTER, 0, Qt.AlignBottom)

        self.stackedWidget.addWidget(self.INTERFACE_PG)

        self.verticalLayout_4.addWidget(self.stackedWidget)


        self.horizontalLayout.addWidget(self.BODY)

        MainWindow.setCentralWidget(self.stylesheet)

        self.retranslateUi(MainWindow)

        self.stackedWidget.setCurrentIndex(2)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"LOGO", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"NAME", None))
        self.interface_btn.setText(QCoreApplication.translate("MainWindow", u"Interface", None))
        self.pushButton_3.setText(QCoreApplication.translate("MainWindow", u"PushButton", None))
        self.settings_btn.setText(QCoreApplication.translate("MainWindow", u"Settings", None))
        self.about_btn.setText(QCoreApplication.translate("MainWindow", u"About", None))
        self.exit_side_menu_btn.setText(QCoreApplication.translate("MainWindow", u"EXIT", None))
        self.size_menu_btn.setText("")
        self.lineEdit.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Search", None))
        self.pushButton_11.setText("")
        self.pushButton_10.setText("")
        self.pushButton_9.setText("")
        self.minin_window.setText("")
        self.max_window.setText("")
        self.exit_window.setText("")
        self.label_6.setText(QCoreApplication.translate("MainWindow", u"SETTINGS PAGE", None))
        self.label_8.setText(QCoreApplication.translate("MainWindow", u"Basic Interface", None))
        self.label_7.setText(QCoreApplication.translate("MainWindow", u"An interface created using Python and PySide (support for PyQt),\n"
"                    and with colors and theme created by NVKDev.\n"
"", None))
        self.label_9.setText(QCoreApplication.translate("MainWindow", u"MIT License", None))
        self.label_10.setText(QCoreApplication.translate("MainWindow", u"Create by: NVKDev", None))
        self.label_3.setText("")
        self.label_5.setText(QCoreApplication.translate("MainWindow", u"Interface", None))
        self.label_4.setText(QCoreApplication.translate("MainWindow", u"Version 0.1.0", None))
        self.pushButton_13.setText("")
    # retranslateUi

