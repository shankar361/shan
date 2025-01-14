import streamlit as st
def currencyConverter(curr1:str,curr2:str):
    if curr1=="Dollar" and curr2=="Ruppee":
        value = 80
        return value
    elif curr1==curr2:
        return 1
    elif curr2=="Dollar" and curr1=="Ruppee":
        value = 1/80
        return value

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

columns = st.columns([1,1])
with columns[0]:
    st.header("Shankar's Calculator")
    choice = st.selectbox("Select an operation",['Add','Subtract','Multiply','Divide'],)
    x = st.number_input("Enter first value")
    y = st.number_input("Enter second value")

    if st.button("Calculate"): 
        res = calcualate(x,y,choice)
        st.subheader(res)
with columns[1]:
    st.header("Shankar's Converter")
    curr1=st.selectbox("Select from currency",['Dollar','Won','Ruppee'])
    curr2=st.selectbox("Select to currency",['Dollar','Won','Ruppee'])
    if st.button("Convert"): 
        val=currencyConverter(curr1,curr2)
        st.subheader("1 "+curr1+" = "+str(val)+" "+curr2)
