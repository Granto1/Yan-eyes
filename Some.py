import serial
import time


# port 'COM#', baudrate, timeout
arduino = serial.Serial(port = 'COM7', baudrate = 9600, timeout = 0.1)

def write_read(x):
    arduino.write(bytes(x, 'utf-8'))
    time.sleep(0.05)
    data = arduino.readline()
    return data
while True:
    ina = input("blah: ")
    value = write_read(ina)
    print(value)