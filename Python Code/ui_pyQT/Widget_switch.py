# =============================================================================
# Created By  : Anton Sundqvist
# Created Date: 2021-03-17
# =============================================================================
""""""
# =============================================================================
# Imports
from LedIndicatorWidget import *
from PyQt5.QtWidgets import QWidget, QPushButton, QVBoxLayout, QHBoxLayout, QLabel
from PyQt5.QtGui import *
from serial_com import write_serial
# =============================================================================

class TrainSwitch(QWidget):
    def __init__(self, parent, train_switch, command_routing):
        super(QWidget, self).__init__(parent)
        self.command_routing = command_routing
        self.train_switch = train_switch
        self.layout = QHBoxLayout()
        self.button = QPushButton()
        self.led = LedIndicator()
        self.button.setCheckable(True)
        self.button.setText("Växel " + train_switch)
        self.button.setStyleSheet(  "background-color: grey;" 
                                    "border-style: outset;"
                                    "border-width: 2px;"
                                    "border-radius: 10px;"
                                    "border-color: beige;"
                                    "font: bold 20px;"
                                    "min-width: 6em;"
                                    "min-height: 2.5em;"
                                    "padding: 2px;")


        self.led.setDisabled(True)  # Make the led non clickable

        self.led.on_color_1 = QColor(255, 0, 0)
        self.led.on_color_2 = QColor(176, 0, 0)
        self.led.off_color_1 = QColor(0, 255, 0)
        self.led.off_color_2 = QColor(0, 192, 0)

        self.layout.addWidget(self.button)
        self.layout.addWidget(self.led)

        self.button.clicked.connect(lambda: self.button_clicked())

    def button_clicked(self):
        self.led.setChecked(not self.led.isChecked())

        if self.button.isChecked(): 
            write_serial(self.command_routing + "1")
            #write_i2c_arduino(self.command_routing + "1")
        # if it is unchecked 
        else: 
            write_serial(self.command_routing + "2")
            #write_i2c_arduino(self.command_routing + "2")

class quitApp(QWidget):
    def __init__(self, parent):
        super(QWidget, self).__init__(parent)
        self.layout = QHBoxLayout()
        self.button = QPushButton()
        self.button.setCheckable(True)
        self.button.setText("Exit Application")

        self.layout.addWidget(self.button)
        self.button.clicked.connect(lambda: self.button_clicked())

    def button_clicked(self):
        QCoreApplication.quit()


class windowLayout(QWidget):
    def __init__(self, parent):
        super(QWidget, self).__init__(parent)

        self.MapLayout = QHBoxLayout()
        self.ButtonLayout = QGridLayout()
        self.ButtonLayout.setAlignment(Qt.AlignLeft)

        self.button_1 = TrainSwitch(self, "1", "11")
        self.button_2 = TrainSwitch(self, "2", "12")
        self.button_3 = TrainSwitch(self, "3", "13")
        self.button_4 = TrainSwitch(self, "4", "14")
        self.button_5 = TrainSwitch(self, "5", "15")
        self.button_6 = TrainSwitch(self, "6", "16")
        self.button_7 = TrainSwitch(self, "7", "17")
        self.button_8 = TrainSwitch(self, "8", "21")
        self.button_9 = TrainSwitch(self, "9", "22")
        self.button_10 = TrainSwitch(self, "10", "23")
        self.button_11 = TrainSwitch(self, "11", "24")
        self.button_12 = TrainSwitch(self, "12", "25")
        self.button_13 = TrainSwitch(self, "13", "26")
        self.button_14 = TrainSwitch(self, "14", "27")
        self.button_15 = TrainSwitch(self, "15", "31")
        self.button_16 = TrainSwitch(self, "16", "32")
        self.button_17 = TrainSwitch(self, "17", "33")
        self.button_18 = TrainSwitch(self, "18", "34")
        self.button_19 = TrainSwitch(self, "19", "35")

        self.button_20 = quitApp(self)

        self.ButtonLayout.addLayout(self.button_1.layout, 1, 0)        
        self.ButtonLayout.addLayout(self.button_2.layout, 1, 1)       
        self.ButtonLayout.addLayout(self.button_3.layout, 1, 2)
        self.ButtonLayout.addLayout(self.button_4.layout, 1, 3)
        self.ButtonLayout.addLayout(self.button_5.layout, 2, 0) 
        self.ButtonLayout.addLayout(self.button_6.layout, 2, 1) 
        self.ButtonLayout.addLayout(self.button_7.layout, 2, 2) 
        self.ButtonLayout.addLayout(self.button_8.layout, 2, 3) 
        self.ButtonLayout.addLayout(self.button_9.layout, 3, 0) 
        self.ButtonLayout.addLayout(self.button_10.layout, 3, 1) 
        self.ButtonLayout.addLayout(self.button_11.layout, 3, 2) 
        self.ButtonLayout.addLayout(self.button_12.layout, 3, 3) 
        self.ButtonLayout.addLayout(self.button_13.layout, 4, 0) 
        self.ButtonLayout.addLayout(self.button_14.layout, 4, 1) 
        self.ButtonLayout.addLayout(self.button_15.layout, 4, 2) 
        self.ButtonLayout.addLayout(self.button_16.layout, 4, 3) 
        self.ButtonLayout.addLayout(self.button_17.layout, 5, 0) 
        self.ButtonLayout.addLayout(self.button_18.layout, 5, 1) 
        self.ButtonLayout.addLayout(self.button_19.layout, 5, 2) 
        self.ButtonLayout.addLayout(self.button_20.layout, 5, 3) 


        self.MapLayout.addLayout(self.ButtonLayout)
        self.setLayout(self.MapLayout)        
