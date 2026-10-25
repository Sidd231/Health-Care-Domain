import os
import pickle
import numpy as np
import pandas as pd
from flask import Flask, request, jsonify, send_from_directory
from flask_cors import CORS

# Initialize Flask app
# Point static_folder to the frontend directory so everything can also be served via Flask
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
FRONTEND_DIR = os.path.join(BASE_DIR, "frontend")

app = Flask(__name__, static_folder=FRONTEND_DIR, static_url_path="")
CORS(app)  # Enable CORS for all routes

# Global model stores
heart_model = None
heart_encoders = None
heart_cols = None

diabetes_model = None
diabetes_encoders = None
diabetes_cols = None

models_loaded = False


def safe_encode(val, col_name, encoders):
    if col_name not in encoders:
        return val

    le = encoders[col_name]
    classes = le.classes_

    if val in classes:
        return int(le.transform([val])[0])

    val_str = str(val)
    if val_str in classes:
        return int(le.transform([val_str])[0])

    try:
        numeric_classes = np.array([float(x) for x in classes])
        val_num = float(val)
        closest_idx = int(np.argmin(np.abs(numeric_classes - val_num)))
        return closest_idx
    except (ValueError, TypeError):
        pass

    return 0


def load_models():
    global heart_model, heart_encoders, heart_cols
    global diabetes_model, diabetes_encoders, diabetes_cols
    global models_loaded

    models_dir = os.path.join(BASE_DIR, "models")
    try:
        with open(os.path.join(models_dir, "heart_disease_model.pkl"), "rb") as f:
            heart_model = pickle.load(f)
        with open(os.path.join(models_dir, "heart_disease_encoders.pkl"), "rb") as f:
            heart_encoders = pickle.load(f)
        with open(os.path.join(models_dir, "heart_disease_columns.pkl"), "rb") as f:
            heart_cols = pickle.load(f)

        with open(os.path.join(models_dir, "diabetes_model.pkl"), "rb") as f:
            diabetes_model = pickle.load(f)
        with open(os.path.join(models_dir, "diabetes_encoders.pkl"), "rb") as f:
            diabetes_encoders = pickle.load(f)
        with open(os.path.join(models_dir, "diabetes_columns.pkl"), "rb") as f:
            diabetes_cols = pickle.load(f)

        models_loaded = True
        print("[Align API] Machine Learning Models & Encoders loaded successfully.")
    except Exception as e:
        print(f"[Align API Error] Failed to load models: {e}")
        models_loaded = False


# Load models immediately
load_models()


# --- SERVE FRONTEND STATIC FILES ---
@app.route("/")
def index():
    if os.path.exists(os.path.join(FRONTEND_DIR, "index.html")):
        return send_from_directory(FRONTEND_DIR, "index.html")
    return jsonify({"message": "Align Health API is running. Frontend build in progress."})


@app.route("/<path:path>")
def static_proxy(path):
    file_path = os.path.join(FRONTEND_DIR, path)
    if os.path.exists(file_path):
        return send_from_directory(FRONTEND_DIR, path)
    if os.path.exists(file_path + ".html"):
        return send_from_directory(FRONTEND_DIR, path + ".html")
    return jsonify({"error": "Resource not found"}), 404


# --- REST API ENDPOINTS ---
@app.route("/api/health", methods=["GET"])
def health():
    return jsonify({
        "status": "healthy" if models_loaded else "degraded",
        "models_loaded": models_loaded,
        "heart_model": "Random Forest Classifier (79.96% Accuracy)",
        "diabetes_model": "XGBoost Classifier (29 Evaluated Features)",
        "clinic": "Align Health & Clinical Diagnostics",
        "location": "Denver, Colorado"
    })


