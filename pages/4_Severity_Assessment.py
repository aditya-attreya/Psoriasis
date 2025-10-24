import streamlit as st
import pandas as pd
import numpy as np
from datetime import datetime
import plotly.express as px
import plotly.graph_objects as go



# Professional Medical CSS
st.markdown("""
<style>
    @import url('https://fonts.googleapis.com/css2?family=Open+Sans:wght@300;400;500;600;700&display=swap');
    
    .main {
        font-family: 'Open Sans', sans-serif;
        background-color: #FAFBFC;
    }
    
    .main-header {
        background: linear-gradient(135deg, #1E40AF 0%, #1E3A8A 100%);
        color: white;
        text-align: center;
        padding: 2.5rem 2rem;
        margin: -1rem -1rem 2rem -1rem;
        border-radius: 0 0 12px 12px;
        box-shadow: 0 4px 12px rgba(30, 64, 175, 0.15);
    }
    
    .main-header h1 {
        font-size: 2.2rem;
        font-weight: 600;
        margin: 0;
        letter-spacing: -0.025em;
    }
    
    .main-header .subtitle {
        font-size: 1.1rem;
        font-weight: 400;
        margin: 0.8rem 0 0 0;
        opacity: 0.9;
        color: #E0E7FF;
    }
    
    .content-section {
        background: white;
        border-radius: 8px;
        padding: 2rem;
        margin: 1.5rem 0;
        border: 1px solid #E5E7EB;
        box-shadow: 0 1px 3px rgba(0, 0, 0, 0.1);
    }
    
    .section-title {
        color: #1E40AF;
        font-size: 1.25rem;
        font-weight: 600;
        margin: 0 0 1rem 0;
        padding-bottom: 0.5rem;
        border-bottom: 2px solid #F3F4F6;
    }
    
    .info-panel {
        background: #F8FAFC;
        border: 1px solid #E2E8F0;
        border-left: 4px solid #1E40AF;
        padding: 1.25rem;
        margin: 1rem 0;
        border-radius: 0 4px 4px 0;
        font-size: 0.95rem;
        line-height: 1.6;
    }
    
    .score-container {
        background: linear-gradient(135deg, #059669 0%, #047857 100%);
        color: white;
        padding: 1.5rem;
        border-radius: 8px;
        text-align: center;
        margin: 1rem 0;
        box-shadow: 0 2px 8px rgba(5, 150, 105, 0.25);
    }
    
    .alert-severe {
        background: #FEF2F2;
        border: 1px solid #FECACA;
        border-left: 4px solid #DC2626;
        color: #7F1D1D;
        padding: 1rem;
        border-radius: 4px;
        margin: 1rem 0;
    }
    
    .alert-moderate {
        background: #FFFBEB;
        border: 1px solid #FDE68A;
        border-left: 4px solid #D97706;
        color: #92400E;
        padding: 1rem;
        border-radius: 4px;
        margin: 1rem 0;
    }
    
    .alert-mild {
        background: #F0FDF4;
        border: 1px solid #BBF7D0;
        border-left: 4px solid #16A34A;
        color: #14532D;
        padding: 1rem;
        border-radius: 4px;
        margin: 1rem 0;
    }
    
    .medication-card {
        background: white;
        border: 1px solid #E5E7EB;
        border-radius: 6px;
        padding: 1.25rem;
        margin: 0.75rem 0;
        transition: box-shadow 0.2s ease;
    }
    
    .age-notice {
        background: #F5F3FF;
        border: 1px solid #DDD6FE;
        border-left: 4px solid #7C3AED;
        color: #581C87;
        padding: 1rem;
        border-radius: 4px;
        margin: 1rem 0;
        font-size: 0.9rem;
    }
    
    .glossary-item {
        background: #F9FAFB;
        border: 1px solid #E5E7EB;
        border-radius: 4px;
        padding: 1rem;
        margin: 0.5rem 0;
    }
    
    .glossary-term {
        font-weight: 600;
        color: #1E40AF;
        font-size: 0.95rem;
        margin-bottom: 0.25rem;
    }
    
    .glossary-definition {
        color: #4B5563;
        font-size: 0.85rem;
        line-height: 1.4;
        margin: 0;
    }
    
    .reference-container {
        background: #F8FAFC;
        border: 1px solid #E2E8F0;
        border-radius: 6px;
        padding: 1rem;
        margin: 1rem 0;
        text-align: center;
    }
    
    .image-container {
        background: #F8FAFC;
        border: 2px solid #E2E8F0;
        border-radius: 8px;
        padding: 1rem;
        margin: 1rem 0;
        text-align: center;
    }
    
    .image-title {
        font-weight: 600;
        color: #1E40AF;
        margin-bottom: 0.5rem;
        font-size: 1rem;
    }
    
    .image-caption {
        font-size: 0.85rem;
        color: #6B7280;
        font-style: italic;
        margin-top: 0.5rem;
    }
</style>
""", unsafe_allow_html=True)

def main():
    # Header
    st.markdown("""
    <div class="main-header">
        <h1>Psoriasis Clinical Decision Support System</h1>
        <div class="subtitle">Comprehensive PASI, BSA, DLQI Assessment & Treatment Guidance</div>
    </div>
    """, unsafe_allow_html=True)
    
    # Initialize session state
    initialize_session_state()
    
    # Sidebar navigation
    create_sidebar()
    
    # Route to appropriate page
    route_to_page()

def initialize_session_state():
    """Initialize session state variables"""
    if 'patient_age' not in st.session_state:
        st.session_state.patient_age = 30
    if 'disease_duration' not in st.session_state:
        st.session_state.disease_duration = 5
    if 'pasi_scores' not in st.session_state:
        st.session_state.pasi_scores = {}
    if 'bsa_score' not in st.session_state:
        st.session_state.bsa_score = 0.0
    if 'dlqi_score' not in st.session_state:
        st.session_state.dlqi_score = 0

