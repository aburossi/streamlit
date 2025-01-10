import streamlit as st
import urllib.parse

# Page configuration
st.set_page_config(page_title="Link Generator", layout="centered")

# Title of the app
st.title("Link Generator")

# Text input with larger size and placeholder
user_input = st.text_area(
    "Enter your text here:",
    "",
    height=100,
    placeholder="Type your text here...",
    key="text_input"
)

# Button to generate the link
generate_button = st.button("Generate Link")

# Check if the button is pressed or Enter is hit
if generate_button or user_input:
    # Encode the user input for URL
    encoded_input = urllib.parse.quote(user_input)
    
    # Generate the link
    generated_link = f"https://allgemeinbildung.github.io/textbox/answers?assignmentId={encoded_input}"
    
    # Display the generated link with a clickable option
    st.write("Generated Link:")
    st.markdown(f"[Click here to open in a new window]({generated_link}){{target=_blank}}", unsafe_allow_html=True)
    
    # Display the link as text for copying
    st.code(generated_link, language="markdown")
