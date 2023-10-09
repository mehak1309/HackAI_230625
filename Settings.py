import os
import streamlit as st
import requests
import pandas as pd
import random, string

st.set_page_config(
    page_title="Currency Exchange Monitor",
    layout="wide"
)

header = st.container()
user_data = st.container()

if 'count' not in st.session_state:
	st.session_state.count = 0

@st.cache_data
def get_data(filename):
    data = pd.read_csv(filename)
    return data

input_rows = []

def add_row(foreign_currency, mode, threshold):
    input_rows.append({"foreign_currency": foreign_currency, "mode": mode, "threshold": threshold})
    foreign_currency = first_column.selectbox("Foreign Currency",
                                              options=currency_codes,
                                              index=1,
                                              key=random.choice(string.ascii_uppercase)+str(random.randint(0,999999)))
    mode = second_column.selectbox("",
                                   options=[">", "<"],
                                   index=0,
                                   key=random.choice(string.ascii_uppercase)+str(random.randint(0,999999)))
    threshold = third_column.text_input("Threshold",
                                        key=random.choice(string.ascii_uppercase)+str(random.randint(0,999999)))

data = get_data(os.path.join("data", "currency_codes.csv"))
currency_codes = data['Codes'].tolist()

with header:
    st.title("Please Enter the Following Details")

with user_data:
    api_key = st.text_input("API Key")
    base_currency = st.selectbox("Base Currency", options=currency_codes, index=0)
    st.text("Get Notified When:")
    first_column, second_column, third_column = st.columns(3)
    foreign_currency = first_column.selectbox("Foreign Currency",
                                              options=currency_codes, index=1)
    mode = second_column.selectbox("",
                                   options=[">", "<"],
                                   index=0)
    threshold = third_column.text_input("Threshold")

    st.write("")

    col1, col2, col3, col4, col5 = st.columns(5)
    if col3.button("Submit"):
        with open(os.path.join("data", ".api_key.txt"), 'w') as f:
            f.write(api_key)

        d = {"Base_Currency": base_currency,
             "Foreign_Currency": foreign_currency,
             "Option": mode,
             "Threshold": threshold}
        
        df = pd.DataFrame(d, index=[0])
        df.to_csv(os.path.join("data", "user_settings.csv"), index=False)






#     if st.button("Add Row"):
#         st.session_state.count += 1
#         add_row(foreign_currency, mode, threshold)
#         if st.session_state.count>1:
#             for i in range(st.session_state.count-1):
#                add_row(foreign_currency, mode, threshold)

# all_input_data = input_rows

# st.write("All Input Data:", all_input_data)
