import pandas as pd
import streamlit as st
if "data_df" not in st.session_state:
    st.session_state["data_df"] = pd.DataFrame()

pg_home = st.Page("views/home.py", title="Home", icon=":material/home:", default=True)
pg_second = st.Page("views/Idealgewicht_Rechner.py", title="Idealgewicht Rechner", icon=":material/info:")

pg = st.navigation([pg_home, pg_second])
pg.run()
