import streamlit as st
from datetime import datetime


# Professional CSS without emojis
st.markdown("""
<style>
    * {
        font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
    }
    
    .main-header {
        background: linear-gradient(135deg, #1e3a5f 0%, #2d5a8c 100%);
        color: white;
        padding: 50px 40px;
        border-radius: 8px;
        text-align: center;
        margin-bottom: 40px;
        box-shadow: 0 4px 15px rgba(0,0,0,0.1);
    }
    
    .main-header h1 {
        margin: 0;
        font-size: 2.5em;
        font-weight: 600;
        letter-spacing: 0.5px;
    }
    
    .main-header p {
        margin: 10px 0 0 0;
        font-size: 1.1em;
        opacity: 0.95;
    }
    
    .section-title {
        font-size: 1.8em;
        font-weight: 600;
        color: #1e3a5f;
        margin-top: 40px;
        margin-bottom: 20px;
        border-bottom: 3px solid #2d5a8c;
        padding-bottom: 10px;
    }
    
    .content-card {
        background: #f8f9fa;
        border-left: 5px solid #2d5a8c;
        padding: 25px;
        margin: 15px 0;
        border-radius: 6px;
        box-shadow: 0 2px 8px rgba(0,0,0,0.05);
    }
    
    .definition-box {
        background: white;
        border: 1px solid #e0e6ed;
        border-radius: 6px;
        padding: 20px;
        margin: 15px 0;
    }
    
    .highlight-text {
        color: #2d5a8c;
        font-weight: 600;
    }
    
    .feature-list {
        list-style: none;
        padding-left: 0;
    }
    
    .feature-list li {
        padding: 10px 0;
        padding-left: 30px;
        position: relative;
        color: #333;
        line-height: 1.6;
    }
    
    .feature-list li:before {
        content: "•";
        position: absolute;
        left: 0;
        color: #2d5a8c;
        font-weight: bold;
        font-size: 1.2em;
    }
    
    .type-box {
        background: white;
        border: 1px solid #e0e6ed;
        border-radius: 6px;
        padding: 20px;
        box-shadow: 0 2px 8px rgba(0,0,0,0.05);
        margin-bottom: 15px;
    }
    
    .type-box h4 {
        color: #2d5a8c;
        margin-top: 0;
        font-size: 1.1em;
        border-bottom: 2px solid #e0e6ed;
        padding-bottom: 10px;
    }
    
    .type-box p {
        margin: 10px 0;
        color: #555;
        line-height: 1.6;
    }
    
    .patient-form {
        background: #f0f4f8;
        border: 1px solid #d0dce6;
        border-radius: 6px;
        padding: 30px;
        margin: 20px 0;
    }
    
    .form-title {
        font-size: 1.5em;
        font-weight: 600;
        color: #1e3a5f;
        margin-bottom: 25px;
    }
    
    .form-section {
        background: white;
        border-left: 4px solid #2d5a8c;
        padding: 20px;
        margin: 20px 0;
        border-radius: 4px;
    }
    
    .form-section-title {
        font-size: 1.15em;
        font-weight: 600;
        color: #1e3a5f;
        margin-bottom: 15px;
    }
    
    .nav-button-container {
        text-align: center;
        padding: 25px;
        background: #f0f4f8;
        border-radius: 8px;
        border: 1px solid #d0dce6;
        margin: 15px 0;
    }
    
    .nav-button-title {
        font-size: 1.2em;
        font-weight: 600;
        color: #1e3a5f;
        margin-bottom: 15px;
    }
    
    .nav-button-desc {
        color: #555;
        font-size: 0.95em;
        margin-bottom: 20px;
        line-height: 1.5;
    }
    
    .info-box {
        background: #e8f1f8;
        border-left: 4px solid #2d5a8c;
        padding: 15px 20px;
        margin: 20px 0;
        border-radius: 4px;
    }
    
    .warning-box {
        background: #fff3cd;
        border-left: 4px solid #ff9800;
        padding: 15px 20px;
        margin: 20px 0;
        border-radius: 4px;
    }
    
    table {
        width: 100%;
        border-collapse: collapse;
        margin: 20px 0;
    }
    
    table th {
        background: #2d5a8c;
        color: white;
        padding: 12px;
        text-align: left;
        font-weight: 600;
    }
    
    table td {
        border-bottom: 1px solid #e0e6ed;
        padding: 12px;
        color: #333;
    }
    
    table tr:hover {
        background: #f8f9fa;
    }
    
    .tab-header {
        font-size: 0.95em;
        font-weight: 600;
    }
</style>
""", unsafe_allow_html=True)

