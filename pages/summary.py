import streamlit as st

st.markdown("# Pandas Summar Page 🎈")
st.sidebar.markdown("# Pandas Summary Page 🎈")


import numpy as np
import pandas as pd
from pandas_profiling import ProfileReport
from streamlit_pandas_profiling import st_profile_report


df = pd.read_csv("./house-construction-cost.csv")

pr = df.profile_report()

st.title("Pandas Profiling in Streamlit")
st_profile_report(pr)
