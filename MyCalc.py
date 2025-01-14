import streamlit as st
def calcualate(x:float,y:float,ops:str):
    match ops:
        case "Add":
            return x+y
        case "Subtract":
            return x-y
        case "Multiply":
            return x*y
        case "Divide":
            return x/y
        
choice = st.selectbox("Select an operation",['Add','Subtract','Multiply','Divide'])
x = st.number_input("Enter first value")
y = st.number_input("Enter second value")
res = calcualate(x,y,choice)
if st.button("Calculate"): 
    st.subheader(res)