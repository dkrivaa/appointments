# This is the main app file
import streamlit as st
import engine

engine.read_data()

st.download_button('Download example CSV file',
                   data='example.csv',
                   file_name='example.csv',
                   mime='text/csv')

