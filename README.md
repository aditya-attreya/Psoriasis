🩺 Psoriasis Clinical Decision Support System (CDSS)
A comprehensive web-based Clinical Decision Support System for psoriasis assessment, diagnosis, and severity evaluation. This platform integrates validated clinical tools including PASI, BSA, and DLQI assessments to support healthcare professionals in psoriasis management.

📋 Table of Contents

    Overview
    Features
    System Modules
    Installation
    Usage
    Deployment
    Clinical Tools
    Repository Structure
    Contributing
    Citation


🎯 Overview

Psoriasis is a chronic inflammatory skin disease affecting 2-3% of the global population. This CDSS provides a structured, evidence-based approach to psoriasis evaluation through four integrated assessment modules:

    Introduction & Patient Registration - Clinical overview and patient data collection

    Diagnostic Matrix - Visual diagnostic screening tool

    Type Identification - Psoriasis subtype classification

    Severity Assessment - Comprehensive PASI, BSA, and DLQI evaluation

The system is designed for use by dermatologists, general practitioners, medical students, and researchers.

✨ Features
Clinical Assessment

    ✅ Evidence-based diagnostic criteria

    ✅ Validated assessment tools (PASI, BSA, DLQI)

    ✅ Interactive visual diagnostic matrix

    ✅ Automated scoring and severity classification

    ✅ Treatment recommendations based on clinical guidelines

User Experience

    🎨 Professional, clinician-friendly interface

    📱 Responsive design - works on desktop, tablet, and mobile

    🔄 Session state management across modules

    📊 Interactive visualizations and charts

    💾 Data continuity between modules

Technical Features

    ⚡ Fast, real-time calculations

    🔒 Secure deployment on Streamlit Cloud

    🌐 Public web access - no installation required

    📈 Plotly-based interactive charts

    🎯 Modular architecture for easy maintenance


🏥 System Modules
Module 1: Introduction & Overview

File: pages/1_Introduction.py

    Comprehensive psoriasis educational content

    Patient demographic information collection

    Overview of assessment tools and scoring systems

    Clinical background on psoriasis types

Module 2: Diagnostic Matrix

File: pages/2_Diagnostic_Matrix.py

    Visual diagnostic screening questionnaire

    Image-based clinical assessment

    Weighted scoring system

    Diagnostic likelihood calculation

    Clinician and patient-friendly interface

Module 3: Type Identification

File: pages/3_Type_Identification.py

    Classification of psoriasis subtypes:

        Plaque Psoriasis (Psoriasis Vulgaris)

        Guttate Psoriasis

        Inverse Psoriasis

        Pustular Psoriasis

        Erythrodermic Psoriasis

    Detailed clinical criteria for each type

    Interactive assessment interface

Module 4: Severity Assessment

File: pages/4_Severity_Assessment.py

    PASI Score - Psoriasis Area and Severity Index

        Body region assessment (head, trunk, upper limbs, lower limbs)

        Erythema, induration, and scaling evaluation

        Automated calculation (0-72 scale)

    BSA Score - Body Surface Area

        Percentage of body surface affected

        Quick assessment method

    DLQI Score - Dermatology Life Quality Index

        Patient-reported quality of life impact

        10-question validated questionnaire

        Score interpretation (0-30 scale)

    Treatment Recommendations

        Guidelines based on severity scores

        Therapy options visualization

        Evidence-based recommendations

💻 Installation
Prerequisites

    Python 3.9 or higher

    pip package manager

    Git

Local Installation
1.Clone the repository
git clone https://github.com/aditya-attreya/Psoriasis_Diagnostic_Matrix.git
cd Psoriasis_Diagnostic_Matrix

2.Create a virtual environment (recommended)
python -m venv venv

# On Windows
venv\Scripts\activate

# On macOS/Linux
source venv/bin/activate

3.Install dependencies
pip install -r requirements.txt

4.Run the application
streamlit run Home.py

5.Open in browser
The app will automatically open at http://localhost:8501


📖 Usage
For Clinicians

    Access the application via the provided URL

    Navigate modules using the sidebar menu

    Start with Module 1 for patient registration (optional)

    Use Module 2 for diagnostic screening if needed

    Proceed to Module 3 for type classification

    Complete Module 4 for severity assessment and treatment guidance

For Researchers

    Use the system for clinical studies and data collection

    Standardized assessment protocols

    Reproducible scoring methods

    Export-ready visualizations

For Medical Education

    Interactive learning tool for psoriasis assessment

    Hands-on practice with clinical scoring systems

    Visual examples of psoriasis presentations

    Evidence-based treatment guidelines

