import streamlit as st

# Custom CSS
st.markdown("""
<style>
    .type-header {
        background: linear-gradient(135deg, #8B5CF6 0%, #7C3AED 100%);
        color: white;
        padding: 20px;
        border-radius: 12px;
        text-align: center;
        font-size: 1.8em;
        font-weight: bold;
        margin: 20px 0;
    }
    .question-text {
        font-size: 1.4em;
        font-weight: bold;
        color: #1E293B;
        margin: 20px 0 15px 0;
    }
    .type-card {
        background: white;
        border: 3px solid #E5E7EB;
        border-radius: 12px;
        padding: 20px;
        margin: 15px 0;
        box-shadow: 0 4px 6px rgba(0,0,0,0.1);
    }
    .type-card-selected {
        background: #DBEAFE;
        border: 3px solid #3B82F6;
        border-radius: 12px;
        padding: 20px;
        margin: 15px 0;
        box-shadow: 0 6px 12px rgba(59,130,246,0.3);
    }
    .result-box {
        background: linear-gradient(135deg, #10B981 0%, #059669 100%);
        color: white;
        padding: 25px;
        border-radius: 12px;
        text-align: center;
        font-size: 1.5em;
        font-weight: bold;
        margin: 20px 0;
    }
</style>
""", unsafe_allow_html=True)

st.markdown('<div class="type-header"> Psoriasis Type Identifier</div>', unsafe_allow_html=True)
st.caption("Compare your clinical findings with the images below to identify the psoriasis type")

# Initialize session state
if 'identified_types' not in st.session_state:
    st.session_state.identified_types = []

