import serial
import time

sm = serial.Serial(port='COM5', baudrate=9600,)

while True:
    ard = sm.readline()
    print(ard[:len(ard)-1].decode())
    time.sleep(0.1)
    usr = input()
    sm.write(usr.encode())
    time.sleep(0.1)

