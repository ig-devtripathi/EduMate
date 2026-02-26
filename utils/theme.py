import streamlit as st

def apply_custom_css():
    st.markdown("""
        <style>
        @import url('https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700;800&display=swap');
        
        /* Global font and background */
        html, body, [class*="css"], #root {
            font-family: 'Inter', system-ui, -apple-system, sans-serif !important;
            background-color: #f8fafc !important;
        }
        
        .stApp, .ea39sxc0 {
            background-color: #f8fafc !important;
            background-image: 
                radial-gradient(at 0% 0%, hsla(215, 100%, 96%, 1) 0, transparent 50%),
                radial-gradient(at 100% 0%, hsla(250, 100%, 97%, 1) 0, transparent 50%),
                radial-gradient(at 100% 100%, hsla(215, 100%, 96%, 1) 0, transparent 50%),
                radial-gradient(at 0% 100%, hsla(250, 100%, 97%, 1) 0, transparent 50%);
            background-attachment: fixed;
            color: #0f172a !important;
            font-weight: 400 !important;
        }

        /* Make Streamlit background header invisible, but KEEP the interactive status/menu at the top right */
        header[data-testid="stHeader"] {
            background: transparent !important;
            border: none !important;
            box-shadow: none !important;
            pointer-events: none !important; /* Let clicks pass through empty space */
        }
        
        /* Restore the "Running..." status box and main menu toggle so they work for deployment */
        header[data-testid="stHeader"] div[data-testid="stStatusWidget"],
        header[data-testid="stHeader"] .stAppDeployButton,
        header[data-testid="stHeader"] button {
            pointer-events: auto !important; 
        }
        
        /* Ensure the sidebar toggle button is highly visible and clickable */
        button[data-testid="collapsedControl"] {
            pointer-events: auto !important;
            background-color: #f1f5f9 !important; /* Solid visible gray to stand out */
            border: 1.5px solid #cbd5e1 !important; /* Visible border ring */
            backdrop-filter: blur(10px) !important;
            border-radius: 50% !important;
            box-shadow: 0 2px 4px rgba(0,0,0,0.15) !important; /* Deeper default shadow */
            color: #0f172a !important;
            margin: 0.5rem !important;
            transition: all 0.2s ease !important;
            z-index: 99999 !important;
        }
        
        button[data-testid="collapsedControl"]:hover {
            transform: scale(1.1) !important;
            box-shadow: 0 10px 15px -3px rgba(37, 99, 235, 0.2) !important;
            color: #2563eb !important;
            background-color: #ffffff !important;
        }

        /* Generic Text override for all markdown blocks */
        .stMarkdown, .stMarkdown p {
            color: #334155 !important;
            font-size: 1.05rem !important;
            line-height: 1.6 !important;
        }

        /* Sidebar Styling for high visibility */
        section[data-testid="stSidebar"] {
            background-color: rgba(255, 255, 255, 0.95) !important;
            backdrop-filter: blur(20px) !important;
            border-right: 1px solid #e2e8f0 !important;
        }
        section[data-testid="stSidebar"] [data-testid="stSidebarNavItems"] span {
            color: #0f172a !important;
            font-weight: 600 !important;
            font-size: 1rem !important;
        }
        section[data-testid="stSidebar"] * { 
            color: #1e293b;
        }

        /* Streamlit Input fields */
        div[data-baseweb="input"] > div, 
        div[data-baseweb="textarea"] > div, 
        div[data-baseweb="select"] > div {
            background-color: #ffffff !important;
            border: 1.5px solid #cbd5e1 !important;
            border-radius: 10px !important;
            transition: all 0.2s ease !important;
            box-shadow: 0 1px 2px 0 rgba(15, 23, 42, 0.05) !important;
        }
        /* Enforce Roman I-beam text cursor for typing inputs */
        div[data-baseweb="input"], div[data-baseweb="input"] *,
        div[data-baseweb="textarea"], div[data-baseweb="textarea"] * {
            cursor: text !important;
        }

        /* Enforce pointer hand cursor only for Select Boxes */
        div[data-baseweb="select"], div[data-baseweb="select"] * {
            cursor: pointer !important;
        }
        
        div[data-baseweb="input"]:hover > div,
        div[data-baseweb="textarea"]:hover > div,
        div[data-baseweb="select"]:hover > div {
            border-color: #93c5fd !important; /* Soft professional blue border on hover */
            background-color: #f8fafc !important;
            box-shadow: 0 2px 4px 0 rgba(59, 130, 246, 0.05) !important;
        }
        
        @keyframes customBlink {
            0%, 100% { border-color: rgba(59, 130, 246, 1); box-shadow: 0 0 0 6px rgba(59, 130, 246, 0.2); }
            50% { border-color: rgba(59, 130, 246, 0.4); box-shadow: 0 0 0 2px rgba(59, 130, 246, 0.05); }
        }
        
        div[data-baseweb="input"]:focus-within > div, 
        div[data-baseweb="textarea"]:focus-within > div, 
        div[data-baseweb="select"]:focus-within > div {
            border-color: #3b82f6 !important;
            animation: customBlink 1.5s ease-in-out infinite !important;
            transform: translateY(-2px) scale(1.01) !important;
            background-color: #f8fafc !important;
        }
        
        input, textarea, div[data-baseweb="select"] * {
            color: #0f172a !important;
            font-weight: 500 !important;
        }

        input:focus, textarea:focus {
            caret-color: #2563eb !important;
        }
        
        input::placeholder, textarea::placeholder {
            color: #94a3b8 !important;
            font-weight: 400 !important;
        }
        
        div[data-testid="stTextInput"] label, div[data-testid="stTextArea"] label, div[data-testid="stSelectbox"] label {
            color: #0f172a !important;
            font-weight: 600 !important;
            font-size: 0.95rem !important;
        }

        /* Modern Headers */
        h1, h2, h3, .stHeadingContainer h1 {
            color: #0f172a !important;
            font-weight: 800 !important;
            letter-spacing: -0.03em !important;
        }

        /* Primary Buttons */
        .stButton > button {
            background: linear-gradient(135deg, #2563eb 0%, #4f46e5 100%) !important;
            color: #ffffff !important;
            font-weight: 600 !important;
            border-radius: 10px !important;
            border: none !important;
            padding: 0.6rem 1.5rem !important;
            box-shadow: 0 4px 6px -1px rgba(59, 130, 246, 0.3), 0 2px 4px -1px rgba(59, 130, 246, 0.2) !important;
            transition: all 0.2s cubic-bezier(0.4, 0, 0.2, 1) !important;
        }
        .stButton > button:hover {
            transform: translateY(-2px) !important;
            box-shadow: 0 10px 15px -3px rgba(59, 130, 246, 0.4), 0 4px 6px -2px rgba(59, 130, 246, 0.2) !important;
        }

        /* Disabled Button States (Professional Faded Processing) */
        .stButton > button:disabled {
            background: #94a3b8 !important; /* Muted Slate Gray instead of bright blue/red */
            color: #f8fafc !important;
            cursor: not-allowed !important;
            box-shadow: none !important;
            border: 1px solid #cbd5e1 !important;
            transform: none !important;
            opacity: 0.65 !important;
        }
        .stButton > button:disabled * {
            color: #f8fafc !important;
            font-weight: 600 !important;
        }
        .stButton > button:disabled:hover {
            border-style: solid !important;
            background: #94a3b8 !important; 
        }
        
        .stButton > button * {
            color: #ffffff !important;
        }

        /* Alerts and Callouts */
        div[data-testid="stAlert"] {
            border-radius: 12px !important;
            border: 1px solid rgba(0,0,0,0.05) !important;
            box-shadow: 0 4px 6px -1px rgba(0, 0, 0, 0.05) !important;
            color: #0f172a !important;
        }
        div[data-testid="stAlert"] p {
            color: #1e293b !important;
            font-weight: 500 !important;
        }

        /* --- THE NEW EDUMATE LOGO --- */
        .edumate-header {
            display: flex;
            align-items: center;
            justify-content: center;
            gap: 1.25rem;
            margin-bottom: 2rem;
            margin-top: 1rem;
        }
        
        .logo-shape {
            display: flex;
            align-items: center;
            justify-content: center;
            width: 80px;
            height: 80px;
            background: linear-gradient(135deg, #0f172a, #3b82f6);
            border-radius: 20px;
            box-shadow: 0 10px 25px -5px rgba(59, 130, 246, 0.4);
            transform: rotate(-5deg);
        }
        
        .logo-shape span {
            font-size: 2.5rem;
            transform: rotate(5deg);
        }
        
        .logo-title {
            font-size: 4rem;
            font-weight: 900;
            background: linear-gradient(to right, #0f172a, #1d4ed8);
            -webkit-background-clip: text;
            -webkit-text-fill-color: transparent;
            letter-spacing: -2px;
            line-height: 1.1;
            margin: 0;
        }
        
        .fade-in-text {
            animation: fadeIn 1.2s cubic-bezier(0.4, 0, 0.2, 1);
            margin-bottom: 3rem;
        }
        
        @keyframes fadeIn {
            from { opacity: 0; transform: translateY(15px); }
            to { opacity: 1; transform: translateY(0); }
        }

        /* Glassmorphism Clickable Cards */
        .glass-card {
            display: block;
            text-decoration: none !important;
            background: rgba(255, 255, 255, 0.6);
            backdrop-filter: blur(16px);
            border: 1px solid rgba(255, 255, 255, 0.8);
            border-radius: 20px;
            padding: 2rem;
            color: inherit;
            transition: all 0.4s cubic-bezier(0.4, 0, 0.2, 1);
            box-shadow: 0 4px 15px -1px rgba(15, 23, 42, 0.05);
            position: relative;
            overflow: hidden;
        }
        
        .glass-card::before {
            content: "";
            position: absolute;
            top: 0; left: 0; right: 0; bottom: 0;
            background: linear-gradient(135deg, rgba(255,255,255,0.4) 0%, rgba(255,255,255,0) 100%);
            opacity: 0;
            transition: opacity 0.4s ease;
        }

        .glass-card:hover {
            transform: translateY(-8px);
            background: rgba(255, 255, 255, 0.95);
            box-shadow: 0 20px 40px -5px rgba(59, 130, 246, 0.15), 0 10px 20px -5px rgba(59, 130, 246, 0.1);
            border-color: rgba(59, 130, 246, 0.4);
            cursor: pointer;
        }
        
        .glass-card:hover::before {
            opacity: 1;
        }

        .glass-card h3 {
            margin-top: 0;
            color: #0f172a !important;
            font-size: 1.35rem !important;
            font-weight: 800 !important;
            margin-bottom: 0.5rem;
            position: relative;
        }

        .glass-card p {
            margin-bottom: 0;
            color: #475569 !important;
            font-size: 1.05rem !important;
            line-height: 1.5;
            position: relative;
        }

        /* Rename sidebar app nav */
        [data-testid="stSidebarNavItems"] li:first-child a span {
            display: none !important;
        }
        [data-testid="stSidebarNavItems"] li:first-child a::after {
            content: "Home";
            font-size: 1rem;
            font-weight: 600;
            color: #0f172a;
            display: block;
            visibility: visible;
        }
        
        @keyframes containerFadeIn {
            0% { opacity: 0; transform: translateY(15px); }
            100% { opacity: 1; transform: translateY(0); }
        }

        /* --- Professional MCQ styling for Radio Buttons (Vertical Quizzes Only) --- */
        div[role="radiogroup"]:not([aria-orientation="horizontal"]) {
            display: flex;
            flex-direction: column;
            gap: 0.85rem;
            margin-top: 0.5rem;
            margin-bottom: 2rem;
        }

        div[role="radiogroup"]:not([aria-orientation="horizontal"]) > label {
            width: 100%;
            margin: 0 !important;
            padding: 0 !important;
        }

        /* Glass / Card styling for MCQ Options */
        div[role="radiogroup"]:not([aria-orientation="horizontal"]) label[data-baseweb="radio"] {
            background-color: #ffffff;
            border: 1.5px solid #e2e8f0; /* Thinner, sleeker default border */
            border-radius: 12px;
            padding: 1.15rem 1.5rem;
            cursor: pointer;
            transition: all 0.2s cubic-bezier(0.4, 0, 0.2, 1);
            display: flex; /* Force specific flex rules for alignment */
            align-items: center !important; /* Force align middle */
            box-shadow: 0 1px 3px 0 rgba(15, 23, 42, 0.05);
            width: 100%;
        }

        /* Hover state for MCQ Card */
        div[role="radiogroup"]:not([aria-orientation="horizontal"]) label[data-baseweb="radio"]:hover {
            border-color: #93c5fd; /* Soft professional blue border, no thickness change */
            background-color: #f8fafc;
            transform: translateY(-2px);
            box-shadow: 0 4px 8px -2px rgba(33, 150, 243, 0.12);
        }

        /* Selected State for MCQ Card */
        div[role="radiogroup"]:not([aria-orientation="horizontal"]) label[data-baseweb="radio"]:has(input:checked) {
            border-color: #3b82f6; /* Modern Blue, consistent thickness */
            background-color: #eff6ff; 
            box-shadow: 0 0 0 1px rgba(59, 130, 246, 0.1), 0 4px 10px -2px rgba(59, 130, 246, 0.15);
        }

        /* Outer container for the text to ensure it stays horizontally aligned with the centered dot */
        div[role="radiogroup"]:not([aria-orientation="horizontal"]) div[data-testid="stMarkdownContainer"] {
            display: flex;
            align-items: center;
        }

        /* MCQ Text Styling */
        div[role="radiogroup"]:not([aria-orientation="horizontal"]) div[data-testid="stMarkdownContainer"] p {
            color: #334155 !important;
            font-weight: 500 !important;
            font-size: 1.05rem !important;
            margin: 0 !important;
            line-height: 1.5;
        }

        /* MCQ Selected Text */
        div[role="radiogroup"]:not([aria-orientation="horizontal"]) label[data-baseweb="radio"]:has(input:checked) div[data-testid="stMarkdownContainer"] p {
            color: #0d47a1 !important; /* Material Blue 900 */
            font-weight: 700 !important;
        }

        /* --- THE RADIO BUTTON ITSELF (Widget.MaterialComponents.CompoundButton.RadioButton) --- */
        div[role="radiogroup"] label[data-baseweb="radio"] > div:first-child {
            margin-right: 1.25rem !important;
            background-color: transparent !important;
            border: 2px solid #757575 !important; /* Material Unchecked Grey 600 */
            width: 20px !important;
            height: 20px !important;
            min-width: 20px !important;
            min-height: 20px !important;
            border-radius: 50% !important;
            display: flex;
            align-items: center;
            justify-content: center;
            transition: border-color 0.2s ease, box-shadow 0.2s ease;
            position: relative;
        }
        
        /* Material Ripple halo approximation on outer circle */
        div[role="radiogroup"]:not([aria-orientation="horizontal"]) label[data-baseweb="radio"]:hover > div:first-child {
            box-shadow: 0 0 0 10px rgba(33, 150, 243, 0.1); 
            border-color: #64b5f6 !important;
        }

        /* Checked State - Outer Ring */
        div[role="radiogroup"] label[data-baseweb="radio"]:has(input:checked) > div:first-child {
            border-color: #2196F3 !important; /* Material Blue 500 */
        }

        /* Material Inner Dot */
        div[role="radiogroup"] label[data-baseweb="radio"] > div:first-child::after {
            content: "";
            width: 10px;
            height: 10px;
            background-color: #2196F3;
            border-radius: 50%;
            transform: scale(0);
            transition: transform 0.2s cubic-bezier(0.4, 0, 0.2, 1);
            position: absolute;
        }

        /* Scale up inner dot */
        div[role="radiogroup"] label[data-baseweb="radio"]:has(input:checked) > div:first-child::after {
            transform: scale(1);
        }

        /* Completely hide Streamlit default internal svg */
        div[role="radiogroup"] label[data-baseweb="radio"] > div:first-child svg {
            display: none !important;
        }

        /* --- Minimalist styling for Horizontal Radio Buttons (Settings/Difficulty) --- */
        div[role="radiogroup"][aria-orientation="horizontal"] {
            display: flex;
            gap: 1.5rem;
            margin-top: 0.25rem;
            margin-bottom: 0.5rem;
        }

        div[role="radiogroup"][aria-orientation="horizontal"] label[data-baseweb="radio"] {
            cursor: pointer;
            display: flex;
            align-items: center;
            background: transparent !important;
            padding: 0.25rem 0.5rem !important;
            border: none !important;
            box-shadow: none !important;
            border-radius: 8px;
            transition: background 0.2s ease;
        }

        div[role="radiogroup"][aria-orientation="horizontal"] label[data-baseweb="radio"]:hover {
            background: rgba(33, 150, 243, 0.1) !important;
            transform: none !important;
        }

        div[role="radiogroup"][aria-orientation="horizontal"] div[data-testid="stMarkdownContainer"],
        div[role="radiogroup"][aria-orientation="horizontal"] div[data-testid="stMarkdownContainer"] p {
            color: #475569 !important;
            font-weight: 500 !important;
            font-size: 0.95rem !important;
            margin: 0;
            line-height: normal;
            cursor: pointer !important;
        }

        div[role="radiogroup"][aria-orientation="horizontal"] label[data-baseweb="radio"]:has(input:checked) div[data-testid="stMarkdownContainer"] p {
            color: #0f172a !important;
            font-weight: 700 !important;
            cursor: pointer !important;
        }
        
        div[role="radiogroup"][aria-orientation="horizontal"] label[data-baseweb="radio"] > div:first-child {
            margin-right: 0.5rem !important;
            width: 18px !important;
            height: 18px !important;
        }
        
        div[role="radiogroup"][aria-orientation="horizontal"] label[data-baseweb="radio"] > div:first-child::after {
            width: 8px !important;
            height: 8px !important;
        }

        /* Give Glassmorphism a subtle touch on main container */
        .block-container {
            animation: containerFadeIn 0.8s cubic-bezier(0.2, 0.8, 0.2, 1) forwards;
            background-color: rgba(255, 255, 255, 0.3);
            backdrop-filter: blur(12px);
            border: 1px solid rgba(255, 255, 255, 0.4);
            border-radius: 30px;
            padding: 3rem !important;
            box-shadow: 0 20px 40px rgba(0, 0, 0, 0.05);
            margin-top: 2rem;
            margin-bottom: 2rem;
        }
        </style>
    """, unsafe_allow_html=True)