# Define psoriasis types with multiple body locations
psoriasis_types = {
    "Plaque Psoriasis": {
        "description": "Most common type (80-90%). Raised, well-demarcated red/salmon plaques with silvery-white scales.",
        "locations": {
            "Elbows": [
                "https://dermnetnz.org/assets/Uploads/scaly/ps3.jpg",
                "https://dermnetnz.org/assets/Uploads/chronic-plaque-psoriasis-019.jpg"
            ],
            "Knees": [
                "https://images.ctfassets.net/1ny4yoiyrqia/54OopOYh9SGLl8xuiNuCJs/1cee8b0661e416b810e417420b31237e/psoriasis-on-knees.gif",
                "https://dermnetnz.org/assets/Uploads/scaly/ps6.jpg"
            ],
            "Hands/Arms": [
                "https://images.prismic.io/npf-website/6c538fed-39a1-40c0-94f0-1b33020eddb5_Plaque%20Psoriasis%20Hand.jpg?ixlib=gatsbyFP&auto=format%2Ccompress&fit=max&rect=0%2C18%2C700%2C402&w=778&h=447",
                "https://images.prismic.io/npf-website/Z_lRqOvxEdbNO8KZ_2-3-up-778x447px-.png?ixlib=gatsbyFP&auto=format%2Ccompress&fit=max&rect=0%2C0%2C778%2C447&w=778&h=447"
            ],
            "Trunk/Back": [
                "https://images.ctfassets.net/1ny4yoiyrqia/6jkrJo9fXjeepYfzp3omZN/fbed12ca68a12ccdacf5ff27d707988b/plaque-psoriasis.gif?fm=webp&w=450&h=450",
                "https://images.prismic.io/npf-website/0c6a5f38-7111-40a8-b103-1a50abf01840_plaque_psoriasis_in_type_v_skin-visualdx.jpeg?ixlib=gatsbyFP&auto=format%2Ccompress&fit=max&rect=0%2C18%2C466%2C268&w=778&h=447"
            ]
        }
    },
    "Inverse Psoriasis": {
        "description": "Smooth, shiny red patches in skin folds. Little to no scales due to moisture.",
        "locations": {
            "Groin/Genitals": [
                "https://dermnetnz.org/assets/Uploads/scaly/genital-psoriasis-12.jpg",
                "https://images.prismic.io/npf-website/c8234450-4ac0-4916-81bf-f97b7b549272_INVERSE.jpg?ixlib=gatsbyFP&auto=format%2Ccompress&fit=max&rect=0%2C62%2C600%2C345&w=778&h=447"
            ],
            "Armpits": [
                "https://dermnetnz.org/assets/Uploads/scaly/a/flexural-psoriasis.jpg",
                "https://images.prismic.io/npf-website/Z93Y-3dAxsiBvwew_inversepsoriasis1.jpg?ixlib=gatsbyFP&auto=format%2Ccompress&fit=max&rect=0%2C95%2C750%2C431&w=778&h=447"
            ],
            "Under Breasts/Skin Folds": [
                "https://images.ctfassets.net/1ny4yoiyrqia/5yQPr9MikItyZT3eQ2ZZnS/416ea6915af2f2771f16dfe009de1615/inverse-psoriasis-2.gif",
                "https://dermnetnz.org/assets/Uploads/psorkai2.jpg"
            ]
        }
    },
    "Guttate Psoriasis": {
        "description": "Small drop-shaped lesions, often after strep throat. Common in children/young adults.",
        "locations": {
            "Trunk": [
                "https://images.prismic.io/npf-website/ca0727c9-352b-4cc1-b748-2b9010e93fe2_Gutate%203.JPG?ixlib=gatsbyFP&auto=format%2Ccompress&fit=max&rect=0%2C323%2C1704%2C979&w=778&h=447",
                "https://dermnetnz.org/assets/Uploads/scaly/ps4.jpg"
            ],
            "Arms/Legs": [
                "https://images.ctfassets.net/1ny4yoiyrqia/21rUYnHQIAUfXeJ5731evq/f77fe53821d9c0b16bc3fc1ed1974b8e/guttate-psoriasis.gif",
                "https://dermnetnz.org/assets/Uploads/scaly/guttate-psoriasis/2763.jpg"
            ],
            "Back": [
                "https://images.prismic.io/npf-website/Z-XiwndAxsiBwA2q_2-3-up-778x447px--15-.png?ixlib=gatsbyFP&auto=format%2Ccompress&fit=max&rect=0%2C0%2C778%2C447&w=778&h=447",
                "https://dermnetnz.org/assets/Uploads/scaly/guttate-psoriasis/2754.jpg"
            ]
        }
    },
    "Pustular Psoriasis": {
        "description": "Sterile pus-filled blisters on red skin. Can be localized (hands/feet) or generalized.",
        "locations": {
            "Palms/Hands": [
                "https://images.prismic.io/npf-website/6f7c42e1-5185-459f-a42c-276c4f06423b_NPF-Pustular-psoriasis.jpg?ixlib=gatsbyFP&auto=format%2Ccompress&fit=max&rect=0%2C53%2C1192%2C685&w=778&h=447",
                "https://images.ctfassets.net/1ny4yoiyrqia/1gFkgrNsD3xrdlQYETpXae/faee7164f712902b110936544948f784/pustular-psoriasis.gif"
            ],
            "Soles/Feet": [
                "https://images.prismic.io/npf-website/Z93fjXdAxsiBvwgx_pustular-psoriasis.jpg?ixlib=gatsbyFP&auto=format%2Ccompress&fit=max&rect=0%2C76%2C1700%2C977&w=778&h=447"
            ],
            "Generalized (Whole Body)": [
                "https://images.ctfassets.net/1ny4yoiyrqia/3Mlm3CAADYIXrAdEqdttFM/12fceed713bcaa5cd4111538961999ef/generalized-pustular-psoriaisis.gif"
            ]
        }
    },
    "Erythrodermic Psoriasis": {
        "description": "MEDICAL EMERGENCY! Widespread redness covering >90% of body. Severe peeling, pain.",
        "locations": {
            "Whole Body (>90% coverage)": [
                "https://images.prismic.io/npf-website/76e978e0-9e7c-4ddb-ab76-b83432e43d25_Erythrodermic.jpg?ixlib=gatsbyFP&auto=format%2Ccompress&fit=max&rect=0%2C130%2C404%2C232&w=778&h=447",
                "https://images.ctfassets.net/1ny4yoiyrqia/2O91Mu5NYf78aBcrfBeztz/b35d08adc8859f3727dcdb395743cee8/erythrodermic-psoriasis.gif"
            ],
            "Severe widespread peeling": [
                "https://dermnetnz.org/assets/Uploads/doctors/emergencies/images/ps-e1.jpg",
                "https://dermnetnz.org/assets/Uploads/doctors/scaly-rashes/images/ps-e2.jpg"
            ],
            "Emergency presentation": [
                "https://dermnetnz.org/assets/Uploads/scaly/ps-e4.jpg"
            ]
        }
    },
    "Nail Psoriasis": {
        "description": "Pitting, thickening, discoloration, onycholysis (nail lifting), crumbling.",
        "locations": {
            "Fingernails": [
                "https://images.ctfassets.net/1ny4yoiyrqia/SHQkmSoXqrQmvekYdyVk0/e55314f0a62a7cc9d4bad6a3c4b84991/nail-psoriasis.gif",
                "https://images.ctfassets.net/1ny4yoiyrqia/6VAjIegRK5DJzI9Y9Z538j/e2b2c31ddbfecc1227facacf4d679b2a/Nail-psoriasis-image-A.gif?fm=webp&w=450&h=450"
            ],
            "Nail pitting": [
                "https://images.ctfassets.net/1ny4yoiyrqia/2e3codhW1ex5BEYw9SMbEN/1e5e04bdb54b68e712ad3fb7e2cb21cd/Nail-psoriasis_image-B.gif?fm=webp&w=450&h=450",
                "https://dermnetnz.org/assets/Uploads/psoriatic-nail-004.jpg"
            ],
            "Onycholysis & discoloration": [
                "https://images.ctfassets.net/1ny4yoiyrqia/6s0R59Z1NYC9wRGWpaPTD4/de6b297b431ede11e2ee8e632a1179c6/Nail-psoriasis_image-C.gif?fm=webp&w=450&h=450",
                "https://images.ctfassets.net/1ny4yoiyrqia/71n3t4UmuaN3de7NbRUTSt/de1335c6d589e7c16bd5acd6ca7bf642/Nail-psoriasis_Image-D.gif?fm=webp&w=450&h=450"
            ],
            "Severe nail changes": [
                "https://images.ctfassets.net/1ny4yoiyrqia/2vrb1CC5QUFQor48yJHnAY/6b1972975a3b49fa395453483396eedf/Nail-psoriasis_Image-E.gif?fm=webp&w=450&h=450",
                "https://dermnetnz.org/assets/Uploads/psoriatic-nail-037.jpg"
            ]
        }
    },
    "Psoriatic Arthritis": {
        "description": "Joint inflammation with swelling, pain, stiffness. Sausage digits, nail changes.",
        "locations": {
            "Hands/Fingers": [
                "https://images.ctfassets.net/1ny4yoiyrqia/7AdSo9Okr8rENi1wLNQnAP/a5db65e125a3fbc2ef9e1598c47cd790/psoriatic-arthritis-hand.jpg?fm=webp&w=450&h=450",
                "https://images.ctfassets.net/1ny4yoiyrqia/3MsppIhaEh5sZMS91sk2Rf/5d36a110f0e6d0d7d45108bc43618eb5/psoriasis-nails.jpg?fm=webp&w=450&h=450"
            ],
            "Feet/Toes": [
                "https://images.ctfassets.net/1ny4yoiyrqia/6lo5SeQcq3TJGID5kti3YW/363c3ee8d95173ee1d5564b83f3c6771/psoriatic-arthritis-toe.gif",
                "https://images.ctfassets.net/1ny4yoiyrqia/4n7D0s0alJXFg6zL2YLcYk/c9d60a2a991569621a223939b2a07a92/foot.jpg?fm=webp&w=450&h=450"
            ],
            "Sausage digit & tendon": [
                "https://images.ctfassets.net/1ny4yoiyrqia/2NSJULHiZo2xMJz5DDt2av/1b1f55d857d0aec8582e26fa2f115794/sausage-digit.jpg?fm=webp&w=450&h=450",
                "https://images.ctfassets.net/1ny4yoiyrqia/6Tdfj0moMWtUSFdZYezjJx/3b4c96151ad1a582e20ccdfad68de957/Archilles-heel.jpg?fm=webp&w=450&h=450"
            ]
        }
    }
}

