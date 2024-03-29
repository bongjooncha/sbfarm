import streamlit as st
import serial

ardu = serial.Serial(port='COM5', baudrate=9600, parity=serial.PARITY_NONE,stopbits=serial.STOPBITS_ONE,bytesize=serial.EIGHTBITS)


st.write('# 스마트 팜')
st.write('# 수위센서')

if st.button('수위1'):
    try:
        ardu.open()
    except:
        pass
    ardu.write('h'.encode())
    if ardu.readable():
        answ = ardu.readline().decode()
        st.write(answ)
    else:
        print('읽기 실패')
    
ardu.close()