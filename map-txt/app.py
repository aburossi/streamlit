import streamlit as st
import urllib.parse

# Set up the Streamlit app
st.title("URL-Generator für Aufgaben")

# Explanation in German
st.markdown("""
### Erklärung:
Geben Sie den Titel der Aufgabe in das Textfeld ein. Nachdem Sie den Titel eingegeben haben, wird eine URL generiert. 
Diese URL können Sie mit Ihren Schüler:innen teilen. Über den Link können die Schüler:innen eine Mindmap auf dem Bildschirm erstellen und darunter Antworten eingeben.
Hinweis: Die Paste-Funktion ist deaktiviert, um das Kopieren und Einfügen von Lösungen zu verhindern.
""")

# Ask the user for an assignment title
assignment_title = st.text_input("Geben Sie den Titel der Aufgabe ein:")

# Generate and display the URL after user inputs the title
if assignment_title:
    # Encode the user input to make it URL-safe
    encoded_title = urllib.parse.quote(assignment_title)
    generated_url = f"https://aburossi.github.io/map-txt/index.html?assignmentId=assignment{encoded_title}"
    
    # Display the generated URL
    st.markdown("### Generierte URL:")
    st.markdown(f"[{generated_url}]({generated_url})")
