import streamlit as st

def show_home():
    # Hero welcome section matching the teal Soulplanet aesthetic
    st.markdown("""
    <div style='background: linear-gradient(135deg, #075E54 0%, #0F766E 50%, #0D9488 100%); padding: 3rem 2rem; border-radius: 20px; color: #FFFFFF; text-align: center; margin-bottom: 2.5rem; box-shadow: 0 10px 30px -5px rgba(13, 148, 136, 0.2);'>
        <div style='background-color: rgba(204, 251, 241, 0.2); color: #CCFBF1; padding: 0.35rem 1rem; border-radius: 9999px; font-size: 11px; font-weight: 700; text-transform: uppercase; letter-spacing: 0.5px; display: inline-block; margin-bottom: 0.75rem;'>Clinical Analytics Suite</div>
        <h1 style='font-family: "Outfit", sans-serif; font-size: 38px; font-weight: 800; margin-bottom: 0.5rem; color: #FFFFFF;'>Welcome to Soulplanet Health Portal</h1>
        <p style='font-size: 16px; font-weight: 300; color: #CCFBF1; margin-bottom: 0;'>Predictive machine learning diagnostics and decision support tools for cardiovascular and diabetic clinical care.</p>
    </div>
    """, unsafe_allow_html=True)

    # Portal metrics dashboard row
    st.markdown("<h4 style='font-family: \"Outfit\", sans-serif; color: #0F172A; margin-bottom: 1.25rem;'>Diagnostics Suite Overview</h4>", unsafe_allow_html=True)
    col_m1, col_m2, col_m3 = st.columns(3)
    
    with col_m1:
        st.markdown("""
        <div style='background-color: #FFFFFF; border: 1px solid #E2E8F0; padding: 1.5rem; border-radius: 14px; box-shadow: 0 4px 6px -1px rgba(0, 0, 0, 0.01);'>
            <div style='font-size: 13px; font-weight: 600; color: #64748B; font-family: "Outfit", sans-serif; text-transform: uppercase;'>Total Screened Patients</div>
            <div style='font-size: 32px; font-weight: 800; color: #0D9488; margin-top: 0.25rem;'>1,482</div>
            <div style='font-size: 11px; color: #10B981; margin-top: 4px;'>📈 +12% increase this month</div>
        </div>
        """, unsafe_allow_html=True)
        
    with col_m2:
        st.markdown("""
        <div style='background-color: #FFFFFF; border: 1px solid #E2E8F0; padding: 1.5rem; border-radius: 14px; box-shadow: 0 4px 6px -1px rgba(0, 0, 0, 0.01);'>
            <div style='font-size: 13px; font-weight: 600; color: #64748B; font-family: "Outfit", sans-serif; text-transform: uppercase;'>High Risk Interventions</div>
            <div style='font-size: 32px; font-weight: 800; color: #EF4444; margin-top: 0.25rem;'>284</div>
            <div style='font-size: 11px; color: #EF4444; margin-top: 4px;'>🚨 Critical clinical review pending</div>
        </div>
        """, unsafe_allow_html=True)
        
    with col_m3:
        st.markdown("""
        <div style='background-color: #FFFFFF; border: 1px solid #E2E8F0; padding: 1.5rem; border-radius: 14px; box-shadow: 0 4px 6px -1px rgba(0, 0, 0, 0.01);'>
            <div style='font-size: 13px; font-weight: 600; color: #64748B; font-family: "Outfit", sans-serif; text-transform: uppercase;'>Readmission Prevention Rate</div>
            <div style='font-size: 32px; font-weight: 800; color: #10B981; margin-top: 0.25rem;'>94.2%</div>
            <div style='font-size: 11px; color: #64748B; margin-top: 4px;'>%🩺 Clinically-validated thresholds</div>
        </div>
        """, unsafe_allow_html=True)

    st.markdown("<hr>", unsafe_allow_html=True)

    # Interactive Patient Lookup Simulator
    st.markdown("<h4 style='font-family: \"Outfit\", sans-serif; color: #0F172A;'>Patient File Simulator & Clinical Registry</h4>", unsafe_allow_html=True)
    st.write("Search the clinical registry database to retrieve a patient's historical records. You can load these profiles directly into the diagnostic analysis tools.")
    
    search_query = st.text_input("Search Clinical Database by Patient ID or Name", placeholder="e.g. PAT-104 or Eleanor Vance")
    
    if search_query:
        # Simple lookup logic mock
        q = search_query.strip().lower()
        if "eleanor" in q or "104" in q:
            st.markdown("""
            <div style='background-color: #FFFFFF; border: 1px solid #0D9488; padding: 1.5rem; border-radius: 12px; margin-bottom: 1.5rem;'>
                <div style='display: flex; justify-content: space-between; align-items: center;'>
                    <span style='font-size: 18px; font-weight: 700; color: #0F172A; font-family: "Outfit", sans-serif;'>Eleanor Vance (Patient ID: PAT-104)</span>
                    <span style='background-color: #ECFDF5; color: #10B981; padding: 0.25rem 0.75rem; border-radius: 9999px; font-size: 11px; font-weight: 600;'>Active Registry File</span>
                </div>
                <hr style='margin: 0.75rem 0;'>
                <div style='display: grid; grid-template-columns: 1fr 1fr; gap: 10px; font-size: 13px; color: #475569;'>
                    <div><strong>Age:</strong> 54 Years</div>
                    <div><strong>Biological Sex:</strong> Female</div>
                    <div><strong>Systolic BP:</strong> 132 mmHg (Pre-hypertensive)</div>
                    <div><strong>Total Cholesterol:</strong> 220 mg/dL (Borderline High)</div>
                    <div><strong>BMI:</strong> 26.2 (Overweight)</div>
                    <div><strong>Fasting Blood Sugar:</strong> 105 mg/dL (Pre-diabetic)</div>
                </div>
            </div>
            """, unsafe_allow_html=True)
            st.info("💡 To analyze Eleanor's profile, switch to the Cardiovascular Center in the sidebar and enter the clinical metrics shown above.")
        elif "vance" in q or "209" in q:
            st.markdown("""
            <div style='background-color: #FFFFFF; border: 1px solid #E2E8F0; padding: 1.5rem; border-radius: 12px; margin-bottom: 1.5rem;'>
                <div style='display: flex; justify-content: space-between; align-items: center;'>
                    <span style='font-size: 18px; font-weight: 700; color: #0F172A; font-family: "Outfit", sans-serif;'>Arthur Vance (Patient ID: PAT-209)</span>
                    <span style='background-color: #FEF2F2; color: #EF4444; padding: 0.25rem 0.75rem; border-radius: 9999px; font-size: 11px; font-weight: 600;'>Flagged High Risk</span>
                </div>
                <hr style='margin: 0.75rem 0;'>
                <div style='display: grid; grid-template-columns: 1fr 1fr; gap: 10px; font-size: 13px; color: #475569;'>
                    <div><strong>Age:</strong> 67 Years</div>
                    <div><strong>Biological Sex:</strong> Male</div>
                    <div><strong>Systolic BP:</strong> 155 mmHg (Stage 2 Hypertension)</div>
                    <div><strong>Total Cholesterol:</strong> 260 mg/dL (High Risk)</div>
                    <div><strong>BMI:</strong> 31.4 (Obese Class I)</div>
                    <div><strong>Fasting Blood Sugar:</strong> 145 mg/dL (Diabetic Range)</div>
                </div>
            </div>
            """, unsafe_allow_html=True)
            st.warning("⚠️ Critical: Patient Arthur Vance exhibits multiple high-risk metabolic biomarkers. Immediate diagnostics recommended.")
        else:
            st.error("🔍 Patient profile not found in active registry. Please enter a valid query like 'Eleanor Vance' or 'PAT-209'.")
    else:
        # Default simulator helper list
        st.markdown("""
        <div style='background-color: #F8FAFC; border: 1px solid #E2E8F0; padding: 1rem; border-radius: 10px; font-size: 13px; color: #64748B;'>
            💡 <strong>Clinician Tip:</strong> Try searching for "<strong>Eleanor Vance</strong>" or "<strong>Arthur Vance</strong>" to test the patient registry lookup integration.
        </div>
        """, unsafe_allow_html=True)

    # Core Features info grid
    st.markdown("<h4 style='font-family: \"Outfit\", sans-serif; color: #0F172A; margin-top: 2rem; margin-bottom: 1rem;'>Diagnostics Capabilities</h4>", unsafe_allow_html=True)
    col_f1, col_f2 = st.columns(2)
    
    with col_f1:
        st.markdown("""
        <div style='background-color: #FFFFFF; border: 1px solid #E2E8F0; padding: 1.5rem; border-radius: 14px;'>
            <div style='font-size: 24px; margin-bottom: 0.5rem;'>❤️</div>
            <div style='font-size: 16px; font-weight: 700; color: #0F172A; font-family: "Outfit", sans-serif; margin-bottom: 0.5rem;'>Cardiovascular Diagnostics Center</div>
            <div style='font-size: 13px; color: #64748B; line-height: 1.5; margin-bottom: 1rem;'>
                Analyzes demographic profiles (Age, Sex), lifestyle indicators (Sleep, Stress, Physical Exercise, Sugar Intake), and clinical biomarkers (BP, Cholesterol, Triglycerides, CRP, Homocysteine) to predict heart disease risk.
            </div>
            <div style='font-size: 12px; color: #0D9488; font-weight: 600;'>Random Forest Model • 79.96% Accuracy</div>
        </div>
        """, unsafe_allow_html=True)
        
    with col_f2:
        st.markdown("""
        <div style='background-color: #FFFFFF; border: 1px solid #E2E8F0; padding: 1.5rem; border-radius: 14px;'>
            <div style='font-size: 24px; margin-bottom: 0.5rem;'>🩸</div>
            <div style='font-size: 16px; font-weight: 700; color: #0F172A; font-family: "Outfit", sans-serif; margin-bottom: 0.5rem;'>Diabetic Readmission Analysis Center</div>
            <div style='font-size: 13px; color: #64748B; line-height: 1.5; margin-bottom: 1rem;'>
                Evaluates diabetic patients during inpatient stay, analyzing laboratory results (lab procedures, diagnostic classifications), medication alterations, and previous hospital stays to forecast 30-day readmission risk.
            </div>
            <div style='font-size: 12px; color: #0D9488; font-weight: 600;'>XGBoost Model • 53.75% Accuracy</div>
        </div>
        """, unsafe_allow_html=True)
