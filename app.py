import streamlit as st
import pyodbc

# Database configuration
SERVER_NAME = 'localhost'
DATABASE_NAME = 'Ex'
DRIVER = '{ODBC Driver 17 for SQL Server}'

CONNECTION_STRING = f'DRIVER={DRIVER};SERVER={SERVER_NAME};DATABASE={DATABASE_NAME};Trusted_Connection=yes;'

def find_matching_words(letters):
    results = []
    with pyodbc.connect(CONNECTION_STRING) as conn:
        with conn.cursor() as cursor:
            cursor.execute("EXEC dbo.sp_FindMatchingWords @letters= ?", (letters,))
            rows = cursor.fetchall()
            results = [row[0] for row in rows]
    return results

# Streamlit interface
st.title("Letter Search Application")

letters = st.text_input("Enter a series of letters:", "")
if st.button("Find"):
    if letters.strip():
        results = find_matching_words(letters)
        if results:
            st.write("### Matching Words:")
            st.write(results)
        else:
            st.write("No matching words found.")