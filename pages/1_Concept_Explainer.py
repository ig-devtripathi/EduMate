import streamlit as st
st.set_page_config(page_title="Concept Explainer", page_icon="💡")
import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from utils.ai_service import explain_concept
from utils.theme import apply_custom_css

st.session_state.page_hash = "concept"
apply_custom_css()

st.title("💡 Concept Explainer")
st.write("Enter a topic you're struggling with, and we'll break it down for you.")

if "app_error" not in st.session_state:
    st.session_state.app_error = None

if st.session_state.app_error:
    st.error(st.session_state.app_error)
    st.session_state.app_error = None

topic = st.text_input("What do you want to learn?", placeholder="e.g., Quantum Computing, Photosynthesis")
difficulty = st.selectbox("Select Difficulty", ["Explain like I'm 5", "High School Level", "College Level", "Expert", "Custom (Type your own)"])

if difficulty == "Custom (Type your own)":
    difficulty = st.text_input("Custom Difficulty", placeholder="e.g., Explain it referencing a video game, Make it poetic, Write it as a sci-fi prologue...")

if "concept_data" not in st.session_state:
    st.session_state.concept_data = None
if "api_locked" not in st.session_state:
    st.session_state.api_locked = False

if st.session_state.api_locked:
    button_label = "Generating..."
else:
    button_label = "Generate Another Explanation" if st.session_state.concept_data else "Explain Concept"

generate_clicked = st.button(button_label, type="primary", use_container_width=True, disabled=st.session_state.api_locked)

if generate_clicked:
    if topic:
        st.session_state.api_locked = True
        st.rerun()
    else:
        st.warning("Please enter a topic.")

if st.session_state.api_locked and topic:
    with st.spinner("Analyzing concept..."):
        st.session_state.concept_data = None
        try:
            explanation = explain_concept(topic, difficulty)
            if explanation.startswith("⚠️") or explanation.startswith("⏱️") or explanation.startswith("System Error") or explanation.startswith("API Error"):
                st.session_state.app_error = explanation
            else:
                st.session_state.concept_data = explanation
        except Exception as e:
            st.session_state.app_error = f"An unexpected error occurred: {str(e)}"
        finally:
            st.session_state.api_locked = False
            st.rerun()

if st.session_state.concept_data:
    st.markdown("### Explanation")
    st.write(st.session_state.concept_data)
