import streamlit as st
import pandas as pd


# Custom CSS for better formatting
st.markdown("""
<style>
    .question-text {
        font-size: 1.4em;
        font-weight: bold;
        color: #1E293B;
        margin-bottom: 15px;
    }
    .section-header {
        background: linear-gradient(135deg, #3B82F6 0%, #2563EB 100%);
        color: white;
        padding: 15px;
        border-radius: 10px;
        font-size: 1.5em;
        font-weight: bold;
        margin: 20px 0;
    }
    .score-box {
        background: linear-gradient(135deg, #10B981 0%, #059669 100%);
        color: white;
        padding: 20px;
        border-radius: 10px;
        text-align: center;
        font-size: 1.8em;
        font-weight: bold;
        margin: 20px 0;
    }
    .stImage {
        border-radius: 10px;
        border: 2px solid #E5E7EB;
    }
</style>
""", unsafe_allow_html=True)

st.title("🩺 Comprehensive Psoriasis Visual Diagnostic Matrix")
st.caption("Clinician + Patient friendly. Each question is illustrated and scored. Final recommendation is driven by matrix score.")

def yes_no_question(question_num, question_text, img_url, caption="", weight=1):
    """Display question with image and radio buttons"""
    st.markdown(f'<div class="question-text">Q{question_num}. {question_text}</div>', unsafe_allow_html=True)
    
    # Display image with fixed size
    st.image(img_url, caption=caption, width=600)
    
    # Radio buttons below image
    answer = st.radio(
        f"Select answer for Question {question_num}:",
        ["No", "Yes"],
        horizontal=True,
        index=0,
        key=f"q{question_num}"
    )
    
    st.markdown("---")
    return (answer == "Yes") * weight

# ===================== Section 1: Clinical Features ======================
st.markdown('<div class="section-header">Section 1: Primary Clinical Features (Max: 12 points)</div>', unsafe_allow_html=True)

q1 = yes_no_question(
    1,
    "Are plaques well-demarcated, thick, and red like these on elbows/knees/face areas?",
    "https://www.researchgate.net/publication/318736667/figure/fig7/AS:962699810852874@1606536929703/a-Plaque-psoriasis-elbow-b-Plaque-psoriasis-knee-c-Psoriasis-face-and-scalp.gif",
    "Classic plaque psoriasis: Red/raised plaques, clear borders, silvery scales on elbows/knees/face.",
    weight=3
)

q2 = yes_no_question(
    2,
    "Are the scales silvery-white, thick, and easily scraped off, as shown?",
    "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcSYTzhZh30dSIa6V-K7MjoCks5wTOjiwxBEPfn4zo7JycGSxW2PPQ950cYPOPdJSnRa9SM&usqp=CAU",
    "Silvery, thick scale typical of psoriasis.",
    weight=3
)

q3 = yes_no_question(
    3,
    "Are lesions mainly on flexural or inverse (inside elbows/knees, wrists)?",
    "data:image/jpeg;base64,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",
    "Flexural/inverse psoriasis.",
    weight=3
)

q4 = yes_no_question(
    4,
    "Are lesions symmetrical (same on both sides of the body)?",
    "https://edge.sitecorecloud.io/mmanual-ssq1ci05/media/professional/images/c/0/2/c0225511_psoriasis_of_the_elbows_science_photo_library_high.jpg?sc_lang=en&mw=828",
    "Bilateral symmetry is typical for psoriasis.",
    weight=3
)

# ===================== Section 2: Pathognomonic Signs ======================
st.markdown('<div class="section-header">Section 2: Pathognomonic Signs (Max: 8 points)</div>', unsafe_allow_html=True)

q5 = yes_no_question(
    5,
    "Does gentle scraping of scale cause pinpoint bleeding (Auspitz sign)?",
    "https://www.researchgate.net/publication/7073510/figure/fig1/AS:341128168656904@1458342701396/Auspitz-sign-multiple-pinpoint-bleeding-observed-on-scraping-the-scales-in-psoriasis.png",
    "Auspitz sign: Pinpoint bleeding after removing scale - highly specific for psoriasis.",
    weight=4
)

q6 = yes_no_question(
    6,
    "Do new lesions appear along trauma/scratch lines (Koebner phenomenon)?",
    "https://img.medscapestatic.com/pi/meds/ckb/91/36191.jpg",
    "Koebner phenomenon: Linear lesions at injury site - characteristic of active psoriasis.",
    weight=4
)

