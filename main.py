import streamlit as st
import pandas as pd
from helpers import *


st.title("OxCal Data Converter")

file = st.file_uploader("Upload your C14-Data", type=["csv", "xlsx"],)

if file != None:
    df = extract_results_to_dataframe(file.read())
    with st.expander("View Data", icon="👁️"):
        st.dataframe(df)

    with st.sidebar:
        st.markdown("#### Select the necessary columns")
        name = st.selectbox("Name Column", df.columns.tolist(),index=None, placeholder="Names")
        c14_data = st.selectbox("C14-Data Column", df.columns.tolist(), index=None, placeholder="C14-Dates")
        threshold = st.selectbox("Threshold Column", df.columns.tolist(), index=None, placeholder="Thresholds")

        st.markdown("#### Select the necessary format")
        date_format = st.selectbox("Formats", ("R_Date", "C_Date"), index=None, placeholder="Format")

        convert = st.button("Convert to OxCal!")

    if name and c14_data and threshold and date_format != None:
        if convert:
            date_list = format_data(df, name, c14_data, threshold, date_format)
    
            if date_list != None:
                full_text = "\n".join(date_list)

                with st.expander("Plain Text", icon="📄"):
                    with st.container():
                        st.write(full_text)
                
                down_text = st.download_button("Download Converted Dates!",
                                            full_text,
                                            f"{date_format}_converted.txt",
                                            icon="🗃️")

            