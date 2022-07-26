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
ser = serial.Serial()
def serial_enviar(data):
    print('dato enviado',data)
    ser.write(data.encode())
def serial_init():
    port = str(window.puerto.text()).upper()
    radio = group1.checkedButton()
    bau = 0
    parity = serial.PARITY_NONE
    val_parity = 'PARITY_NONE'
    if paridad.isChecked():
        parity = serial.PARITY_EVEN
        val_parity = 'PARITY_EVEN'
    else:
        parity = serial.PARITY_NONE
        val_parity = 'PARITY_NONE'
    if(port.strip() != '' and str(radio) != 'None'):
        if str(radio.objectName()) == 'baud1':
            bau = 9600
        if str(radio.objectName()) == 'baud2':
            bau = 19200
        if str(radio.objectName()) == 'baud3':
            bau = 115200
        try:
            ser.baudrate = bau
            ser.port = port
            ser.parity = parity
            window.estado_ser.setText("Conectado")
            window.velocidad_ser.setText(str(bau))
            window.com_ser.setText(str(port))
            window.parity_ser.setText(str(val_parity))
            ser.open()
            print("se conecto")
        except PermissionError:
            print("algo ocurrio mal")
            window.estado_ser.setText("Desconectado")
            window.velocidad_ser.setText(str('####'))
            window.com_ser.setText(str('0'))
            window.parity_ser.setText("PARITY_NONE")
    else:
        window.estado_ser.setText("Desconectado")
        print('empty')
def serial_desconectar():
    window.estado_ser.setText("Desconectado")
    window.velocidad_ser.setText(str('####'))
    window.com_ser.setText(str('0'))
    window.parity_ser.setText("PARITY_NONE")
    ser.close()
    print("se desconecto")
def enviarComando():
    cmd = window.lineComand.text()
    string = '{}\r\n'.format(cmd)
    print(cmd)
    ser.write(string.encode())
def setS1(angle):
    if angle <= 10:
        pos_s1 = 10
    else:
        pos_s1 = angle
    dato = f"1,{pos_s1}"
    window.s1.setText(str(pos_s1))
    serial_enviar(dato)
    print(dato)

def setS2(angle):
    if angle <= 10:
        pos_s2=10
    elif angle >= 150:
        pos_s2 = 150
    else:
        pos_s2 = angle
    dato = f"2,{pos_s2}"
    window.s2.setText(str(pos_s2))
    serial_enviar(dato)
    print(dato)

def homePosition():
    print('5')
    window.servo1.setValue(90)
    window.servo2.setValue(90)
    window.servo3.setValue(90)
    window.s2.setText(str(90))
    window.s1.setText(str(90))
    window.s3.setText(str(90))
    serial_enviar('5')

def setS3(angle):
    pos_s3 = angle
    dato = f"3,{pos_s3}"
    window.s3.setText(str(angle))
    serial_enviar(dato)
    print(dato)
def set_gripper(value):
    window.gripper.setText(str(value))
    if value == True:
        print('4,1')
        serial_enviar('4,1')
    if value == False:
        print('4,0')
        serial_enviar('4,0')
    else:
        pass
if __name__ == "__main__":
    app = QApplication(sys.argv)
    ui_file_name = "mainwindow.ui"
    ui_file = QFile(ui_file_name)
    if not ui_file.open(QIODevice.ReadOnly):
        print(f"Cannot open {ui_file_name}: {ui_file.errorString()}")
        sys.exit(-1)
    loader = QUiLoader()
    window = loader.load(ui_file)
    group1 = QButtonGroup()
    gripper = CSwitch(active_color="#17A589")
    paridad = CSwitch(active_color="#17A589", )
    window.customBtn.addWidget(gripper,0,Qt.AlignLeft)
    window.paridad_container.addWidget(paridad, 0, Qt.AlignLeft)
    window.op1.clicked.connect(lambda : window.stackedWidget.setCurrentWidget(window.page1))
    window.op2.clicked.connect(lambda : window.stackedWidget.setCurrentWidget(window.page2))
    window.menuBtn.clicked.connect(lambda : window.stackedWidget.setCurrentWidget(window.page))
    window.menuBtn.clicked.connect(lambda : window.stackedWidget.setCurrentWidget(window.page))

    window.servo1.sliderReleased.connect(lambda: setS1(window.servo1.value()))
    window.servo2.sliderReleased.connect(lambda: setS2(window.servo2.value()))
    window.servo3.sliderReleased.connect(lambda: setS3(window.servo3.value()))
    window.homeBtn.clicked.connect(lambda : homePosition())
    gripper.clicked.connect(lambda : set_gripper(gripper.isChecked()))
    window.salir.clicked.connect(lambda: window.close())
    window.conectar.clicked.connect(lambda: serial_init())
    window.desconectar.clicked.connect(lambda: serial_desconectar())
    group1.addButton(window.baud1)
    group1.addButton(window.baud2)
    group1.addButton(window.baud3)

    ui_file.close()
    if not window:
        print(loader.errorString())
        sys.exit(-1)
    window.show()
    sys.exit(app.exec())