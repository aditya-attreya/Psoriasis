import streamlit as st

# Page configuration - This replaces all the st.set_page_config() in your individual files
st.set_page_config(
    page_title="Psoriasis Clinical Decision Support System",
    page_icon="🩺",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Professional CSS styling
st.markdown("""
    <style>
    /* Main header styling */
    .main-header {
        background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
        padding: 2rem;
        border-radius: 10px;
        color: white;
        text-align: center;
        margin-bottom: 2rem;
        box-shadow: 0 4px 6px rgba(0,0,0,0.1);
    }
    
    .main-header h1 {
        margin: 0;
        font-size: 2.5rem;
        font-weight: 700;
    }
    
    .main-header p {
        margin: 0.5rem 0 0 0;
        font-size: 1.2rem;
        opacity: 0.9;
    }
    
    /* Module card styling */
    .module-card {
        background: white;
        padding: 1.5rem;
        border-radius: 10px;
        border-left: 4px solid #667eea;
        margin-bottom: 1rem;
        box-shadow: 0 2px 4px rgba(0,0,0,0.1);
        transition: transform 0.2s, box-shadow 0.2s;
    }
    
    .module-card:hover {
        transform: translateY(-2px);
        box-shadow: 0 4px 8px rgba(0,0,0,0.15);
    }
    
    .module-card h4 {
        color: #667eea;
        margin-top: 0;
    }
    
    .module-card p {
        color: #666;
        margin-bottom: 0;
    }
    
    /* Info box styling */
    .info-box {
        background: #f0f7ff;
        border-left: 4px solid #2196F3;
        padding: 1rem;
        border-radius: 5px;
        margin: 1rem 0;
    }
    
    /* Feature list styling */
    .feature-list {
        list-style: none;
        padding-left: 0;
    }
    
    .feature-list li {
        padding: 0.5rem 0;
        padding-left: 1.5rem;
        position: relative;
    }
    
    .feature-list li:before {
        content: "✓";
        color: #4CAF50;
        font-weight: bold;
        position: absolute;
        left: 0;
    }
    </style>
""", unsafe_allow_html=True)

# Main header
st.markdown("""
    <div class="main-header">
        <h1>🩺 Psoriasis Clinical Decision Support System</h1>
        <p>Comprehensive Assessment & Treatment Guidance Platform</p>
    </div>
""", unsafe_allow_html=True)

# Welcome section
st.write("## Welcome to the Psoriasis CDSS")

st.write("""
This Clinical Decision Support System provides a comprehensive, evidence-based platform for psoriasis 
assessment and management. The system integrates multiple validated clinical tools and diagnostic 
approaches to support healthcare professionals in delivering optimal patient care.
""")

# System overview
st.write("### 🔬 Integrated Assessment Modules")

st.write("""
This platform combines four specialized modules that work together to provide complete psoriasis evaluation:
""")

# Module cards in two columns
col1, col2 = st.columns(2)

with col1:
    st.markdown("""
        <div class="module-card">
            <h4>📄 Module 1: Introduction & Overview</h4>
            <p><strong>Purpose:</strong> Patient registration and clinical background</p>
            <p>Learn about psoriasis types, assessment methods, and clinical tools. 
            Collect patient demographic information to personalize the assessment process.</p>
        </div>
    """, unsafe_allow_html=True)
    
    st.markdown("""
        <div class="module-card">
            <h4>🏷️ Module 3: Type Identification</h4>
            <p><strong>Purpose:</strong> Psoriasis subtype classification</p>
            <p>Identify the specific type of psoriasis using clinical criteria. 
            Accurate subtype identification guides appropriate treatment selection.</p>
        </div>
    """, unsafe_allow_html=True)

with col2:
    st.markdown("""
        <div class="module-card">
            <h4>🔬 Module 2: Diagnostic Matrix</h4>
            <p><strong>Purpose:</strong> Visual diagnostic screening</p>
            <p>Image-based diagnostic assessment with weighted scoring system. 
            Helps determine likelihood of psoriasis through clinical manifestations.</p>
        </div>
    """, unsafe_allow_html=True)
    
    st.markdown("""
        <div class="module-card">
            <h4>📊 Module 4: Severity Assessment</h4>
            <p><strong>Purpose:</strong> Comprehensive severity evaluation</p>
            <p>Calculate PASI, BSA, and DLQI scores. Receive evidence-based treatment 
            recommendations with interactive visualizations and detailed explanations.</p>
        </div>
    """, unsafe_allow_html=True)

# How to use section
st.write("### 📋 How to Use This System")

st.info("""
**👈 Navigate using the sidebar** on the left to access different modules.

- Each module is designed as a standalone assessment tool
- Modules can be used independently or in sequence
- Patient information entered in Module 1 will be available across all modules
- Complete any or all modules based on your clinical needs
""")

# Clinical tools information
st.write("### 🎯 Validated Clinical Assessment Tools")

col1, col2, col3 = st.columns(3)

with col1:
    st.markdown("""
        **PASI Score**
        
        Psoriasis Area and Severity Index
        - Gold standard for severity
        - Measures erythema, induration, scaling
        - Ranges from 0-72
    """)

with col2:
    st.markdown("""
        **BSA Score**
        
        Body Surface Area
        - Extent of involvement
        - Quick assessment method
        - Percentage of body affected
    """)

with col3:
    st.markdown("""
        **DLQI Score**
        
        Dermatology Life Quality Index
        - Patient-reported outcomes
        - Impact on daily life
        - Ranges from 0-30
    """)

# Features section
st.write("### ✨ Key Features")

st.markdown("""
<ul class="feature-list">
    <li>Evidence-based diagnostic criteria and assessment tools</li>
    <li>Interactive visual assessment with clinical images</li>
    <li>Automated scoring and severity classification</li>
    <li>Treatment recommendations based on validated guidelines</li>
    <li>Patient-friendly interface for quality of life assessment</li>
    <li>Comprehensive reports with visualizations</li>
    <li>Session continuity across all modules</li>
</ul>
""", unsafe_allow_html=True)

# Getting started
st.write("### 🚀 Getting Started")

st.markdown("""
1. **Start with Module 1 (Introduction)** to understand the system and enter patient information
2. **Use Module 2 (Diagnostic Matrix)** for initial screening if diagnosis is uncertain
3. **Proceed to Module 3 (Type Identification)** to classify the psoriasis subtype
4. **Complete Module 4 (Severity Assessment)** for detailed evaluation and treatment guidance

**Or jump directly to any module** based on your current clinical needs using the sidebar navigation.
""")

# Clinical note
st.warning("""
**Clinical Note:** This system is designed to support clinical decision-making and should be used 
in conjunction with professional medical judgment. All assessments should be interpreted within 
the context of individual patient presentations and clinical expertise.
""")

# Footer
st.markdown("---")
col1, col2, col3 = st.columns(3)

with col1:
    st.caption("**Target Users**")
    st.caption("Dermatologists, General Practitioners, Medical Students, Researchers")

with col2:
    st.caption("**Assessment Tools**")
    st.caption("PASI, BSA, DLQI, Visual Diagnostic Matrix")

with col3:
    st.caption("**Version**")
    st.caption("Psoriasis CDSS v1.0 | October 2025")

st.caption("For Clinical Research and Educational Purposes")