def create_sidebar():
    """Create navigation sidebar"""
    
    st.sidebar.markdown("""
    <div style="background: linear-gradient(135deg, #1E40AF 0%, #1E3A8A 100%); color: white; padding: 1rem; border-radius: 6px; margin-bottom: 1rem; text-align: center;">
        <h3 style="margin: 0; font-size: 1.1rem; font-weight: 600;">Navigation</h3>
    </div>
    """, unsafe_allow_html=True)
    
    st.session_state.current_page = st.sidebar.selectbox(
        "Select Assessment Section",
        [
            "Psoriasis Overview",
            "PASI Scoring System", 
            "BSA Assessment",
            "DLQI Evaluation",
            "Treatment Recommendations",
            "Clinical Reference"
        ],
        key="navigation"
    )
    
    # Patient Information Section
    st.sidebar.markdown("---")
    st.sidebar.markdown("### Patient Information")
    
    with st.sidebar:
        st.session_state.patient_age = st.number_input(
            "Patient Age (years)", 
            min_value=1, max_value=100, 
            value=st.session_state.patient_age, 
            key="age_input"
        )
        st.session_state.disease_duration = st.number_input(
            "Disease Duration (years)", 
            min_value=0, max_value=50, 
            value=st.session_state.disease_duration, 
            key="duration_input"
        )
    
    # Assessment Summary
    if any([st.session_state.pasi_scores, st.session_state.bsa_score > 0, st.session_state.dlqi_score > 0]):
        st.sidebar.markdown("---")
        st.sidebar.markdown("### Assessment Summary")
        
        if st.session_state.pasi_scores:
            pasi_total = calculate_total_pasi(st.session_state.pasi_scores)
            st.sidebar.metric("PASI Score", f"{pasi_total:.1f}/72", help="Psoriasis Area and Severity Index")
        
        if st.session_state.bsa_score > 0:
            st.sidebar.metric("BSA Score", f"{st.session_state.bsa_score:.1f}%", help="Body Surface Area affected")
        
        if st.session_state.dlqi_score > 0:
            st.sidebar.metric("DLQI Score", f"{st.session_state.dlqi_score}/30", help="Dermatology Life Quality Index")

def route_to_page():
    """Route to appropriate page based on navigation"""
    if st.session_state.current_page == "Psoriasis Overview":
        psoriasis_overview_page()
    elif st.session_state.current_page == "PASI Scoring System":
        pasi_scoring_page()
    elif st.session_state.current_page == "BSA Assessment":
        bsa_assessment_page()
    elif st.session_state.current_page == "DLQI Evaluation":
        dlqi_evaluation_page()
    elif st.session_state.current_page == "Treatment Recommendations":
        treatment_recommendations_page()
    elif st.session_state.current_page == "Clinical Reference":
        clinical_reference_page()

def psoriasis_overview_page():
    """Psoriasis overview and education page"""
    
    st.markdown("## Understanding Psoriasis")
    
    # Main content in columns
    col1, col2 = st.columns([2, 1])
    
    with col1:
        # Disease Definition
        st.markdown("### What is Psoriasis?")
        
        st.info("""
        **Psoriasis** is a chronic, immune-mediated inflammatory skin disease characterized by well-demarcated, erythematous plaques with silvery-white scales. It affects approximately 2-3% of the global population and can significantly impact quality of life.
        
        **Key Characteristics:**
        - **Autoimmune Nature:** Overactive immune system causes rapid skin cell turnover (3-5 days vs normal 28-30 days)
        - **Chronic Course:** Lifelong condition with periods of flares and remission
        - **Genetic Component:** Family history in 30-40% of patients
        - **Systemic Disease:** Can affect joints (psoriatic arthritis) and increase cardiovascular risk
        """)
        
        # Display psoriasis severity comparison image
        st.markdown("### Psoriasis Severity Levels")
        st.markdown("""
        <div class="image-container">
            <div class="image-title">Psoriasis Severity Comparison</div>
        </div>
        """, unsafe_allow_html=True)
        
        # Display the severity comparison image
        st.image("data:image/png;base64,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", 
                 caption="Comparison of mild, moderate, and severe psoriasis showing different body surface areas affected",
                 width=500)
        
        
        # Pathophysiology
        st.markdown("### Pathophysiology")
        
        st.info("""
        Psoriasis results from dysregulation of both innate and adaptive immune responses:
        - **T-cell Activation:** Th1, Th17, and Th22 cell activation drives inflammation
        - **Cytokine Networks:** IL-17, IL-23, TNF-α are key inflammatory mediators
        - **Keratinocyte Hyperproliferation:** Accelerated cell division and incomplete differentiation
        - **Angiogenesis:** Increased blood vessel formation contributes to erythema
        """)
        
        # Types of Psoriasis
        st.markdown("### Types of Psoriasis")
        
        psoriasis_types = {
            "Plaque Psoriasis (85-90%)": "Most common form with well-demarcated, raised erythematous plaques covered with silvery scales. Typically affects extensor surfaces (elbows, knees), scalp, and lower back.",
            "Guttate Psoriasis (8-10%)": "Small, drop-shaped lesions scattered across the trunk and limbs. Often triggered by streptococcal infections. More common in children and young adults.",
            "Inverse Psoriasis (3-7%)": "Affects flexural areas (axillae, groin, inframammary areas). Appears as smooth, well-demarcated erythematous patches without typical scaling.",
            "Pustular Psoriasis (<3%)": "Characterized by sterile pustules on erythematous base. Can be localized (palmoplantar) or generalized (life-threatening).",
            "Erythrodermic Psoriasis (<3%)": "Rare, severe form with widespread erythema and scaling covering >90% of body surface area. Medical emergency requiring hospitalization."
        }
        
        for ptype, description in psoriasis_types.items():
            with st.expander(ptype):
                st.write(description)
    
    with col2:
        # Clinical Assessment Tools
        st.markdown("### Assessment Tools")
        
        st.info("""
        This system provides three validated assessment instruments:
        """)
        
        # PASI Overview
        with st.container():
            st.markdown("**PASI Scoring**")
            st.markdown("**Psoriasis Area and Severity Index**")
            st.caption("""
            Gold standard for measuring disease severity combining area involvement and lesion characteristics.
            - **Range:** 0-72
            - **Components:** Erythema, induration, scaling, area
            - **Use:** Clinical trials, treatment monitoring
            """)
        
        # BSA Overview
        with st.container():
            st.markdown("**BSA Assessment**")
            st.markdown("**Body Surface Area**")
            st.caption("""
            Simple estimate of percentage of body affected by psoriasis lesions.
            - **Range:** 0-100%
            - **Method:** Palm method (1 palm = 1% BSA)
            - **Use:** Quick severity assessment
            """)
        
        # DLQI Overview
        with st.container():
            st.markdown("**DLQI Evaluation**")
            st.markdown("**Dermatology Life Quality Index**")
            st.caption("""
            Validated questionnaire measuring impact on patient's quality of life.
            - **Range:** 0-30
            - **Questions:** 10 items across 6 domains
            - **Use:** Treatment decisions, monitoring
            """)
        
        # Common Triggers
        st.markdown("### Common Triggers")
        
        st.warning("""
        - **Infections:** Streptococcal throat infections, skin trauma
        - **Medications:** Beta-blockers, lithium, antimalarials
        - **Stress:** Physical or emotional stress
        - **Climate:** Cold, dry weather conditions
        - **Lifestyle:** Smoking, excessive alcohol consumption
        - **Trauma:** Cuts, burns, sunburn (Koebner phenomenon)
        """)

