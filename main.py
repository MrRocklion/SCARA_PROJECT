###########################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QFrame, QGridLayout, QHBoxLayout,
    QLabel, QMainWindow, QPushButton, QSizePolicy,
    QSlider, QSpacerItem, QStackedWidget, QVBoxLayout,
    QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(921, 600)
        MainWindow.setStyleSheet(u"#Container{\n"
"	background-color: #DADADA ;\n"
"\n"
"}\n"
"#barTitle{\n"
"background-color: rgb(72, 138, 153);\n"
"}\n"
"#Menu{\n"
"background-color: rgb(236, 240, 241);\n"
"border-radius:15px;\n"
"}\n"
"#Body{\n"
"background-color: rgb(236, 240, 241);\n"
"border-radius:15px;\n"
"}\n"
"QLabel{\n"
"font-family:Roboto;\n"
"}\n"
"#titulo{\n"
" 	color: rgb(236, 240, 241);\n"
"	font-size: 19px;\n"
"	font-weight: bold;\n"
"}\n"
"\n"
"\n"
"\n"
"\n"
"")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.verticalLayout = QVBoxLayout(self.centralwidget)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.Container = QFrame(self.centralwidget)
        self.Container.setObjectName(u"Container")
        self.Container.setFrameShape(QFrame.StyledPanel)
        self.Container.setFrameShadow(QFrame.Raised)
        self.verticalLayout_2 = QVBoxLayout(self.Container)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.barTitle = QFrame(self.Container)
        self.barTitle.setObjectName(u"barTitle")
        self.barTitle.setMaximumSize(QSize(16777215, 60))
        self.barTitle.setFrameShape(QFrame.StyledPanel)
        self.barTitle.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_2 = QHBoxLayout(self.barTitle)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.Home = QFrame(self.barTitle)
        self.Home.setObjectName(u"Home")
        self.Home.setMaximumSize(QSize(150, 16777215))
        self.Home.setFrameShape(QFrame.StyledPanel)
        self.Home.setFrameShadow(QFrame.Raised)
        self.verticalLayout_3 = QVBoxLayout(self.Home)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.pushButton = QPushButton(self.Home)
        self.pushButton.setObjectName(u"pushButton")

        self.verticalLayout_3.addWidget(self.pushButton)


        self.horizontalLayout_2.addWidget(self.Home)

        self.Title = QFrame(self.barTitle)
        self.Title.setObjectName(u"Title")
        self.Title.setFrameShape(QFrame.StyledPanel)
        self.Title.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_4 = QHBoxLayout(self.Title)
        self.horizontalLayout_4.setSpacing(0)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.horizontalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.titulo = QLabel(self.Title)
        self.titulo.setObjectName(u"titulo")
        self.titulo.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_4.addWidget(self.titulo)


        self.horizontalLayout_2.addWidget(self.Title)


        self.verticalLayout_2.addWidget(self.barTitle)

        self.frame_2 = QFrame(self.Container)
        self.frame_2.setObjectName(u"frame_2")
        self.frame_2.setFrameShape(QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QFrame.Raised)
        self.horizontalLayout = QHBoxLayout(self.frame_2)
        self.horizontalLayout.setSpacing(20)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.Menu = QFrame(self.frame_2)
        self.Menu.setObjectName(u"Menu")
        self.Menu.setMaximumSize(QSize(150, 16777215))
        self.Menu.setFrameShape(QFrame.StyledPanel)
        self.Menu.setFrameShadow(QFrame.Raised)
        self.verticalLayout_4 = QVBoxLayout(self.Menu)
        self.verticalLayout_4.setSpacing(0)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.verticalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.frame_3 = QFrame(self.Menu)
        self.frame_3.setObjectName(u"frame_3")
        self.frame_3.setFrameShape(QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QFrame.Raised)
        self.verticalLayout_7 = QVBoxLayout(self.frame_3)
        self.verticalLayout_7.setObjectName(u"verticalLayout_7")
        self.pushButton_4 = QPushButton(self.frame_3)
        self.pushButton_4.setObjectName(u"pushButton_4")

        self.verticalLayout_7.addWidget(self.pushButton_4)

        self.pushButton_5 = QPushButton(self.frame_3)
        self.pushButton_5.setObjectName(u"pushButton_5")

        self.verticalLayout_7.addWidget(self.pushButton_5)

        self.pushButton_2 = QPushButton(self.frame_3)
        self.pushButton_2.setObjectName(u"pushButton_2")

        self.verticalLayout_7.addWidget(self.pushButton_2)

        self.pushButton_3 = QPushButton(self.frame_3)
        self.pushButton_3.setObjectName(u"pushButton_3")

        self.verticalLayout_7.addWidget(self.pushButton_3)


        self.verticalLayout_4.addWidget(self.frame_3, 0, Qt.AlignTop)


        self.horizontalLayout.addWidget(self.Menu)

        self.Body = QFrame(self.frame_2)
        self.Body.setObjectName(u"Body")
        self.Body.setFrameShape(QFrame.StyledPanel)
        self.Body.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_3 = QHBoxLayout(self.Body)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.stackedWidget = QStackedWidget(self.Body)
        self.stackedWidget.setObjectName(u"stackedWidget")
        self.page1 = QWidget()
        self.page1.setObjectName(u"page1")
        self.horizontalLayout_5 = QHBoxLayout(self.page1)
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.frame = QFrame(self.page1)
        self.frame.setObjectName(u"frame")
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.verticalLayout_5 = QVBoxLayout(self.frame)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.controls = QGridLayout()
        self.controls.setObjectName(u"controls")
        self.label_4 = QLabel(self.frame)
        self.label_4.setObjectName(u"label_4")

        self.controls.addWidget(self.label_4, 3, 0, 1, 1)

        self.horizontalSlider = QSlider(self.frame)
        self.horizontalSlider.setObjectName(u"horizontalSlider")
        self.horizontalSlider.setOrientation(Qt.Horizontal)

        self.controls.addWidget(self.horizontalSlider, 2, 0, 1, 1)

        self.horizontalSlider_3 = QSlider(self.frame)
        self.horizontalSlider_3.setObjectName(u"horizontalSlider_3")
        self.horizontalSlider_3.setOrientation(Qt.Horizontal)

        self.controls.addWidget(self.horizontalSlider_3, 6, 0, 1, 1)

        self.label_5 = QLabel(self.frame)
        self.label_5.setObjectName(u"label_5")

        self.controls.addWidget(self.label_5, 5, 0, 1, 1)

        self.label_2 = QLabel(self.frame)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setAlignment(Qt.AlignCenter)

        self.controls.addWidget(self.label_2, 0, 0, 1, 1)

        self.label_6 = QLabel(self.frame)
        self.label_6.setObjectName(u"label_6")

        self.controls.addWidget(self.label_6, 7, 0, 1, 1)

        self.horizontalSlider_2 = QSlider(self.frame)
        self.horizontalSlider_2.setObjectName(u"horizontalSlider_2")
        self.horizontalSlider_2.setOrientation(Qt.Horizontal)

        self.controls.addWidget(self.horizontalSlider_2, 4, 0, 1, 1)

        self.label_3 = QLabel(self.frame)
        self.label_3.setObjectName(u"label_3")

        self.controls.addWidget(self.label_3, 1, 0, 1, 1)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.controls.addItem(self.verticalSpacer, 8, 0, 1, 1)


        self.verticalLayout_5.addLayout(self.controls)


        self.horizontalLayout_5.addWidget(self.frame)

        self.frame_4 = QFrame(self.page1)
        self.frame_4.setObjectName(u"frame_4")
        self.frame_4.setMinimumSize(QSize(344, 0))
        self.frame_4.setFrameShape(QFrame.StyledPanel)
        self.frame_4.setFrameShadow(QFrame.Raised)
        self.verticalLayout_6 = QVBoxLayout(self.frame_4)
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.info = QGridLayout()
        self.info.setObjectName(u"info")

        self.verticalLayout_6.addLayout(self.info)


        self.horizontalLayout_5.addWidget(self.frame_4)

        self.stackedWidget.addWidget(self.page1)
        self.page_2 = QWidget()
        self.page_2.setObjectName(u"page_2")
        self.stackedWidget.addWidget(self.page_2)

        self.horizontalLayout_3.addWidget(self.stackedWidget)


        self.horizontalLayout.addWidget(self.Body)


        self.verticalLayout_2.addWidget(self.frame_2)


        self.verticalLayout.addWidget(self.Container)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.pushButton.setText(QCoreApplication.translate("MainWindow", u"PushButton", None))
        self.titulo.setText(QCoreApplication.translate("MainWindow", u"Panel de control Robot Scara", None))
        self.pushButton_4.setText(QCoreApplication.translate("MainWindow", u"PushButton", None))
        self.pushButton_5.setText(QCoreApplication.translate("MainWindow", u"PushButton", None))
        self.pushButton_2.setText(QCoreApplication.translate("MainWindow", u"PushButton", None))
        self.pushButton_3.setText(QCoreApplication.translate("MainWindow", u"PushButton", None))
        self.label_4.setText(QCoreApplication.translate("MainWindow", u"Eslabon1", None))
        self.label_5.setText(QCoreApplication.translate("MainWindow", u"Eslabon 2", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"Panel de Control", None))
        self.label_6.setText(QCoreApplication.translate("MainWindow", u"Actuador Final", None))
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"Base", None))
    # retranslateUi

