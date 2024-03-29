import serial

ard = serial.Serial("COM5",9600,)

a = ard.write(input("입력해줘").encode())

print(ard.readline().decode())