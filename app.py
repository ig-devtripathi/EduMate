import streamlit as st
import sys
import os
sys.path.append(os.path.dirname(os.path.abspath(__file__)))
from utils.theme import apply_custom_css

st.set_page_config(
    page_title="EduMate",
    page_icon="📚",
    layout="wide",
    initial_sidebar_state="expanded"
)

st.session_state.page_hash = "home"
apply_custom_css()

# Modern Custom Logo Section
st.markdown("""
<div class='edumate-header'>
    <div class='logo-shape'>
        <span>📚</span>
    </div>
    <h1 class='logo-title'>EduMate</h1>
</div>
""", unsafe_allow_html=True)

st.markdown("""
<div class='fade-in-text'>
    <h2 style='text-align: center; color: #334155; font-weight: 600; font-size: 1.75rem; margin-top: -1rem;'>Advanced AI Assistance for Elevated Learning</h2>
</div>
""", unsafe_allow_html=True)

st.write("### Prepare for Excellence")
st.write("Elevate your learning experience with our world-class AI models. Select a tool below or from the sidebar to get started.")

st.markdown("""
<div style="display: flex; gap: 1.5rem; flex-wrap: wrap; margin-top: 1.5rem;">
    <a href="Concept_Explainer" target="_self" class="glass-card" style="flex: 1; min-width: 300px;">
        <h3>🧠 Concept Explainer</h3>
        <p>Break down complex topics into simple, digestible terms.</p>
    </a>
    <a href="Note_Summarizer" target="_self" class="glass-card" style="flex: 1; min-width: 300px;">
        <h3>📝 Note Summarizer</h3>
        <p>Turn lengthy, dense notes into crisp, concise bullet points.</p>
    </a>
</div>
<div style="display: flex; gap: 1.5rem; flex-wrap: wrap; margin-top: 1.5rem;">
    <a href="Quiz_Generator" target="_self" class="glass-card" style="flex: 1; min-width: 300px;">
        <h3>🎯 Quiz Generator</h3>
        <p>Test your knowledge with interactive, dynamic quizzes.</p>
    </a>
    <a href="Document_Analyzer" target="_self" class="glass-card" style="flex: 1; min-width: 300px;">
        <h3>📄 Document Analyzer</h3>
        <p>Chat seamlessly with your PDFs, DOCXs, and image files.</p>
    </a>
</div>
<div style="display: flex; gap: 1.5rem; flex-wrap: wrap; margin-top: 1.5rem; margin-bottom: 2rem; justify-content: center;">
    <a href="Ask_EduMate" target="_self" class="glass-card" style="flex: 0 1 calc(50% - 0.75rem); min-width: 300px;">
        <h3>🎓 Ask EduMate</h3>
        <p>Your personal AI academic tutor for step-by-step problem solving.</p>
    </a>
</div>
""", unsafe_allow_html=True)

st.markdown("<br><hr style='border: 1px solid #e2e8f0;'><br>", unsafe_allow_html=True)
st.markdown("<div style='text-align: center; color: #94a3b8; font-weight: 500; font-size: 0.9rem; letter-spacing: 0.05em;'>EDUMATE • AI LEARNING PLATFORM</div>", unsafe_allow_html=True)