# ===================== Section 3: Associated Features ======================
st.markdown('<div class="section-header">Section 3: Associated Features (Max: 6 points)</div>', unsafe_allow_html=True)

q7 = yes_no_question(
    7,
    "Are there changes in nails (pitting, thickening, yellow discoloration, separation)?",
    "https://www.jrheum.org/content/jrheum/48/8/1208/F2.large.jpg",
    "Nail psoriasis: Pitting, onycholysis, thickening, oil-drop discoloration.",
    weight=3
)

q8 = yes_no_question(
    8,
    "Is there persistent, thick, scaly plaque on the scalp (possibly extending beyond hairline)?",
    "https://hips.hearstapps.com/hmg-prod/images/scalp-psoriasis-1525275705.jpg",
    "Scalp psoriasis: Well-defined red plaques with scaling.",
    weight=3
)

# ===================== Section 4: Clinical History ======================
st.markdown('<div class="section-header">Section 4: Clinical History (Max: 8 points)</div>', unsafe_allow_html=True)

st.markdown('<div class="question-text">Q9. Have lesions lasted more than 6 weeks?</div>', unsafe_allow_html=True)
q9 = st.radio(
    "Chronic duration (>6 weeks) supports psoriasis diagnosis:",
    ["No", "Yes"],
    horizontal=True,
    index=0,
    key="q9"
) == "Yes"
q9_score = 2 if q9 else 0
st.markdown("---")

st.markdown('<div class="question-text">Q10. Family history of psoriasis (parent, sibling, child)?</div>', unsafe_allow_html=True)
q10 = st.radio(
    "30-40% of psoriasis patients have positive family history:",
    ["No", "Yes"],
    horizontal=True,
    index=0,
    key="q10"
) == "Yes"
q10_score = 3 if q10 else 0
st.markdown("---")

st.markdown('<div class="question-text">Q11. Did symptoms start at typical ages (20-30 or 50-60 years)?</div>', unsafe_allow_html=True)
q11 = st.radio(
    "Psoriasis has two peak ages of onset:",
    ["No", "Yes"],
    horizontal=True,
    index=0,
    key="q11"
) == "Yes"
q11_score = 2 if q11 else 0
st.markdown("---")

st.markdown('<div class="question-text">Q12. Any recent triggers? (skin injury, stress, new medications, recent strep throat)</div>', unsafe_allow_html=True)
q12 = st.radio(
    "Common psoriasis triggers:",
    ["No", "Yes"],
    horizontal=True,
    index=0,
    key="q12"
) == "Yes"
q12_score = 1 if q12 else 0
st.markdown("---")

# ===================== Section 5: Symptom Characteristics ======================
st.markdown('<div class="section-header">Section 5: Symptom Characteristics (Max: 4 points)</div>', unsafe_allow_html=True)

st.markdown('<div class="question-text">Q13. Is itching mild or absent?</div>', unsafe_allow_html=True)
q13 = st.radio(
    "Psoriasis typically causes mild itching (severe itching suggests eczema):",
    ["No", "Yes"],
    horizontal=True,
    index=0,
    key="q13"
) == "Yes"
q13_score = 2 if q13 else 0
st.markdown("---")

st.markdown('<div class="question-text">Q14. Are the patches thick, dry, and raised (not oozing/crusting)?</div>', unsafe_allow_html=True)
q14 = st.radio(
    "Psoriasis lesions are dry and raised (oozing suggests eczema):",
    ["No", "Yes"],
    horizontal=True,
    index=0,
    key="q14"
) == "Yes"
q14_score = 2 if q14 else 0
st.markdown("---")

# ===================== Section 6: Exclusion Features (Subtract points) ======================
st.markdown('<div class="section-header">Section 6: Exclusion Criteria (Negative Points)</div>', unsafe_allow_html=True)
st.warning("⚠️ These features REDUCE likelihood of psoriasis and suggest alternative diagnoses")

st.markdown('<div class="question-text">Q15. Are lesions mainly on flexor areas (inside elbows/knees)?</div>', unsafe_allow_html=True)
q15 = st.radio(
    "Flexor distribution suggests ECZEMA rather than psoriasis:",
    ["No", "Yes"],
    horizontal=True,
    index=0,
    key="q15"
) == "Yes"
q15_score = -3 if q15 else 0
st.markdown("---")

