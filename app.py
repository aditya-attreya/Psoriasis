import streamlit as st
from datetime import datetime

# ========================================================================
# MAIN APP - Entry Point for Multipage Streamlit Application
# File name: app.py (in psoriasis_cdss/ directory)
# ========================================================================
# This is the ONLY file that should have st.set_page_config()
# ========================================================================

# Page Configuration (ONLY in main app.py)
st.set_page_config(
    page_title="Psoriasis Clinical Decision Support System",
    page_icon="🩺",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Initialize Session State Variables
if 'patient_info' not in st.session_state:
    st.session_state.patient_info = {}

if 'diagnostic_score' not in st.session_state:
    st.session_state.diagnostic_score = None

if 'identified_types' not in st.session_state:
    st.session_state.identified_types = []

if 'pasi_score' not in st.session_state:
    st.session_state.pasi_score = None

if 'bsa_score' not in st.session_state:
    st.session_state.bsa_score = None

if 'dlqi_score' not in st.session_state:
    st.session_state.dlqi_score = None

# Professional CSS Styling
st.markdown("""
<style>
    * {
        font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
    }
    
    .main-header {
        background: linear-gradient(135deg, #1e3a5f 0%, #2d5a8c 100%);
        color: white;
        padding: 2rem;
        border-radius: 10px;
        text-align: center;
        margin-bottom: 2rem;
    }
    
    .main-header h1 {
        margin: 0;
        font-size: 2.5rem;
        font-weight: 700;
    }
    
    .subtitle {
        color: #e0e0e0;
        font-size: 1.1rem;
        margin-top: 0.5rem;
    }
    
    .info-box {
        background-color: #f0f8ff;
        padding: 1.5rem;
        border-radius: 10px;
        border-left: 5px solid #1e3a5f;
        margin: 1rem 0;
    }
    
    .workflow-box {
        background: linear-gradient(135deg, #f5f7fa 0%, #c3cfe2 100%);
        padding: 1.5rem;
        border-radius: 10px;
        margin: 1rem 0;
    }
    
    .step-box {
        background-color: #f9f9f9;
        padding: 1rem;
        border-radius: 8px;
        border-left: 4px solid #667eea;
        margin: 0.5rem 0;
    }
    
    .status-box {
        background-color: #e8f5e9;
        border: 1px solid #4caf50;
        padding: 1rem;
        border-radius: 8px;
        margin: 1rem 0;
    }
    
    .footer {
        text-align: center;
        color: #666;
        font-size: 0.9rem;
        margin-top: 3rem;
        padding-top: 2rem;
        border-top: 1px solid #ddd;
    }
</style>
""", unsafe_allow_html=True)

# Main Header
st.markdown("""
<div class="main-header">
    <h1>🩺 Psoriasis Clinical Decision Support System</h1>
    <p class="subtitle">Comprehensive Diagnostic and Severity Assessment Platform</p>
</div>
""", unsafe_allow_html=True)

# Introduction Section
st.markdown("""
<div class="info-box">
    <h3>Welcome to the Psoriasis CDSS</h3>
    <p>This system provides a comprehensive approach to psoriasis evaluation through:</p>
    <ul>
    <li>Patient demographic information collection</li>
    <li>Diagnostic screening using clinical criteria</li>
    <li>Psoriasis subtype identification</li>
    <li>Severity assessment using PASI, BSA, and DLQI scales</li>
    <li>Evidence-based treatment recommendations</li>
    </ul>
</div>
""", unsafe_allow_html=True)

# Workflow Section
st.markdown("## 📊 System Workflow")

st.markdown("""
<div class="workflow-box">
    <h3>Follow These Steps:</h3>
</div>
""", unsafe_allow_html=True)

col1, col2, col3, col4 = st.columns(4)

with col1:
    st.markdown("""
    <div class="step-box">
    <b>Step 1️⃣</b><br>
    <b>Patient Registration</b><br>
    Collect patient demographics and clinical history
    </div>
    """, unsafe_allow_html=True)

with col2:
    st.markdown("""
    <div class="step-box">
    <b>Step 2️⃣</b><br>
    <b>Diagnostic Screening</b><br>
    12 diagnostic questions to assess psoriasis likelihood
    </div>
    """, unsafe_allow_html=True)

with col3:
    st.markdown("""
    <div class="step-box">
    <b>Step 3️⃣</b><br>
    <b>Type Identification</b><br>
    Classify psoriasis subtypes based on presentation
    </div>
    """, unsafe_allow_html=True)

with col4:
    st.markdown("""
    <div class="step-box">
    <b>Step 4️⃣</b><br>
    <b>Severity Assessment</b><br>
    Calculate PASI, BSA, DLQI scores and get recommendations
    </div>
    """, unsafe_allow_html=True)

# Navigation Instructions
st.markdown("---")
st.markdown("## 🗺️ Navigation Guide")

st.markdown("""
<div class="info-box">
    <h4>How to Use This Application:</h4>
    <ol>
    <li><b>Look at the sidebar</b> on the left - you will see 4 module buttons</li>
    <li><b>Click each module in order:</b>
        <ul>
        <li>1️⃣ Patient Registration</li>
        <li>2️⃣ Diagnostic Screening</li>
        <li>3️⃣ Type Identification</li>
        <li>4️⃣ Severity Assessment</li>
        </ul>
    </li>
    <li><b>Complete each step</b> to unlock the next one</li>
    <li><b>Data persists</b> as you navigate between modules</li>
    <li><b>Review results</b> at the end for treatment recommendations</li>
    </ol>
</div>
""", unsafe_allow_html=True)

# Current Status Section
st.markdown("---")
st.markdown("## 📋 Current Status")

status_col1, status_col2 = st.columns(2)

with status_col1:
    st.markdown("<div class='status-box'><b>✅ Patient Registered:</b> " + 
                ("Yes - " + st.session_state.patient_info.get('patient_name', 'Unknown') if st.session_state.patient_info else "No") + 
                "</div>", unsafe_allow_html=True)

with status_col2:
    st.markdown("<div class='status-box'><b>✅ Diagnostic Score:</b> " + 
                (str(st.session_state.diagnostic_score) if st.session_state.diagnostic_score else "Not Yet Assessed") + 
                "</div>", unsafe_allow_html=True)

col3, col4 = st.columns(2)

with col3:
    st.markdown("<div class='status-box'><b>✅ Types Identified:</b> " + 
                (str(len(st.session_state.identified_types)) + " type(s)" if st.session_state.identified_types else "Not Yet Assessed") + 
                "</div>", unsafe_allow_html=True)

with col4:
    st.markdown("<div class='status-box'><b>✅ Severity Assessed:</b> " + 
                ("Yes - PASI: " + str(round(st.session_state.pasi_score, 2)) if st.session_state.pasi_score else "Not Yet Assessed") + 
                "</div>", unsafe_allow_html=True)

# Key Features Section
st.markdown("---")
st.markdown("## ✨ Key Features")

feature_col1, feature_col2, feature_col3 = st.columns(3)

with feature_col1:
    st.markdown("""
    ### 📝 Comprehensive Assessment
    - Patient demographics
    - Clinical history
    - Disease duration tracking
    - Treatment modality recording
    """)

with feature_col2:
    st.markdown("""
    ### 🎯 Evidence-Based Evaluation
    - 12 diagnostic criteria
    - 7 psoriasis subtypes
    - PASI scoring system
    - BSA and DLQI assessment
    """)

with feature_col3:
    st.markdown("""
    ### 💊 Treatment Guidance
    - Severity classification
    - Personalized recommendations
    - Topical/systemic options
    - Biologic therapy guidance
    """)

# Getting Started Section
st.markdown("---")
st.markdown("## 🚀 Getting Started")

st.markdown("""
<div class="info-box">
    <h4>To Begin Assessment:</h4>
    <p><b>👉 Look at the sidebar and click on:</b></p>
    <p style="font-size: 1.1rem; color: #667eea;">
    <b>1_Patient_Registration</b>
    </p>
    <p>This will open the first module where you can register a patient and begin the comprehensive assessment process.</p>
</div>
""", unsafe_allow_html=True)

# Important Notes
st.markdown("---")
st.markdown("## ℹ️ Important Notes")

st.info("""
✓ **Data Persistence:** All patient data is stored in session memory and persists as you navigate between modules.

✓ **Required Sequence:** Complete modules in order (1→2→3→4) for best results.

✓ **Clinical Use:** This system is designed to support clinical decision-making and should be used with qualified healthcare professionals.

✓ **Prerequisite Checks:** Each module verifies that the previous step is complete before allowing access.
""")

# Technical Information
with st.expander("ℹ️ Technical Information"):
    st.markdown("""
    **Architecture:**
    - Main App: `app.py` (current file)
    - Page Modules: Located in `pages/` directory
      - `1_Patient_Registration.py`
      - `2_Diagnostic_Screening.py`
      - `3_Type_Identification.py`
      - `4_Severity_Assessment.py`
    
    **Session State Variables:**
    - `patient_info`: Patient demographics
    - `diagnostic_score`: Screening score
    - `identified_types`: Selected psoriasis types
    - `pasi_score`: Severity index
    - `bsa_score`: Body surface area
    - `dlqi_score`: Quality of life index
    
    **Framework:** Streamlit 1.28+
    
    **Dependencies:**
    - pandas
    - numpy
    - plotly
    """)

# Footer
st.markdown("""
<div class="footer">
    <p><strong>Psoriasis Clinical Decision Support System</strong></p>
    <p>Version 1.0 | Multipage Application</p>
    <p>For clinical use in controlled settings. Always consult qualified healthcare professionals.</p>
    <p style="font-size: 0.85rem; color: #999;">
    Last Updated: """ + datetime.now().strftime("%Y-%m-%d %H:%M:%S") + """
    </p>
</div>
""", unsafe_allow_html=True)
