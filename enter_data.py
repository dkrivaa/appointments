import streamlit as st
import pandas as pd


def enter_data():
    n_prefs_pos = st.number_input('Managers - Number of choices',
                                   min_value=1, max_value=10, value=3
                                   )

    with st.form('Enter your data'):
        data_type = st.radio('Choose type of data', ('open position', 'candidate'))
        identity = st.text_input('Enter ID of position or candidate')


        submit = st.form_submit_button()

