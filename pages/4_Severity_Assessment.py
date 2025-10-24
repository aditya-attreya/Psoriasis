import streamlit as st
import pandas as pd
import numpy as np
from datetime import datetime
import plotly.express as px
import plotly.graph_objects as go

# ========================================================================
# MULTIPAGE APP - Page Module 4: Severity Assessment
# File name: 4_Severity_Assessment.py (for pages/ directory)
# ========================================================================
# NOTE: st.set_page_config() is REMOVED - only main app.py should have it
# ========================================================================

# Check if patient is registered (prerequisite check)
if 'patient_info' not in st.session_state or not st.session_state.patient_info:
    st.warning("⚠️ Please complete Patient Registration first")
    st.info("Use the sidebar to navigate to '1_Patient_Registration'")
    st.stop()

# Initialize severity scores
if 'pasi_score' not in st.session_state:
    st.session_state.pasi_score = None
if 'bsa_score' not in st.session_state:
    st.session_state.bsa_score = None
if 'dlqi_score' not in st.session_state:
    st.session_state.dlqi_score = None

st.markdown("""
<style>
    .main-header {
        background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
        color: white;
        padding: 1.5rem;
        border-radius: 10px;
        text-align: center;
        margin-bottom: 1rem;
    }
    
    .score-box {
        background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
        color: white;
        padding: 1.5rem;
        border-radius: 10px;
        text-align: center;
        margin: 1rem 0;
        font-size: 1.2rem;
        font-weight: bold;
    }
    
    .severity-mild {
        background-color: #d4edda;
        border-left: 4px solid #28a745;
        padding: 1rem;
        border-radius: 10px;
    }
    
    .severity-moderate {
        background-color: #fff3cd;
        border-left: 4px solid #ffc107;
        padding: 1rem;
        border-radius: 10px;
    }
    
    .severity-severe {
        background-color: #f8d7da;
        border-left: 4px solid #dc3545;
        padding: 1rem;
        border-radius: 10px;
    }
    
    .treatment-box {
        background-color: #e7f3ff;
        border-left: 4px solid #0066cc;
        padding: 1rem;
        border-radius: 10px;
    }
</style>
""", unsafe_allow_html=True)

st.markdown('<div class="main-header"><h2>📊 Severity Assessment</h2></div>', unsafe_allow_html=True)

# Get patient info
patient_name = st.session_state.patient_info.get('patient_name', 'Unknown')
patient_age = st.session_state.patient_info.get('patient_age', 0)
st.markdown(f"**Patient:** {patient_name} | **Age:** {patient_age} years")
st.markdown("---")

# PASI Scoring Section
st.markdown("## 📌 PASI (Psoriasis Area and Severity Index)")
st.markdown("**Score range: 0-72** (Higher = More Severe)")
st.info("Assess erythema (redness), desquamation (scaling), and induration (thickening) for each body area")

col1, col2, col3, col4 = st.columns(4)

with col1:
    st.markdown("### HEAD (10%)")
    head_area = st.slider("Head Area (%)", 0, 100, 10, key="head_area")
    head_erythema = st.slider("Head Erythema (0-4)", 0, 4, 2, key="head_erythema")
    head_desquamation = st.slider("Head Desquamation (0-4)", 0, 4, 2, key="head_desq")
    head_induration = st.slider("Head Induration (0-4)", 0, 4, 2, key="head_indu")

with col2:
    st.markdown("### TRUNK (30%)")
    trunk_area = st.slider("Trunk Area (%)", 0, 100, 20, key="trunk_area")
    trunk_erythema = st.slider("Trunk Erythema (0-4)", 0, 4, 2, key="trunk_erythema")
    trunk_desquamation = st.slider("Trunk Desquamation (0-4)", 0, 4, 2, key="trunk_desq")
    trunk_induration = st.slider("Trunk Induration (0-4)", 0, 4, 2, key="trunk_indu")

