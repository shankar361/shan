import streamlit as sl
import json
import requests
sl.write("My calculator App")
choice=sl.selectbox("Select the Operation",['Add','Subtract','Divide','Multiply'])

x=sl.slider("Take first value",0,100,5)
y=sl.slider("Take second value",0,100,5)
inputdataJson={"x":x,"y":y,"options":choice}
if sl.button("Calculate"):
    sl.write("The Result is:")
    res = requests.post(url="192.168.176.51:8001/calculate",data=json.dumps(inputdataJson))
    sl.subheader(res.text)
