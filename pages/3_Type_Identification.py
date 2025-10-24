import streamlit as st
from datetime import datetime

# ========================================================================
# MULTIPAGE APP - Page Module 3: Type Identification
# File name: 3_Type_Identification.py (for pages/ directory)
# ========================================================================
# NOTE: st.set_page_config() is REMOVED - only main app.py should have it
# ========================================================================

# Check if patient is registered (prerequisite check)
if 'patient_info' not in st.session_state or not st.session_state.patient_info:
    st.warning("⚠️ Please complete Patient Registration first")
    st.info("Use the sidebar to navigate to '1_Patient_Registration'")
    st.stop()

# Initialize identified types if not exists
if 'identified_types' not in st.session_state:
    st.session_state.identified_types = []

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
    
    .type-box {
        background-color: #f9f9f9;
        padding: 1.5rem;
        border-radius: 10px;
        border-left: 4px solid #667eea;
        margin: 1rem 0;
    }
    
    .type-description {
        background-color: #f0f8ff;
        padding: 1rem;
        border-radius: 8px;
        margin: 0.5rem 0;
        border-left: 3px solid #1e3a5f;
    }
</style>
""", unsafe_allow_html=True)

st.markdown('<div class="main-header"><h2>🏷️ Psoriasis Type Identification</h2></div>', unsafe_allow_html=True)

# Get patient info for display
patient_name = st.session_state.patient_info.get('patient_name', 'Unknown')
st.markdown(f"**Patient:** {patient_name}")
st.markdown("---")

st.markdown("### Classification of Psoriasis Subtypes")
st.markdown("Select all psoriasis types/subtypes that match the patient's clinical presentation.")

# Psoriasis types with descriptions
psoriasis_types = {
    'Plaque Psoriasis (Psoriasis Vulgaris)': {
        'prevalence': '80-90%',
        'description': 'Well-demarcated, erythematous plaques with silvery-white scales',
        'typical_locations': 'Elbows, knees, scalp, lower back, extensor surfaces',
        'characteristics': 'Most common form; chronic, sharply demarcated plaques'
    },
    'Guttate Psoriasis': {
        'prevalence': '8-10%',
        'description': 'Small (2-10mm), drop-shaped papules and plaques',
        'typical_locations': 'Trunk, proximal extremities',
        'characteristics': 'Acute onset; often preceded by streptococcal pharyngitis'
    },
    'Pustular Psoriasis': {
        'prevalence': '<1%',
        'description': 'Sterile pustules on erythematous base',
        'typical_locations': 'Palms, soles, or generalized',
        'characteristics': 'Can be localized or generalized; severe form'
    },
    'Inverse Psoriasis': {
        'prevalence': '3-7%',
        'description': 'Smooth, shiny erythematous patches without scales',
        'typical_locations': 'Intertriginous areas (skin folds)',
        'characteristics': 'Lack of typical scales; worse with moisture and friction'
    },
    'Erythrodermic Psoriasis': {
        'prevalence': '<1%',
        'description': 'Diffuse erythema and scaling covering >90% of BSA',
        'typical_locations': 'Generalized, entire body surface',
        'characteristics': 'Medical emergency; systemic symptoms possible'
    },
    'Nail Psoriasis': {
        'prevalence': '5-10%',
        'description': 'Nail changes including pitting, discoloration, onycholysis',
        'typical_locations': 'Fingernails or toenails',
        'characteristics': 'Can occur without skin involvement'
    },
    'Psoriatic Arthritis': {
        'prevalence': '5-10% of psoriasis patients',
        'description': 'Joint inflammation affecting peripheral and/or axial joints',
        'typical_locations': 'Peripheral joints (symmetrical) or spine',
        'characteristics': 'May precede or follow skin manifestations'
    }
}

# Create checkboxes for each type
selected_types = []

for type_name, type_info in psoriasis_types.items():
    with st.expander(f"📋 {type_name}"):
        col1, col2 = st.columns([3, 1])
        with col1:
            st.write(f"**Prevalence:** {type_info['prevalence']}")
            st.write(f"**Description:** {type_info['description']}")
            st.write(f"**Typical Locations:** {type_info['typical_locations']}")
            st.write(f"**Key Characteristics:** {type_info['characteristics']}")
        with col2:
            is_selected = st.checkbox(f"Select", key=f"check_{type_name}")
            if is_selected:
                selected_types.append(type_name)

# Identification form
st.markdown("---")
st.markdown("### Type Identification Summary")

# Additional clinical notes
additional_notes = st.text_area(
    "Additional Clinical Notes (Optional)",
    placeholder="Enter any additional observations or clinical notes...",
    height=100
)

# Submit button
col1, col2, col3 = st.columns(3)

with col2:
    if st.button("✅ Save Type Identification", type="primary", use_container_width=True):
        if selected_types:
            # Save to session state
            st.session_state.identified_types = selected_types
            
            st.success(f"✅ Identified {len(selected_types)} psoriasis type(s)!")
            st.balloons()
            
            # Display identified types
            st.markdown("### Identified Types")
            for idx, ptype in enumerate(selected_types, 1):
                st.markdown(f"{idx}. **{ptype}**")
            
            if additional_notes:
                st.markdown(f"**Clinical Notes:** {additional_notes}")
            
            # ===== NEW: NAVIGATION HINT =====
            st.markdown("---")
            st.info("""
            ➡️ **Next Step:** Proceed to **'Severity Assessment'** in the sidebar
            
            The severity assessment module will calculate PASI, BSA, and DLQI scores 
            along with treatment recommendations.
            """)
        else:
            st.error("⚠️ Please select at least one psoriasis type")

# Footer
st.markdown("---")
st.markdown("""
<div style="text-align: center; color: #666; font-size: 0.9rem;">
    <p><strong>Type Identification Module</strong> | Classification based on clinical presentation</p>
</div>
""", unsafe_allow_html=True)