with col3:
    st.markdown("### UPPER EXTREMITY (20%)")
    ue_area = st.slider("Upper Extremity Area (%)", 0, 100, 15, key="ue_area")
    ue_erythema = st.slider("UE Erythema (0-4)", 0, 4, 2, key="ue_erythema")
    ue_desquamation = st.slider("UE Desquamation (0-4)", 0, 4, 2, key="ue_desq")
    ue_induration = st.slider("UE Induration (0-4)", 0, 4, 2, key="ue_indu")

with col4:
    st.markdown("### LOWER EXTREMITY (40%)")
    le_area = st.slider("Lower Extremity Area (%)", 0, 100, 25, key="le_area")
    le_erythema = st.slider("LE Erythema (0-4)", 0, 4, 2, key="le_erythema")
    le_desquamation = st.slider("LE Desquamation (0-4)", 0, 4, 2, key="le_desq")
    le_induration = st.slider("LE Induration (0-4)", 0, 4, 2, key="le_indu")

# PASI Calculation
pasi_head = (head_area / 100) * 4 * (head_erythema + head_desquamation + head_induration)
pasi_trunk = (trunk_area / 100) * 4 * (trunk_erythema + trunk_desquamation + trunk_induration)
pasi_ue = (ue_area / 100) * 4 * (ue_erythema + ue_desquamation + ue_induration)
pasi_le = (le_area / 100) * 4 * (le_erythema + le_desquamation + le_induration)

total_pasi = pasi_head * 0.1 + pasi_trunk * 0.3 + pasi_ue * 0.2 + pasi_le * 0.4

st.markdown(f'<div class="score-box">PASI Score: {total_pasi:.2f} / 72</div>', unsafe_allow_html=True)

# BSA Scoring Section
st.markdown("---")
st.markdown("## 📌 BSA (Body Surface Area)")
st.markdown("**Percentage of body surface area affected: 0-100%**")
st.info("Estimate the percentage of total body surface area covered by psoriasis")

bsa = st.slider("BSA (%)", 0, 100, 25, key="bsa_slider")

st.markdown(f'<div class="score-box">BSA Score: {bsa}%</div>', unsafe_allow_html=True)

# DLQI Scoring Section
st.markdown("---")
st.markdown("## 📌 DLQI (Dermatology Life Quality Index)")
st.markdown("**Score range: 0-30** (Higher = More Impact on Quality of Life)")
st.info("Rate how much each aspect affects the patient's quality of life (0=Not at all, 3=Very much)")

dlqi_scores = {}
dlqi_scores['Q1'] = st.slider("Q1: How itchy, sore, or painful has your skin been?", 0, 3, 0, key="dlqi_q1")
dlqi_scores['Q2'] = st.slider("Q2: How embarrassed or self-conscious have you been?", 0, 3, 0, key="dlqi_q2")
dlqi_scores['Q3'] = st.slider("Q3: Interfered with shopping, housework, or gardening?", 0, 3, 0, key="dlqi_q3")
dlqi_scores['Q4'] = st.slider("Q4: Affected your choice of clothes?", 0, 3, 0, key="dlqi_q4")
dlqi_scores['Q5'] = st.slider("Q5: Affected social or leisure activities?", 0, 3, 0, key="dlqi_q5")
dlqi_scores['Q6'] = st.slider("Q6: Difficulty with sports/exercise?", 0, 3, 0, key="dlqi_q6")
dlqi_scores['Q7'] = st.slider("Q7: Prevented you from working/studying?", 0, 3, 0, key="dlqi_q7")
dlqi_scores['Q8'] = st.slider("Q8: Difficulty with partner/family/friends?", 0, 3, 0, key="dlqi_q8")
dlqi_scores['Q9'] = st.slider("Q9: Sexual difficulties?", 0, 3, 0, key="dlqi_q9")
dlqi_scores['Q10'] = st.slider("Q10: Problem with treatment side effects?", 0, 3, 0, key="dlqi_q10")

total_dlqi = sum(dlqi_scores.values())

st.markdown(f'<div class="score-box">DLQI Score: {total_dlqi} / 30</div>', unsafe_allow_html=True)

# Results Summary
st.markdown("---")
st.markdown("## 📊 Assessment Results Summary")

