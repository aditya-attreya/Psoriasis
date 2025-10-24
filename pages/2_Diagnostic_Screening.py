import streamlit as st
import pandas as pd
from datetime import datetime

# Check if patient is registered (prerequisite check)
if 'patient_info' not in st.session_state or not st.session_state.patient_info:
    st.warning("⚠️ Please complete Patient Registration first")
    st.info("Use the sidebar to navigate to '1_Patient_Registration'")
    st.stop()

if 'diagnostic_score' not in st.session_state:
    st.session_state.diagnostic_score = None

# Custom CSS
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
    
    .question-box {
        background-color: #f9f9f9;
        padding: 1.5rem;
        border-radius: 10px;
        border-left: 4px solid #667eea;
        margin: 1rem 0;
    }
    
    .score-display {
        background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
        color: white;
        padding: 1.5rem;
        border-radius: 10px;
        text-align: center;
        margin: 1rem 0;
        font-size: 1.2rem;
        font-weight: bold;
    }
    
    .recommendation-high {
        background-color: #fff3cd;
        border-left: 4px solid #ffc107;
        padding: 1rem;
        border-radius: 10px;
    }
    
    .recommendation-moderate {
        background-color: #d1ecf1;
        border-left: 4px solid #17a2b8;
        padding: 1rem;
        border-radius: 10px;
    }
    
    .recommendation-mild {
        background-color: #d4edda;
        border-left: 4px solid #28a745;
        padding: 1rem;
        border-radius: 10px;
    }
</style>
""", unsafe_allow_html=True)

st.markdown('<div class="main-header"><h2>🔍 Diagnostic Screening Matrix</h2></div>', unsafe_allow_html=True)

patient_name = st.session_state.patient_info.get('patient_name', 'Unknown')
st.markdown(f"**Patient:** {patient_name}")
st.markdown("---")

def yes_no_question(question_num, question_text, weight=1):
    st.markdown(f'<div class="question-box"><b>Q{question_num}:</b> {question_text}</div>', unsafe_allow_html=True)
    response = st.radio(f"Answer:", ["Select", "Yes", "No"], key=f"q{question_num}", horizontal=True)
    if response == "Yes":
        return weight
    elif response == "No":
        return 0
    else:
        return None

st.markdown("### Clinical Screening Questions")

scores = {}

st.markdown("#### Section 1: Clinical Presentation")
scores['q1'] = yes_no_question(1, "Do you observe well-demarcated erythematous plaques with silvery-white scales?", 3)
scores['q2'] = yes_no_question(2, "Is the distribution symmetric (bilateral)?", 2)
scores['q3'] = yes_no_question(3, "Are plaques in characteristic areas (elbows, knees, scalp)?", 2)

st.markdown("#### Section 2: Associated Features")
scores['q4'] = yes_no_question(4, "Do you observe nail involvement (pitting, discoloration)?", 2)
scores['q5'] = yes_no_question(5, "Does patient report joint pain or swelling?", 2)
scores['q6'] = yes_no_question(6, "Are sterile pustules present on erythematous base?", 2)

st.markdown("#### Section 3: Severity Indicators")
scores['q7'] = yes_no_question(7, "Does affected body surface area appear >10%?", 3)
scores['q8'] = yes_no_question(8, "Does the lesion show deep inflammation?", 2)
scores['q9'] = yes_no_question(9, "Does patient report significant pruritus/itching?", 1)

st.markdown("#### Section 4: Patient History")
scores['q10'] = yes_no_question(10, "Is there a family history of psoriasis?", 2)
scores['q11'] = yes_no_question(11, "Were lesions preceded by infection or stress?", 1)
scores['q12'] = yes_no_question(12, "Does patient report chronic/recurrent course?", 2)

st.markdown("---")
st.markdown("### Diagnostic Assessment")

valid_scores = {k: v for k, v in scores.items() if v is not None}

if len(valid_scores) == len(scores):
    total_score = sum(valid_scores.values())
    max_possible_score = 28
    percentage_score = (total_score / max_possible_score) * 100
    
    st.markdown(f'<div class="score-display">Diagnostic Score: {total_score}/{max_possible_score} ({percentage_score:.1f}%)</div>', unsafe_allow_html=True)
    
    if percentage_score >= 75:
        recommendation = "HIGH likelihood of psoriasis. Recommend immediate dermatological evaluation."
        st.markdown(f'<div class="recommendation-high">⚠️ <b>HIGH SUSPICION:</b> {recommendation}</div>', unsafe_allow_html=True)
        severity_level = "High"
    elif percentage_score >= 50:
        recommendation = "MODERATE likelihood. Clinical evaluation recommended."
        st.markdown(f'<div class="recommendation-moderate">ℹ️ <b>MODERATE SUSPICION:</b> {recommendation}</div>', unsafe_allow_html=True)
        severity_level = "Moderate"
    else:
        recommendation = "LOW likelihood. Consider alternative diagnoses."
        st.markdown(f'<div class="recommendation-mild">✓ <b>LOW SUSPICION:</b> {recommendation}</div>', unsafe_allow_html=True)
        severity_level = "Low"
    
    st.session_state.diagnostic_score = total_score
    
    col1, col2 = st.columns(2)
    with col1:
        st.success("✅ Diagnostic screening complete!")
    with col2:
        st.balloons()
    
    results_df = pd.DataFrame({
        'Metric': ['Total Score', 'Maximum Score', 'Percentage', 'Severity Level'],
        'Value': [total_score, max_possible_score, f'{percentage_score:.1f}%', severity_level]
    })
    st.dataframe(results_df, use_container_width=True)
    
    st.markdown("---")
    st.info("""
    ➡️ **Next Step:** Proceed to **'Type Identification'** in the sidebar
    """)
else:
    st.warning(f"⚠️ Please answer all {len(scores)} questions")

st.markdown("---")
st.markdown("<div style='text-align: center; color: #666;'><p><strong>Diagnostic Screening Module</strong></p></div>", unsafe_allow_html=True)
