import streamlit as st

def show_home():
    # --- HERO SECTION ---
    st.markdown("""<div class="align-hero">
<div class="align-hero-wash"></div>
<div class="align-hero-content">
<p class="align-eyebrow text-sky">Personalized Clinical Care &middot; Denver &amp; Regional Health</p>
<h1 class="align-hero-title">Move with ease.<br/><span class="italic font-light">Live in alignment.</span></h1>
<p class="align-hero-description">Thoughtful, clinically-validated health analytics for the life you want to live. Cardiovascular diagnostics, diabetic readmission prevention, and evidence-based clinical guidance.</p>
<div class="align-hero-cta-group">
<span class="align-action-btn primary">Predictive Clinical Suite Active</span>
<span class="align-action-btn outlined">Evidence-Based Medicine</span>
</div>
<p class="align-hero-tagline">Care that listens. A diagnostic protocol that&rsquo;s yours.</p>
</div>
<div class="align-hero-side-note">Back to balance &middot; Back to you &middot; Clinical Suite</div>
</div>""", unsafe_allow_html=True)

    # --- SECTION 2: MEET THE CLINICAL DIRECTOR / GOOD CARE STARTS WITH BEING HEARD ---
    st.markdown("""<div class="align-section">
<div class="align-split-grid">
<div class="align-figure">
<div class="align-image-frame">
<img src="https://images.hostinger.com/01b11d58-1bbc-4a81-8ee3-647467389668/646b9df4-3870-488a-8e89-23b9a70fccaa.png" onerror="this.src='https://images.unsplash.com/photo-1594824813587-c1d4285b144e?auto=format&fit=crop&w=900&q=80'" alt="Clinical Director in Consultation" class="align-img-cover" />
</div>
<p class="align-caption">Dr. Sarah Kim, MD &amp; Diagnostics Lead &middot; Clinical Analytics Suite</p>
</div>
<div class="align-doctor-text">
<p class="align-section-eyebrow">A human approach to clinical precision</p>
<h2 class="align-display-heading">Good care starts<br/>with <span class="italic">being heard.</span></h2>
<p class="align-body-text">You&rsquo;re more than an isolated set of symptoms or laboratory readouts. At Align Health, our clinical analytics protocol considers your holistic physiological picture&mdash;metabolic trends, lifestyle stressors, and cardiovascular biomarkers.</p>
<p class="align-body-text">Together, we leverage machine learning decision-support algorithms to forecast risks, prevent hospital readmissions, and build tailored preventative strategies.</p>
<div class="align-credentials-box">
<p class="align-credentials-title">Validated Clinical Credentials &amp; Governance</p>
<ul class="align-credentials-list">
<li><span class="check-icon">&check;</span> Board Certified in Internal Medicine &amp; Preventative Cardiology</li>
<li><span class="check-icon">&check;</span> Trained Random Forest &amp; XGBoost Decision-Support Systems</li>
<li><span class="check-icon">&check;</span> HIPAA Compliant &amp; Clinically-Calibrated Risk Models</li>
</ul>
</div>
</div>
</div>
</div>""", unsafe_allow_html=True)

    # --- SECTION 3: THREE SPECIALTY CARE MODULES ("Find your way back to well") ---
    st.markdown("""<div id="care-suites" class="align-section bg-secondary">
<div class="align-container">
<div class="align-header-row">
<div>
<p class="align-section-eyebrow">Diagnostic Modules for Every Health Stage</p>
<h2 class="align-display-heading">Find your way <span class="italic">back to well.</span></h2>
</div>
<div class="align-status-pill">
<span class="status-dot"></span> Clinical Models Active
</div>
</div>
<div class="align-specialty-grid">
<!-- CARD 1 -->
<div class="align-care-card">
<div class="align-image-frame card-aspect">
<img src="https://images.hostinger.com/01b11d58-1bbc-4a81-8ee3-647467389668/1cd9f2d0-2b7b-4439-9c42-2e5ea232fdf6.png" onerror="this.src='https://images.unsplash.com/photo-1576091160399-112ba8d25d1d?auto=format&fit=crop&w=800&q=80'" alt="Cardiovascular Diagnostics" class="align-img-cover" />
</div>
<p class="align-card-number">01 / Machine Learning Classifier</p>
<h3 class="align-card-title">Cardiovascular Risk Profile</h3>
<p class="align-card-desc">Comprehensive screening for heart disease risk by correlating age, systolic blood pressure, serum lipids, and chronic stress biomarkers.</p>
<div class="align-card-details">
<p class="align-details-text">Powered by a 20-feature Random Forest Classifier with an evaluated 79.96% cross-validated accuracy. Generates tailored clinical lifestyle and medical intervention advice.</p>
<span class="align-metric-tag">Random Forest &bull; 79.96% Accuracy</span>
</div>
</div>
<!-- CARD 2 -->
<div class="align-care-card">
<div class="align-image-frame card-aspect">
<img src="https://images.hostinger.com/01b11d58-1bbc-4a81-8ee3-647467389668/9fd081bc-1f7e-4b98-ba8b-8cfc49ab715a.png" onerror="this.src='https://images.unsplash.com/photo-1505751172876-fa1923c5c528?auto=format&fit=crop&w=800&q=80'" alt="Diabetic Readmission Analysis" class="align-img-cover" />
</div>
<p class="align-card-number">02 / Predictive Clinical Classifier</p>
<h3 class="align-card-title">Diabetic Hospital Readmission</h3>
<p class="align-card-desc">Evaluates inpatient admissions, medication titrations, and laboratory procedures to forecast 30-day post-discharge readmission likelihood.</p>
<div class="align-card-details">
<p class="align-details-text">Utilizes a 29-feature XGBoost decision architecture trained on extensive patient hospital encounters, providing early identification of readmission triggers.</p>
<span class="align-metric-tag">XGBoost Engine &bull; 29 Features</span>
</div>
</div>
<!-- CARD 3 -->
<div class="align-care-card">
<div class="align-image-frame card-aspect">
<img src="https://images.hostinger.com/01b11d58-1bbc-4a81-8ee3-647467389668/4fc0200d-9b59-44c2-8256-aea18557f25c.png" onerror="this.src='https://images.unsplash.com/photo-1506126613408-eca07ce68773?auto=format&fit=crop&w=800&q=80'" alt="Preventative Health &amp; Vitals" class="align-img-cover" />
</div>
<p class="align-card-number">03 / Continuous Wellness</p>
<h3 class="align-card-title">Integrative Vitals &amp; Lifestyle</h3>
<p class="align-card-desc">Evidence-based assessment connecting sleep hygiene, inflammatory markers (CRP), homocysteine, and nutritional guidance.</p>
<div class="align-card-details">
<p class="align-details-text">Integrates with patient registries and laboratory panels to help patients implement sustainable physical routines, cardiac exercise plans, and stress mitigation.</p>
<span class="align-metric-tag">Integrative Health &bull; Preventative Care</span>
</div>
</div>
</div>
</div>
</div>""", unsafe_allow_html=True)

    # --- SECTION 4: EDITORIAL PHILOSOPHY BANNER ---
    st.markdown("""<div class="align-section bg-muted align-center-text">
<div class="align-narrow-container">
<p class="align-section-eyebrow">Our Clinical Philosophy</p>
<h2 class="align-philosophy-quote">We believe feeling better begins with slowing down, listening closely, and helping your body find its way back to <span class="italic">balance.</span></h2>
<p class="align-body-text" style="max-width: 600px; margin: 1.5rem auto 0 auto;">Less guesswork. More partnership. We harness modern computational intelligence to empower clinicians and patients to move forward with clarity and confidence.</p>
</div>
</div>""", unsafe_allow_html=True)

    # --- SECTION 5: THOUGHTFUL TECHNIQUES & PROTOCOLS ---
    st.markdown("""<div class="align-section">
<div class="align-container">
<div class="align-center-text" style="margin-bottom: 3.5rem;">
<p class="align-section-eyebrow">Considered Techniques. Lasting Vitality.</p>
<h2 class="align-display-heading">Small shifts.<br/><span class="italic">Meaningful movement.</span></h2>
<p class="align-body-text" style="max-width: 520px; margin: 1rem auto 0 auto;">No rigid one-size-fits-all diagnostics. Just a calibrated blend of medical science, algorithm precision, and individualized health guidance.</p>
</div>
<div class="align-split-grid">
<div class="align-figure">
<div class="align-image-frame" style="height: 100%; min-height: 380px;">
<img src="https://images.hostinger.com/01b11d58-1bbc-4a81-8ee3-647467389668/bc7a1219-5326-4f4b-a7fb-1947784f26cd.png" onerror="this.src='https://images.unsplash.com/photo-1629909613654-28e377c37b09?auto=format&fit=crop&w=900&q=80'" alt="Hands-on care technique" class="align-img-cover" />
</div>
<p class="align-caption">Gentle, deliberate clinical care centered on comfort.</p>
</div>
<div class="align-steps-list">
<div class="align-step-item">
<span class="align-step-num">01</span>
<div>
<h3 class="align-step-title">Evidence-Based Cardiac Profiling</h3>
<p class="align-body-text">Multivariable analysis examining high-density lipoprotein, triglycerides, arterial pressure, and familial cardiovascular predisposition.</p>
</div>
</div>
<div class="align-step-item">
<span class="align-step-num">02</span>
<div>
<h3 class="align-step-title">Metabolic Biomarker Optimization</h3>
<p class="align-body-text">Early detection of fasting blood glucose deviations, HbA1c fluctuations, and systemic inflammation (CRP) before acute symptom onset.</p>
</div>
</div>
<div class="align-step-item">
<span class="align-step-num">03</span>
<div>
<h3 class="align-step-title">Transitional Discharge Protocols</h3>
<p class="align-body-text">Proactive titration tracking and physician coordination to substantially mitigate 30-day post-hospitalization complications.</p>
</div>
</div>
</div>
</div>
</div>
</div>""", unsafe_allow_html=True)

    # --- SECTION 6: INTERACTIVE PATIENT REGISTRY SIMULATOR ---
    st.markdown("""<div class="align-section bg-secondary">
<div class="align-container">
<p class="align-section-eyebrow">Clinical File Lookup Simulator</p>
<h2 class="align-display-heading">Patient Registry <span class="italic">&amp; Case History</span></h2>
<p class="align-body-text" style="max-width: 640px; margin-bottom: 1.5rem;">Search the active diagnostic database to inspect patient files and pre-load biomarker records directly into our risk assessment models.</p>
</div>
</div>""", unsafe_allow_html=True)

    search_query = st.text_input(
        "Search Clinical Database by Patient ID or Name",
        placeholder="Try 'Eleanor Vance' (PAT-104) or 'Arthur Vance' (PAT-209)...",
        key="align_search_box"
    )

    if search_query:
        q = search_query.strip().lower()
        if "eleanor" in q or "104" in q:
            st.markdown("""<div class="align-patient-card safe">
<div class="align-patient-header">
<div>
<h4 class="align-patient-name">Eleanor Vance</h4>
<span class="align-patient-sub">Patient ID: PAT-104 &middot; Age: 54 &middot; Female</span>
</div>
<span class="align-badge success">Active Baseline Profile</span>
</div>
<div class="align-patient-grid">
<div><strong>Systolic BP:</strong> 132 mmHg (Mild Pre-hypertension)</div>
<div><strong>Total Serum Cholesterol:</strong> 220 mg/dL</div>
<div><strong>Body Mass Index (BMI):</strong> 26.2 (Overweight)</div>
<div><strong>Fasting Blood Sugar:</strong> 105 mg/dL</div>
<div><strong>Daily Physical Activity:</strong> Moderate (Walking 4x/wk)</div>
<div><strong>Homocysteine Assay:</strong> 10.2 &micro;mol/L (Optimal)</div>
</div>
</div>""", unsafe_allow_html=True)
            st.info("💡 **Clinician Insight:** Select **❤️ Cardiovascular Diagnostics** from the sidebar to analyze Eleanor's full profile.")
        elif "vance" in q or "209" in q:
            st.markdown("""<div class="align-patient-card danger">
<div class="align-patient-header">
<div>
<h4 class="align-patient-name">Arthur Vance</h4>
<span class="align-patient-sub">Patient ID: PAT-209 &middot; Age: 67 &middot; Male</span>
</div>
<span class="align-badge danger">🚨 High Risk Flagged</span>
</div>
<div class="align-patient-grid">
<div><strong>Systolic BP:</strong> 155 mmHg (Stage 2 Hypertension)</div>
<div><strong>Total Serum Cholesterol:</strong> 260 mg/dL (High Risk)</div>
<div><strong>Body Mass Index (BMI):</strong> 31.4 (Obese Class I)</div>
<div><strong>Fasting Blood Sugar:</strong> 145 mg/dL (Diabetic Range)</div>
<div><strong>Prior Inpatient Stays:</strong> 3 Admissions in 12 Mos</div>
<div><strong>CRP Inflammatory Assay:</strong> 4.8 mg/L (High)</div>
</div>
</div>""", unsafe_allow_html=True)
            st.warning("⚠️ **Critical Flag:** Multiple elevated biomarkers detected. Immediate clinical intervention recommended.")
        else:
            st.error("🔍 Patient not found. Try searching for 'Eleanor Vance' or 'Arthur Vance'.")
    else:
        st.markdown("""<div class="align-tip-box">
💡 <strong>Registry Tip:</strong> Type <em>"Eleanor Vance"</em> or <em>"Arthur Vance"</em> above to simulate real-time patient record lookup.
</div>""", unsafe_allow_html=True)

    # --- SECTION 7: NEW PATIENTS & ACCORDION FAQ ---
    st.markdown("""<div class="align-section">
<div class="align-container">
<div class="align-split-grid">
<div>
<p class="align-section-eyebrow">Your First Step, Made Simple</p>
<h2 class="align-display-heading">New here?<br/><span class="italic">You&rsquo;re in good hands.</span></h2>
<p class="align-body-text" style="margin-top: 1.5rem;">You don&rsquo;t need to have all the medical jargon figured out beforehand. Select your diagnostics suite from the left sidebar to begin.</p>
<div class="align-timeline-box">
<p class="align-timeline-header">Your Diagnostic Pathway, at a Glance</p>
<p class="align-timeline-item"><strong>01</strong> &mdash; Comprehensive intake of health history &amp; lifestyle</p>
<p class="align-timeline-item"><strong>02</strong> &mdash; Machine learning classification &amp; biomarker inspection</p>
<p class="align-timeline-item"><strong>03</strong> &mdash; A personalized, evidence-based wellness &amp; care plan</p>
</div>
</div>
<div>
<p class="align-section-eyebrow">A little clarity before you begin &middot; FAQ</p>
</div>
</div>
</div>
</div>""", unsafe_allow_html=True)

    with st.expander("What happens during a risk profile screening?"):
        st.write("Our algorithms assess key clinical indicators—including blood pressure, cholesterol panels, BMI, and lifestyle routines—to project risk probabilities and produce actionable recommendations.")

    with st.expander("How were the diagnostic models developed and trained?"):
        st.write("The Cardiovascular model uses a Random Forest Classifier trained on clinically recorded patient parameters (79.96% accuracy), and the Diabetic Readmission engine uses XGBoost evaluated on tens of thousands of inpatient records.")

    with st.expander("Can these models substitute for a licensed physician?"):
        st.write("No. These tools serve as a Clinical Decision Support System (CDSS) designed to assist healthcare professionals and provide educational risk insights, not replace clinical judgment.")

    with st.expander("How do I analyze a new patient record?"):
        st.write("Simply navigate to 'Cardiovascular Diagnostics' or 'Diabetic Readmission Analysis' in the sidebar navigation and fill in the patient values to generate immediate risk calculations.")

    # --- SECTION 8: PATIENT STORIES (TESTIMONIAL QUOTE) ---
    st.markdown("""<div class="align-section bg-secondary align-center-text">
<div class="align-narrow-container">
<p class="align-section-eyebrow">The Human Side of Health</p>
<h2 class="align-display-heading">Room for <span class="italic">real stories.</span></h2>
<div class="align-quote-mark">&ldquo;</div>
<div class="align-story-quote">I felt listened to from the very first conversation. Having a clear data-backed plan made getting back to my daily morning walks feel completely achievable.</div>
<p class="align-story-author">Cardiovascular Health Patient &middot; Denver, Colorado</p>
<div class="align-story-dots">
<span class="dot active"></span>
<span class="dot"></span>
<span class="dot"></span>
</div>
</div>
</div>""", unsafe_allow_html=True)

    # --- SECTION 9: VISIT & CONTACT DETAILS ---
    st.markdown("""<div class="align-section">
<div class="align-container">
<div class="align-split-grid">
<div>
<p class="align-section-eyebrow">A Calmer Space. A Fresh Start.</p>
<h2 class="align-display-heading">Make room<br/>for <span class="italic">feeling better.</span></h2>
<p class="align-body-text" style="margin-top: 1.5rem;">A welcoming clinical practice in Denver, and evidence-driven predictive diagnostics configured for your wellbeing.</p>
<div class="align-contact-details">
<div class="contact-row">
<div class="contact-icon">&oplus;</div>
<div>
<strong>Denver, Colorado Clinical Center</strong><br/>
<span class="text-muted">1250 S. Pearl St., Suite 200, Denver, CO 80210</span>
</div>
</div>
<div class="contact-row">
<div class="contact-icon">&odot;</div>
<div>
<strong>Practice &amp; Diagnostics Consultation Hours</strong><br/>
<span class="text-muted">Monday &ndash; Friday &middot; 9:00 AM &ndash; 5:00 PM Mountain Time</span>
</div>
</div>
<div class="contact-row">
<div class="contact-icon">&phone;</div>
<div>
<strong>Clinical Support Line &amp; Enquiries</strong><br/>
<span class="text-muted">(303) 555-0142 &middot; care@alignhealth.example</span>
</div>
</div>
</div>
</div>
<div class="align-figure">
<div class="align-image-frame" style="height: 100%; min-height: 400px;">
<img src="https://images.hostinger.com/01b11d58-1bbc-4a81-8ee3-647467389668/450992d7-be7c-42e6-a2fd-635e663da463.png" onerror="this.src='https://images.unsplash.com/photo-1516549655169-df83a0774514?auto=format&fit=crop&w=900&q=80'" alt="Welcoming treatment room" class="align-img-cover" />
</div>
<p class="align-caption">A quiet, light-filled space designed for thoughtful care.</p>
</div>
</div>
</div>
</div>""", unsafe_allow_html=True)
