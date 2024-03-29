import streamlit as st

st.write('# 스마트팜')
st.write('## 수위센서')
v = [100,150,30]
st.bar_chart(v)

x = st.slider('x')
st.write(x, 'squared is', x * x)

st.header('checkbox')
cb = st.checkbox('체크팍스')
if cb:
    st.write('체크')
else:
    st.write('아님')

st.header('button')
if st.button('버튼'):
    st.write('버튼 눌 림')
else:
    st.write('버 튼 눌림')