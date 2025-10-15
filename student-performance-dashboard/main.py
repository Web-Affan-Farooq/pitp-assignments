# accept and read the csv file . also add the file into the database with a label ,

import streamlit as st 
import pandas as pd 

from app import StudentDashboard , DisplayTable 

st.title("Student performance dashboard")

file_paths_accepted = ["csv", "xlsx"]

uploaded_file = st.file_uploader('Select a file')

if uploaded_file is not None:
    extension = uploaded_file.name.split(".")[1] 
    if(extension == file_paths_accepted[0]):
        df = pd.read_csv(uploaded_file)
        
    else:
        df = pd.read_excel(uploaded_file)
        st.write("## Data table")
        st.write("> Data extracted from csv file")
        
        DisplayTable(df)