# Display each type with locations
st.markdown("---")
st.subheader(" Compare Your Clinical Findings")
st.info("Select ALL psoriasis types that match your patient's presentation. Multiple types can coexist.")

for psoriasis_type, data in psoriasis_types.items():
    with st.expander(f"{psoriasis_type}", expanded=False):
        st.markdown(f"**Description:** {data['description']}")
        
        # Checkbox for selection
        is_selected = st.checkbox(
            f"Patient has {psoriasis_type}",
            key=f"select_{psoriasis_type}"
        )
        
        if is_selected and psoriasis_type not in st.session_state.identified_types:
            st.session_state.identified_types.append(psoriasis_type)
        elif not is_selected and psoriasis_type in st.session_state.identified_types:
            st.session_state.identified_types.remove(psoriasis_type)
        
        # Display images by body location
        for location, images in data['locations'].items():
            st.markdown(f"**{location}:**")
            cols = st.columns(len(images))
            for idx, img_url in enumerate(images):
                with cols[idx]:
                    st.image(img_url, caption=f"{psoriasis_type} - {location}", width=300)
        
        st.markdown("---")

# Display Results
st.markdown("---")
st.markdown("#  IDENTIFICATION RESULTS")

if len(st.session_state.identified_types) > 0:
    st.markdown(f'<div class="result-box">Identified Type(s): {len(st.session_state.identified_types)}</div>', unsafe_allow_html=True)
    
    for idx, ptype in enumerate(st.session_state.identified_types, 1):
        st.success(f"**{idx}. {ptype}**")
        st.write(f"📋 {psoriasis_types[ptype]['description']}")
        
        # Clinical recommendations based on type
        if ptype == "Erythrodermic Psoriasis":
            st.error("⚠️ **IMMEDIATE MEDICAL ATTENTION REQUIRED** - This is a life-threatening emergency!")
        elif ptype == "Pustular Psoriasis":
            st.warning("⚠️ **URGENT** - Requires specialist evaluation and systemic therapy")
        elif ptype == "Psoriatic Arthritis":
            st.warning("**Rheumatology Referral Needed** - Joint damage can be progressive")
    
    st.markdown("---")
    st.subheader(" Next Steps:")
    st.write("""
    1. Psoriasis type(s) identified
    2. Proceed to severity assessment (PASI/BSA/DLQI)
    3. Develop treatment plan based on type and severity
    4. Consider specialist referral if indicated
    """)
    
    if st.button("Proceed to PASI/BSA/DLQI Assessment", type="primary"):
        st.balloons()
        st.info(" Loading severity assessment tools...")
    
else:
    st.info(" Select the psoriasis type(s) that match your clinical findings from the expandable sections above")

# Summary table
if len(st.session_state.identified_types) > 0:
    st.markdown("---")
    st.subheader(" Summary Table")
    
    import pandas as pd
    summary_data = []
    for ptype in st.session_state.identified_types:
        locations = list(psoriasis_types[ptype]['locations'].keys())
        summary_data.append({
            'Psoriasis Type': ptype,
            'Body Locations': ', '.join(locations),
            'Description': psoriasis_types[ptype]['description']
        })
    
    df = pd.DataFrame(summary_data)
    st.table(df)
