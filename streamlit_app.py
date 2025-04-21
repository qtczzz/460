
import streamlit as st

# Title
st.title("📊 Simple Streamlit App")

# Sidebar
st.sidebar.header("User Input")
user_input = st.sidebar.text_input("Enter some text")

# File uploader
uploaded_file = st.sidebar.file_uploader("Upload a CSV file", type=["csv"])

# Main output
st.write("## Output")

# Display user input
if user_input:
    st.write(f"You entered: {user_input}")
else:
    st.write("Please enter some text in the sidebar.")

# Display file content
if uploaded_file:
    import pandas as pd
    df = pd.read_csv(uploaded_file)
    st.write("### Uploaded CSV Preview")
    st.dataframe(df)
else:
    st.write("Upload a CSV file to view its contents.")
