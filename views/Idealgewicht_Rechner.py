import streamlit as st
from functions.idealgewichtrechner import idealgewicht_rechnen
import pandas as pd

st.set_page_config(page_title="Idealgewicht Rechner", page_icon="⚖️")

st.title("⚖️ Idealgewicht Rechner")
st.subheader("Berechne dein Referenzgewicht")

st.write(
    "Dieser Rechner verwendet die Broca-Formel (Größe in cm − 100), "
    "um ein ungefähres Idealgewicht zu bestimmen."
)

st.divider()

with st.form("idealgewicht_form"):

    col1, col2 = st.columns(2)

    with col1:
        name = st.text_input("Dein Name")
        height = st.slider("Körpergröße (cm)", 120, 220, 170)

    with col2:
        weight = st.number_input("Aktuelles Gewicht (kg)", 30.0, 200.0, 65.0)
        gender = st.radio("Geschlecht", ["Weiblich", "Männlich"])

    info = st.checkbox("Ich weiss, dass dies nur ein Richtwert ist")

    submitted = st.form_submit_button("Berechnen")

st.divider()

if submitted:

    if not info:
        st.warning("Bitte bestätige zuerst die Checkbox.")
    else:
        idealgewicht = idealgewicht_rechnen(height)

        st.success(f"{name}, dein Idealgewicht beträgt {idealgewicht:.1f} kg")

        differenz = weight - idealgewicht
        st.metric("Abweichung vom Idealgewicht", f"{differenz:.1f} kg")

        if differenz > 0:
            st.error("Du liegst über dem Referenzwert.")
        elif differenz < 0:
            st.info("Du liegst unter dem Referenzwert.")
        else:
            st.balloons()

        st.progress(min(int(abs(differenz) * 5), 100))
        st.caption("Hinweis: Die Broca-Formel ist eine sehr vereinfachte Methode.")

       # Verlauf speichern – mit mehreren Spalten
        st.session_state["data_df"] = pd.concat(
            [st.session_state["data_df"],
            pd.DataFrame([{
            "Name": name,
            "Größe (cm)": height,
            "Gewicht (kg)": weight,
            "Idealgewicht (kg)": idealgewicht,
            "Differenz (kg)": differenz
            }])], ignore_index=True)

# Verlauf anzeigen
df_anzeige = st.session_state["data_df"].copy()
st.dataframe(df_anzeige)