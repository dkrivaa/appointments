# This is the main app file
import streamlit as st
import engine2
import example

###############################################
### EXAMPLE FILE
df = example.example()
def convert_df(df):
    return df.to_csv(index=False).encode('windows-1255')

csv = convert_df(df)
st.download_button('Download example CSV file',
                   data=csv,
                   file_name='example.csv',
                   mime='text/csv')
st.markdown('___')
#########################################

engine2.start()





