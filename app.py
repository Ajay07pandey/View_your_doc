import streamlit as st
import pandas as pd

st.set_page_config(page_title="Excel Data Viewer", layout="wide")

st.title("📊 Excel Data Viewer")

# Upload section
uploaded_file = st.file_uploader("Upload your Excel file", type=["xlsx", "xls"])

if uploaded_file:
    try:
        # Read the Excel file
        excel_data = pd.ExcelFile(uploaded_file)

        # Show file info
        st.success(f"File uploaded successfully!")
        st.write(f"**Sheets available:** {list(excel_data.sheet_names)}")

        # Select sheet
        sheet_name = st.selectbox("Select a sheet", excel_data.sheet_names)
        df = pd.read_excel(excel_data, sheet_name=sheet_name)

        # Show file info for the selected sheet
        st.write(f"**Rows:** {df.shape[0]} | **Columns:** {df.shape[1]}")
        st.write(f"**Columns:** {list(df.columns)}")

        # Display the dataframe of the selected sheet
        st.subheader("Sheet Data Preview")
        st.dataframe(df, use_container_width=True)

    except Exception as e:
        st.error(f"❌ Error reading file: {e}")
else:
    st.info("Please upload an Excel file to view its contents.")