# Initialize session state
if 'page' not in st.session_state:
    st.session_state.page = 'home'
if 'patient_info' not in st.session_state:
    st.session_state.patient_info = {}

def page_introduction():
    st.markdown("""
    <div class="main-header">
        <h1>Psoriasis Clinical Assessment System</h1>
        <p>Comprehensive Diagnostic and Severity Evaluation Platform</p>
    </div>
    """, unsafe_allow_html=True)
    
    # Introduction Section
    st.markdown("""
    <div class="section-title">Overview</div>
    """, unsafe_allow_html=True)
    
    st.markdown("""
    <div class="content-card">
        <p class="subtitle" style="font-size: 1.05em; line-height: 1.8; color: #555; margin: 0;">
            Psoriasis is a chronic, non-contagious inflammatory skin disease that affects approximately 2-3% of the global population. 
            This clinical assessment system provides a comprehensive approach to psoriasis evaluation through diagnostic screening, 
            type identification, and severity assessment using validated clinical tools.
        </p>
    </div>
    """, unsafe_allow_html=True)
    
    # Definition Section
    st.markdown("""
    <div class="section-title">Clinical Definition</div>
    """, unsafe_allow_html=True)
    
    st.markdown("""
    <div class="definition-box">
        <p style="line-height: 1.8; color: #333;">
            <span class="highlight-text">Psoriasis</span> is a chronic autoimmune condition characterized by abnormal keratinocyte proliferation 
            and altered immune function, resulting in the formation of well-demarcated, erythematous plaques with silvery-white scales. 
            The condition is mediated by T-cell dysfunction and cytokine dysregulation, particularly involving TNF-alpha, IL-17, and IL-23 pathways.
        </p>
    </div>
    """, unsafe_allow_html=True)
    
    # Clinical Features
    st.markdown("""
    <div class="section-title">Key Clinical Characteristics</div>
    """, unsafe_allow_html=True)
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.markdown("""
        <div class="content-card">
            <h3 style="color: #1e3a5f; margin-top: 0;">Dermatological Features</h3>
            <ul class="feature-list">
                <li>Well-demarcated erythematous plaques</li>
                <li>Silvery-white scales easily scraped off</li>
                <li>Auspitz sign: pinpoint bleeding after scale removal</li>
                <li>Koebner phenomenon: lesions at trauma sites</li>
                <li>Symmetrical distribution pattern</li>
                <li>Predilection for extensor surfaces</li>
                <li>Nail involvement in 50-80% of patients</li>
            </ul>
        </div>
        """, unsafe_allow_html=True)
    
    with col2:
        st.markdown("""
        <div class="content-card">
            <h3 style="color: #1e3a5f; margin-top: 0;">Associated Systemic Features</h3>
            <ul class="feature-list">
                <li>Psoriatic arthritis in 5-10% of cases</li>
                <li>Increased metabolic syndrome risk</li>
                <li>Elevated cardiovascular mortality</li>
                <li>Psychological and social impact</li>
                <li>Sleep disturbances</li>
                <li>Reduced quality of life measures</li>
                <li>Family history in 30-40% of patients</li>
            </ul>
        </div>
        """, unsafe_allow_html=True)
    
    # Epidemiology
    st.markdown("""
    <div class="section-title">Epidemiology</div>
    """, unsafe_allow_html=True)
    
    epidemiology_data = {
        'Parameter': [
            'Global Prevalence',
            'Age of Onset - Early',
            'Age of Onset - Late',
            'Male to Female Ratio',
            'Family History Present',
            'Nail Involvement',
            'Psoriatic Arthritis Development'
        ],
        'Value': [
            '2-3% of population',
            '20-30 years (Type 1)',
            '50-60 years (Type 2)',
            '1:1 (Equal)',
            '30-40% of cases',
            '50-80% of patients',
            '5-10% of psoriasis patients'
        ]
    }
    
    st.table(epidemiology_data)
    
    # Psoriasis Types
    st.markdown("""
    <div class="section-title">Psoriasis Classification</div>
    """, unsafe_allow_html=True)
    
    st.markdown("""
    <div class="info-box">
        <strong>Clinical subtypes of psoriasis are classified based on morphology, distribution, and severity patterns. 
        Accurate type identification is essential for treatment planning and patient counseling.</strong>
    </div>
    """, unsafe_allow_html=True)
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.markdown("""
        <div class="type-box">
            <h4>Plaque Psoriasis</h4>
            <p><strong>Prevalence:</strong> 80-90% of cases</p>
            <p><strong>Description:</strong> Well-demarcated erythematous plaques with silvery-white scales, 
            typically on elbows, knees, scalp, and lower back.</p>
        </div>
        """, unsafe_allow_html=True)
        
        st.markdown("""
        <div class="type-box">
            <h4>Guttate Psoriasis</h4>
            <p><strong>Prevalence:</strong> 8-10% of cases</p>
            <p><strong>Description:</strong> Acute onset of small (2-10mm), drop-shaped papules and plaques, 
            frequently preceded by streptococcal pharyngitis.</p>
        </div>
        """, unsafe_allow_html=True)
        
        st.markdown("""
        <div class="type-box">
            <h4>Pustular Psoriasis</h4>
            <p><strong>Prevalence:</strong> Less than 1% of cases</p>
            <p><strong>Description:</strong> Sterile pustules on erythematous base, may be localized or generalized.</p>
        </div>
        """, unsafe_allow_html=True)
    
    with col2:
        st.markdown("""
        <div class="type-box">
            <h4>Inverse Psoriasis</h4>
            <p><strong>Prevalence:</strong> 3-7% of cases</p>
            <p><strong>Description:</strong> Smooth, shiny erythematous patches in intertriginous areas without typical scales.</p>
        </div>
        """, unsafe_allow_html=True)
        
        st.markdown("""
        <div class="type-box">
            <h4>Erythrodermic Psoriasis</h4>
            <p><strong>Prevalence:</strong> Rare, less than 1% of cases</p>
            <p><strong>Description:</strong> Diffuse erythema and scaling covering greater than 90% of body surface.</p>
        </div>
        """, unsafe_allow_html=True)
        
        st.markdown("""
        <div class="type-box">
            <h4>Psoriatic Arthritis</h4>
            <p><strong>Prevalence:</strong> 5-10% of psoriasis patients</p>
            <p><strong>Description:</strong> Joint inflammation affecting peripheral and axial joints, often with nail changes.</p>
        </div>
        """, unsafe_allow_html=True)
    
    # Assessment Tools
    st.markdown("""
    <div class="section-title">Clinical Assessment Tools</div>
    """, unsafe_allow_html=True)
    
    col1, col2, col3 = st.columns(3)
    
    with col1:
        st.markdown("""
        <div class="type-box">
            <h4>PASI Score</h4>
            <p><strong>Range:</strong> 0-72 points</p>
            <p><strong>Evaluation:</strong> Body surface area and lesion severity in head, trunk, upper and lower extremities.</p>
        </div>
        """, unsafe_allow_html=True)
    
    with col2:
        st.markdown("""
        <div class="type-box">
            <h4>BSA Assessment</h4>
            <p><strong>Range:</strong> 0-100%</p>
            <p><strong>Evaluation:</strong> Percentage of body surface area affected by psoriasis.</p>
        </div>
        """, unsafe_allow_html=True)
    
    with col3:
        st.markdown("""
        <div class="type-box">
            <h4>DLQI Score</h4>
            <p><strong>Range:</strong> 0-30 points</p>
            <p><strong>Evaluation:</strong> Impact on quality of life including symptoms, emotions, and activities.</p>
        </div>
        """, unsafe_allow_html=True)
    
    # Warnings
    st.markdown("""
    <div class="warning-box">
        <strong>Important Disclaimer:</strong> This clinical assessment system is designed for diagnostic support and education purposes. 
        It does not replace professional clinical judgment. For medical emergencies, immediate medical attention is required.
    </div>
    """, unsafe_allow_html=True)