st.markdown('<div class="question-text">Q16. Are lesions oozing, crusting, or weeping?</div>', unsafe_allow_html=True)
q16 = st.radio(
    "Oozing/crusting suggests ECZEMA rather than psoriasis:",
    ["No", "Yes"],
    horizontal=True,
    index=0,
    key="q16"
) == "Yes"
q16_score = -3 if q16 else 0
st.markdown("---")

st.markdown('<div class="question-text">Q17. Has a doctor found fungal infection by test (KOH/fungal culture)?</div>', unsafe_allow_html=True)
q17 = st.radio(
    "Positive fungal test confirms TINEA infection:",
    ["No", "Yes"],
    horizontal=True,
    index=0,
    key="q17"
) == "Yes"
q17_score = -5 if q17 else 0
st.markdown("---")

st.markdown('<div class="question-text">Q18. Is there a clear pattern matching a chemical/allergen exposure?</div>', unsafe_allow_html=True)
q18 = st.radio(
    "Exposure pattern suggests CONTACT DERMATITIS:",
    ["No", "Yes"],
    horizontal=True,
    index=0,
    key="q18"
) == "Yes"
q18_score = -2 if q18 else 0
st.markdown("---")

st.markdown('<div class="question-text">Q19. Is itching severe (especially at night)?</div>', unsafe_allow_html=True)
q19 = st.radio(
    "Severe nocturnal itching suggests ECZEMA:",
    ["No", "Yes"],
    horizontal=True,
    index=0,
    key="q19"
) == "Yes"
q19_score = -2 if q19 else 0
st.markdown("---")

# ============ Calculate Scores ============
primary_score = q1 + q2 + q3 + q4
pathognomonic_score = q5 + q6
associated_score = q7 + q8
history_score = q9_score + q10_score + q11_score + q12_score
symptom_score = q13_score + q14_score
exclusion_score = q15_score + q16_score + q17_score + q18_score + q19_score
total_score = primary_score + pathognomonic_score + associated_score + history_score + symptom_score + exclusion_score

# ============ Display Results ============
st.markdown("---")
st.markdown("# 📊 DIAGNOSTIC RESULTS")

# Detailed Score Breakdown Table
st.subheader("🔢 Detailed Scoring Matrix")

score_data = {
    'Section': [
        '1. Primary Clinical Features',
        '2. Pathognomonic Signs',
        '3. Associated Features',
        '4. Clinical History',
        '5. Symptom Characteristics',
        '6. Exclusion Criteria',
        '📍 TOTAL SCORE'
    ],
    'Your Score': [
        f'{primary_score}',
        f'{pathognomonic_score}',
        f'{associated_score}',
        f'{history_score}',
        f'{symptom_score}',
        f'{exclusion_score}',
        f'{total_score}'
    ],
    'Maximum Possible': [
        '12',
        '8',
        '6',
        '8',
        '4',
        '0 (penalties only)',
        '38'
    ]
}

df = pd.DataFrame(score_data)
st.table(df)

# Score Display
st.markdown(f'<div class="score-box">Total Score: {total_score} / 38</div>', unsafe_allow_html=True)

# Progress bar
progress = min(max(total_score/38, 0), 1)
st.progress(progress)

# ============ Diagnosis and Recommendations ============
st.markdown("---")
st.subheader("🩺 CLINICAL INTERPRETATION")

if total_score >= 18:
    st.success("✅ **DIAGNOSIS: HIGH PROBABILITY OF PSORIASIS**")
    st.markdown("""
    ### Clinical Recommendation:
    Based on the scoring matrix, clinical features strongly support psoriasis diagnosis.
    
    ### Next Steps:
    1. **Proceed to severity assessment** using PASI/BSA/DLQI tools
    2. Document psoriasis type (plaque, guttate, inverse, etc.)
    3. Consider dermatology referral if moderate-severe
    4.  Initiate appropriate treatment based on severity
    
    ### Treatment Pathway:
    - **Mild** (BSA <3%): Topical therapy
    - **Moderate** (BSA 3-10%): Phototherapy or systemic therapy
    - **Severe** (BSA >10%): Systemic therapy or biologics
    """)
    
    if st.button("📊 Proceed to PASI/BSA/DLQI Assessment", type="primary"):
        st.info("➡️ Loading severity assessment tools...")
        st.balloons()

elif total_score >= 12:
    st.warning("⚠️ **DIAGNOSIS: MODERATE PROBABILITY OF PSORIASIS**")
  

else:
    st.error("❌ **DIAGNOSIS: LOW PROBABILITY - Features NOT typical for psoriasis**")
    
# ============ Footer ============
st.markdown("---")
