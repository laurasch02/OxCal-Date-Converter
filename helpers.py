import pandas as pd
import streamlit as st
from io import StringIO, BytesIO

def extract_results_to_dataframe(file_content):
    # Read all lines from the uploaded file content
    lines = file_content.decode("utf-8").splitlines()

    # Find the start and end of the "Results" section
    start_idx, end_idx = None, None
    for i, line in enumerate(lines):
        if line.strip() == "Results":
            start_idx = i + 1  # Start from the line after "Results"
        elif start_idx is not None and line.strip() == "References":
            end_idx = i  # End at the line before "References"
            break

    # Check if the Results section was found
    if start_idx is None or end_idx is None:
        st.warning("Warning: 'Results' section not found in the uploaded file.")
        return None

    # Extract the Results section lines
    results_lines = lines[start_idx:end_idx]

    # Convert the Results section to a DataFrame
    results_data = "\n".join(results_lines)
    results_df = pd.read_csv(StringIO(results_data))  # Use StringIO to read from the in-memory string

    return results_df

def read_data(file: str):
    df = pd.read_csv(file)
    return df

def format_data(data: pd.DataFrame, names: str, c14s: str, thresh: str, d_format: str):

    dates = []

    if d_format == "R_Date":
        for name, c14, d_range in zip(data[names].tolist(), data[c14s].tolist(), data[thresh].tolist()):
            dates.append(f"R_Date('{name}', {c14}, {d_range});")
    
    elif d_format == "C_Date":
        for name, c14, d_range in zip(data[names].tolist(), data[c14s].tolist(), data[thresh].tolist()):
            dates.append(f"C_Date('{name}', {c14}, {d_range});")
    return dates
    