def pasi_scoring_page():
    """PASI scoring section with visual references"""
    
    st.markdown("## PASI Scoring System")
    
    # About PASI section
    st.markdown("### About PASI (Psoriasis Area and Severity Index)")
    
    st.info("""
    The PASI is the gold standard tool for measuring psoriasis severity, developed by Fredriksson and Pettersson in 1978. It provides a quantitative assessment by combining **lesion severity** and **area involvement** across four body regions.
    
    **PASI Formula:**
    PASI = 0.1×(Eh+Ih+Dh)×Ah + 0.2×(Ea+Ia+Da)×Aa + 0.3×(Et+It+Dt)×At + 0.4×(El+Il+Dl)×Al
    
    **Where:**
    - E = Erythema (redness), I = Induration (thickness), D = Desquamation (scaling)
    - A = Area score, Subscripts: h=head, a=arms, t=trunk, l=legs
    
    **Scoring Range:** 0-72 (higher scores indicate more severe disease)
    """)
    
    # Visual Reference Section
    st.markdown("### Visual Scoring References")
    
    tab1, tab2, tab3, tab4 = st.tabs(["Severity Scale", "Clinical Examples", "PASI Guide", "Reference Tables"])
    
    with tab1:
        st.markdown("#### PASI Severity Scale (0-4)")
        
        st.markdown("""
        <div class="image-container">
            <div class="image-title">Clinical Severity Scale</div>
        </div>
        """, unsafe_allow_html=True)
        
        # Display clinical severity scale
        st.image("data:image/jpeg;base64,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", 
                  width=500)
        st.caption("Clinical severity scale showing healthy skin through very severe psoriasis with examples of each grade (0-4)")
        
        # Create columns for severity descriptions
        col1, col2 = st.columns(2)
        
        with col1:
            st.markdown("**Erythema (Redness):**")
            st.markdown("""
            - **Score 0 - None:** No erythema present
            - **Score 1 - Slight:** Light pink coloration
            - **Score 2 - Moderate:** Red coloration  
            - **Score 3 - Severe:** Dark red coloration
            - **Score 4 - Very Severe:** Deep red to purple coloration
            """)
            
            st.markdown("**Induration (Thickness):**")
            st.markdown("""
            - **Score 0 - None:** Flat, no elevation
            - **Score 1 - Slight:** Barely palpable elevation
            - **Score 2 - Moderate:** Clearly palpable elevation
            - **Score 3 - Severe:** Thick, raised plaques
            - **Score 4 - Very Severe:** Very thick, markedly elevated plaques
            """)
        
        with col2:
            st.markdown("**Desquamation (Scaling):**")
            st.markdown("""
            - **Score 0 - None:** No visible scaling
            - **Score 1 - Slight:** Fine, minimal scaling
            - **Score 2 - Moderate:** Moderate scaling, easily removed
            - **Score 3 - Severe:** Coarse, adherent scaling
            - **Score 4 - Very Severe:** Very thick, heavy scaling
            """)
            
            st.markdown("**Area Assessment:**")
            st.markdown("""
            - **Score 0:** No involvement (0%)
            - **Score 1:** <10% of region affected
            - **Score 2:** 10-29% of region affected
            - **Score 3:** 30-49% of region affected
            - **Score 4:** 50-69% of region affected
            - **Score 5:** 70-89% of region affected
            - **Score 6:** 90-100% of region affected
            """)
    
    with tab2:
        st.markdown("#### Clinical Examples with Scoring")
        
        st.markdown("""
        <div class="image-container">
            <div class="image-title">Erythema and Scaling Examples</div>
        </div>
        """, unsafe_allow_html=True)
        
        # Display erythema and scaling examples
        st.image("data:image/jpeg;base64,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", 
                  width=600)
        st.caption("Clinical examples showing different severity levels of erythema and scaling with corresponding PASI scores")
        
        st.info("Use these clinical examples to guide your PASI parameter scoring:")
        
        st.markdown("""
        <div class="image-container">
            <div class="image-title">PASI Scoring Methodology</div>
        </div>
        """, unsafe_allow_html=True)
        
        # Display PASI scoring methodology example
        st.image("data:image/jpeg;base64,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", 
                   width=500)
        st.caption("PASI scoring table and clinical example showing how to apply the scoring system on actual patient")
        
        # Example scoring interpretations
        col1, col2 = st.columns(2)
        
        with col1:
            st.success("""
            **Mild Example:**
            - Erythema: 1-2 (Light pink to red)
            - Induration: 1 (Barely raised)
            - Scaling: 1-2 (Fine to moderate)
            - Area: <10% of region
            """)
        
        with col2:
            st.error("""
            **Severe Example:**
            - Erythema: 3-4 (Dark red to purple)
            - Induration: 3-4 (Very thick plaques)
            - Scaling: 3-4 (Coarse, heavy scaling)
            - Area: >30% of region
            """)
    
    with tab3:
        st.markdown("#### PASI Scoring Guide")
        
        st.markdown("""
        <div class="image-container">
            <div class="image-title">Comprehensive PASI Assessment</div>
        </div>
        """, unsafe_allow_html=True)
        
        # Display comprehensive PASI guide
        st.image("data:image/jpeg;base64,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", 
                width=600)
        st.caption("Advanced imaging techniques and assessment process for standardized psoriasis severity evaluation")
        
        # Body Region Weights
        st.markdown("**Body Region Weights**")
        
        regions_df = pd.DataFrame({
            'Body Region': ['Head/Neck', 'Upper Limbs', 'Trunk', 'Lower Limbs'],
            'Weight Factor': [0.1, 0.2, 0.3, 0.4],
            'Body Surface %': ['10%', '20%', '30%', '40%'],
            'Examples': ['Scalp, face, neck', 'Arms, hands', 'Chest, back, abdomen', 'Legs, feet']
        })
        
        st.dataframe(regions_df, use_container_width=True)
        
        # Scoring Tips
        st.markdown("**Scoring Tips:**")
        st.success("""
        1. **Assess each parameter independently** - Don't let one parameter influence another
        2. **Use adequate lighting** - Natural light preferred for erythema assessment
        3. **Compare to normal skin** - Use adjacent normal skin as reference
        4. **Consider the worst lesion** - Score based on most severe lesion in each region
        5. **Area estimation** - Use palm method (1 palm = 1% of region) for accuracy
        """)
    
    with tab4:
        display_pasi_reference_tables()
    
    # PASI Calculation Section
    st.markdown("### PASI Calculation")
    
    pasi_scores = calculate_pasi_interactive()
    
    # Results Display
    if pasi_scores:
        total_pasi = calculate_total_pasi(pasi_scores)
        st.session_state.pasi_scores = pasi_scores
        
        col1, col2 = st.columns([2, 1])
        
        with col1:
            display_pasi_results(pasi_scores, total_pasi)
        
        with col2:
            display_pasi_interpretation(total_pasi)
    
    # PASI Glossary
    display_pasi_glossary()

