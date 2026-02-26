import streamlit as st
st.set_page_config(page_title="Document Analyzer", page_icon="📄")
import sys
import os
import io
from PIL import Image
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from utils.file_utils import extract_text_from_pdf, extract_text_from_docx
from utils.ai_service import analyze_document_or_image
from utils.theme import apply_custom_css

st.session_state.page_hash = "docs"
apply_custom_css()

st.title("📄 Document & Image Analyzer")
st.write("Upload a document (PDF, DOCX) or an image and ask questions about it.")

if "app_error" not in st.session_state:
    st.session_state.app_error = None

if st.session_state.app_error:
    st.error(st.session_state.app_error)
    st.session_state.app_error = None

uploaded_file = st.file_uploader("Upload File", type=["pdf", "docx", "png", "jpg", "jpeg"])
prompt = st.text_input("What would you like to know about this file?", placeholder="e.g., Summarize the main points, What does the image show?")

if "doc_data" not in st.session_state:
    st.session_state.doc_data = None
if "api_locked" not in st.session_state:
    st.session_state.api_locked = False

if st.session_state.api_locked:
    button_label = "Analyzing..."
else:
    button_label = "Analyze Another File" if st.session_state.doc_data else "Analyze"

generate_clicked = st.button(button_label, type="primary", use_container_width=True, disabled=st.session_state.api_locked)

if generate_clicked:
    if uploaded_file and prompt:
        st.session_state.api_locked = True
        st.rerun()
    else:
        st.warning("Please upload a file and enter a prompt.")

if st.session_state.api_locked and uploaded_file and prompt:
    with st.spinner("Analyzing document..."):
        st.session_state.doc_data = None
        try:
            file_type = uploaded_file.name.split('.')[-1].lower()
            text_content = None
            image_parts = None
            
            if file_type == 'pdf':
                text_content = extract_text_from_pdf(uploaded_file.getvalue())
            elif file_type == 'docx':
                text_content = extract_text_from_docx(uploaded_file.getvalue())
            elif file_type in ['png', 'jpg', 'jpeg']:
                image_parts = {
                    "mime_type": uploaded_file.type,
                    "data": uploaded_file.getvalue()
                }
            
            response = analyze_document_or_image(prompt, text_content=text_content, image_parts=image_parts)
            
            if response.startswith("⚠️") or response.startswith("⏱️") or response.startswith("System Error") or response.startswith("API Error"):
                st.session_state.app_error = response
            else:
                st.session_state.doc_data = response
        except Exception as e:
            st.session_state.app_error = f"An unexpected error occurred: {str(e)}"
        finally:
            st.session_state.api_locked = False
            st.rerun()

# Display image if uploaded regardless of generation state
if uploaded_file and uploaded_file.name.split('.')[-1].lower() in ['png', 'jpg', 'jpeg']:
     st.image(Image.open(io.BytesIO(uploaded_file.getvalue())), caption="Uploaded Image", use_container_width=True)

if st.session_state.doc_data:
    st.markdown("### Analysis Result")
    st.write(st.session_state.doc_data)
