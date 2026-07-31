import os
import pickle
import numpy as np
import pandas as pd
import streamlit as st
from home import show_home

#.venv\Scripts\Activate.ps1
# streamlit run app.py


# Set page configuration
st.set_page_config(
    page_title="Soulplanet Health & Wellness Portal",
    page_icon="🩺",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Custom CSS for styling (resembling the Soulplanet design: teals, navies, elegant cards, and modern typography)
st.markdown("""
<style>
    @import url('https://fonts.googleapis.com/css2?family=Outfit:wght@300;400;500;600;700;800&family=Inter:wght@300;400;500;600;700&display=swap');

    /* Hide default Streamlit elements for pure branding */
    #MainMenu {visibility: hidden;}
    footer {visibility: hidden;}
    header {visibility: hidden;}
    [data-testid="stHeader"] {background-color: transparent !important;}

    /* Global styling */
    html, body, [data-testid="stAppViewContainer"] {
        font-family: 'Inter', sans-serif;
        background-color: #F8FAFC;
        color: #1E293B;
    }

    h1, h2, h3, h4, h5, h6 {
        font-family: 'Outfit', sans-serif;
        font-weight: 700;
        color: #0F172A;
    }

    /* Target all Streamlit widget labels to color them black and style them cleanly */
    div[data-testid="stWidgetLabel"] p, label, .stSlider label, .stSelectbox label, .stNumberInput label {
        color: #0F172A !important;
        font-weight: 600 !important;
        font-family: 'Outfit', sans-serif !important;
        font-size: 14px !important;
        margin-bottom: 0.5rem !important;
    }

    /* Style selectboxes/dropdowns background and text color to look premium */
    div[data-baseweb="select"] > div {
        background-color: #FFFFFF !important;
        border: 1px solid #E2E8F0 !important;
        color: #0F172A !important;
        border-radius: 10px !important;
        padding: 2px 4px !important;
        font-size: 14px !important;
        box-shadow: 0 1px 2px 0 rgba(0, 0, 0, 0.05) !important;
    }
    div[data-baseweb="select"] > div:hover {
        border-color: #0D9488 !important;
    }

    /* Selectbox icon */
    div[data-baseweb="select"] svg {
        fill: #64748B !important;
    }

    /* Number inputs and general inputs background and text */
    div[data-baseweb="input"] {
        background-color: #FFFFFF !important;
        border: 1px solid #E2E8F0 !important;
        border-radius: 10px !important;
        box-shadow: 0 1px 2px 0 rgba(0, 0, 0, 0.05) !important;
    }
    div[data-baseweb="input"]:hover {
        border-color: #0D9488 !important;
    }
    div[data-baseweb="input"]:focus-within {
        border-color: #0D9488 !important;
        box-shadow: 0 0 0 3px rgba(13, 148, 136, 0.15) !important;
    }
    div[data-baseweb="input"] input {
        color: #0F172A !important;
        background-color: #FFFFFF !important;
        border: none !important;
        font-size: 14px !important;
    }

    /* Number input buttons */
    div[data-testid="stNumberInput"] button {
        background-color: #F1F5F9 !important;
        border: none !important;
        color: #475569 !important;
        border-radius: 6px !important;
        margin: 2px !important;
    }
    div[data-testid="stNumberInput"] button:hover {
        background-color: #E2E8F0 !important;
        color: #0F172A !important;
    }

    /* Form styling as a premium card */
    div[data-testid="stForm"] {
        background-color: #FFFFFF !important;
        border: 1px solid #E2E8F0 !important;
        border-radius: 16px !important;
        padding: 2.5rem !important;
        box-shadow: 0 4px 6px -1px rgba(0, 0, 0, 0.02), 0 2px 4px -1px rgba(0, 0, 0, 0.02) !important;
        margin-bottom: 2rem !important;
    }

    /* Custom form spacing */
    div[data-testid="stForm"] div.element-container {
        margin-bottom: 1.5rem !important;
    }

    /* Slider styling adjustments */
    div[data-testid="stSlider"] div[role="slider"] {
        background-color: #0D9488 !important;
        border: 2px solid #FFFFFF !important;
    }

    /* Sidebar styling overrides */
    section[data-testid="stSidebar"] {
        background-color: #FFFFFF !important;
        border-right: 1px solid #E2E8F0 !important;
    }

    /* Logo & Header */
    .header-bar {
        display: flex;
        justify-content: space-between;
        align-items: center;
        padding: 1rem 1.5rem;
        background-color: #FFFFFF;
        border-bottom: 1px solid #E2E8F0;
        margin-bottom: 1.5rem;
        border-radius: 12px;
        box-shadow: 0 1px 3px 0 rgba(0, 0, 0, 0.05);
    }
    .logo-container {
        display: flex;
        align-items: center;
    }
    .logo-text {
        font-size: 26px;
        font-weight: 800;
        color: #0D9488;
        letter-spacing: -0.5px;
        font-family: 'Outfit', sans-serif;
    }
    .logo-tagline {
        font-size: 11px;
        color: #64748B;
        margin-left: 8px;
        font-weight: 400;
    }
    .nav-links {
        display: flex;
        gap: 1.5rem;
        font-family: 'Outfit', sans-serif;
        font-weight: 500;
        color: #475569;
        font-size: 14px;
    }

    /* Hero Banner */
    .hero-container {
        background: linear-gradient(135deg, #075E54 0%, #0F766E 50%, #0D9488 100%);
        color: #FFFFFF;
        padding: 3.5rem 2rem;
        border-radius: 20px;
        margin-bottom: 2.5rem;
        text-align: center;
        box-shadow: 0 10px 30px -5px rgba(13, 148, 136, 0.2);
        position: relative;
        overflow: hidden;
    }
    .hero-container::before {
        content: "";
        position: absolute;
        top: -50%;
        left: -50%;
        width: 200%;
        height: 200%;
        background: radial-gradient(circle, rgba(255,255,255,0.03) 0%, transparent 60%);
        pointer-events: none;
    }
    .hero-badge {
        background-color: rgba(204, 251, 241, 0.15);
        color: #CCFBF1;
        padding: 0.35rem 1rem;
        border-radius: 9999px;
        font-size: 12px;
        font-weight: 600;
        letter-spacing: 0.5px;
        text-transform: uppercase;
        display: inline-block;
        margin-bottom: 1rem;
        border: 1px solid rgba(204, 251, 241, 0.25);
    }
    .hero-title {
        font-size: 36px;
        font-weight: 800;
        margin-bottom: 0.5rem;
        color: #FFFFFF !important;
        letter-spacing: -0.5px;
    }
    .hero-subtitle {
        font-size: 16px;
        font-weight: 300;
        color: #CCFBF1;
        margin-bottom: 0;
    }

    /* Tabs pill custom styling */
    .stTabs [data-baseweb="tab-list"] {
        gap: 12px !important;
        background-color: #F1F5F9 !important;
        padding: 8px !important;
        border-radius: 12px !important;
        border: 1px solid #E2E8F0 !important;
    }
    .stTabs [data-baseweb="tab"] {
        height: 48px !important;
        background-color: transparent !important;
        border-radius: 10px !important;
        color: #475569 !important;
        font-family: 'Outfit', sans-serif !important;
        font-weight: 600 !important;
        font-size: 15px !important;
        border: none !important;
        padding: 0 24px !important;
        transition: all 0.3s cubic-bezier(0.4, 0, 0.2, 1) !important;
    }
    .stTabs [aria-selected="true"] {
        background-color: #0D9488 !important;
        color: #FFFFFF !important;
        box-shadow: 0 4px 12px rgba(13, 148, 136, 0.25) !important;
    }
    .stTabs [data-baseweb="tab"]:hover:not([aria-selected="true"]) {
        background-color: #E2E8F0 !important;
        color: #0F172A !important;
    }

    /* Styled buttons */
    .stButton > button {
        background: linear-gradient(135deg, #0D9488 0%, #0F766E 100%) !important;
        color: #FFFFFF !important;
        font-family: 'Outfit', sans-serif !important;
        font-weight: 700 !important;
        font-size: 16px !important;
        padding: 0.9rem 2rem !important;
        border-radius: 12px !important;
        border: none !important;
        transition: all 0.3s cubic-bezier(0.4, 0, 0.2, 1) !important;
        box-shadow: 0 4px 6px -1px rgba(13, 148, 136, 0.1), 0 2px 4px -1px rgba(13, 148, 136, 0.06) !important;
        width: 100%;
        margin-top: 1.5rem !important;
    }
    .stButton > button:hover {
        background: linear-gradient(135deg, #0F766E 0%, #0D9488 100%) !important;
        transform: translateY(-2px) !important;
        box-shadow: 0 10px 15px -3px rgba(13, 148, 136, 0.3) !important;
    }

    /* Prediction Card Display */
    .result-card {
        background-color: #FFFFFF;
        border-radius: 16px;
        padding: 2.25rem;
        border-left: 6px solid #0D9488;
        box-shadow: 0 10px 15px -3px rgba(0, 0, 0, 0.02), 0 4px 6px -4px rgba(0, 0, 0, 0.02);
        margin-top: 1.5rem;
        border: 1px solid #E2E8F0;
        border-left-width: 6px;
    }
    .result-card.danger {
        border-left-color: #EF4444;
        background-color: #FEF2F2;
        border-top-color: #FEE2E2;
        border-right-color: #FEE2E2;
        border-bottom-color: #FEE2E2;
    }
    .result-card.success {
        border-left-color: #10B981;
        background-color: #ECFDF5;
        border-top-color: #D1FAE5;
        border-right-color: #D1FAE5;
        border-bottom-color: #D1FAE5;
    }
    .result-card.warning {
        border-left-color: #F59E0B;
        background-color: #FFFBEB;
        border-top-color: #FEF3C7;
        border-right-color: #FEF3C7;
        border-bottom-color: #FEF3C7;
    }
    .result-header {
        font-family: 'Outfit', sans-serif;
        font-size: 22px;
        font-weight: 800;
        margin-bottom: 0.5rem;
    }
    .result-body {
        font-size: 15px;
        line-height: 1.6;
        color: #334155;
    }

    /* Diagnostic progress metrics */
    .metric-progress-container {
        margin-bottom: 1.25rem;
    }
    .metric-progress-header {
        display: flex;
        justify-content: space-between;
        font-size: 13px;
        font-weight: 600;
        color: #475569;
        margin-bottom: 6px;
    }
    .metric-progress-track {
        background-color: #E2E8F0;
        border-radius: 9999px;
        height: 10px;
        width: 100%;
        overflow: hidden;
    }
    .metric-progress-bar {
        height: 100%;
        border-radius: 9999px;
    }
    .metric-progress-bar.success {
        background-color: #10B981;
    }
    .metric-progress-bar.warning {
        background-color: #F59E0B;
    }
    .metric-progress-bar.danger {
        background-color: #EF4444;
    }

    /* Info card grid styling */
    .info-card {
        background-color: #FFFFFF;
        border-radius: 12px;
        padding: 1.5rem;
        text-align: center;
        border: 1px solid #E2E8F0;
        box-shadow: 0 1px 3px 0 rgba(0, 0, 0, 0.02);
        transition: all 0.3s ease;
    }
    .info-card:hover {
        transform: translateY(-4px);
        box-shadow: 0 10px 15px -3px rgba(0, 0, 0, 0.05);
        border-color: #CBD5E1;
    }
    .info-icon {
        font-size: 32px;
        margin-bottom: 0.75rem;
    }
    .info-title {
        font-size: 16px;
        font-weight: 700;
        color: #0F172A;
        margin-bottom: 0.5rem;
    }
    .info-desc {
        font-size: 13px;
        color: #64748B;
        line-height: 1.5;
    }

    /* Clean divider */
    hr {
        margin: 2.5rem 0;
        border: 0;
        border-top: 1px solid #E2E8F0;
    }
</style>
""", unsafe_allow_html=True)

# Load cached models and encoders
@st.cache_resource
def load_models_and_encoders():
    # Relative path from project directory
    models_dir = os.path.join(os.path.dirname(__file__), "models")
    
    # Heart disease model files
    with open(os.path.join(models_dir, "heart_disease_model.pkl"), "rb") as f:
        heart_model = pickle.load(f)
    with open(os.path.join(models_dir, "heart_disease_encoders.pkl"), "rb") as f:
        heart_encoders = pickle.load(f)
    with open(os.path.join(models_dir, "heart_disease_columns.pkl"), "rb") as f:
        heart_cols = pickle.load(f)
        
    # Diabetes model files
    with open(os.path.join(models_dir, "diabetes_model.pkl"), "rb") as f:
        diabetes_model = pickle.load(f)
    with open(os.path.join(models_dir, "diabetes_encoders.pkl"), "rb") as f:
        diabetes_encoders = pickle.load(f)
    with open(os.path.join(models_dir, "diabetes_columns.pkl"), "rb") as f:
        diabetes_cols = pickle.load(f)
        
    return (heart_model, heart_encoders, heart_cols, 
            diabetes_model, diabetes_encoders, diabetes_cols)

# Load model data
try:
    (heart_model, heart_encoders, heart_cols, 
     diabetes_model, diabetes_encoders, diabetes_cols) = load_models_and_encoders()
    models_loaded = True
except Exception as e:
    st.error(f"Error loading machine learning models: {e}")
    models_loaded = False

# Safe label encoding function to prevent ValueError with unseen labels
def safe_encode(val, col_name, encoders):
    if col_name not in encoders:
        # If no label encoder exists for this column, return raw val (assume numerical)
        return val
        
    le = encoders[col_name]
    classes = le.classes_
    
    # Check if value matches directly in encoder classes
    if val in classes:
        return le.transform([val])[0]
        
    # Check string representation match
    val_str = str(val)
    if val_str in classes:
        return le.transform([val_str])[0]
        
    # Try numeric proximity if class labels are numeric
    try:
        numeric_classes = np.array([float(x) for x in classes])
        val_num = float(val)
        closest_idx = np.argmin(np.abs(numeric_classes - val_num))
        return closest_idx
    except ValueError:
        pass
        
    # Fallback to first class index or 0
    return 0

# --- SIDEBAR BRANDING & NAVIGATION ---
with st.sidebar:
    st.markdown("""
    <div style='text-align: center; padding: 1rem 0;'>
        <div style='font-family: "Outfit", sans-serif; font-size: 28px; font-weight: 800; color: #0D9488;'>Soulplanet</div>
        <div style='font-size: 11px; color: #64748B;'>Clinical Diagnostics Portal</div>
    </div>
    <hr style='margin: 0.5rem 0 1.5rem 0;'>
    """, unsafe_allow_html=True)
    
    st.markdown("<h5 style='font-family: \"Outfit\", sans-serif; color: #0F172A; margin-bottom: 0.5rem;'>Diagnostics Suite Portal</h5>", unsafe_allow_html=True)
    page = st.radio(
        "Select Portal View",
        options=["🏠 Portal Home Dashboard", "❤️ Cardiovascular Diagnostics", "🩸 Diabetic Readmission Analysis"],
        label_visibility="collapsed"
    )
    st.markdown("<hr style='margin: 1.5rem 0;'>", unsafe_allow_html=True)
    
    st.markdown("<h5 style='font-family: \"Outfit\", sans-serif; color: #0F172A; margin-bottom: 1rem;'>Suite Statistics</h5>", unsafe_allow_html=True)
    
    # Model 1 Metrics
    st.markdown("""
    <div style='background-color: #F8FAFC; padding: 1rem; border-radius: 10px; border: 1px solid #E2E8F0; margin-bottom: 1rem;'>
        <div style='font-weight: 700; font-size: 12px; color: #0D9488; font-family: "Outfit", sans-serif; margin-bottom: 2px;'>CARDIOVASCULAR MODEL</div>
        <div style='font-size: 11px; color: #64748B; margin-bottom: 10px;'>Random Forest Classifier</div>
        <div style='display: flex; justify-content: space-between; font-size: 12px; margin-bottom: 4px; color: #334155;'>
            <span>Model Accuracy:</span>
            <strong>79.96%</strong>
        </div>
        <div style='display: flex; justify-content: space-between; font-size: 12px; color: #334155;'>
            <span>Trained Features:</span>
            <strong>20 Columns</strong>
        </div>
    </div>
    """, unsafe_allow_html=True)
    
    # Model 2 Metrics
    st.markdown("""
    <div style='background-color: #F8FAFC; padding: 1rem; border-radius: 10px; border: 1px solid #E2E8F0; margin-bottom: 1.5rem;'>
        <div style='font-weight: 700; font-size: 12px; color: #0D9488; font-family: "Outfit", sans-serif; margin-bottom: 2px;'>DIABETES READMISSION</div>
        <div style='font-size: 11px; color: #64748B; margin-bottom: 10px;'>XGBoost Classifier</div>
        <div style='display: flex; justify-content: space-between; font-size: 12px; margin-bottom: 4px; color: #334155;'>
            <span>Model Accuracy:</span>
            <strong>53.75%</strong>
        </div>
        <div style='display: flex; justify-content: space-between; font-size: 12px; color: #334155;'>
            <span>Trained Features:</span>
            <strong>32 Columns</strong>
        </div>
    </div>
    """, unsafe_allow_html=True)
    
    st.markdown("""
    <hr style='margin: 1.5rem 0;'>
    <div style='font-size: 11px; color: #94A3B8; text-align: center;'>
        Active Session: Clinician Mode<br>
        Version 1.2 (Validated)
    </div>
    """, unsafe_allow_html=True)

# --- HEADER BAR ---
st.markdown("""
<div class="header-bar">
    <div class="logo-container">
        <span class="logo-text">Soulplanet</span>
        <span class="logo-tagline">Health & Wellness Diagnostics</span>
    </div>
    <div class="nav-links">
        <span>Clinical Suite</span>
        <span>Ailment Centers</span>
        <span>Diagnostics Info</span>
        <span>Wellness Hub</span>
    </div>
</div>
""", unsafe_allow_html=True)

# --- HERO SECTION ---
st.markdown("""
<div class="hero-container">
    <div class="hero-badge">Clinical Decision Support System</div>
    <h1 class="hero-title">Cardiovascular & Metabolic Risk Assessment Suite</h1>
    <p class="hero-subtitle">Machine learning algorithms for early risk classification and hospital readmission prevention.</p>
</div>
""", unsafe_allow_html=True)

if models_loaded:
    if page == "🏠 Portal Home Dashboard":
        show_home()
    elif page == "❤️ Cardiovascular Diagnostics":
        st.markdown("<h3 style='margin-bottom:1.5rem; color:#0F172A;'>Cardiovascular Risk Profile Analysis</h3>", unsafe_allow_html=True)
        st.write("Complete the patient details below to estimate the likelihood of heart disease status. The prediction is powered by a Random Forest Classifier trained on patient metrics.")
        
        with st.form("heart_form"):
            col1, col2 = st.columns(2)
            
            # Column 1: Core Profile
            with col1:
                st.markdown("<h5 style='color:#0D9488;'>Core Patient Profile</h5>", unsafe_allow_html=True)
                age = st.slider("Patient Age (Years)", min_value=1, max_value=120, value=45, step=1)
                
                # Fetch gender classes dynamically
                gender_options = list(heart_encoders['Gender'].classes_)
                gender = st.selectbox("Biological Sex / Gender", options=gender_options)
                
                bmi = st.number_input("Body Mass Index (BMI)", min_value=10.0, max_value=65.0, value=24.5, step=0.1)

            # Column 2: Primary Clinical Metrics
            with col2:
                st.markdown("<h5 style='color:#0D9488;'>Primary Clinical Metrics</h5>", unsafe_allow_html=True)
                bp = st.number_input("Systolic Blood Pressure (mmHg)", min_value=70.0, max_value=250.0, value=122.0, step=1.0)
                chol = st.number_input("Total Serum Cholesterol (mg/dL)", min_value=80.0, max_value=500.0, value=195.0, step=1.0)
                
                diabetes_options = list(heart_encoders['Diabetes'].classes_)
                diabetes = st.selectbox("Patient Diagnosed with Diabetes", options=diabetes_options)

            # Secondary lifestyle and biomarkers hidden under an expander to reduce UI complexity
            with st.expander("Lifestyle Factors & Secondary Lab Biomarkers (Optional)"):
                exp_col1, exp_col2 = st.columns(2)
                
                with exp_col1:
                    st.markdown("<h6 style='color:#0D9488;'>Lifestyle Details</h6>", unsafe_allow_html=True)
                    sleep_hours = st.slider("Average Sleep (Hours/Night)", min_value=2.0, max_value=14.0, value=7.0, step=0.5)
                    
                    alcohol_options = list(heart_encoders['Alcohol Consumption'].classes_)
                    alcohol_display = [x if x != '0.0' else 'None / Minimal' for x in alcohol_options]
                    alcohol_sel = st.selectbox("Alcohol Consumption Level", options=alcohol_display)
                    alcohol = alcohol_options[alcohol_display.index(alcohol_sel)]
                    
                    exercise_options = list(heart_encoders['Exercise Habits'].classes_)
                    exercise = st.selectbox("Physical Exercise Level", options=exercise_options)
                    
                    smoking_options = list(heart_encoders['Smoking'].classes_)
                    smoking = st.selectbox("Tobacco Smoking Status", options=smoking_options)
                    
                    stress_options = list(heart_encoders['Stress Level'].classes_)
                    stress = st.selectbox("Chronic Stress Level", options=stress_options)
                    
                    sugar_options = list(heart_encoders['Sugar Consumption'].classes_)
                    sugar = st.selectbox("Sugar Intake Level", options=sugar_options)
                    
                with exp_col2:
                    st.markdown("<h6 style='color:#0D9488;'>Secondary Lab Assays</h6>", unsafe_allow_html=True)
                    trig = st.number_input("Serum Triglyceride Level (mg/dL)", min_value=40.0, max_value=600.0, value=148.0, step=1.0)
                    fbs = st.number_input("Fasting Blood Sugar (mg/dL)", min_value=40.0, max_value=300.0, value=92.0, step=1.0)
                    crp = st.number_input("C-Reactive Protein (CRP) Level (mg/L)", min_value=0.0, max_value=30.0, value=1.2, step=0.1)
                    homo = st.number_input("Homocysteine Level (µmol/L)", min_value=2.0, max_value=60.0, value=9.8, step=0.1)
                    
                    family_options = list(heart_encoders['Family Heart Disease'].classes_)
                    family = st.selectbox("Family History of Premature Heart Disease", options=family_options)
                    
                    hbp_options = list(heart_encoders['High Blood Pressure'].classes_)
                    hbp = st.selectbox("Patient Diagnosed with Hypertension", options=hbp_options)
                    
                    hdl_options = list(heart_encoders['Low HDL Cholesterol'].classes_)
                    hdl = st.selectbox("Present: Low HDL Cholesterol Status", options=hdl_options)
                    
                    ldl_options = list(heart_encoders['High LDL Cholesterol'].classes_)
                    ldl = st.selectbox("Present: High LDL Cholesterol Status", options=ldl_options)
                    
            submit_heart = st.form_submit_button("Analyze Cardiovascular Risk")
            
        if submit_heart:
            # Map input to features
            input_dict = {
                'Age': age,
                'Gender': gender,
                'Blood Pressure': bp,
                'Cholesterol Level': chol,
                'Exercise Habits': exercise,
                'Smoking': smoking,
                'Family Heart Disease': family,
                'Diabetes': diabetes,
                'BMI': bmi,
                'High Blood Pressure': hbp,
                'Low HDL Cholesterol': hdl,
                'High LDL Cholesterol': ldl,
                'Alcohol Consumption': alcohol,
                'Stress Level': stress,
                'Sleep Hours': sleep_hours,
                'Sugar Consumption': sugar,
                'Triglyceride Level': trig,
                'Fasting Blood Sugar': fbs,
                'CRP Level': crp,
                'Homocysteine Level': homo
            }
            
            # Format and Encode in correct columns order
            encoded_vals = []
            for col in heart_cols:
                raw_val = input_dict[col]
                encoded_val = safe_encode(raw_val, col, heart_encoders)
                encoded_vals.append(encoded_val)
                
            input_features = np.array([encoded_vals])
            
            # Make prediction
            prob = heart_model.predict_proba(input_features)[0]
            pred = heart_model.predict(input_features)[0]
            
            # Get class labels from target encoder
            target_classes = list(heart_encoders['Heart Disease Status'].classes_)
            pred_label = target_classes[pred]
            
            # Determine color & text depending on prediction
            # Find index of Yes (case-insensitive)
            yes_index = 0
            for idx, cls in enumerate(target_classes):
                if str(cls).strip().lower() == 'yes':
                    yes_index = idx
                    break
            
            prob_pct = prob[yes_index] * 100
            
            if pred_label.lower() == 'yes':
                risk_style = "danger"
                risk_status = "🚨 High Cardiovascular Risk Detected"
                risk_color = "#EF4444"
                progress_class = "danger"
                clinical_desc = "The random forest classifier has identified high-risk indicators matching heart disease status. Immediate clinical review and biomarker profiling are strongly recommended."
            else:
                risk_style = "success"
                risk_status = "✅ Low Cardiovascular Risk Profile"
                risk_color = "#10B981"
                progress_class = "success"
                clinical_desc = "The patient profile corresponds to normal physiological metrics and low cardiovascular risk indicators. Encourage continued health maintenance."
                
            st.markdown(f"""
<div class="result-card {risk_style}">
<div class="result-header" style="color: {risk_color};">{risk_status}</div>
<div class="result-body" style="margin-top: 1rem;">
<div class="metric-progress-container">
<div class="metric-progress-header">
<span>Cardiovascular Risk Factor Probability</span>
<strong>{prob_pct:.2f}%</strong>
</div>
<div class="metric-progress-track">
<div class="metric-progress-bar {progress_class}" style="width: {prob_pct}%;"></div>
</div>
</div>
<hr style="margin: 1rem 0; border-top: 1px solid #E2E8F0;">
<strong>Model Clinical Insight:</strong> {clinical_desc}
</div>
</div>
""", unsafe_allow_html=True)
            
            # Recommendations grid
            st.markdown("<h4 style='margin-top:2rem; margin-bottom:1rem;'>Personalized Clinical Recommendations</h4>", unsafe_allow_html=True)
            recs = []
            
            # Check lifestyle conditions
            if smoking.lower() == 'yes':
                recs.append("🚬 <strong>Smoking Cessation</strong>: Patient reports active smoking status. Highly recommend enrollment in tobacco cessation counseling and prescription therapy if indicated.")
            if exercise.lower() == 'low':
                recs.append("🏃 <strong>Physical Activity</strong>: Low physical activity levels recorded. Recommend scaling to at least 150 minutes of moderate aerobic exercise per week.")
            if bmi > 27.0:
                recs.append("⚖️ <strong>Weight Management</strong>: Elevated BMI ({:.1f}). Advise calorie restriction, caloric tracking, and potential dietary consult.".format(bmi))
            if sugar.lower() == 'high':
                recs.append("🍬 <strong>Sugar Intake Reduction</strong>: High sugar intake noted. Advise patient to replace processed sweets with low-glycemic dietary choices.")
            if sleep_hours < 6.0:
                recs.append("💤 <strong>Sleep Hygiene</strong>: Sleep hours ({:.1f} hrs) are below recommended clinical guidelines. Advise regular sleep routines and caffeine restriction.".format(sleep_hours))
            if stress.lower() == 'high':
                recs.append("🧠 <strong>Stress Mitigation</strong>: High stress levels recorded. Recommend mindfulness techniques, yoga, or professional wellness consultation.")
            
            # Check clinical biomarkers
            if bp >= 130.0 or hbp.lower() == 'yes':
                recs.append("🩺 <strong>Hypertension Control</strong>: Systolic blood pressure is elevated. Advise a sodium-restricted DASH diet and regular home monitoring.")
            if chol >= 240.0 or ldl.lower() == 'yes':
                recs.append("🥑 <strong>Lipid Panel Optimization</strong>: Hypercholesterolemia. Advise reducing saturated fats, increasing soluble fiber, and check statin eligibility if risk scores are high.")
            if crp > 2.0:
                recs.append("🧪 <strong>Inflammatory Markers</strong>: C-Reactive Protein ({:.1f} mg/L) indicates active systemic inflammation. Inspect dental health, joint pain, or chronic autoimmune symptoms.".format(crp))
            if homo > 12.0:
                recs.append("🧬 <strong>Homocysteine Regulation</strong>: Elevated homocysteine ({:.1f} µmol/L). Recommend dietary supplementation with Folic Acid (Vitamin B9), Vitamin B6, and Vitamin B12.".format(homo))
                
            if not recs:
                st.info("✅ Patient profile is within normal range for all clinical and lifestyle parameters. Maintain current wellness routine.")
            else:
                for r in recs:
                    st.markdown(f"<div style='background-color:#FFFFFF; padding:0.75rem 1rem; border-radius:8px; border:1px solid #E2E8F0; margin-bottom:0.5rem;'>{r}</div>", unsafe_allow_html=True)

    elif page == "🩸 Diabetic Readmission Analysis":
        st.markdown("<h3 style='margin-bottom:1.5rem; color:#0F172A;'>Diabetic Hospital Readmission Analysis</h3>", unsafe_allow_html=True)
        st.write("Predict the likelihood of a diabetic patient being readmitted to the hospital based on their clinical record, demographic profile, and medication changes. The model uses an XGBoost Classifier.")
        
        with st.form("diabetes_form"):
            col1, col2 = st.columns(2)
            
            # Column 1: Core Profile
            with col1:
                st.markdown("<h5 style='color:#0D9488;'>Core Patient Profile</h5>", unsafe_allow_html=True)
                
                gender_options = list(diabetes_encoders['gender'].classes_)
                gender = st.selectbox("Biological Sex", options=gender_options)
                
                age_options = list(diabetes_encoders['age'].classes_)
                age = st.selectbox("Age Range Bracket", options=age_options)
                
                time_in_hospital = st.slider("Time Spent in Hospital (Days)", min_value=1, max_value=14, value=3)

            # Column 2: Core Clinical Metrics
            with col2:
                st.markdown("<h5 style='color:#0D9488;'>Primary Clinical Metrics</h5>", unsafe_allow_html=True)
                
                diag1_options = list(diabetes_encoders['diag_1'].classes_)
                diag1 = st.selectbox("Primary Diagnosis ICD-9 Code", options=diag1_options, index=diag1_options.index("250") if "250" in diag1_options else 0)
                
                num_lab_procedures = st.number_input("Number of Lab Procedures", min_value=1, max_value=120, value=40, step=1)
                
                diabetes_med_options = list(diabetes_encoders['diabetesMed'].classes_)
                diabetes_med = st.selectbox("Any Diabetes Medication Prescribed?", options=diabetes_med_options, index=diabetes_med_options.index("Yes"))

            # Advanced clinical parameters expander
            with st.expander("Advanced Clinical Parameters & Dosing Profiles (Optional)"):
                exp_col1, exp_col2 = st.columns(2)
                
                with exp_col1:
                    st.markdown("<h6 style='color:#0D9488;'>Admission & History Details</h6>", unsafe_allow_html=True)
                    race_options = list(diabetes_encoders['race'].classes_)
                    race = st.selectbox("Race / Ethnicity Group", options=race_options)
                    
                    admission_type = st.slider("Admission Type ID (1: Emergency, 2: Urgent, 3: Elective)", min_value=1, max_value=8, value=1)
                    admission_src = st.slider("Admission Source ID (1: Physician, 7: Emergency Room)", min_value=1, max_value=25, value=7)
                    discharge_disp = st.slider("Discharge Disposition ID (1: Discharged to Home, 3: SNF)", min_value=1, max_value=28, value=1)
                    
                    st.markdown("<h6 style='color:#0D9488; margin-top:1rem;'>Prior Year Hospital Utilization</h6>", unsafe_allow_html=True)
                    num_outpatient = st.number_input("Number of Outpatient Visits (Prior Year)", min_value=0, max_value=40, value=0, step=1)
                    num_emergency = st.number_input("Number of Emergency Room Visits (Prior Year)", min_value=0, max_value=40, value=0, step=1)
                    num_inpatient = st.number_input("Number of Inpatient Admissions (Prior Year)", min_value=0, max_value=30, value=0, step=1)
                    
                with exp_col2:
                    st.markdown("<h6 style='color:#0D9488;'>Secondary Diagnoses & Procedures</h6>", unsafe_allow_html=True)
                    num_procedures = st.slider("Number of Procedures (During Stay)", min_value=0, max_value=6, value=1)
                    num_medications = st.number_input("Number of Generic Medications Prescribed", min_value=1, max_value=100, value=15, step=1)
                    num_diagnoses = st.number_input("Number of Diagnoses Recorded", min_value=1, max_value=20, value=6, step=1)
                    
                    diag2_options = list(diabetes_encoders['diag_2'].classes_)
                    diag2 = st.selectbox("Secondary Diagnosis ICD-9 Code", options=diag2_options, index=diag2_options.index("250") if "250" in diag2_options else 0)
                    
                    diag3_options = list(diabetes_encoders['diag_3'].classes_)
                    diag3 = st.selectbox("Additional Diagnosis ICD-9 Code", options=diag3_options, index=diag3_options.index("250") if "250" in diag3_options else 0)
                    
                    st.markdown("<h6 style='color:#0D9488; margin-top:1rem;'>Medication Titrations</h6>", unsafe_allow_html=True)
                    metformin_options = list(diabetes_encoders['metformin'].classes_)
                    metformin = st.selectbox("Metformin Dosing", options=metformin_options, index=metformin_options.index("No"))
                    
                    repaglinide_options = list(diabetes_encoders['repaglinide'].classes_)
                    repaglinide = st.selectbox("Repaglinide Dosing", options=repaglinide_options, index=repaglinide_options.index("No"))
                    
                    nateglinide_options = list(diabetes_encoders['nateglinide'].classes_)
                    nateglinide = st.selectbox("Nateglinide Dosing", options=nateglinide_options, index=nateglinide_options.index("No"))
                    
                    glimepiride_options = list(diabetes_encoders['glimepiride'].classes_)
                    glimepiride = st.selectbox("Glimepiride Dosing", options=glimepiride_options, index=glimepiride_options.index("No"))
                    
                    glipizide_options = list(diabetes_encoders['glipizide'].classes_)
                    glipizide = st.selectbox("Glipizide Dosing", options=glipizide_options, index=glipizide_options.index("No"))
                    
                    glyburide_options = list(diabetes_encoders['glyburide'].classes_)
                    glyburide = st.selectbox("Glyburide Dosing", options=glyburide_options, index=glyburide_options.index("No"))
                    
                    pioglitazone_options = list(diabetes_encoders['pioglitazone'].classes_)
                    pioglitazone = st.selectbox("Pioglitazone Dosing", options=pioglitazone_options, index=pioglitazone_options.index("No"))
                    
                    rosiglitazone_options = list(diabetes_encoders['rosiglitazone'].classes_)
                    rosiglitazone = st.selectbox("Rosiglitazone Dosing", options=rosiglitazone_options, index=rosiglitazone_options.index("No"))
                    
                    acarbose_options = list(diabetes_encoders['acarbose'].classes_)
                    acarbose = st.selectbox("Acarbose Dosing", options=acarbose_options, index=acarbose_options.index("No"))
                    
            submit_diabetes = st.form_submit_button("Analyze Readmission Risk")
            
        if submit_diabetes:
            # Map input to features.
            # Notice we auto-generate mock ids for 'encounter_id' and 'patient_nbr' since they are required features by the model
            input_dict = {
                'encounter_id': 1234567,
                'patient_nbr': 9876543,
                'race': race,
                'gender': gender,
                'age': age,
                'admission_type_id': admission_type,
                'discharge_disposition_id': discharge_disp,
                'admission_source_id': admission_src,
                'time_in_hospital': time_in_hospital,
                'num_lab_procedures': num_lab_procedures,
                'num_procedures': num_procedures,
                'num_medications': num_medications,
                'number_outpatient': num_outpatient,
                'number_emergency': num_emergency,
                'number_inpatient': num_inpatient,
                'diag_1': diag1,
                'diag_2': diag2,
                'diag_3': diag3,
                'number_diagnoses': num_diagnoses,
                'metformin': metformin,
                'repaglinide': repaglinide,
                'nateglinide': nateglinide,
                'glimepiride': glimepiride,
                'glipizide': glipizide,
                'glyburide': glyburide,
                'pioglitazone': pioglitazone,
                'rosiglitazone': rosiglitazone,
                'acarbose': acarbose,
                'diabetesMed': diabetes_med
            }
            
            # Format and Encode in correct columns order
            encoded_vals = []
            for col in diabetes_cols:
                raw_val = input_dict[col]
                encoded_val = safe_encode(raw_val, col, diabetes_encoders)
                encoded_vals.append(encoded_val)
                
            input_features = np.array([encoded_vals])
            
            # Make prediction
            prob = diabetes_model.predict_proba(input_features)[0]
            pred = diabetes_model.predict(input_features)[0]
            
            # Target labels: '<30', '>30', 'NO'
            target_classes = list(diabetes_encoders['readmitted'].classes_)
            pred_label = target_classes[pred]
            
            # Map style and display names based on readmission status
            prob_less_30 = prob[target_classes.index('<30')] * 100
            prob_more_30 = prob[target_classes.index('>30')] * 100
            prob_no = prob[target_classes.index('NO')] * 100
            
            if pred_label == '<30':
                risk_style = "danger"
                risk_status = "🚨 High Risk: Rapid Readmission Predicted (<30 Days)"
                risk_color = "#EF4444"
                clinical_desc = "The XGBoost model predicts a high likelihood of patient readmission within 30 days of discharge. Implement intensive transitional care protocols."
            elif pred_label == '>30':
                risk_style = "warning"
                risk_status = "⚠️ Moderate Risk: Post-Discharge Readmission Predicted (>30 Days)"
                risk_color = "#F59E0B"
                clinical_desc = "The XGBoost model predicts moderate readmission risk occurring after 30 days. Recommend standard discharge follow-up and phone check-ins."
            else:
                risk_style = "success"
                risk_status = "✅ Low Risk: Safe Discharge (No Readmission Predicted)"
                risk_color = "#10B981"
                clinical_desc = "The patient profile indicates a low likelihood of readmission. Coordinate routine post-discharge care."
                
            st.markdown(f"""
<div class="result-card {risk_style}">
<div class="result-header" style="color: {risk_color};">{risk_status}</div>
<div class="result-body" style="margin-top: 1.5rem;">
<div class="metric-progress-container">
<div class="metric-progress-header">
<span>Rapid Readmission Probability (&lt;30 days)</span>
<strong>{prob_less_30:.2f}%</strong>
</div>
<div class="metric-progress-track">
<div class="metric-progress-bar danger" style="width: {prob_less_30}%;"></div>
</div>
</div>
<div class="metric-progress-container">
<div class="metric-progress-header">
<span>Late Readmission Probability (&gt;30 days)</span>
<strong>{prob_more_30:.2f}%</strong>
</div>
<div class="metric-progress-track">
<div class="metric-progress-bar warning" style="width: {prob_more_30}%;"></div>
</div>
</div>
<div class="metric-progress-container">
<div class="metric-progress-header">
<span>Safe Discharge Probability (No Readmission)</span>
<strong>{prob_no:.2f}%</strong>
</div>
<div class="metric-progress-track">
<div class="metric-progress-bar success" style="width: {prob_no}%;"></div>
</div>
</div>
<hr style="margin: 1rem 0; border-top: 1px solid #E2E8F0;">
<strong>Model Clinical Insight:</strong> {clinical_desc}
</div>
</div>
""", unsafe_allow_html=True)
            
            # Recommendations
            st.markdown("<h4 style='margin-top:2rem; margin-bottom:1rem;'>Patient Discharge Optimization Recommendations</h4>", unsafe_allow_html=True)
            recs = []
            
            # Utilisation check
            if num_inpatient > 1 or num_emergency > 1:
                recs.append("🏥 <strong>Frequent Hospital Utilization</strong>: Patient has multiple emergency or inpatient admissions in the prior year. Designate a dedicated clinical care coordinator for post-discharge tracking.")
            
            # Length of stay check
            if time_in_hospital >= 5:
                recs.append("🛌 <strong>Extended Length of Stay</strong>: Hospital stay was {} days. Long hospital stays increase deconditioning risk. Recommend physical therapy consult and transitional home health evaluation.".format(time_in_hospital))
            
            # Medication volume check
            if num_medications > 20:
                recs.append("💊 <strong>Polypharmacy Management</strong>: Patient is prescribed {} generic medications. Strongly recommend a pharmacist-led medication reconciliation prior to discharge to prevent adverse drug events.".format(num_medications))
                
            # Check discharge disposition
            if discharge_disp in [3, 4, 5, 22]:
                recs.append("🏠 <strong>Subacute Placement Coordination</strong>: Discharge disposition indicates referral to a skilled nursing facility (SNF) or intermediate care. Ensure immediate transfer of clinical summaries and active orders.")
                
            # Med changes check
            changes = []
            for med_name, val in [("Metformin", metformin), ("Glipizide", glipizide), ("Glyburide", glyburide)]:
                if val in ["Up", "Down"]:
                    changes.append(f"{med_name} ({val})")
            if changes:
                recs.append("📈 <strong>Active Glycemic Titration</strong>: Doses for {} were titrated during stay. Schedule a follow-up outpatient endocrine visit within 7–14 days to monitor target glycemia and prevent hypoglycemia.".format(", ".join(changes)))
                
            if not recs:
                st.info("✅ Routine diabetic discharge protocol recommended. Coordinate standard post-discharge endocrinologist check-in within 30 days.")
            else:
                for r in recs:
                    st.markdown(f"<div style='background-color:#FFFFFF; padding:0.75rem 1rem; border-radius:8px; border:1px solid #E2E8F0; margin-bottom:0.5rem;'>{r}</div>", unsafe_allow_html=True)
else:
    st.warning("Please execute the Jupyter notebooks inside the 'Health-Care-Domain' folder first to generate the models under 'models/' directory.")

# --- FOOTER & WELLNESS SECTION ---
st.markdown("<hr>", unsafe_allow_html=True)
st.markdown("<h3 style='text-align:center; margin-bottom:2rem;'>Our Wellness Philosophy</h3>", unsafe_allow_html=True)

col_f1, col_f2, col_f3 = st.columns(3)

with col_f1:
    st.markdown("""
    <div class="info-card">
        <div class="info-icon">🛡️</div>
        <div class="info-title">Preventative Medicine</div>
        <div class="info-desc">Catch risk factors and subclinical abnormalities early using ML before they progress to overt clinical conditions.</div>
    </div>
    """, unsafe_allow_html=True)
    
with col_f2:
    st.markdown("""
    <div class="info-card">
        <div class="info-icon">🧬</div>
        <div class="info-title">Precision Health</div>
        <div class="info-desc">No two bodies are identical. Our platform maps unique biomarker levels and lifestyles to patient risk classifications.</div>
    </div>
    """, unsafe_allow_html=True)
    
with col_f3:
    st.markdown("""
    <div class="info-card">
        <div class="info-icon">🌿</div>
        <div class="info-title">Integrative Wellness</div>
        <div class="info-desc">Supporting healthy lifestyle behaviors, sleep hygiene, nutrition, and exercise as core pillars alongside medical care.</div>
    </div>
    """, unsafe_allow_html=True)

st.markdown("""
<div style="text-align:center; padding:3rem 0; color:#64748B; font-size:12px; font-family:'Outfit', sans-serif;">
    © 2026 Soulplanet Health & Wellness Portal. Built for Health Care Domain Clinical Diagnostics.
</div>
""", unsafe_allow_html=True)
