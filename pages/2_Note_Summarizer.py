import streamlit as st
st.set_page_config(page_title="Note Summarizer", page_icon="📝")
import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from utils.ai_service import summarize_notes
from utils.theme import apply_custom_css

st.session_state.page_hash = "notes"
apply_custom_css()

st.title("📝 Note Summarizer")
st.write("Paste your lengthy notes below to get crisp, clear bullet points.")

if "app_error" not in st.session_state:
    st.session_state.app_error = None

if st.session_state.app_error:
    st.error(st.session_state.app_error)
    st.session_state.app_error = None

notes = st.text_area("Paste your notes here:", height=300, placeholder="Machine Learning is a subfield of artificial intelligence that focuses on building systems that learn from data... Paste your lecture or reading notes here.")

if "notes_data" not in st.session_state:
    st.session_state.notes_data = None
if "api_locked" not in st.session_state:
    st.session_state.api_locked = False

if st.session_state.api_locked:
    button_label = "Generating..."
else:
    button_label = "Summarize Another Note" if st.session_state.notes_data else "Summarize Notes"

generate_clicked = st.button(button_label, type="primary", use_container_width=True, disabled=st.session_state.api_locked)

if generate_clicked:
    if notes.strip():
        st.session_state.api_locked = True
        st.rerun()
    else:
        st.warning("Please paste some notes to summarize.")

if st.session_state.api_locked and notes.strip():
    with st.spinner("Analyzing text..."):
        st.session_state.notes_data = None
        try:
            summary = summarize_notes(notes)
            if summary.startswith("⚠️") or summary.startswith("⏱️") or summary.startswith("System Error") or summary.startswith("API Error"):
                st.session_state.app_error = summary
            else:
                st.session_state.notes_data = summary
        except Exception as e:
            st.session_state.app_error = f"An unexpected error occurred: {str(e)}"
        finally:
            st.session_state.api_locked = False
            st.rerun()

if st.session_state.notes_data:
    st.markdown("### Summary")
    st.write(st.session_state.notes_data)
