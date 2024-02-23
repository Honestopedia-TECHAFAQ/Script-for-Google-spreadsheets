import gspread
from oauth2client.service_account import ServiceAccountCredentials
import time
import streamlit as st
import pandas as pd
scope = ['https://spreadsheets.google.com/feeds', 'https://www.googleapis.com/auth/drive']
uploaded_file = st.file_uploader("Upload JSON file", type=["json"])

if uploaded_file is not None:
    credentials = ServiceAccountCredentials.from_json_keyfile_dict(uploaded_file, scope)
    client = gspread.authorize(credentials)
    spreadsheet = client.open("Your Spreadsheet Title")
    worksheet = spreadsheet.worksheet("Sheet1")  
    def fetch_and_filter_data():
        while True:
            values = worksheet.get_all_values()
            filtered_data = [row for row in values if "Keyword" in row]
            filtered_df = pd.DataFrame(filtered_data)
            st.dataframe(filtered_df)
            time.sleep(5)
    fetch_and_filter_data()