def bsa_assessment_page():
    """BSA assessment with clear instructions"""
    
    st.markdown("## Body Surface Area (BSA) Assessment")
    
    # About BSA section
    st.markdown("### About BSA Assessment")
    
    st.info("""
    **Body Surface Area (BSA)** assessment provides a simple estimate of the percentage of total body surface affected by psoriasis. This method is faster than PASI scoring and correlates well with disease severity.
    
    **Clinical Significance:**
    - **Mild Psoriasis:** Less than 3% BSA affected
    - **Moderate Psoriasis:** 3-10% BSA affected  
    - **Severe Psoriasis:** Greater than 10% BSA affected
    
    **Assessment Methods:** Palm method, visual estimation, or rule of nines
    """)
    
    col1, col2 = st.columns([2, 1])
    
    with col1:
        # Palm Method Section
        st.markdown("### Method 1: Palm Method")
        
        st.info("""
        **Instructions:**
        The palm method uses the patient's hand (palm plus fingers) as a reference unit. One palm equals approximately 1% of total body surface area.
        
        **How to use:**
        1. Use the patient's own palm (including fingers) as a measuring tool
        2. Count how many palm-sized areas would be needed to cover all psoriasis lesions
        3. Include scattered small lesions by imagining them combined together
        4. Each palm unit equals 1% BSA
        """)
        
        st.markdown("""
        <div class="image-container">
            <div class="image-title">Palm Method Reference</div>
        </div>
        """, unsafe_allow_html=True)
        
        # Visual reference for palm method - create a simple diagram
        st.info("**Visual Guide:** One palm (including fingers) = 1% Body Surface Area")
        
        palm_count = st.number_input(
            "Number of palm-sized areas affected",
            min_value=0, max_value=100, value=0, step=1,
            help="Count all psoriasis lesions using your palm as a reference",
            key="palm_method"
        )
        
        st.markdown("---")
        
        # Visual Estimation Method
        st.markdown("### Method 2: Visual Estimation by Body Region")
        
        st.info("""
        **Instructions:**
        Estimate the percentage of each body region affected by psoriasis lesions. The total BSA will be calculated automatically based on standard body surface area proportions.
        """)
        
        # Body regions with standard proportions
        body_regions = {
            "Head & Neck": {"proportion": 9, "affected": 0},
            "Both Arms": {"proportion": 18, "affected": 0},
            "Chest": {"proportion": 9, "affected": 0},
            "Abdomen": {"proportion": 9, "affected": 0},
            "Upper Back": {"proportion": 9, "affected": 0},
            "Lower Back": {"proportion": 9, "affected": 0},
            "Both Legs": {"proportion": 36, "affected": 0},
            "Genitals": {"proportion": 1, "affected": 0}
        }
        
        visual_estimation_total = 0
        
        for region, info in body_regions.items():
            col_region, col_slider = st.columns([1, 2])
            
            with col_region:
                st.markdown(f"**{region}**")
                st.caption(f"Normal proportion: {info['proportion']}% of total body")
            
            with col_slider:
                affected_pct = st.slider(
                    f"Percentage of {region} affected",
                    min_value=0, max_value=100, value=0,
                    key=f"visual_{region}",
                    help=f"Estimate what percentage of your {region.lower()} has psoriasis lesions"
                )
                
                # Calculate contribution to total BSA
                contribution = (affected_pct / 100) * info['proportion']
                visual_estimation_total += contribution
    
    with col2:
        # BSA Results
        final_bsa = max(palm_count, visual_estimation_total)
        st.session_state.bsa_score = final_bsa
        
        # Score display
        st.markdown(f"""
        <div class="score-container">
            <h3>BSA Score</h3>
            <div style="font-size: 2.5rem; font-weight: 700; margin: 0.5rem 0;">{final_bsa:.1f}%</div>
            <div>Body Surface Area Affected</div>
        </div>
        """, unsafe_allow_html=True)
        
        # Interpretation
        if final_bsa < 3:
            severity = "Mild Psoriasis"
            alert_class = "alert-mild"
            recommendations = [
                "Topical corticosteroids (medium potency)",
                "Vitamin D analogs (calcipotriol)",
                "Topical calcineurin inhibitors",
                "Regular moisturizers"
            ]
        elif final_bsa <= 10:
            severity = "Moderate Psoriasis"
            alert_class = "alert-moderate"
            recommendations = [
                "Optimize topical therapy",
                "Consider phototherapy (NB-UVB)",
                "Systemic therapy if topicals inadequate",
                "Specialist consultation"
            ]
        else:
            severity = "Severe Psoriasis"
            alert_class = "alert-severe"
            recommendations = [
                "Systemic therapy indicated",
                "Biologic therapy consideration",
                "Immediate specialist referral",
                "Comprehensive monitoring"
            ]
        
        if final_bsa > 0:
            st.markdown(f'<div class="{alert_class}"><h4>{severity}</h4>', unsafe_allow_html=True)
            st.markdown("**Recommended Approach:**")
            for rec in recommendations:
                st.markdown(f"• {rec}")
            st.markdown('</div>', unsafe_allow_html=True)
        
        # BSA Distribution Visualization
        if final_bsa > 0:
            display_bsa_visualization()
        
        # Rule of Nines Reference
        st.markdown("### Rule of Nines Reference")
        st.info("""
        **Standard Body Surface Area Proportions:**
        - Head & Neck: 9%
        - Each Arm: 9% (Both Arms: 18%)
        - Front Torso: 18%
        - Back Torso: 18%
        - Each Leg: 18% (Both Legs: 36%)
        - Genitals: 1%
        """)

