from flask import Flask, jsonify
import serial

app = Flask(__name__)
arduino = serial.Serial('COM5', 9600,)  # 아두이노가 연결된 포트로 변경하세요.

@app.route("/getWaterLevel")
def get_water_level():
    arduino.write(b'a')
    water_level = arduino.readline().decode().strip()
    return jsonify({"waterLevel": water_level})

if __name__ == "__main__":
    app.run(debug=True)
