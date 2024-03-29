import serial

def get_water_level():
    arduino = serial.Serial('COM5', 9600)  # 아두이노가 연결된 포트로 변경하세요.
    arduino.write(b'a')  # 아두이노에 "a"를 보내 수위 값을 요청합니다.
    water_level = arduino.readline().decode().strip()  # 아두이노로부터 읽은 값 디코딩
    arduino.close()
    return water_level