def dlqi_evaluation_page():
    """DLQI evaluation page"""
    
    st.markdown("## DLQI (Dermatology Life Quality Index) Evaluation")
    
    # About DLQI section
    st.markdown("### About DLQI")
    
    st.info("""
    The **Dermatology Life Quality Index (DLQI)** is a validated 10-question questionnaire developed by Finlay and Khan in 1994. It measures the impact of skin disease on a patient's quality of life over the preceding one week.
    
    **Assessment Domains:**
    - **Symptoms and feelings** (questions 1-2)
    - **Daily activities** (questions 3-4)  
    - **Leisure** (questions 5-6)
    - **Work and school** (question 7)
    - **Personal relationships** (questions 8-9)
    - **Treatment** (question 10)
    
    **Scoring:** Each question scored 0-3, total range 0-30. Higher scores indicate greater impact on quality of life.
    """)
    
    # DLQI Questionnaire
    st.markdown("### DLQI Questionnaire")
    
    st.info("""
    **Instructions:** Please answer each question by selecting the response that most closely reflects your experience over the **last week**. All questions are optional.
    """)
    
    dlqi_questions = [
        {
            "domain": "Symptoms and Feelings",
            "question": "Over the last week, how itchy, sore, painful or stinging has your skin been?",
            "options": ["Not at all", "A little", "A lot", "Very much"],
            "key": "dlqi_1"
        },
        {
            "domain": "Symptoms and Feelings", 
            "question": "Over the last week, how embarrassed or self conscious have you been because of your skin?",
            "options": ["Not at all", "A little", "A lot", "Very much"],
            "key": "dlqi_2"
        },
        {
            "domain": "Daily Activities",
            "question": "Over the last week, how much has your skin interfered with you going shopping or looking after your home or garden?",
            "options": ["Not at all", "A little", "A lot", "Very much"],
            "key": "dlqi_3"
        },
        {
            "domain": "Daily Activities",
            "question": "Over the last week, how much has your skin influenced the clothes you wear?",
            "options": ["Not at all", "A little", "A lot", "Very much"],
            "key": "dlqi_4"
        },
        {
            "domain": "Leisure",
            "question": "Over the last week, how much has your skin affected any social or leisure activities?",
            "options": ["Not at all", "A little", "A lot", "Very much"],
            "key": "dlqi_5"
        },
        {
            "domain": "Leisure",
            "question": "Over the last week, how much has your skin made it difficult for you to do any sport?",
            "options": ["Not at all", "A little", "A lot", "Very much"],
            "key": "dlqi_6"
        },
        {
            "domain": "Work/School",
            "question": "Over the last week, has your skin prevented you from working or studying?",
            "options": ["Not relevant", "Not at all", "A little", "A lot"],
            "key": "dlqi_7",
            "special": True
        },
        {
            "domain": "Personal Relationships",
            "question": "Over the last week, how much has your skin created problems with your partner or any of your close friends or relatives?",
            "options": ["Not relevant", "Not at all", "A little", "A lot"],
            "key": "dlqi_8",
            "special": True
        },
        {
            "domain": "Personal Relationships",
            "question": "Over the last week, how much has your skin caused any sexual difficulties?",
            "options": ["Not relevant", "Not at all", "A little", "A lot"],
            "key": "dlqi_9",
            "special": True
        },
        {
            "domain": "Treatment",
            "question": "Over the last week, how much of a problem has the treatment for your skin been (e.g. making your home messy, or time consuming)?",
            "options": ["Not relevant", "Not at all", "A little", "A lot"],
            "key": "dlqi_10",
            "special": True
        }
    ]
    
    dlqi_total = 0
    answered_questions = 0
    domain_scores = {}
    current_domain = None
    
    for i, q in enumerate(dlqi_questions, 1):
        # Group questions by domain
        if q["domain"] != current_domain:
            current_domain = q["domain"]
            st.markdown(f"#### {current_domain}")
            domain_scores[q["domain"]] = []
        
        st.markdown(f"**Question {i}:** {q['question']}")
        
        # Handle special scoring for questions 7-10
        if q.get('special'):
            answer = st.radio(
                "Select your answer:",
                options=list(range(len(q['options']))),
                format_func=lambda x, opts=q['options']: opts[x],
                key=q['key'],
                index=None,
                help="Select 'Not relevant' if this question doesn't apply to your situation"
            )
            
            if answer is not None:
                answered_questions += 1
                if answer == 0:  # "Not relevant" 
                    score = 0
                else:
                    score = answer - 1  # Adjust for "Not relevant" option
                dlqi_total += score
                domain_scores[q["domain"]].append(score)
        else:
            answer = st.radio(
                "Select your answer:",
                options=list(range(len(q['options']))),
                format_func=lambda x, opts=q['options']: opts[x],
                key=q['key'],
                index=None
            )
            
            if answer is not None:
                answered_questions += 1
                dlqi_total += answer
                domain_scores[q["domain"]].append(answer)
        
        st.markdown("---")
    
    # DLQI Results
    if answered_questions > 0:
        st.session_state.dlqi_score = dlqi_total
        
        col1, col2 = st.columns([2, 1])
        
        with col1:
            # Score display
            st.markdown(f"""
            <div class="score-container">
                <h3>DLQI Score</h3>
                <div style="font-size: 2.5rem; font-weight: 700; margin: 0.5rem 0;">{dlqi_total}</div>
                <div>out of 30 ({answered_questions}/10 questions answered)</div>
            </div>
            """, unsafe_allow_html=True)
            
            # Display domain analysis
            display_dlqi_domain_analysis(domain_scores)
        
        with col2:
            # Interpretation
            if dlqi_total <= 1:
                impact = "No Impact on Quality of Life"
                alert_class = "alert-mild"
                description = "The psoriasis has no impact on the patient's life."
            elif dlqi_total <= 5:
                impact = "Small Impact on Quality of Life"
                alert_class = "alert-mild"
                description = "The psoriasis has a small impact on the patient's life."
            elif dlqi_total <= 10:
                impact = "Moderate Impact on Quality of Life"
                alert_class = "alert-moderate"
                description = "The psoriasis has a moderate impact on the patient's life."
            elif dlqi_total <= 20:
                impact = "Large Impact on Quality of Life"
                alert_class = "alert-severe"
                description = "The psoriasis has a large impact on the patient's life."
            else:
                impact = "Extremely Large Impact on Quality of Life"
                alert_class = "alert-severe"
                description = "The psoriasis has an extremely large impact on the patient's life."
            
            st.markdown(f'<div class="{alert_class}"><h4>{impact}</h4><p>{description}</p></div>', 
                       unsafe_allow_html=True)
            
            # Clinical Significance
            st.markdown("#### Clinical Significance")
            st.info("""
            **DLQI Interpretation:**
            - **0-1:** No impairment
            - **2-5:** Mild impairment
            - **6-10:** Moderate impairment
            - **11-20:** Severe impairment
            - **21-30:** Extremely severe impairment
            """)

def treatment_recommendations_page():
    """Treatment recommendations based on scores and patient factors"""
    
    st.markdown("## Treatment Recommendations")
    
    st.info("""
    Treatment recommendations are generated based on **psoriasis severity**, **patient age**, **disease duration**, and **quality of life impact**. All recommendations follow current clinical guidelines and consider age-specific factors.
    """)
    
    # Current Assessment Summary
    col1, col2, col3 = st.columns(3)
    
    with col1:
        current_pasi = calculate_total_pasi(st.session_state.pasi_scores) if st.session_state.pasi_scores else 0
        pasi_score = st.number_input(
            "PASI Score", 
            min_value=0.0, max_value=72.0, 
            value=float(current_pasi), 
            step=0.1,
            help="Psoriasis Area and Severity Index (0-72)"
        )
    
    with col2:
        bsa_score = st.number_input(
            "BSA Score (%)", 
            min_value=0.0, max_value=100.0, 
            value=st.session_state.bsa_score, 
            step=0.1,
            help="Body Surface Area affected (0-100%)"
        )
    
    with col3:
        dlqi_score = st.number_input(
            "DLQI Score", 
            min_value=0, max_value=30, 
            value=st.session_state.dlqi_score,
            help="Dermatology Life Quality Index (0-30)"
        )
    
    # Generate and display recommendations
    if st.button("Generate Treatment Recommendations", type="primary"):
        recommendations = generate_treatment_recommendations(
            pasi_score, bsa_score, dlqi_score, 
            st.session_state.patient_age, st.session_state.disease_duration
        )
        
        display_treatment_recommendations(recommendations)

