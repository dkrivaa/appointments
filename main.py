# This is the main app file
import streamlit as st
import engine2
import example

engine2.start()

###############################################
### EXAMPLE FILE
st.markdown('___')

df = example.example()
def convert_df(df):
    return df.to_csv(index=False).encode('windows-1255')

csv = convert_df(df)
st.download_button('Download example CSV file',
                   data=csv,
                   file_name='example.csv',
                   mime='text/csv')
#########################################