🌐 Deployment
Deploy to Streamlit Community Cloud (Free)

    Prepare your repository

        Ensure all files are committed to GitHub

        Verify requirements.txt is in the repository root

        Ensure Home.py is in the repository root

    Deploy on Streamlit Cloud

        Go to share.streamlit.io

        Sign in with GitHub

        Click "New app"

        Select your repository

        Set main file: Home.py

        Click "Deploy"

    Access your app

        Your app will be available at: https://[username]-[repo-name].streamlit.app

        Share this URL with users

Alternative Deployment Options

    Heroku: Follow Streamlit Heroku deployment guide

    AWS EC2: Deploy on cloud infrastructure

    Docker: Containerize the application

    Azure Web Apps: Microsoft cloud platform


🔬 Clinical Tools
PASI (Psoriasis Area and Severity Index)

    Range: 0-72

    Components: Erythema, induration, desquamation, area involvement

    Body regions: Head (10%), trunk (30%), upper limbs (20%), lower limbs (40%)

    Interpretation:

        0-5: Mild

        5-10: Moderate

            10: Severe

BSA (Body Surface Area)

    Range: 0-100%

    Method: Palm method (1 palm = 1% BSA)

    Interpretation:

        <3%: Mild

        3-10%: Moderate

            10%: Severe

DLQI (Dermatology Life Quality Index)

    Range: 0-30

    Domains: Symptoms, daily activities, leisure, work/school, relationships, treatment

    Interpretation:

        0-1: No effect

        2-5: Small effect

        6-10: Moderate effect

        11-20: Very large effect

        21-30: Extremely large effect



📁 Repository Structure
psoriasis-cdss/
│
├── Home.py                           # Main entry point
│
├── pages/                            # Module pages
│   ├── 1_Introduction.py            # Module 1: Introduction
│   ├── 2_Diagnostic_Matrix.py       # Module 2: Diagnostic screening
│   ├── 3_Type_Identification.py     # Module 3: Type classification
│   └── 4_Severity_Assessment.py     # Module 4: PASI/BSA/DLQI
│
├── requirements.txt                  # Python dependencies
├── README.md                         # This file
├── LICENSE                           # MIT License
└── .gitignore                        # Git ignore rules


🛠️ Technologies Used

    Streamlit - Web framework

    Pandas - Data manipulation

    NumPy - Numerical computing

    Plotly - Interactive visualizations

    Python 3.9+ - Programming language

🤝 Contributing

Contributions are welcome! Please follow these steps:

    Fork the repository

    Create a feature branch (git checkout -b feature/AmazingFeature)

    Commit your changes (git commit -m 'Add some AmazingFeature')

    Push to the branch (git push origin feature/AmazingFeature)

    Open a Pull Request

Areas for Contribution

    Additional psoriasis types or subtypes

    More clinical images for diagnostic matrix

    Treatment guideline updates

    Localization/internationalization

    Performance improvements

    Additional assessment tools


📚 Citation

If you use this system in your research or clinical practice, please cite:

@software{psoriasis_cdss_2025,
  title = {Psoriasis Clinical Decision Support System},
  author = Aditya Attreya
  year = {2025},
  url = {https://github.com/aditya-attreya/Psoriasis_Diagnostics_Matrix},
  note = {Web-based clinical assessment tool for psoriasis}
}


📞 Contact

Project Maintainer: Aditya Attreya
Email: sharma020101@gmail.com
GitHub: aditya-attreya


🙏 Acknowledgments

    Clinical guidelines from international dermatology associations

    PASI, BSA, and DLQI scoring systems from published literature

    Streamlit community for excellent documentation and support

    Healthcare professionals who provided clinical insights


⚠️ Disclaimer

For Clinical Research and Educational Purposes

This Clinical Decision Support System is designed to assist healthcare professionals in psoriasis assessment and should be used as a supplementary tool. It does not replace professional medical judgment, diagnosis, or treatment decisions. All clinical assessments should be interpreted within the context of individual patient presentations and professional expertise.
🔄 Version History

    v1.0.0 (October 2025) - Initial release

        Four integrated modules

        PASI, BSA, and DLQI assessment tools

        Visual diagnostic matrix

        Treatment recommendations

📈 Future Roadmap

    Multi-language support

    Patient data export (PDF reports)

    Historical tracking of patient scores

    Integration with EHR systems

    Mobile application version

    AI-powered image analysis

    Expanded treatment guidelines

    Telemedicine integration