def clinical_reference_page():
    """Clinical reference and resources"""
    
    st.markdown("## Clinical Reference Guide")
    
    tab1, tab2, tab3, tab4 = st.tabs([
        "Clinical Guidelines", 
        "Medication Reference", 
        "Monitoring Protocols", 
        "Complete Glossary"
    ])
    
    with tab1:
        display_clinical_guidelines()
    
    with tab2:
        display_medication_reference()
    
    with tab3:
        display_monitoring_protocols()
    
    with tab4:
        display_complete_glossary()

# Helper Functions
def calculate_pasi_interactive():
    """Interactive PASI calculation"""
    regions = {
        'head': {'name': 'Head/Neck', 'weight': 0.1},
        'arms': {'name': 'Upper Limbs', 'weight': 0.2}, 
        'trunk': {'name': 'Trunk', 'weight': 0.3},
        'legs': {'name': 'Lower Limbs', 'weight': 0.4}
    }
    
    pasi_scores = {}
    
    for region_key, region_info in regions.items():
        st.markdown(f"#### {region_info['name']}")
        
        col1, col2, col3, col4 = st.columns(4)
        
        with col1:
            erythema = st.selectbox(
                "Erythema (Redness)",
                options=[0, 1, 2, 3, 4],
                format_func=lambda x: f"{x} - {['None', 'Slight', 'Moderate', 'Severe', 'Very Severe'][x]}",
                key=f"{region_key}_erythema",
                help="Rate the redness/inflammation of lesions"
            )
        
        with col2:
            induration = st.selectbox(
                "Induration (Thickness)",
                options=[0, 1, 2, 3, 4],
                format_func=lambda x: f"{x} - {['None', 'Slight', 'Moderate', 'Severe', 'Very Severe'][x]}",
                key=f"{region_key}_induration", 
                help="Rate the thickness/elevation of lesions"
            )
        
        with col3:
            scaling = st.selectbox(
                "Scaling (Desquamation)",
                options=[0, 1, 2, 3, 4],
                format_func=lambda x: f"{x} - {['None', 'Slight', 'Moderate', 'Severe', 'Very Severe'][x]}",
                key=f"{region_key}_scaling",
                help="Rate the amount of scaling on lesions"
            )
        
        with col4:
            area_percentage = st.number_input(
                f"Area Affected (%)",
                min_value=0, max_value=100, value=0,
                key=f"{region_key}_area",
                help=f"Percentage of {region_info['name'].lower()} affected"
            )
        
        # Calculate regional PASI
        area_score = convert_area_to_score(area_percentage)
        severity_sum = erythema + induration + scaling
        regional_pasi = region_info['weight'] * severity_sum * area_score
        
        pasi_scores[region_key] = {
            'name': region_info['name'],
            'erythema': erythema,
            'induration': induration,
            'scaling': scaling,
            'area_percentage': area_percentage,
            'area_score': area_score,
            'severity_sum': severity_sum,
            'regional_pasi': regional_pasi,
            'weight': region_info['weight']
        }
        
        # Show regional result
        if any([erythema, induration, scaling, area_percentage]):
            st.success(f"**Regional PASI: {regional_pasi:.2f}**")
    
    return pasi_scores

def convert_area_to_score(percentage):
    """Convert area percentage to PASI area score"""
    if percentage == 0:
        return 0
    elif percentage < 10:
        return 1
    elif percentage <= 29:
        return 2
    elif percentage <= 49:
        return 3
    elif percentage <= 69:
        return 4
    elif percentage <= 89:
        return 5
    else:
        return 6

def calculate_total_pasi(pasi_scores):
    """Calculate total PASI score"""
    if not pasi_scores:
        return 0.0
    return sum(scores['regional_pasi'] for scores in pasi_scores.values())

def display_pasi_results(pasi_scores, total_pasi):
    """Display PASI results"""
    st.markdown(f"""
    <div class="score-container">
        <h3>Total PASI Score</h3>
        <div style="font-size: 2.5rem; font-weight: 700; margin: 0.5rem 0;">{total_pasi:.1f}</div>
        <div>out of 72 maximum</div>
    </div>
    """, unsafe_allow_html=True)
    
    # Detailed breakdown
    st.markdown("### Regional Breakdown")
    breakdown_data = []
    for region, scores in pasi_scores.items():
        breakdown_data.append({
            'Region': scores['name'],
            'Erythema': scores['erythema'],
            'Induration': scores['induration'],
            'Scaling': scores['scaling'],
            'Area %': scores['area_percentage'],
            'Area Score': scores['area_score'],
            'Regional PASI': round(scores['regional_pasi'], 2)
        })
    
    if breakdown_data:
        df = pd.DataFrame(breakdown_data)
        st.dataframe(df, use_container_width=True)

def display_pasi_interpretation(total_pasi):
    """Display PASI interpretation"""
    if total_pasi < 5:
        severity = "Mild Psoriasis"
        alert_class = "alert-mild"
        description = "Topical therapy typically appropriate"
        recommendations = [
            "Topical corticosteroids (medium potency)",
            "Vitamin D analogs",
            "Topical calcineurin inhibitors",
            "Regular emollients"
        ]
    elif total_pasi < 10:
        severity = "Moderate Psoriasis"
        alert_class = "alert-moderate"
        description = "Consider phototherapy or systemic therapy"
        recommendations = [
            "Optimize topical therapy",
            "NB-UVB phototherapy",
            "Consider systemic therapy",
            "Specialist consultation"
        ]
    else:
        severity = "Severe Psoriasis"
        alert_class = "alert-severe"
        description = "Systemic therapy typically indicated"
        recommendations = [
            "Systemic therapy or biologics",
            "Specialist referral required",
            "Comprehensive monitoring",
            "Consider clinical trial participation"
        ]
    
    st.markdown(f'<div class="{alert_class}"><h4>{severity}</h4><p>{description}</p></div>', 
               unsafe_allow_html=True)
    
    st.markdown("**Typical Treatment Approach:**")
    for rec in recommendations:
        st.markdown(f"• {rec}")

def display_pasi_reference_tables():
    """Display PASI reference tables"""
    col1, col2 = st.columns(2)
    
    with col1:
        st.markdown("#### Severity Parameters")
        severity_df = pd.DataFrame({
            'Score': [0, 1, 2, 3, 4],
            'Description': ['None', 'Slight', 'Moderate', 'Severe', 'Very Severe'],
            'Clinical Appearance': [
                'No lesional activity',
                'Barely perceptible',
                'Clearly present',
                'Marked changes',
                'Maximum severity'
            ]
        })
        st.dataframe(severity_df, use_container_width=True)
    
    with col2:
        st.markdown("#### Area Parameters")
        area_df = pd.DataFrame({
            'Score': [0, 1, 2, 3, 4, 5, 6],
            'Area Range': ['0%', '<10%', '10-29%', '30-49%', '50-69%', '70-89%', '90-100%']
        })
        st.dataframe(area_df, use_container_width=True)

