import sys
import rc_icons
from PySide6.QtUiTools import QUiLoader
from PySide6.QtWidgets import QApplication,QButtonGroup,QLabel
from PySide6.QtCore import QFile, QIODevice, Qt
from CustomWidgetsPyhton.CustomSwitch import CSwitch

if __name__ == "__main__":
    app = QApplication(sys.argv)
    ui_file_name = "mainwindow.ui"
    ui_file = QFile(ui_file_name)
    if not ui_file.open(QIODevice.ReadOnly):
        print(f"Cannot open {ui_file_name}: {ui_file.errorString()}")
        sys.exit(-1)
    loader = QUiLoader()
    window = loader.load(ui_file)
    etiqueta = CSwitch(active_color="#17A589",)
    window.customBtn.addWidget(etiqueta,0,Qt.AlignLeft)
    window.op1.clicked.connect(lambda : window.stackedWidget.setCurrentWidget(window.page1))
    window.op2.clicked.connect(lambda : window.stackedWidget.setCurrentWidget(window.page2))
    window.op3.clicked.connect(lambda : window.stackedWidget.setCurrentWidget(window.page3))
    window.menuBtn.clicked.connect(lambda : window.stackedWidget.setCurrentWidget(window.page))
    window.salir.clicked.connect(lambda: window.close())
    ui_file.close()
    if not window:
        print(loader.errorString())
        sys.exit(-1)
    window.show()
    sys.exit(app.exec())