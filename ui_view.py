import sys
import rc_icons
from PySide6.QtUiTools import QUiLoader
from PySide6.QtWidgets import QApplication,QButtonGroup,QLabel
from PySide6.QtCore import QFile, QIODevice, Qt
from CustomWidgetsPyhton.CustomSwitch import CSwitch
import serial
pos_s1 = 0
pos_s2 = 0
pos_s3 = 0
status = False
def setS1(angle):
    pos_s1=angle
    window.s1.setText(str(pos_s1))
def setS2(angle):
    pos_s2=angle
    window.s2.setText(str(pos_s2))
def setS3(angle):
    pos_s3 = angle
    window.s3.setText(str(angle))
def set_gripper(value):
    window.gripper.setText(str(value))
if __name__ == "__main__":
    app = QApplication(sys.argv)
    ui_file_name = "mainwindow.ui"
    ui_file = QFile(ui_file_name)
    if not ui_file.open(QIODevice.ReadOnly):
        print(f"Cannot open {ui_file_name}: {ui_file.errorString()}")
        sys.exit(-1)
    loader = QUiLoader()
    window = loader.load(ui_file)
    gripper = CSwitch(active_color="#17A589",)
    window.customBtn.addWidget(gripper,0,Qt.AlignLeft)
    window.op1.clicked.connect(lambda : window.stackedWidget.setCurrentWidget(window.page1))
    window.op2.clicked.connect(lambda : window.stackedWidget.setCurrentWidget(window.page2))
    window.op3.clicked.connect(lambda : window.stackedWidget.setCurrentWidget(window.page3))
    window.menuBtn.clicked.connect(lambda : window.stackedWidget.setCurrentWidget(window.page))
    window.servo1.sliderReleased.connect(lambda: setS1(window.servo1.value()))
    window.servo2.sliderReleased.connect(lambda: setS2(window.servo2.value()))
    window.servo3.sliderReleased.connect(lambda: setS3(window.servo3.value()))
    gripper.clicked.connect(lambda : set_gripper(gripper.isChecked()))
    window.salir.clicked.connect(lambda: window.close())
    ui_file.close()
    if not window:
        print(loader.errorString())
        sys.exit(-1)
    window.show()
    sys.exit(app.exec())