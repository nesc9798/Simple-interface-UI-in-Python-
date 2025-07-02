import sys
from PySide6.QtWidgets import (QApplication, QMainWindow, QStackedWidget, 
                              QGraphicsDropShadowEffect, QSizeGrip)
from PySide6.QtCore import QPropertyAnimation, QEasingCurve, Qt
from PySide6.QtGui import QColor, QIcon
import PySide6.QtCore as QtCore
import PySide6.QtGui as QtGui
#######################################################
from UI_Interface import Ui_MainWindow  # Import the generated UI class
from icons import icons_rc
#######################################################
#DATABASE
#######################################################

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow()  # Create an instance of the UI class
        self.ui.setupUi(self)
        #########################################################
        #* Window title and icon
        #########################################################
        #self.setWindowIcon(QIcon(":/icons/feather-archive.svg")) --> ICON
        self.setWindowTitle("My Application")
        ###########################################
        #*Flags
        ###########################################
        self.setWindowFlags(QtCore.Qt.FramelessWindowHint)
        self.setAttribute(QtCore.Qt.WA_TranslucentBackground)
        ###########################################
        #*Shadow Effect
        ############################################ 
        self.shadow = QGraphicsDropShadowEffect(self)
        self.shadow.setBlurRadius(50)
        self.shadow.setXOffset(0)
        self.shadow.setYOffset(0)
        self.shadow.setColor(QColor(0, 92, 157, 150))  
        self.ui.stylesheet.setGraphicsEffect(self.shadow)
        ##################################################
        #* Button Window Menu
        ###########################################
        self.ui.minin_window.clicked.connect(lambda: self.showMinimized())
        self.ui.exit_window.clicked.connect(lambda: self.close())
        #close the left side menu
        self.ui.exit_side_menu_btn.clicked.connect(lambda: self.slideLeftMenu())
        self.ui.max_window.clicked.connect(self.restore_or_maximize_window)
        ###########################################
        #*Handle header mouse events for window dragging
        ###########################################
        self.ui.header.mousePressEvent = self.headerMousePressEvent  
        self.ui.header.mouseMoveEvent = self.headerMouseMoveEvent  

        self.show()
        ###########################################
        QSizeGrip(self.ui.size_grip)
        ###########################################
        #*BUTTOM CONNECTIONS
        #########################################################
        self.ui.size_menu_btn.clicked.connect(lambda: self.slideLeftMenu())
        self.ui.settings_btn.clicked.connect(lambda: self.ui.stackedWidget.setCurrentWidget(self.ui.NEXT_PG))
        self.ui.interface_btn.clicked.connect(lambda: self.ui.stackedWidget.setCurrentWidget(self.ui.INTERFACE_PG))
        self.ui.about_btn.clicked.connect(lambda: self.ui.stackedWidget.setCurrentWidget(self.ui.ABOUT_PG))
        #############################################################
        #*FUNCTIONS
        #############################################################
    def headerMousePressEvent(self, event):
        self.clickPosition = event.globalPos()
        event.accept()

    def headerMouseMoveEvent(self, event):
        if not self.isMaximized():
            if event.buttons() == Qt.LeftButton:
                current_pos = self.pos()
                global_pos = event.globalPos()
                self.move(current_pos + global_pos - self.clickPosition)
                self.clickPosition = global_pos
                event.accept()

    def restore_or_maximize_window(self):
        if self.isMaximized():
            self.showNormal()
            self.ui.max_window.setIcon(QIcon(":/icons/maximize-2.svg"))
        else:
            self.showMaximized()
            self.ui.max_window.setIcon(QIcon(":/icons/minimize-2.svg"))

    def slideLeftMenu(self):
        current_width = self.ui.SIDE_MENU_CONTAINER.width()  
        new_width = 200 if current_width == 0 else 0
        
       
        self.animation = QPropertyAnimation(self.ui.SIDE_MENU_CONTAINER, b"minimumWidth")
        self.animation.setDuration(250)
        self.animation.setStartValue(current_width)
        self.animation.setEndValue(new_width)
        self.animation.setEasingCurve(QtCore.QEasingCurve.InOutQuart)
        self.animation.start()

        
############################################################################################
#
############################################################################################
if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())