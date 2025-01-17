import streamlit as st
import urllib.parse

# Page configuration (must be the first Streamlit command)
st.set_page_config(page_title="Multi-Link Generator", layout="centered")

# Custom style for light mode
st.markdown(
    """
    <style>
    body {
        background-color: white;
        color: black;
    }
    textarea {
        background-color: #f0f0f0;
        color: black;
        font-size: 16px;
    }
    </style>
    """,
    unsafe_allow_html=True
)

# Title of the app
st.title("Multi-Link Generator")

# Multi-line text input
user_input = st.text_area(
    "Enter one text per line (each line will generate a separate link):",
    "",
    height=200,
    placeholder="Type your text here, each line will generate a link...",
    key="text_input"
)

# Button to generate the links
generate_button = st.button("Generate Links")

if generate_button or user_input:
    # Split input by lines and remove empty lines
    lines = [line.strip() for line in user_input.splitlines() if line.strip()]
    
    if lines:
        st.write("Generated Links:")
        generated_links = []
        
        # Generate and display each link with the input text as the hyperlink text
        for line in lines:
            encoded_line = urllib.parse.quote(line)
            link = f"https://allgemeinbildung.github.io/textbox/answers?assignmentId={encoded_line}"
            st.markdown(f"- [{line}]({link})", unsafe_allow_html=True)
            generated_links.append(link)
        
        # Display all links as plain text for bulk copying
        st.text_area("Bulk Copy All Links", "\n".join(generated_links), height=150)
        
        # Add a "Copy All Links" button
        if st.button("Copy All Links"):
            st.experimental_set_query_params(links="\n".join(generated_links))
            st.success("All links copied to clipboard!")
