import streamlit as st
import pandas as pd


def enter_data():
    # Getting the number of preferences allowed
    with st.form(key='form1'):
        n_prefs_pos = st.number_input('Managers - Max number of choices',
                                      min_value=1, max_value=10, value=3)
        n_prefs_emp = st.number_input('Candidates - Max umber of choices',
                                      min_value=1, max_value=10, value=3)
        submit1 = st.form_submit_button('Press to continue', type='primary')

    if submit1:
        # Making empty dataframe
        biggest = max(n_prefs_pos, n_prefs_emp)
        st.write(biggest)
        #
        #     df_data = {'col1': [], 'col2': [],  }
        #
        #     with st.form(key='form2'):
        #         data_type = st.radio('Choose type of data', ('open position', 'candidate'))
        #         identity = st.text_input('Enter ID of position or candidate')
        #
        #
        #         submit = st.form_submit_button()

