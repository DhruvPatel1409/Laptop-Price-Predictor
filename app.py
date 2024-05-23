import streamlit as st
import pickle
import math
import numpy as np

df = pickle.load(open('df.pkl','rb'))
pipe = pickle.load(open('pipe.pkl','rb'))

st.title("💻 LAPTOP PRICE PREDICTOR")
st.header("Enter Laptop Details")

company = st.selectbox("Brand",df['Company'].unique())
type = st.selectbox("Type",df['TypeName'].unique())
ram = st.selectbox("RAM(in GB)",[2,4,6,8,12,16,24,32,64])
weight = st.number_input("Weight of Laptop")
touchscreen = st.selectbox("TouchScreen",['No','Yes'])
ips = st.selectbox("IPS",['No','Yes'])
screen_size = st.number_input('Screen Size')
resolution = st.selectbox("Resolution",['1920x1080','1366x768','1600x900','3840x2160','3200x1800','2880x1800','2560x1600','2560x1440','2304x1440'])
cpu = st.selectbox("CPU",df['Cpu Brand'].unique())
hdd = st.selectbox("HDD(in GB)",[0,128,256,512,1024,2048])
ssd = st.selectbox("SSD(in GB)",[0,8,128,256,512,1024])
gpu = st.selectbox('GPU',df['Gpu Brand'].unique())
os = st.selectbox('OS',df['os'].unique())

if st.button("PREDICT PRICE"):
   
    if touchscreen == 'Yes':
        touchscreen = 1
    else:
        touchscreen = 0
    
    if ips == 'Yes':
        ips = 1
    else:
        ips = 0

    X_res = int(resolution.split('x')[0])
    Y_res = int(resolution.split('x')[1])
    ppi = ((X_res**2) + (Y_res**2))**0.5 / screen_size

    query = np.array([company,type,ram,weight,touchscreen,ips,ppi,cpu,hdd,ssd,gpu,os])
    query = query.reshape(1,12)
    st.header("The predicted price of this laptop is " + str(math.floor(pipe.predict(query))) + " ₹")

st.markdown("---")
st.markdown("Made with 🤖 by Dhruv Patel")