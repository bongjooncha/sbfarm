import serial

ardu = serial.Serial(port='COM7', baudrate='9600',)


class ARD: 
    def ask(x):
        commend = x
        ardu.write(commend.encode())  #아두이노에게 보내는 언어 endoing

        if ardu.readable():
            answ = ardu.readline().decode()  #아두이노의 응답 decode
            print(answ)
    