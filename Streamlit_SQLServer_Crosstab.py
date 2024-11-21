import streamlit as st
import pandas as pd
import pyodbc
import numpy as np
import streamlit.components.v1 as components
from st_aggrid import AgGrid

# SQL Server connection parameters
server = 'SPM.nala.roche.com'
database = 'Agility'

# Connect to SQL Server and fetch raw data
def fetch_raw_data():
    conn_str = f'DRIVER={{ODBC Driver 17 for SQL Server}};SERVER={server};DATABASE={database}; Trusted_Connection=yes'
    conn = pyodbc.connect(conn_str)
    query = "SELECT * FROM PathLab_Adjustments"
    df = pd.read_sql(query, conn)
    conn.close()
    return df

def commit_changes_to_sql_server(updated_df):
    conn_str = f'DRIVER={{ODBC Driver 17 for SQL Server}};SERVER={server};DATABASE={database}; Trusted_Connection=yes'
    conn = pyodbc.connect(conn_str)
    cursor = conn.cursor()

    # Loop through the DataFrame rows and commit changes
    for index, row in updated_df.iterrows():
        try:
            
            query = f"UPDATE PathLab_Adjustments SET InstrumentQty = ?, Adjustment = ? WHERE RowID = ?"
            cursor.execute(query,row['InstrumentQty'],row['Adjustment'],row['RowID'])
            
            conn.commit()  # Commit after each update
        except Exception as e:
            conn.rollback()  # Rollback if there's an error
            st.error(f"Error updating record: {e}")
            continue
    cursor.close()
    conn.close()  

# Fetch raw data from SQL Server
df = fetch_raw_data()

# Streamlit app layout
st.title("Crosstab Data from SQL Server")
st.write("This table shows the crosstab data fetched from SQL Server:")

# Display Data in Streamlit
grid_response = AgGrid(df, editable=True)

# Get edited data (after users make changes)
edited_df = grid_response['data']
#st.write("Edited Data:", edited_df)

# Commit changes to SQL Server when user clicks a button
if st.button("Commit Changes"):
    # Commit updated data back to SQL Server
    commit_changes_to_sql_server(edited_df)
    st.success("Changes committed successfully!")