def display_pasi_glossary():
    """Display PASI-specific glossary"""
    st.markdown("### PASI Glossary")
    
    with st.expander("PASI Terms and Definitions"):
        pasi_terms = {
            "PASI": "Psoriasis Area and Severity Index - Gold standard scoring system (range 0-72)",
            "Erythema": "Redness of skin lesions due to inflammation and vasodilation",
            "Induration": "Thickening and elevation of skin lesions above normal skin level",
            "Desquamation": "Scaling - shedding of the outer layer of skin in flakes or scales",
            "Area Score": "Categorical score (0-6) representing percentage of body region affected",
            "Regional Weight": "Multiplication factor reflecting proportion of total body surface area",
            "PASI 75": "75% improvement in PASI score from baseline - primary endpoint in clinical trials",
            "PASI 90": "90% improvement in PASI score from baseline - stringent treatment response",
            "PASI 100": "Complete clearance - 100% improvement in PASI score"
        }
        
        for term, definition in pasi_terms.items():
            st.markdown(f"**{term}:** {definition}")



def display_dlqi_domain_analysis(domain_scores):
    """Display DLQI domain analysis"""
    st.markdown("#### Domain Analysis")
    
    # Calculate domain totals
    domain_totals = {}
    for domain, scores in domain_scores.items():
        if scores:  # Only include domains with answers
            domain_totals[domain] = sum(scores)
    
    if domain_totals:
        # Create domain visualization
        fig = px.bar(
            x=list(domain_totals.keys()),
            y=list(domain_totals.values()),
            title="DLQI Domain Impact Scores",
            labels={'x': 'Life Domain', 'y': 'Impact Score'},
            color=list(domain_totals.values()),
            color_continuous_scale='RdYlBu_r'
        )
        fig.update_layout(showlegend=False, height=300)
        fig.update_xaxes(tickangle=45)
        
        st.plotly_chart(fig, use_container_width=True)

def generate_treatment_recommendations(pasi_score, bsa_score, dlqi_score, age, duration):
    """Generate comprehensive treatment recommendations"""
    
    # Determine overall severity
    if pasi_score >= 10 or bsa_score >= 10 or dlqi_score >= 10:
        severity = "severe"
    elif pasi_score >= 5 or bsa_score >= 5 or dlqi_score >= 5:
        severity = "moderate"
    else:
        severity = "mild"
    
    # Age categories
    if age < 18:
        age_group = "pediatric"
    elif age >= 65:
        age_group = "elderly"
    else:
        age_group = "adult"
    
    # Duration categories
    duration_category = "new_onset" if duration < 2 else "established"
    
    return {
        'severity': severity,
        'age_group': age_group,
        'duration_category': duration_category,
        'pasi_score': pasi_score,
        'bsa_score': bsa_score,
        'dlqi_score': dlqi_score,
        'age': age,
        'duration': duration
    }

def display_treatment_recommendations(recommendations):
    """Display comprehensive treatment recommendations"""
    
    severity = recommendations['severity']
    age_group = recommendations['age_group']
    age = recommendations['age']
    
    # Age-specific considerations
    if age_group == "pediatric":
        st.warning(f"""
        **Pediatric Considerations (Age: {age} years)**
        - **Topical therapy preferred:** First-line approach in children
        - **Limited systemic options:** Methotrexate and some biologics approved
        - **Weight-based dosing:** All medications require pediatric dosing
        - **Psychological support:** Important for school-age children
        - **Growth monitoring:** Required during systemic therapy
        """)
    elif age_group == "elderly":
        st.warning(f"""
        **Elderly Considerations (Age: {age} years)**
        - **Comorbidity assessment:** Screen for cardiovascular, renal, hepatic conditions
        - **Drug interactions:** Review all concurrent medications
        - **Reduced starting doses:** Lower initial doses may be appropriate
        - **Enhanced monitoring:** More frequent safety assessments
        - **Infection risk:** Increased susceptibility to infections
        """)
    
    # Treatment recommendations by severity
    col1, col2 = st.columns(2)
    
    with col1:
        if severity == "mild":
            st.success("""
            **First-line Treatment (Mild Psoriasis)**
            
            **Topical Therapy:**
            - Medium-potency corticosteroids
            - Vitamin D analogs (calcipotriol)
            - Combination products (calcipotriol/betamethasone)
            - Topical calcineurin inhibitors (face/flexures)
            
            **Adjunctive:**
            - Regular emollients and moisturizers
            - Lifestyle modifications
            """)
        
        elif severity == "moderate":
            st.warning("""
            **Treatment Options (Moderate Psoriasis)**
            
            **First-line:**
            - Optimize topical therapy
            - NB-UVB phototherapy
            - Consider systemic therapy if inadequate response
            
            **Systemic Options:**
            - Methotrexate 15-25mg weekly
            - Apremilast 30mg twice daily
            - Acitretin (if appropriate)
            """)
        
        else:  # severe
            st.error("""
            **Treatment Options (Severe Psoriasis)**
            
            **Systemic therapy indicated:**
            - Biologic therapy preferred
            - Conventional systemics if biologics contraindicated
            - Combination approaches may be needed
            
            **Biologic Options:**
            - IL-17 inhibitors: Ixekizumab, Secukinumab
            - IL-23 inhibitors: Guselkumab, Risankizumab
            - TNF inhibitors: Adalimumab, Etanercept
            """)
    
    with col2:
        # Monitoring requirements
        st.info("""
        **Monitoring Requirements**
        
        **Baseline Assessment:**
        - Complete blood count
        - Comprehensive metabolic panel
        - Liver function tests
        - Infectious disease screening
        
        **Ongoing Monitoring:**
        - Clinical assessment every 4-12 weeks
        - Laboratory monitoring per medication
        - PASI assessment at each visit
        - Safety monitoring for adverse events
        """)
        
        # Treatment goals
        st.info("""
        **Treatment Goals**
        
        **Primary Goals:**
        - PASI 75 response (75% improvement)
        - Absolute PASI ≤2-3 (almost clear skin)
        - DLQI improvement ≥5 points
        - Symptom relief (itch, pain)
        
        **Long-term Goals:**
        - Sustained disease control
        - Prevention of joint involvement
        - Improved quality of life
        - Minimal treatment burden
        """)

