import streamlit as st

st.title("Idealgewicht Rechner")

with st.form("idealgewicht_form"):
    height = st.number_input("Größe (cm)", value=170.0)
    submit_button = st.form_submit_button("Berechnen")

if submit_button:
    ideal_weight = height - 100
    st.success(f"Dein ungefähres Idealgewicht ist: {ideal_weight:.1f} kg")
