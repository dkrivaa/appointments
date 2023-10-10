# This is the main app file
import streamlit as st
import engine2
import example
import enter_data

# engine2.start()

if __name__ == '__main__':
    # call main function
    engine2.start()

###############################################
### EXAMPLE FILE
st.header('', divider='rainbow')

df = example.example()
def convert_df(df):
    return df.to_csv(index=False).encode('windows-1255')

csv = convert_df(df)
st.download_button('Download example CSV file',
                   data=csv,
                   file_name='example.csv',
                   mime='text/csv')
#########################################

# my_data_button = st.button('Enter data online')
#
# if my_data_button:
#     enter_data.enter_data()


st.link_button('Enter data online', 'https://familyshopping.streamlit.app/')
