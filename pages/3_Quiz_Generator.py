import streamlit as st
st.set_page_config(page_title="Quiz Generator", page_icon="🎯")
import sys
import os
import json
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from utils.ai_service import generate_quiz
from utils.theme import apply_custom_css

st.session_state.page_hash = "quiz"
apply_custom_css()

st.title("🎯 Quiz Generator")
st.write("Test your knowledge. Configure your quiz settings below.")

if "app_error" not in st.session_state:
    st.session_state.app_error = None

if st.session_state.app_error:
    st.error(st.session_state.app_error)
    st.session_state.app_error = None

topic = st.text_input("Topic for the quiz:", placeholder="e.g., Python Basics, World War II")

col1, col2 = st.columns(2)
with col1:
    difficulty = st.radio("Difficulty Level", ["Easy", "Medium", "Hard"], index=1, horizontal=True)
with col2:
    num_questions = st.radio("Number of Questions", [5, 10], index=0, horizontal=True)

if "quiz_data" not in st.session_state:
    st.session_state.quiz_data = None
if "user_answers" not in st.session_state:
    st.session_state.user_answers = {}
if "quiz_submitted" not in st.session_state:
    st.session_state.quiz_submitted = False
if "api_locked" not in st.session_state:
    st.session_state.api_locked = False


# Button Logic
if st.session_state.api_locked:
    button_label = "Generating..."
else:
    button_label = "Generate Another Quiz" if st.session_state.quiz_data else "Generate Quiz"

generate_clicked = st.button(button_label, type="primary", use_container_width=True, disabled=st.session_state.api_locked)

if generate_clicked:
    if topic:
        # First legitimate click intercepts correctly because it is not locked yet
        st.session_state.api_locked = True
        st.rerun() # Force UI refresh to draw the button as disabled and trigger logic below
    else:
        st.warning("Please enter a topic.")

if st.session_state.api_locked and topic:
    with st.spinner("Generating quiz..."):
        st.session_state.last_topic = topic
        st.session_state.quiz_data = None # Clear old data
        st.session_state.user_answers = {}
        st.session_state.quiz_submitted = False
        
        quiz_json_str = generate_quiz(topic, difficulty=difficulty, num_questions=num_questions)
            
        try:
            # Basic cleaning if markdown blocks are included
            quiz_json_str = quiz_json_str.strip()
            if quiz_json_str.startswith("```json"):
                quiz_json_str = quiz_json_str[7:-3].strip()
            elif quiz_json_str.startswith("```"):
                quiz_json_str = quiz_json_str[3:-3].strip()
            
            # Check for API Quota/Error string intercepting the JSON format from the backend
            if quiz_json_str.startswith("⚠️") or quiz_json_str.startswith("⏱️"):
                st.session_state.app_error = quiz_json_str
                st.session_state.api_locked = False
                st.rerun()
            elif quiz_json_str.startswith("System Error") or quiz_json_str.startswith("API Error") or quiz_json_str.startswith("Error:"):
                st.session_state.app_error = f"Generate Error: {quiz_json_str}"
                st.session_state.api_locked = False
                st.rerun()
            else:    
                st.session_state.quiz_data = json.loads(quiz_json_str)
                st.session_state.api_locked = False # Unlock API on success
                st.rerun() # Force a rerun to show the generated quiz immediately
                
        except json.JSONDecodeError:
            st.session_state.api_locked = False
            st.session_state.app_error = f"Failed to parse the quiz data. The AI returned a malformed response. Please try again. \n\n**Raw output that broke the parser:**\n```\n{quiz_json_str}\n```"
            st.rerun()
        except Exception as e:
            st.session_state.api_locked = False # Unlock on failure
            st.session_state.app_error = f"An unexpected error occurred: {str(e)}"
            st.rerun()

if st.session_state.quiz_data:
    st.markdown("### Your Quiz")
    questions = st.session_state.quiz_data.get("questions", [])
    
    score = 0
    for i, q in enumerate(questions):
        st.markdown(f"**Q{i+1}: {q['question']}**")
        
        if not st.session_state.quiz_submitted:
            st.session_state.user_answers[i] = st.radio(
                "Select an option:",
                q['options'],
                key=f"q_{i}",
                index=None,
                label_visibility="collapsed"
            )
        else:
            user_ans = st.session_state.user_answers.get(i)
            correct_ans = q['answer']
            
            if user_ans == correct_ans:
                score += 1
            
            for opt in q['options']:
                if opt == correct_ans and opt == user_ans:
                    st.markdown(f"<div style='padding: 10px; border-radius: 5px; background-color: rgba(34, 197, 94, 0.2); border: 2px solid #22c55e; color: #166534; margin-bottom: 8px; font-weight: 600;'>✅ {opt}</div>", unsafe_allow_html=True)
                elif opt == user_ans and opt != correct_ans:
                    st.markdown(f"<div style='padding: 10px; border-radius: 5px; background-color: rgba(239, 68, 68, 0.2); border: 2px solid #ef4444; color: #991b1b; margin-bottom: 8px; font-weight: 600;'>❌ {opt}</div>", unsafe_allow_html=True)
                elif opt == correct_ans and opt != user_ans:
                    st.markdown(f"<div style='padding: 10px; border-radius: 5px; background-color: rgba(34, 197, 94, 0.1); border: 2px dashed #22c55e; color: #166534; margin-bottom: 8px; font-weight: 600;'>✓ {opt} (Correct Answer)</div>", unsafe_allow_html=True)
                else:
                    st.markdown(f"<div style='padding: 10px; border-radius: 5px; border: 1px solid #cbd5e1; color: #475569; margin-bottom: 8px;'>○ {opt}</div>", unsafe_allow_html=True)
            
            st.info(f"**Explanation:** {q['explanation']}")
            
        st.markdown("---")
        
    if not st.session_state.quiz_submitted:
        if st.button("Submit Answers"):
            st.session_state.quiz_submitted = True
            st.rerun()
    else:
        st.markdown(f"### 🏆 Final Score: {score}/{len(questions)}")
        if st.button("Take Another Quiz"):
            st.session_state.quiz_data = None
            st.session_state.user_answers = {}
            st.session_state.quiz_submitted = False
            st.session_state.last_topic = ""
            st.session_state.api_locked = False
            st.rerun()
