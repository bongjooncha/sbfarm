import serial

ardu = serial.Serial(port='COM7', baudrate='9600',)

while True:
    commend = input('a를 누르면 온습도 확인: ')
    ardu.write(commend.encode())  #아두이노에게 보내는 언어 endoing

    if ardu.readable():
        answ = ardu.readline().decode()  #아두이노의 응답 decode
        print(answ)
    