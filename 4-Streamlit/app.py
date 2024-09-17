import streamlit as st 
import pandas as pd
import numpy as np

## Title of the application 
st.title("Hello duniya")

#Display simple Text
st.write("This is simple text ")

#Create DataFrame
df=pd.DataFrame({
    'first column': [1,2,3,4,5],
    'second column':[5,6,8,5,4]
})

#Display  DataFrame
st.write("This is dataframe ")
st.write(df)

chart_data = pd.DataFrame(
    np.random.rand(20,3),columns=['a','b','c']
)
st.line_chart(chart_data)