@app.route("/api/predict/heart", methods=["POST"])
def predict_heart():
    if not models_loaded or heart_model is None:
        return jsonify({"error": "Heart disease model is not loaded"}), 503

    try:
        data = request.get_json(force=True)
        if not data:
            return jsonify({"error": "No JSON payload received"}), 400

        # Extract values with safe defaults matching app.py
        age = float(data.get("Age", 48))
        gender = str(data.get("Gender", "Male"))
        bp = float(data.get("Blood Pressure", 126.0))
        chol = float(data.get("Cholesterol Level", 205.0))
        exercise = str(data.get("Exercise Habits", "Medium"))
        smoking = str(data.get("Smoking", "No"))
        family = str(data.get("Family Heart Disease", "No"))
        diabetes = str(data.get("Diabetes", "No"))
        bmi = float(data.get("BMI", 25.8))
        hbp = str(data.get("High Blood Pressure", "No"))
        hdl = str(data.get("Low HDL Cholesterol", "No"))
        ldl = str(data.get("High LDL Cholesterol", "No"))
        alcohol = str(data.get("Alcohol Consumption", "Low"))
        stress = str(data.get("Stress Level", "Medium"))
        sleep_hours = float(data.get("Sleep Hours", 7.0))
        sugar = str(data.get("Sugar Consumption", "Medium"))
        trig = float(data.get("Triglyceride Level", 150.0))
        fbs = float(data.get("Fasting Blood Sugar", 96.0))
        crp = float(data.get("CRP Level", 1.4))
        homo = float(data.get("Homocysteine Level", 10.2))

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

        # Encode features in strict column order
        encoded_vals = [safe_encode(input_dict.get(col, 0), col, heart_encoders) for col in heart_cols]
        input_df = pd.DataFrame([encoded_vals], columns=heart_cols)

        # Inferences
        prob = heart_model.predict_proba(input_df)[0]
        pred = heart_model.predict(input_df)[0]

        target_classes = list(heart_encoders['Heart Disease Status'].classes_)
        pred_label = str(target_classes[pred])

        # Identify 'Yes' index
        yes_index = 0
        for idx, cls in enumerate(target_classes):
            if str(cls).strip().lower() == 'yes':
                yes_index = idx
                break

        prob_pct = round(float(prob[yes_index] * 100), 1)

        is_high_risk = pred_label.strip().lower() == 'yes'

        if is_high_risk:
            card_style = "danger"
            status_title = "Elevated Cardiovascular Risk Detected"
            fill_class = "danger"
            clinical_desc = (
                "The random forest decision-support architecture has detected biomarker and lifestyle "
                "indicators consistent with elevated cardiovascular risk. Comprehensive lipid profiling, "
                "arterial monitoring, and lifestyle guidance are indicated."
            )
        else:
            card_style = "success"
            status_title = "Normal Cardiovascular Risk Profile"
            fill_class = "success"
            clinical_desc = (
                "The evaluated biometric metrics correspond to low cardiovascular risk parameters. "
                "Maintain routine preventive screening and regular physical exercise."
            )

        # Generate evidence-based clinical recommendations
        recs = []
        if smoking.lower() == 'yes':
            recs.append({
                "icon": "🚬",
                "title": "Smoking Cessation Support",
                "detail": "Patient indicates active tobacco smoking. Advise enrollment in evidence-based cessation and pulmonary support protocols."
            })
        if exercise.lower() == 'low':
            recs.append({
                "icon": "🏃",
                "title": "Physical Conditioning",
                "detail": "Low physical activity recorded. Recommend progressive transition to 150 minutes of moderate aerobic movement weekly."
            })
        if bmi > 27.0:
            recs.append({
                "icon": "⚖️",
                "title": "Body Composition Protocol",
                "detail": f"Elevated BMI ({bmi:.1f} kg/m²). Coordinate dietary guidance emphasizing whole, unrefined foods and glycemic moderation."
            })
        if bp >= 130.0 or hbp.lower() == 'yes':
            recs.append({
                "icon": "🩺",
                "title": "Arterial Pressure Monitoring",
                "detail": f"Systolic pressure is elevated ({bp:.0f} mmHg). Advise sodium moderation and ambulatory blood pressure logging."
            })
        if chol >= 240.0 or ldl.lower() == 'yes':
            recs.append({
                "icon": "🥑",
                "title": "Lipid Panel Optimization",
                "detail": f"Hypercholesterolemia indicators present (Total: {chol:.0f} mg/dL). Consider advanced apolipoprotein B and particle count testing."
            })
        if crp > 2.0:
            recs.append({
                "icon": "🧪",
                "title": "Systemic Inflammation Assay",
                "detail": f"Elevated CRP ({crp:.1f} mg/L). Inspect periodontal, articular, and metabolic stress factors."
            })

        if not recs:
            recs.append({
                "icon": "✅",
                "title": "Clinical Harmony",
                "detail": "All evaluated physiological biomarkers fall within clinically recommended target parameters. Continue standard annual wellness screening."
            })

        return jsonify({
            "status": "success",
            "prediction_label": pred_label,
            "is_high_risk": is_high_risk,
            "risk_probability": prob_pct,
            "card_style": card_style,
            "status_title": status_title,
            "fill_class": fill_class,
            "clinical_desc": clinical_desc,
            "recommendations": recs
        })

    except Exception as e:
        return jsonify({"error": f"Error during cardiovascular prediction: {str(e)}"}), 500