def page_patient_info():
    st.markdown("""
    <div class="main-header">
        <h1>Patient Information</h1>
        <p>Clinical Assessment Registration</p>
    </div>
    """, unsafe_allow_html=True)
    
    st.markdown("""
    <div class="patient-form">
        <div class="form-section">
            <div class="form-section-title">Patient Demographics</div>
    """, unsafe_allow_html=True)
    
    col1, col2, col3 = st.columns(3)
    
    with col1:
        st.session_state.patient_info['patient_name'] = st.text_input(
            "Patient Name *",
            value=st.session_state.patient_info.get('patient_name', ''),
            key="name_input"
        )
    
    with col2:
        st.session_state.patient_info['patient_age'] = st.number_input(
            "Age (years) *",
            min_value=1,
            max_value=120,
            value=st.session_state.patient_info.get('patient_age', 30),
            key="age_input"
        )
    
    with col3:
        st.session_state.patient_info['patient_sex'] = st.selectbox(
            "Biological Sex *",
            ["Select", "Male", "Female", "Other"],
            index=0 if st.session_state.patient_info.get('patient_sex', '') == '' else (
                ["Select", "Male", "Female", "Other"].index(st.session_state.patient_info.get('patient_sex', 'Select'))
            ),
            key="sex_input"
        )
    
    st.markdown("""
        </div>
        <div class="form-section">
            <div class="form-section-title">Additional Information</div>
    """, unsafe_allow_html=True)
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.session_state.patient_info['patient_mrn'] = st.text_input(
            "Medical Record Number (Optional)",
            value=st.session_state.patient_info.get('patient_mrn', ''),
            key="mrn_input"
        )
    
    with col2:
        st.session_state.patient_info['assessment_date'] = st.date_input(
            "Assessment Date",
            value=datetime.now(),
            key="date_input"
        )
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.session_state.patient_info['patient_contact'] = st.text_input(
            "Contact Number (Optional)",
            value=st.session_state.patient_info.get('patient_contact', ''),
            key="contact_input"
        )
    
    with col2:
        st.session_state.patient_info['patient_email'] = st.text_input(
            "Email (Optional)",
            value=st.session_state.patient_info.get('patient_email', ''),
            key="email_input"
        )
    
    st.markdown("""
        </div>
    </div>
    """, unsafe_allow_html=True)
    
    # Form validation message
    form_complete = (
        st.session_state.patient_info.get('patient_name', '').strip() != '' and
        st.session_state.patient_info.get('patient_age', 0) > 0 and
        st.session_state.patient_info.get('patient_sex', '') != 'Select'
    )
    
    if form_complete:
        st.success("Patient information complete. You can now proceed to select an assessment tool.")
    else:
        st.warning("Please complete all required fields (marked with *) to proceed.")

