# Soulplanet Health & Wellness Portal (Health Care Domain)

This repository contains machine learning decision-support tools and diagnostics for predicting cardiovascular disease and diabetes.

## Project Structure
- **`app.py` & `home.py`**: The Streamlit web portal.
- **`models/`**: Pre-trained scikit-learn models, columns metadata, and label encoders.
- **`model code/`**: Jupyter notebooks containing the data analysis, pre-processing, and model training pipelines.

## Setup & How to Run

1. **Activate your virtual environment** (if not already activated):
   - **PowerShell**:
     ```powershell
     .venv\Scripts\Activate.ps1
     ```
   - **Command Prompt (CMD)**:
     ```cmd
     .venv\Scripts\activate.bat
     ```
   - **Git Bash / Bash**:
     ```bash
     source .venv/Scripts/activate
     ```

2. **Install the required packages**:
   ```bash
   pip install -r requirements.txt
   ```

3. **Run the Streamlit application**:
   ```bash
   streamlit run app.py
   ```
   *(If you get a launcher or pathing error due to moving the folder, run `python -m streamlit run app.py` instead).*

