import serial 
import time
import math

#arduino = serial.Serial(port='COM4', baudrate=115200, timeout = .1)
arduino = serial.Serial(port='/dev/ttyACM0', baudrate=115200, timeout = None)

def write_serial_arduino(command):

    address = math.floor(int(command) / 100)
    command_send =  int(command) % 100
    result = (address << 8) + command_send

    arduino.write(bytes(str(result), 'utf-8'))