def page_tool_selection():
    st.markdown("""
    <div class="main-header">
        <h1>Assessment Tools</h1>
        <p>Select Clinical Evaluation Module</p>
    </div>
    """, unsafe_allow_html=True)
    
    st.markdown("""
    <p style="color: #555; font-size: 1.05em; line-height: 1.8; margin-bottom: 30px;">
        Select the assessment tool to proceed with clinical evaluation. Each tool utilizes evidence-based clinical criteria 
        and validated measurement scales for comprehensive psoriasis assessment.
    </p>
    """, unsafe_allow_html=True)
    
    # Check if patient info is provided
    patient_ready = (
        st.session_state.patient_info.get('patient_name', '').strip() != '' and
        st.session_state.patient_info.get('patient_age', 0) > 0 and
        st.session_state.patient_info.get('patient_sex', '') != 'Select'
    )
    
    if patient_ready:
        st.markdown(f"""
        <div class="info-box">
            <strong>Patient:</strong> {st.session_state.patient_info.get('patient_name', 'Unknown')} | 
            <strong>Age:</strong> {st.session_state.patient_info.get('patient_age', 'N/A')} years | 
            <strong>Sex:</strong> {st.session_state.patient_info.get('patient_sex', 'N/A')}
        </div>
        """, unsafe_allow_html=True)
    else:
        st.warning("Please complete patient information in the 'Patient Information' tab before selecting an assessment tool.")
    
    col1, col2, col3 = st.columns(3)
    
    with col1:
        st.markdown("""
        <div class="nav-button-container">
            <div class="nav-button-title">Diagnostic Screening</div>
            <div class="nav-button-desc">19-question clinical questionnaire with visual reference images for initial psoriasis diagnosis assessment.</div>
        </div>
        """, unsafe_allow_html=True)
        
        if st.button("Access Diagnostic Tool", use_container_width=True, key="btn_diagnostic", disabled=not patient_ready):
            if patient_ready:
                st.session_state.page = 'diagnosis'
                st.rerun()
    
    with col2:
        st.markdown("""
        <div class="nav-button-container">
            <div class="nav-button-title">Type Identification</div>
            <div class="nav-button-desc">Clinical image gallery and classification tool for identifying specific psoriasis subtypes and presentations.</div>
        </div>
        """, unsafe_allow_html=True)
        
        if st.button("Access Type Tool", use_container_width=True, key="btn_type", disabled=not patient_ready):
            if patient_ready:
                st.session_state.page = 'type'
                st.rerun()
    
    with col3:
        st.markdown("""
        <div class="nav-button-container">
            <div class="nav-button-title">Severity Assessment</div>
            <div class="nav-button-desc">Comprehensive severity evaluation using PASI, BSA, and DLQI validated measurement scales.</div>
        </div>
        """, unsafe_allow_html=True)
        
        if st.button("Access Severity Tool", use_container_width=True, key="btn_severity", disabled=not patient_ready):
            if patient_ready:
                st.session_state.page = 'severity'
                st.rerun()