col1, col2, col3 = st.columns(3)
with col1:
    st.metric("PASI Score", f"{total_pasi:.2f}", "Severity Index")
with col2:
    st.metric("BSA Score", f"{bsa}%", "Body Surface Area")
with col3:
    st.metric("DLQI Score", f"{total_dlqi}", "Quality of Life")

# Severity Classification
st.markdown("---")
st.markdown("## 🎯 Severity Classification")

if total_pasi <= 10 and bsa <= 10:
    classification = "MILD"
    st.markdown('<div class="severity-mild">✅ <b>MILD PSORIASIS</b><br>Limited involvement, good prognosis with topical treatment</div>', unsafe_allow_html=True)
elif total_pasi <= 20 and bsa <= 30:
    classification = "MODERATE"
    st.markdown('<div class="severity-moderate">⚠️ <b>MODERATE PSORIASIS</b><br>Significant involvement, requires systemic treatment consideration</div>', unsafe_allow_html=True)
else:
    classification = "SEVERE"
    st.markdown('<div class="severity-severe">🔴 <b>SEVERE PSORIASIS</b><br>Extensive involvement, biologic therapy recommended</div>', unsafe_allow_html=True)

# Save scores to session state
st.session_state.pasi_score = total_pasi
st.session_state.bsa_score = bsa
st.session_state.dlqi_score = total_dlqi

# Treatment Recommendations
st.markdown("---")
st.markdown("## 💊 Treatment Recommendations")

if classification == "MILD":
    st.markdown("""
    <div class="treatment-box">
    <h4>Mild Psoriasis - First Line Treatment:</h4>
    <ul>
    <li>Topical corticosteroids (Class II-III)</li>
    <li>Topical vitamin D analogs (calcipotriene)</li>
    <li>Emollients and moisturizers</li>
    <li>Behavioral modifications (avoid triggers)</li>
    <li>Regular dermatology follow-up every 3-6 months</li>
    </ul>
    </div>
    """, unsafe_allow_html=True)
elif classification == "MODERATE":
    st.markdown("""
    <div class="treatment-box">
    <h4>Moderate Psoriasis - Second Line Treatment:</h4>
    <ul>
    <li>Systemic therapy (Methotrexate, Acitretin, Cyclosporine)</li>
    <li>Phototherapy (UVB, PUVA)</li>
    <li>Combination topical and systemic</li>
    <li>Consider biologic agents if inadequate response</li>
    <li>Rheumatology/Dermatology coordination</li>
    </ul>
    </div>
    """, unsafe_allow_html=True)
else:
    st.markdown("""
    <div class="treatment-box">
    <h4>Severe Psoriasis - Biologic/Advanced Treatment:</h4>
    <ul>
    <li>Biologic agents (TNF inhibitors: Etanercept, Infliximab)</li>
    <li>IL-17/IL-23 inhibitors (Secukinumab, Ixekizumab)</li>
    <li>JAK inhibitors (Tofacitinib)</li>
    <li>Multidisciplinary approach (Dermatology, Rheumatology, Psychiatry)</li>
    <li>Urgent specialist consultation recommended</li>
    </ul>
    </div>
    """, unsafe_allow_html=True)

# Completion message
col1, col2 = st.columns(2)
with col1:
    st.success("✅ Severity Assessment Complete!")
with col2:
    st.balloons()

# Results table
st.markdown("---")
st.markdown("## 📋 Complete Assessment Summary")

summary_data = {
    'Metric': ['PASI Score', 'BSA (%)', 'DLQI Score', 'Severity Classification', 'Treatment Tier'],
    'Value': [
        f"{total_pasi:.2f} / 72",
        f"{bsa}%",
        f"{total_dlqi} / 30",
        classification,
        "Mild" if classification == "MILD" else ("Moderate" if classification == "MODERATE" else "Severe")
    ]
}

summary_df = pd.DataFrame(summary_data)
st.dataframe(summary_df, use_container_width=True)

st.markdown("---")
st.markdown("<div style='text-align: center; color: #666;'><p><strong>Severity Assessment Module - Final Step Complete</strong></p></div>", unsafe_allow_html=True)
