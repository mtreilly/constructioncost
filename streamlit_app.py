"""
# My first app
Here's our first attempt at using data to create a table:
"""

import streamlit as st
import pandas as pd
import numpy as np

st.markdown("# Summary Page 🎈")

construction_cost = pd.read_csv("house-construction-cost.csv")

st.write(construction_cost)

# chart_data = pd.DataFrame(construction_cost, columns=["value"])

# st.line_chart(chart_data)