# Main layout with tabs
st.markdown("<br>", unsafe_allow_html=True)

tab1, tab2, tab3 = st.tabs(["Introduction", "Patient Information", "Assessment Tools"])

with tab1:
    page_introduction()

with tab2:
    page_patient_info()

with tab3:
    page_tool_selection()

# Handle page navigation for assessment modules
if st.session_state.page == 'diagnosis':
    st.markdown("""
    <div class="main-header">
        <h1>Diagnostic Screening</h1>
        <p>Clinical assessment module</p>
    </div>
    """, unsafe_allow_html=True)
    st.info("Diagnostic screening module - Ready for implementation")
    if st.button("Return to Main Navigation"):
        st.session_state.page = 'home'
        st.rerun()
elif st.session_state.page == 'type':
    st.markdown("""
    <div class="main-header">
        <h1>Type Identification</h1>
        <p>Psoriasis subtype classification module</p>
    </div>
    """, unsafe_allow_html=True)
    st.info("Type identification module - Ready for implementation")
    if st.button("Return to Main Navigation"):
        st.session_state.page = 'home'
        st.rerun()
elif st.session_state.page == 'severity':
    st.markdown("""
    <div class="main-header">
        <h1>Severity Assessment</h1>
        <p>PASI, BSA, and DLQI evaluation module</p>
    </div>
    """, unsafe_allow_html=True)
    st.info("Severity assessment module - Ready for implementation")
    if st.button("Return to Main Navigation"):
        st.session_state.page = 'home'
        st.rerun()
