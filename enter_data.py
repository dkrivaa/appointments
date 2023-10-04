import streamlit as st
import pandas as pd


def enter_data():
    with st.form('Enter your data'):
        data_type = st.radio('Choose type of data', ('open position', 'candidate'))
        identity = st.text_input('Enter ID of position or candidate')


        submit = st.form_submit_button()

    if submit:
        st.write('test')