def display_clinical_guidelines():
    """Display clinical guidelines"""
    st.markdown("""
    ### Current Clinical Guidelines
    
    #### Severity Assessment
    
    **Rule of Tens (Moderate-to-Severe Psoriasis):**
    - PASI ≥10 OR BSA ≥10% OR DLQI ≥10
    
    **Severity Categories:**
    - **Mild:** PASI <5, BSA <5%, DLQI <5
    - **Moderate:** PASI 5-10, BSA 5-10%, DLQI 5-10
    - **Severe:** PASI >10, BSA >10%, DLQI >10
    
    #### Treatment Algorithms
    
    **Step 1: Topical Therapy**
    - Medium-potency corticosteroids
    - Vitamin D analogs (calcipotriol)
    - Combination products
    - Duration: 4-8 weeks trial
    
    **Step 2: Phototherapy**
    - NB-UVB preferred
    - PUVA for specific indications
    - 24-48 sessions typically required
    
    **Step 3: Systemic Therapy**
    - Conventional: Methotrexate, cyclosporine, acitretin
    - Biologics: TNF, IL-17, IL-23 inhibitors
    - Selection based on patient factors
    
    #### Treatment Targets
    - **PASI 75:** Primary endpoint (75% improvement)
    - **PASI 90:** Stringent response (90% improvement)
    - **Absolute PASI ≤2:** Almost clear skin
    - **DLQI improvement ≥5 points:** Clinically meaningful
    """)

def display_medication_reference():
    """Display medication reference"""
    
    medications = {
        "Topical Corticosteroids": {
            "examples": "Clobetasol propionate 0.05%, Betamethasone dipropionate 0.05%",
            "mechanism": "Anti-inflammatory, immunosuppressive, antiproliferative effects",
            "dosing": "Apply thin layer once or twice daily to affected areas",
            "duration": "Maximum 2-4 weeks for high potency on body, avoid face/flexures",
            "monitoring": "Monitor for skin atrophy, striae, HPA axis suppression with prolonged use"
        },
        "Vitamin D Analogs": {
            "examples": "Calcipotriol 50mcg/g, Calcitriol 3mcg/g",
            "mechanism": "Modulates keratinocyte differentiation and proliferation",
            "dosing": "Apply twice daily, maximum 100g/week (calcipotriol)",
            "duration": "Long-term use acceptable, maintenance therapy",
            "monitoring": "Monitor serum calcium with extensive use (>100g/week)"
        },
        "Methotrexate": {
            "examples": "Methotrexate tablets 2.5mg, injection 25mg/ml",
            "mechanism": "Folate antagonist, inhibits DNA synthesis and cell proliferation",
            "dosing": "15-25mg once weekly, with folic acid 5mg daily",
            "duration": "Long-term use acceptable with monitoring",
            "monitoring": "CBC, liver function, creatinine every 3 months; baseline chest X-ray"
        },
        "TNF Inhibitors": {
            "examples": "Adalimumab 40mg, Etanercept 50mg",
            "mechanism": "Blocks tumor necrosis factor-alpha signaling",
            "dosing": "Adalimumab 80mg initial, then 40mg every other week",
            "duration": "Long-term use, reassess annually",
            "monitoring": "TB screening, hepatitis B/C, CBC, LFTs every 3-6 months"
        }
    }
    
    for med, details in medications.items():
        with st.expander(med):
            st.markdown(f"**Examples:** {details['examples']}")
            st.markdown(f"**Mechanism:** {details['mechanism']}")
            st.markdown(f"**Dosing:** {details['dosing']}")
            st.markdown(f"**Duration:** {details['duration']}")
            st.markdown(f"**Monitoring:** {details['monitoring']}")

def display_monitoring_protocols():
    """Display monitoring protocols"""
    st.markdown("""
    ### Laboratory Monitoring Protocols
    
    #### Pre-treatment Screening
    
    **All Systemic Therapies:**
    - Complete blood count with differential
    - Comprehensive metabolic panel
    - Liver function tests
    - Hepatitis B surface antigen, core antibody, surface antibody
    - Hepatitis C antibody
    - Pregnancy test (if applicable)
    
    **Biologics Additional Screening:**
    - Tuberculosis screening (chest X-ray, interferon-gamma release assay)
    - HIV testing (if risk factors present)
    - Complete physical examination
    
    #### Ongoing Monitoring
    
    **Methotrexate:**
    - CBC, liver function tests: Every 4-8 weeks initially, then every 3 months
    - Serum creatinine: Every 3 months
    - Annual chest X-ray
    - Consider liver biopsy if cumulative dose >1.5g
    
    **Biologics:**
    - CBC, liver function tests: Every 3-6 months
    - Annual tuberculosis screening (chest X-ray)
    - Monitor for signs/symptoms of infection
    - Annual skin cancer screening
    
    **Cyclosporine:**
    - Serum creatinine, blood pressure: Every 2 weeks x 3 months, then monthly
    - CBC, liver function tests: Every 3 months
    - Lipid profile: Every 3 months
    - Maximum duration: 2 years continuously
    """)

def display_complete_glossary():
    """Display complete clinical glossary"""
    
    st.markdown("### Complete Clinical Glossary")
    
    glossary_terms = {
        "Psoriasis": "Chronic inflammatory skin disease characterized by well-demarcated erythematous plaques with silvery scales",
        "PASI": "Psoriasis Area and Severity Index - gold standard assessment tool (range 0-72)",
        "BSA": "Body Surface Area - percentage of total body surface affected by psoriasis",
        "DLQI": "Dermatology Life Quality Index - validated quality of life questionnaire (range 0-30)",
        "Erythema": "Redness of skin due to inflammation and vasodilation",
        "Induration": "Thickening and hardening of skin tissue, elevation above normal skin level",
        "Desquamation": "Scaling - shedding of outer skin layer in flakes or scales",
        "Plaque Psoriasis": "Most common form (85-90%) with raised, well-demarcated erythematous lesions",
        "Guttate Psoriasis": "Small, drop-shaped lesions, often following streptococcal infection",
        "Koebner Phenomenon": "Development of psoriatic lesions at sites of skin trauma",
        "PASI 75": "75% improvement in PASI score from baseline - primary clinical trial endpoint",
        "Rule of Tens": "PASI ≥10 OR BSA ≥10% OR DLQI ≥10 defines moderate-to-severe psoriasis",
        "TNF-α": "Tumor necrosis factor-alpha - key inflammatory cytokine in psoriasis pathogenesis",
        "IL-17": "Interleukin-17 - inflammatory cytokine, target of newer biologic therapies",
        "IL-23": "Interleukin-23 - upstream cytokine in Th17 pathway, biologic target",
        "Biologics": "Targeted immunosuppressive medications derived from living organisms",
        "NB-UVB": "Narrowband ultraviolet B phototherapy - preferred phototherapy modality",
        "Psoriatic Arthritis": "Inflammatory arthritis associated with psoriasis (affects ~30% of patients)",
        "HPA Axis Suppression": "Hypothalamic-pituitary-adrenal axis suppression from topical corticosteroids",
        "Tachyphylaxis": "Diminished response to topical corticosteroids with prolonged use"
    }
    
    for term, definition in glossary_terms.items():
        with st.expander(term):
            st.write(definition)

if __name__ == "__main__":
    main()
