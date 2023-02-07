#%%
import streamlit as st
import math
# %%
st.header('คำนวณหาจำนวนแผ่นที่ต้องใช้')
input1, input2 = st.columns(2)
with input1:
    width = st.number_input('ความกว้าง (เมตร)')
with input2:
    height = st.number_input('ความสูง (เมตร)')
panel = math.ceil(width * height * 4)

st.subheader('จำนวนแผ่นที่ต้องใช้ : ' + str(panel) + ' แผ่น')