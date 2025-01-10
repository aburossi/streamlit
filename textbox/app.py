import streamlit as st
import urllib.parse

# Title of the app
st.title("Link Generator")

# User input
user_input = st.text_input("Enter your text here:", "")

if user_input:
    # Encode the user input for URL
    encoded_input = urllib.parse.quote(user_input)
    
    # Generate the link
    generated_link = f"https://allgemeinbildung.github.io/textbox/answers?assignmentId={encoded_input}"
    
    # Display the generated link
    st.write("Generated Link:")
    st.code(generated_link, language="markdown")
    
    # Button to copy link
    st.button("Copy Link")