@app.route("/api/predict/diabetes", methods=["POST"])
def predict_diabetes():
    if not models_loaded or diabetes_model is None:
        return jsonify({"error": "Diabetes readmission model is not loaded"}), 503

    try:
        data = request.get_json(force=True)
        if not data:
            return jsonify({"error": "No JSON payload received"}), 400

        # Parse inputs
        gender = str(data.get("gender", "Female"))
        age = str(data.get("age", "[60-70)"))
        race = str(data.get("race", "Caucasian"))
        time_in_hospital = int(data.get("time_in_hospital", 3))
        diag1 = str(data.get("diag_1", "250"))
        diag2 = str(data.get("diag_2", "250"))
        diag3 = str(data.get("diag_3", "250"))
        num_lab_procedures = int(data.get("num_lab_procedures", 42))
        num_procedures = int(data.get("num_procedures", 1))
        num_medications = int(data.get("num_medications", 16))
        num_diagnoses = int(data.get("number_diagnoses", 7))
        admission_type = int(data.get("admission_type_id", 1))
        admission_src = int(data.get("admission_source_id", 7))
        discharge_disp = int(data.get("discharge_disposition_id", 1))
        num_outpatient = int(data.get("number_outpatient", 0))
        num_emergency = int(data.get("number_emergency", 0))
        num_inpatient = int(data.get("number_inpatient", 0))
        diabetes_med = str(data.get("diabetesMed", "Yes"))

        # Medication titrations
        metformin = str(data.get("metformin", "No"))
        repaglinide = str(data.get("repaglinide", "No"))
        nateglinide = str(data.get("nateglinide", "No"))
        glimepiride = str(data.get("glimepiride", "No"))
        glipizide = str(data.get("glipizide", "No"))
        glyburide = str(data.get("glyburide", "No"))
        pioglitazone = str(data.get("pioglitazone", "No"))
        rosiglitazone = str(data.get("rosiglitazone", "No"))
        acarbose = str(data.get("acarbose", "No"))

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

        # Encode values
        encoded_vals = [safe_encode(input_dict.get(col, 0), col, diabetes_encoders) for col in diabetes_cols]
        input_df = pd.DataFrame([encoded_vals], columns=diabetes_cols)

        # Inferences
        prob = diabetes_model.predict_proba(input_df)[0]
        pred = diabetes_model.predict(input_df)[0]

        target_classes = list(diabetes_encoders['readmitted'].classes_)
        pred_label = str(target_classes[pred])

        # Get exact class probabilities
        prob_less_30 = round(float(prob[target_classes.index('<30')] * 100), 1) if '<30' in target_classes else 0.0
        prob_more_30 = round(float(prob[target_classes.index('>30')] * 100), 1) if '>30' in target_classes else 0.0
        prob_no = round(float(prob[target_classes.index('NO')] * 100), 1) if 'NO' in target_classes else 0.0

        if pred_label == '<30':
            card_style = "danger"
            status_title = "High Risk: Rapid Readmission Predicted (<30 Days)"
            clinical_desc = (
                "The XGBoost gradient-boosted decision engine predicts an elevated risk of inpatient hospital "
                "readmission within 30 days of initial discharge. Structured transitional discharge planning, "
                "reconciliation of insulin regimens, and timely nurse tele-triage are urgently advised."
            )
        elif pred_label == '>30':
            card_style = "warning"
            status_title = "Moderate Risk: Late Readmission Predicted (>30 Days)"
            clinical_desc = (
                "The patient profile exhibits indicators for potential extended-horizon readmission past 30 days. "
                "Recommend scheduled outpatient endocrinology follow-up within 14 calendar days."
            )
        else:
            card_style = "success"
            status_title = "Low Risk: Standard Outpatient Discharge (No Readmission Predicted)"
            clinical_desc = (
                "The clinical inpatient markers correspond to low readmission risk. Maintain established "
                "outpatient chronic disease management and routine post-discharge checkup."
            )

        # Clinical care recommendations
        recs = []
        if num_inpatient > 1 or num_emergency > 1:
            recs.append({
                "icon": "🏥",
                "title": "Complex Utilization History",
                "detail": f"Recorded {num_inpatient} inpatient admissions and {num_emergency} ER visits in prior year. Assign a transitional care navigator."
            })
        if time_in_hospital >= 5:
            recs.append({
                "icon": "🛌",
                "title": "Extended Length of Stay Recovery",
                "detail": f"{time_in_hospital} days hospitalized. Screen for muscular deconditioning and initiate physical therapy / mobility support."
            })
        if num_medications > 20:
            recs.append({
                "icon": "💊",
                "title": "Polypharmacy Review",
                "detail": f"{num_medications} distinct medications active. Order comprehensive clinical pharmacist medication therapy management (MTM)."
            })
        if discharge_disp in [3, 4, 5, 22]:
            recs.append({
                "icon": "🏠",
                "title": "Subacute Placement Coordination",
                "detail": "Patient discharging to skilled nursing or home health agency. Ensure immediate electronic transfer of discharge care summary."
            })

        if not recs:
            recs.append({
                "icon": "✅",
                "title": "Standard Outpatient Protocol",
                "detail": "Standard discharge pathway indicated. Coordinate routine outpatient endocrine consultation within 30 days of release."
            })

        return jsonify({
            "status": "success",
            "prediction_label": pred_label,
            "card_style": card_style,
            "status_title": status_title,
            "clinical_desc": clinical_desc,
            "prob_less_30": prob_less_30,
            "prob_more_30": prob_more_30,
            "prob_no": prob_no,
            "recommendations": recs
        })

    except Exception as e:
        return jsonify({"error": f"Error during diabetic readmission prediction: {str(e)}"}), 500


if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    print(f"\n==================================================")
    print(f"  ALIGN HEALTH CLINICAL DECISION SUPPORT SERVER")
    print(f"  Running at: http://localhost:{port}")
    print(f"  API Heart:      POST http://localhost:{port}/api/predict/heart")
    print(f"  API Diabetes:   POST http://localhost:{port}/api/predict/diabetes")
    print(f"  API Health:     GET  http://localhost:{port}/api/health")
    print(f"==================================================\n")
    app.run(host="0.0.0.0", port=port, debug=False)
