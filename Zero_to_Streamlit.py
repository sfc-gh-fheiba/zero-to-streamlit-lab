import streamlit as st
import pandas as pd
from snowflake.snowpark import Session
from snowflake.snowpark.exceptions import SnowparkSQLException
import snowflake.snowpark.functions as F
import os

st.set_page_config(
    page_title="Zero to Streamlit",
    page_icon="📈",
    layout="wide",
    initial_sidebar_state="expanded"
)

