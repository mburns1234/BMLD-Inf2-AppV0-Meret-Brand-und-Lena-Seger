import streamlit as st
from functions.addieren import add

st.title("Addition Calculator") 

st.write("Geben Sie zwei Zahlen ein, um ihre Summe zu berechnen.")

with st.form("addition_form"):
    number1 = st.number_input("Zahl 1", value=0)
    number2 = st.number_input("Zahl 2", value=0)
    submit_button = st.form_submit_button("Berechnen")
if submit_button:
    result = add(number1, number2)
    st.write(f"Die Summe von {number1} und {number2} ist: {result}")    