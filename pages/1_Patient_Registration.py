import streamlit as st
from datetime import datetime

# ========================================================================
# MULTIPAGE APP - Page Module (intro_psorasis.py)
# Rename to: 1_Patient_Registration.py in pages/ directory
# ========================================================================
# NOTE: st.set_page_config() is removed - only main app.py should have it
# ========================================================================

# Professional CSS without emojis
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
    
    .info-box {
        background-color: #f0f8ff;
        padding: 1.5rem;
        border-radius: 10px;
        border-left: 5px solid #1e3a5f;
        margin: 1rem 0;
    }
    
    .form-container {
        background-color: #f9f9f9;
        padding: 2rem;
        border-radius: 10px;
        border: 1px solid #ddd;
        margin: 2rem 0;
    }
    
    .section-title {
        font-size: 1.5rem;
        font-weight: 700;
        color: #1e3a5f;
        margin: 1.5rem 0 1rem 0;
        border-bottom: 2px solid #ddd;
        padding-bottom: 0.5rem;
    }
</style>
""", unsafe_allow_html=True)

# Initialize session state variables
if 'patient_info' not in st.session_state:
    st.session_state.patient_info = {}

def page_introduction():
    """Display introduction and information about psoriasis"""
    st.markdown("""
    <div class="info-box">
        <h3>Welcome to Psoriasis Clinical Assessment System</h3>
        <p>Psoriasis is a chronic, non-contagious inflammatory skin disease that affects approximately 2-3% of the global population.</p>
    </div>
    """, unsafe_allow_html=True)
    
    st.markdown("**Psoriasis Pathophysiology:**")
    st.markdown("Psoriasis is characterized by abnormal keratinocyte proliferation and altered immune function, mediated by T-cell dysfunction and cytokine dysregulation.")
    
    st.markdown('<div class="section-title">Types of Psoriasis</div>', unsafe_allow_html=True)
    
    col1, col2 = st.columns(2)
    with col1:
        st.markdown("""
        **1. Plaque Psoriasis (80-90%)**
        - Well-demarcated erythematous plaques with silvery-white scales
        - Typically on elbows, knees, scalp, and lower back
        
        **2. Guttate Psoriasis (8-10%)**
        - Small drop-shaped papules and plaques
        - Often preceded by streptococcal pharyngitis
        """)
    
    with col2:
        st.markdown("""
        **3. Pustular Psoriasis (<1%)**
        - Sterile pustules on erythematous base
        - Can be localized or generalized
        
        **4. Inverse Psoriasis (3-7%)**
        - Smooth erythematous patches in skin folds
        - Without typical scales
        """)

def page_patient_registration():
    """Patient registration form"""
    st.markdown('<div class="section-title">👤 Patient Registration</div>', unsafe_allow_html=True)
    
    st.markdown("""
    <div class="info-box">
        <h4>Please enter patient demographic information</h4>
        <p>This information will be used throughout the assessment process.</p>
    </div>
    """, unsafe_allow_html=True)
    
    with st.form("patient_registration_form", clear_on_submit=False):
        col1, col2 = st.columns(2)
        
        with col1:
            patient_name = st.text_input(
                "Patient Name *",
                value=st.session_state.patient_info.get('patient_name', ''),
                help="Enter full name of the patient"
            )
            patient_age = st.number_input(
                "Age (years) *",
                min_value=0,
                max_value=150,
                value=st.session_state.patient_info.get('patient_age', 0),
                help="Enter patient age in years"
            )
        
        with col2:
            patient_sex = st.selectbox(
                "Sex/Gender *",
                options=['Select', 'Male', 'Female', 'Other', 'Prefer not to say'],
                index=['Select', 'Male', 'Female', 'Other', 'Prefer not to say'].index(
                    st.session_state.patient_info.get('patient_sex', 'Select')
                ),
                help="Select patient sex/gender"
            )
            patient_id = st.text_input(
                "Patient ID (Optional)",
                value=st.session_state.patient_info.get('patient_id', ''),
                help="Enter unique patient identifier if available"
            )
        
        st.markdown("**Clinical History** (Optional)")
        col1, col2 = st.columns(2)
        
        with col1:
            disease_duration = st.selectbox(
                "Disease Duration",
                options=['Select', 'Recently diagnosed', '<1 year', '1-5 years', '5-10 years', '>10 years'],
                index=['Select', 'Recently diagnosed', '<1 year', '1-5 years', '5-10 years', '>10 years'].index(
                    st.session_state.patient_info.get('disease_duration', 'Select')
                )
            )
        
        with col2:
            current_treatment = st.selectbox(
                "Current Treatment",
                options=['Select', 'None', 'Topical', 'Systemic', 'Biologic', 'Combination'],
                index=['Select', 'None', 'Topical', 'Systemic', 'Biologic', 'Combination'].index(
                    st.session_state.patient_info.get('current_treatment', 'Select')
                )
            )
        
        submitted = st.form_submit_button(
            "✅ Register Patient and Continue",
            type="primary",
            use_container_width=True
        )
        
        if submitted:
            if not patient_name.strip():
                st.error("❌ Patient name is required")
            elif patient_age <= 0:
                st.error("❌ Please enter a valid age")
            elif patient_sex == 'Select':
                st.error("❌ Please select patient sex/gender")
            else:
                st.session_state.patient_info = {
                    'patient_name': patient_name.strip(),
                    'patient_age': int(patient_age),
                    'patient_sex': patient_sex,
                    'patient_id': patient_id.strip() if patient_id else 'N/A',
                    'disease_duration': disease_duration if disease_duration != 'Select' else 'Not specified',
                    'current_treatment': current_treatment if current_treatment != 'Select' else 'Not specified',
                    'registration_date': datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
                    'registration_timestamp': datetime.now().isoformat()
                }
                
                st.success("✅ Patient registered successfully!")
                st.balloons()
                
                st.info("""
                ➡️ **Next Step:** Proceed to **'Diagnostic Screening'** in the sidebar
                
                The diagnostic screening matrix will help identify if this patient has psoriasis.
                """)
                
                st.markdown("**Registered Patient Information:**")
                st.json(st.session_state.patient_info)

def page_tool_selection():
    """Tool selection page"""
    st.markdown('<div class="section-title">🔧 Assessment Tools Overview</div>', unsafe_allow_html=True)
    
    if st.session_state.patient_info and st.session_state.patient_info.get('patient_name'):
        st.success(f"✅ Patient registered: **{st.session_state.patient_info.get('patient_name')}**")
        st.markdown("""
        ### Available Assessment Modules:
        
        1. **🔍 Diagnostic Screening** - Visual diagnostic matrix for psoriasis screening
        2. **🏷️ Type Identification** - Classification of psoriasis subtypes
        3. **📊 Severity Assessment** - PASI, BSA, and DLQI evaluation
        
        Use the **sidebar navigation** to access each module in sequence.
        """)
    else:
        st.warning("""
        ⚠️ **Patient Registration Required**
        
        Please complete the **Patient Registration** step first.
        """)

def main():
    """Main application"""
    st.markdown("""
    <div class="main-header">
        <h1>🩺 Psoriasis Clinical Assessment System</h1>
    </div>
    """, unsafe_allow_html=True)
    
    tab1, tab2, tab3 = st.tabs([
        "📚 Introduction",
        "👤 Patient Registration",
        "🔧 Assessment Tools"
    ])
    
    with tab1:
        page_introduction()
    with tab2:
        page_patient_registration()
    with tab3:
        page_tool_selection()
    
    st.markdown("---")
    st.markdown("""
    <div style="text-align: center; color: #666; font-size: 0.9rem;">
        <p><strong>Psoriasis Clinical Assessment System</strong></p>
    </div>
    """, unsafe_allow_html=True)

if __name__ == "__main__":
    main()
