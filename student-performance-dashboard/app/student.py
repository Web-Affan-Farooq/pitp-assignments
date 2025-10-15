import pandas as pd
import streamlit as st

class DisplayTable():
    def __init__(self , df ):
        self.df = df
        st.table(self.df)
    
    def find_topper(self):

class StudentDashboard():
    ## ____Define file paths that are accepted ...
    file_paths_accepted = ["csv", "xlsx"]

    def __init__ (self , df:pd.DataFrame ):
        pass