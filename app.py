import os
import pickle
import numpy as np
import pandas as pd
import streamlit as st
from home import show_home

# Set page configuration
st.set_page_config(
    page_title="Align Health | Thoughtful Clinical Diagnostics & Care",
    page_icon="🩺",
    layout="wide",
    initial_sidebar_state="expanded"
)

# --- ALIGN HEALTHCARE DESIGN SYSTEM CSS ---
st.markdown("""
<style>
    @import url('https://fonts.googleapis.com/css2?family=Cormorant+Garamond:ital,wght@0,300;0,400;0,500;0,600;0,700;1,300;1,400;1,500;1,600&family=DM+Sans:ital,opsz,wght@0,9..40,100..1000;1,9..40,100..1000&display=swap');

    :root {
        --navy: #1F3A4D;
        --sky: #7FB3D5;
        --sky-light: #EBF3F8;
        --sand: #EDE6DA;
        --sand-light: #F8F6F2;
        --muted: #F4F7F9;
        --muted-foreground: #6C8291;
        --border: #DCE4E8;
        --white: #FFFFFF;
        --success: #10B981;
        --danger: #EF4444;
        --warning: #F59E0B;
    }

    /* Hide default Streamlit adornments */
    #MainMenu {visibility: hidden;}
    footer {visibility: hidden;}
    header {visibility: hidden;}
    [data-testid="stHeader"] {background-color: transparent !important;}

    /* Global typography & canvas */
    html, body, [data-testid="stAppViewContainer"], .main {
        font-family: 'DM Sans', -apple-system, BlinkMacSystemFont, sans-serif !important;
        background-color: #FFFFFF !important;
        color: var(--navy) !important;
        -webkit-font-smoothing: antialiased;
    }

    .block-container {
        padding-top: 1.5rem !important;
        padding-bottom: 3.5rem !important;
        max-width: 1180px !important;
    }

    h1, h2, h3, h4, .align-display-heading, .align-hero-title, .align-philosophy-quote {
        font-family: 'Cormorant Garamond', Georgia, serif !important;
        font-weight: 400 !important;
        color: var(--navy) !important;
        letter-spacing: -0.025em !important;
    }

    p, span, label, div {
        font-family: 'DM Sans', sans-serif;
    }

    /* Force all links to look clean with no browser blue underlines */
    a, a:visited, a:hover, a:active {
        text-decoration: none !important;
        color: inherit !important;
    }

    /* Top Brand Bar */
    .align-site-header {
        position: relative;
        width: 100%;
        padding: 0.75rem 0 1.25rem 0;
        margin-bottom: 1.75rem;
        border-bottom: 1px solid var(--border);
        background-color: #FFFFFF;
    }
    .align-header-rail {
        display: flex;
        justify-content: space-between;
        align-items: center;
    }
    .align-brand-wrap {
        display: flex;
        align-items: center;
        gap: 12px;
        text-decoration: none !important;
    }
    .align-brand-wrap:hover {
        opacity: 0.9;
    }
    .align-logo-title {
        font-family: 'Cormorant Garamond', serif !important;
        font-size: 36px;
        font-weight: 400;
        line-height: 0.85;
        color: var(--navy);
        letter-spacing: -0.04em;
    }
    .align-logo-dot {
        color: var(--sky);
    }
    .align-logo-sub {
        display: block;
        font-size: 8px;
        text-transform: uppercase;
        letter-spacing: 0.25em;
        color: var(--muted-foreground);
        font-weight: 600;
        margin-top: 4px;
        text-decoration: none !important;
    }
    .align-header-meta {
        display: flex;
        align-items: center;
        gap: 16px;
    }
    .align-location-tag {
        font-size: 10px;
        text-transform: uppercase;
        letter-spacing: 0.18em;
        color: var(--muted-foreground);
        font-weight: 500;
    }
    .align-header-cta {
        display: inline-flex;
        align-items: center;
        gap: 8px;
        padding: 8px 16px;
        border: 1px solid var(--navy);
        color: var(--navy) !important;
        font-size: 10px;
        text-transform: uppercase;
        letter-spacing: 0.16em;
        font-weight: 600;
        text-decoration: none !important;
        transition: all 0.25s ease;
    }
    .align-header-cta:hover {
        background-color: var(--navy);
        color: #FFFFFF !important;
    }

    /* Subpage Header */
    .align-page-header {
        background-color: var(--sand-light);
        border: 1px solid var(--border);
        padding: 2.5rem 2rem;
        border-radius: 3px;
        margin-bottom: 2rem;
    }

    /* Hero Section */
    .align-hero {
        position: relative;
        min-height: 500px;
        background-color: var(--navy);
        background-image: url('https://images.hostinger.com/01b11d58-1bbc-4a81-8ee3-647467389668/450992d7-be7c-42e6-a2fd-635e663da463.png');
        background-size: cover;
        background-position: center;
        border-radius: 4px;
        overflow: hidden;
        margin-bottom: 3.5rem;
        color: #FFFFFF;
    }
    .align-hero-wash {
        position: absolute;
        inset: 0;
        background: linear-gradient(135deg, rgba(31, 58, 77, 0.93) 0%, rgba(31, 58, 77, 0.74) 100%);
    }
    .align-hero-content {
        position: relative;
        z-index: 2;
        padding: 4.5rem 3rem 3.5rem 3rem;
        max-width: 800px;
    }
    .align-eyebrow {
        font-size: 10px;
        letter-spacing: 0.24em;
        text-transform: uppercase;
        font-weight: 600;
        margin-bottom: 1rem;
    }
    .text-sky {
        color: var(--sky);
    }
    .text-muted {
        color: var(--muted-foreground);
    }
    .align-hero-title {
        color: #FFFFFF !important;
        font-size: clamp(2.8rem, 5.2vw, 4.6rem) !important;
        line-height: 1.02 !important;
        margin-bottom: 1.25rem !important;
    }
    .italic {
        font-style: italic;
    }
    .font-light {
        font-weight: 300;
    }
    .align-hero-description {
        font-size: 15px;
        line-height: 1.8;
        color: rgba(255, 255, 255, 0.88);
        max-width: 560px;
        margin-bottom: 2rem;
    }
    .align-hero-cta-group {
        display: flex;
        flex-wrap: wrap;
        gap: 14px;
        align-items: center;
        margin-bottom: 1.75rem;
    }
    .align-action-btn {
        display: inline-flex;
        align-items: center;
        justify-content: center;
        gap: 10px;
        padding: 14px 26px;
        font-size: 10px;
        text-transform: uppercase;
        letter-spacing: 0.16em;
        font-weight: 600;
        text-decoration: none !important;
        transition: all 0.25s ease;
        border: 1px solid transparent;
        cursor: pointer;
    }
    .align-action-btn.primary {
        background-color: var(--sky);
        color: var(--navy) !important;
    }
    .align-action-btn.primary:hover {
        background-color: #FFFFFF;
        color: var(--navy) !important;
    }
    .align-action-btn.outlined {
        background-color: transparent;
        border-color: rgba(255, 255, 255, 0.7);
        color: #FFFFFF !important;
    }
    .align-action-btn.outlined:hover {
        background-color: #FFFFFF;
        color: var(--navy) !important;
    }
    .align-hero-tagline {
        font-size: 10px;
        letter-spacing: 0.08em;
        color: rgba(255, 255, 255, 0.75);
    }
    .align-hero-side-note {
        position: absolute;
        right: 28px;
        bottom: 45px;
        writing-mode: vertical-rl;
        font-size: 9px;
        text-transform: uppercase;
        letter-spacing: 0.25em;
        color: rgba(255, 255, 255, 0.7);
        z-index: 2;
    }

    /* Sections */
    .align-section {
        padding: 3.5rem 0;
    }
    .bg-secondary {
        background-color: var(--sand-light);
        padding: 3.5rem 2rem;
        border-top: 1px solid var(--border);
        border-bottom: 1px solid var(--border);
        border-radius: 4px;
        margin-bottom: 2rem;
    }
    .bg-muted {
        background-color: var(--muted);
        padding: 3.5rem 2rem;
        border-radius: 4px;
        margin-bottom: 2rem;
    }
    .align-center-text {
        text-align: center;
    }
    .align-container {
        width: 100%;
        max-width: 1140px;
        margin: 0 auto;
    }
    .align-narrow-container {
        width: 100%;
        max-width: 820px;
        margin: 0 auto;
    }
    .align-section-eyebrow {
        font-size: 10px;
        letter-spacing: 0.24em;
        text-transform: uppercase;
        font-weight: 600;
        color: var(--muted-foreground);
        margin-bottom: 0.65rem;
    }
    .align-display-heading {
        font-size: clamp(2.2rem, 3.8vw, 3.5rem) !important;
        line-height: 1.05 !important;
        margin-bottom: 1rem !important;
    }
    .align-body-text {
        font-size: 14px;
        line-height: 1.8;
        color: #4A6375;
    }

    /* Split Grid */
    .align-split-grid {
        display: grid;
        grid-template-columns: 1fr 1fr;
        gap: 3.5rem;
        align-items: center;
    }
    @media (max-width: 850px) {
        .align-split-grid {
            grid-template-columns: 1fr;
            gap: 2rem;
        }
        .align-hero-side-note {
            display: none;
        }
    }

    /* Figures and Images */
    .align-figure {
        margin: 0;
    }
    .align-image-frame {
        background-color: var(--sand);
        border-radius: 3px;
        overflow: hidden;
        border: 1px solid var(--border);
    }
    .align-img-cover {
        width: 100%;
        height: 100%;
        object-fit: cover;
        display: block;
        transition: transform 0.5s ease;
    }
    .align-image-frame:hover .align-img-cover {
        transform: scale(1.025);
    }
    .align-caption {
        font-size: 10px;
        letter-spacing: 0.08em;
        color: var(--muted-foreground);
        margin-top: 8px;
    }

    /* Credentials Box */
    .align-credentials-box {
        margin-top: 1.75rem;
        border-top: 1px solid var(--border);
        border-bottom: 1px solid var(--border);
        padding: 1.25rem 0;
    }
    .align-credentials-title {
        font-size: 11px;
        font-weight: 600;
        text-transform: uppercase;
        letter-spacing: 0.12em;
        color: var(--navy);
        margin-bottom: 0.65rem;
    }
    .align-credentials-list {
        list-style: none;
        padding: 0;
        margin: 0;
    }
    .align-credentials-list li {
        display: flex;
        align-items: center;
        gap: 10px;
        font-size: 13px;
        color: #4A6375;
        margin-bottom: 0.45rem;
    }
    .check-icon {
        color: var(--sky);
        font-weight: bold;
    }

    /* Specialty Care Cards */
    .align-header-row {
        display: flex;
        justify-content: space-between;
        align-items: flex-end;
        margin-bottom: 2.5rem;
    }
    .align-status-pill {
        display: inline-flex;
        align-items: center;
        gap: 8px;
        background-color: #FFFFFF;
        border: 1px solid var(--border);
        padding: 5px 12px;
        font-size: 10px;
        text-transform: uppercase;
        letter-spacing: 0.14em;
        font-weight: 600;
        color: var(--navy);
    }
    .status-dot {
        width: 7px;
        height: 7px;
        background-color: var(--success);
        border-radius: 50%;
        display: inline-block;
    }
    .align-specialty-grid {
        display: grid;
        grid-template-columns: repeat(3, 1fr);
        gap: 1.75rem;
    }
    @media (max-width: 900px) {
        .align-specialty-grid {
            grid-template-columns: 1fr;
        }
    }
    .align-care-card {
        background-color: #FFFFFF;
        border: 1px solid var(--border);
        padding: 1.5rem;
        border-radius: 3px;
        transition: all 0.25s ease;
    }
    .align-care-card:hover {
        transform: translateY(-3px);
        box-shadow: 0 10px 20px -8px rgba(31, 58, 77, 0.08);
        border-color: #CBD5E1;
    }
    .card-aspect {
        aspect-ratio: 4 / 3;
        margin-bottom: 1.25rem;
    }
    .align-card-number {
        font-size: 10px;
        letter-spacing: 0.2em;
        text-transform: uppercase;
        color: var(--muted-foreground);
        font-weight: 600;
        margin-bottom: 0.4rem;
    }
    .align-card-title {
        font-size: 24px !important;
        line-height: 1.15 !important;
        margin-bottom: 0.65rem !important;
    }
    .align-card-desc {
        font-size: 13px;
        line-height: 1.7;
        color: #4A6375;
        margin-bottom: 1rem;
    }
    .align-card-details {
        border-top: 1px solid var(--border);
        padding-top: 0.85rem;
    }
    .align-details-text {
        font-size: 12px;
        line-height: 1.7;
        color: #64748B;
        margin-bottom: 0.5rem;
    }
    .align-metric-tag {
        display: inline-block;
        background-color: var(--sky-light);
        color: var(--navy);
        padding: 3px 8px;
        font-size: 10px;
        font-weight: 600;
        letter-spacing: 0.05em;
        text-transform: uppercase;
    }

    /* Philosophy Quote */
    .align-philosophy-quote {
        font-size: clamp(1.8rem, 3.2vw, 2.8rem) !important;
        line-height: 1.2 !important;
        max-width: 760px;
        margin: 0 auto !important;
    }

    /* Steps List */
    .align-steps-list {
        display: flex;
        flex-direction: column;
        justify-content: center;
    }
    .align-step-item {
        display: flex;
        gap: 1.25rem;
        border-top: 1px solid var(--border);
        padding: 1.5rem 0;
    }
    .align-step-num {
        font-size: 11px;
        font-weight: 600;
        letter-spacing: 0.15em;
        color: var(--muted-foreground);
        padding-top: 3px;
    }
    .align-step-title {
        font-size: 20px !important;
        line-height: 1.2 !important;
        margin-bottom: 0.4rem !important;
    }

    /* Patient Card */
    .align-patient-card {
        background-color: #FFFFFF;
        border: 1px solid var(--border);
        border-left: 4px solid var(--navy);
        padding: 1.5rem;
        margin-top: 1rem;
        margin-bottom: 1.5rem;
    }
    .align-patient-card.safe {
        border-left-color: var(--success);
    }
    .align-patient-card.danger {
        border-left-color: var(--danger);
        background-color: #FFF9F9;
    }
    .align-patient-header {
        display: flex;
        justify-content: space-between;
        align-items: center;
        border-bottom: 1px solid var(--border);
        padding-bottom: 0.65rem;
        margin-bottom: 0.85rem;
    }
    .align-patient-name {
        font-family: 'Cormorant Garamond', serif !important;
        font-size: 22px;
        margin: 0;
        color: var(--navy);
    }
    .align-patient-sub {
        font-size: 11px;
        color: var(--muted-foreground);
    }
    .align-badge {
        padding: 3px 8px;
        font-size: 10px;
        font-weight: 600;
        text-transform: uppercase;
        letter-spacing: 0.1em;
    }
    .align-badge.success {
        background-color: #ECFDF5;
        color: #065F46;
    }
    .align-badge.danger {
        background-color: #FEF2F2;
        color: #991B1B;
    }
    .align-patient-grid {
        display: grid;
        grid-template-columns: 1fr 1fr;
        gap: 10px;
        font-size: 13px;
        color: #334155;
    }
    .align-tip-box {
        background-color: var(--sand-light);
        border: 1px solid var(--border);
        padding: 0.85rem 1.15rem;
        font-size: 13px;
        color: var(--navy);
        margin-top: 0.65rem;
    }

    /* Timeline Box */
    .align-timeline-box {
        border-left: 2px solid var(--navy);
        padding-left: 1.25rem;
        margin-top: 1.5rem;
    }
    .align-timeline-header {
        font-size: 11px;
        font-weight: 600;
        text-transform: uppercase;
        letter-spacing: 0.12em;
        margin-bottom: 0.65rem;
        color: var(--navy);
    }
    .align-timeline-item {
        font-size: 13px;
        color: #4A6375;
        margin-bottom: 0.45rem;
    }

    /* Testimonial Quote */
    .align-quote-mark {
        font-family: 'Cormorant Garamond', serif;
        font-size: 54px;
        color: var(--sky);
        line-height: 1;
        margin-top: 0.5rem;
    }
    .align-story-quote {
        font-family: 'Cormorant Garamond', serif !important;
        font-size: clamp(1.6rem, 2.8vw, 2.4rem);
        line-height: 1.35;
        color: var(--navy);
        max-width: 740px;
        margin: 0 auto;
    }
    .align-story-author {
        font-size: 10px;
        letter-spacing: 0.2em;
        text-transform: uppercase;
        color: var(--muted-foreground);
        font-weight: 600;
        margin-top: 1.25rem;
    }
    .align-story-dots {
        display: flex;
        justify-content: center;
        gap: 7px;
        margin-top: 1.25rem;
    }
    .align-story-dots .dot {
        width: 6px;
        height: 6px;
        border-radius: 50%;
        background-color: var(--border);
    }
    .align-story-dots .dot.active {
        background-color: var(--navy);
    }

    /* Contact Details */
    .align-contact-details {
        margin-top: 1.75rem;
        border-top: 1px solid var(--border);
        padding-top: 1.25rem;
    }
    .contact-row {
        display: flex;
        align-items: flex-start;
        gap: 12px;
        font-size: 13px;
        margin-bottom: 1.15rem;
        color: var(--navy);
    }
    .contact-icon {
        font-size: 16px;
        color: var(--navy);
    }

    /* Streamlit Control Overrides */
    div[data-testid="stWidgetLabel"] p, label {
        font-size: 11px !important;
        font-weight: 600 !important;
        text-transform: uppercase !important;
        letter-spacing: 0.1em !important;
        color: var(--navy) !important;
        margin-bottom: 0.35rem !important;
    }

    div[data-baseweb="input"], div[data-baseweb="select"] > div {
        background-color: #FFFFFF !important;
        border: 1px solid var(--border) !important;
        border-radius: 2px !important;
        color: var(--navy) !important;
        box-shadow: none !important;
    }
    div[data-baseweb="input"]:focus-within, div[data-baseweb="select"] > div:focus-within {
        border-color: var(--sky) !important;
        box-shadow: 0 0 0 1px var(--sky) !important;
    }

    /* Streamlit Form Card */
    div[data-testid="stForm"] {
        background-color: #FFFFFF !important;
        border: 1px solid var(--border) !important;
        border-radius: 3px !important;
        padding: 2.25rem !important;
        box-shadow: 0 4px 12px rgba(31, 58, 77, 0.03) !important;
        margin-bottom: 2rem !important;
    }

    /* Streamlit Button */
    .stButton > button {
        background-color: var(--navy) !important;
        color: #FFFFFF !important;
        font-family: 'DM Sans', sans-serif !important;
        font-size: 11px !important;
        text-transform: uppercase !important;
        letter-spacing: 0.16em !important;
        font-weight: 600 !important;
        padding: 14px 28px !important;
        border-radius: 0px !important;
        border: 1px solid var(--navy) !important;
        transition: all 0.25s ease !important;
        width: 100% !important;
        margin-top: 1.25rem !important;
    }
    .stButton > button:hover {
        background-color: var(--sky) !important;
        border-color: var(--sky) !important;
        color: var(--navy) !important;
        transform: translateY(-1px) !important;
    }

    /* Result Card */
    .align-result-card {
        background-color: #FFFFFF;
        border: 1px solid var(--border);
        border-left: 5px solid var(--navy);
        padding: 2.25rem;
        margin-top: 1.75rem;
        margin-bottom: 1.75rem;
    }
    .align-result-card.success {
        border-left-color: var(--success);
        background-color: #F8FCFA;
    }
    .align-result-card.danger {
        border-left-color: var(--danger);
        background-color: #FFF9F9;
    }
    .align-result-card.warning {
        border-left-color: var(--warning);
        background-color: #FFFDF7;
    }
    .align-result-status {
        font-family: 'Cormorant Garamond', serif !important;
        font-size: 26px;
        font-weight: 500;
        margin-bottom: 0.5rem;
    }

    /* Progress meter */
    .align-meter-wrap {
        margin-top: 1.25rem;
        margin-bottom: 1.25rem;
    }
    .align-meter-header {
        display: flex;
        justify-content: space-between;
        font-size: 11px;
        font-weight: 600;
        text-transform: uppercase;
        letter-spacing: 0.1em;
        margin-bottom: 5px;
    }
    .align-meter-track {
        height: 6px;
        background-color: var(--border);
        border-radius: 2px;
        overflow: hidden;
    }
    .align-meter-fill {
        height: 100%;
        background-color: var(--navy);
        transition: width 0.5s ease;
    }
    .align-meter-fill.success {
        background-color: var(--success);
    }
    .align-meter-fill.danger {
        background-color: var(--danger);
    }
    .align-meter-fill.warning {
        background-color: var(--warning);
    }

    /* Recommendation tile */
    .align-rec-tile {
        background-color: #FFFFFF;
        border: 1px solid var(--border);
        padding: 0.85rem 1.15rem;
        font-size: 13px;
        color: var(--navy);
        margin-bottom: 0.45rem;
    }

    /* Sidebar Styling */
    section[data-testid="stSidebar"] {
        background-color: #FAFBFB !important;
        border-right: 1px solid var(--border) !important;
    }
    section[data-testid="stSidebar"] .stRadio label {
        font-size: 13px !important;
        font-weight: 500 !important;
        text-transform: none !important;
        letter-spacing: 0.02em !important;
        color: var(--navy) !important;
    }

    /* Footer */
    .align-site-footer {
        background-color: var(--navy);
        color: #FFFFFF;
        padding: 3.5rem 2rem 2rem 2rem;
        margin-top: 4rem;
        border-radius: 4px;
    }
    .align-footer-container {
        max-width: 1140px;
        margin: 0 auto;
    }
    .align-footer-top {
        display: flex;
        justify-content: space-between;
        align-items: flex-start;
        border-bottom: 1px solid rgba(255, 255, 255, 0.15);
        padding-bottom: 2.5rem;
        margin-bottom: 2.5rem;
    }
    .align-footer-grid {
        display: grid;
        grid-template-columns: repeat(4, 1fr);
        gap: 2rem;
        padding-bottom: 2.5rem;
        border-bottom: 1px solid rgba(255, 255, 255, 0.15);
    }
    @media (max-width: 768px) {
        .align-footer-grid {
            grid-template-columns: 1fr 1fr;
        }
        .align-footer-top {
            flex-direction: column;
            gap: 1.5rem;
        }
    }
    .align-footer-col h4 {
        color: rgba(255, 255, 255, 0.6) !important;
        font-family: 'DM Sans', sans-serif !important;
        font-size: 10px !important;
        letter-spacing: 0.2em !important;
        text-transform: uppercase !important;
        margin-bottom: 0.85rem !important;
    }
    .align-footer-col ul {
        list-style: none;
        padding: 0;
        margin: 0;
    }
    .align-footer-col li {
        font-size: 12px;
        color: rgba(255, 255, 255, 0.8);
        margin-bottom: 0.5rem;
    }
    .align-footer-disclaimer {
        font-size: 11px;
        line-height: 1.7;
        color: rgba(255, 255, 255, 0.5);
        margin-top: 1.75rem;
    }
    .align-footer-bottom {
        display: flex;
        justify-content: space-between;
        font-size: 10px;
        color: rgba(255, 255, 255, 0.5);
        margin-top: 1.25rem;
    }
</style>
""", unsafe_allow_html=True)

# --- LOAD CACHED MODELS AND ENCODERS ---
@st.cache_resource
def load_models_and_encoders():
    models_dir = os.path.join(os.path.dirname(__file__), "models")
    
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
        
    return (heart_model, heart_encoders, heart_cols, 
            diabetes_model, diabetes_encoders, diabetes_cols)

try:
    (heart_model, heart_encoders, heart_cols, 
     diabetes_model, diabetes_encoders, diabetes_cols) = load_models_and_encoders()
    models_loaded = True
except Exception as e:
    st.error(f"Error loading machine learning models: {e}")
    models_loaded = False

# Safe label encoding function
def safe_encode(val, col_name, encoders):
    if col_name not in encoders:
        return val
        
    le = encoders[col_name]
    classes = le.classes_
    
    if val in classes:
        return le.transform([val])[0]
        
    val_str = str(val)
    if val_str in classes:
        return le.transform([val_str])[0]
        
    try:
        numeric_classes = np.array([float(x) for x in classes])
        val_num = float(val)
        closest_idx = np.argmin(np.abs(numeric_classes - val_num))
        return closest_idx
    except ValueError:
        pass
        
    return 0

# --- SIDEBAR NAVIGATION (ALIGN BRANDING) ---
with st.sidebar:
    st.markdown("""<div style="padding: 1rem 0; border-bottom: 1px solid #DCE4E8; margin-bottom: 1.5rem;">
<div style="display: flex; align-items: center; gap: 10px;">
<svg width="22" height="36" viewBox="0 0 25 42" fill="none"><path d="M17 2C-3 13 29 25 8 40" stroke="#1F3A4D" stroke-width="2"></path><path d="M22 4C2 15 34 27 13 42" stroke="#7FB3D5" stroke-width="1.6" opacity=".7"></path></svg>
<div>
<span style="font-family:'Cormorant Garamond', serif; font-size:28px; font-weight:400; color:#1F3A4D; line-height:0.9;">align<span style="color:#7FB3D5;">.</span></span>
<span style="display:block; font-size:8px; text-transform:uppercase; letter-spacing:0.25em; color:#6C8291; font-weight:600;">Health &amp; Diagnostics</span>
</div>
</div>
</div>""", unsafe_allow_html=True)
    
    st.markdown("<p style='font-size:10px; text-transform:uppercase; letter-spacing:0.18em; font-weight:600; color:#6C8291; margin-bottom:0.75rem;'>Clinical Navigation</p>", unsafe_allow_html=True)
    page = st.radio(
        "Select Portal View",
        options=[
            "🏠 Clinic Overview & Home", 
            "❤️ Cardiovascular Diagnostics", 
            "🩸 Diabetic Readmission Analysis"
        ],
        label_visibility="collapsed"
    )
    
    st.markdown("<hr style='margin: 1.75rem 0; border:0; border-top:1px solid #DCE4E8;'>", unsafe_allow_html=True)
    st.markdown("<p style='font-size:10px; text-transform:uppercase; letter-spacing:0.18em; font-weight:600; color:#6C8291; margin-bottom:0.85rem;'>Validated Algorithms</p>", unsafe_allow_html=True)
    
    # Model 1 Metric Card
    st.markdown("""<div style='background-color:#FFFFFF; border:1px solid #DCE4E8; padding:1.15rem; margin-bottom:0.85rem;'>
<div style='font-size:9px; letter-spacing:0.16em; text-transform:uppercase; color:#7FB3D5; font-weight:700;'>Random Forest Model</div>
<div style='font-family:"Cormorant Garamond", serif; font-size:18px; color:#1F3A4D; margin:3px 0;'>Cardiovascular Risk</div>
<div style='display:flex; justify-content:space-between; font-size:11px; color:#6C8291; margin-top:6px;'>
<span>Evaluation Accuracy</span>
<strong style='color:#1F3A4D;'>79.96%</strong>
</div>
</div>""", unsafe_allow_html=True)
    
    # Model 2 Metric Card
    st.markdown("""<div style='background-color:#FFFFFF; border:1px solid #DCE4E8; padding:1.15rem; margin-bottom:1.25rem;'>
<div style='font-size:9px; letter-spacing:0.16em; text-transform:uppercase; color:#7FB3D5; font-weight:700;'>XGBoost Classifier</div>
<div style='font-family:"Cormorant Garamond", serif; font-size:18px; color:#1F3A4D; margin:3px 0;'>Diabetic Readmission</div>
<div style='display:flex; justify-content:space-between; font-size:11px; color:#6C8291; margin-top:6px;'>
<span>Encounters Evaluated</span>
<strong style='color:#1F3A4D;'>29 Features</strong>
</div>
</div>""", unsafe_allow_html=True)
    
    st.markdown("""<div style='font-size:10px; color:#6C8291; text-align:center; padding-top:0.5rem;'>
Denver, Colorado &middot; Suite 200<br/>Clinical Decision Support v2.4
</div>""", unsafe_allow_html=True)

# --- TOP MINIMAL HEADER BAR ---
st.markdown("""<div class="align-site-header">
<div class="align-header-rail">
<div class="align-brand-wrap">
<svg width="22" height="38" viewBox="0 0 25 42" fill="none"><path d="M17 2C-3 13 29 25 8 40" stroke="#1F3A4D" stroke-width="1.8"></path><path d="M22 4C2 15 34 27 13 42" stroke="#7FB3D5" stroke-width="1.5" opacity=".7"></path></svg>
<div>
<span class="align-logo-title">align<span class="align-logo-dot">.</span></span>
<span class="align-logo-sub">CLINICAL HEALTH &amp; DIAGNOSTICS</span>
</div>
</div>
<div class="align-header-meta">
<span class="align-location-tag">Denver, Colorado</span>
<span class="align-header-cta">Clinical Decision Support Active</span>
</div>
</div>
</div>""", unsafe_allow_html=True)

# --- PAGE ROUTING ---
if models_loaded:
    if page == "🏠 Clinic Overview & Home":
        show_home()
        
    elif page == "❤️ Cardiovascular Diagnostics":
        st.markdown("""<div class="align-page-header">
<p class="align-section-eyebrow">Diagnostic Suite 01 &middot; Clinical Decision Support</p>
<h2 class="align-display-heading">Cardiovascular Risk <span class="italic">Profile Analysis</span></h2>
<p class="align-body-text" style="max-width: 680px;">Complete the clinical parameters below to assess heart disease likelihood. Our evaluated Random Forest Classifier cross-references arterial blood pressure, lipid panels, and chronic lifestyle markers.</p>
</div>""", unsafe_allow_html=True)
        
        with st.form("heart_form"):
            col1, col2 = st.columns(2)
            
            with col1:
                st.markdown("<p class='align-section-eyebrow'>Core Patient Demographics</p>", unsafe_allow_html=True)
                age = st.slider("Patient Age (Years)", min_value=1, max_value=120, value=48, step=1)
                
                gender_options = list(heart_encoders['Gender'].classes_)
                gender = st.selectbox("Biological Sex / Gender", options=gender_options)
                
                bmi = st.number_input("Body Mass Index (BMI)", min_value=10.0, max_value=65.0, value=25.8, step=0.1)

            with col2:
                st.markdown("<p class='align-section-eyebrow'>Primary Hemodynamic Vitals</p>", unsafe_allow_html=True)
                bp = st.number_input("Systolic Blood Pressure (mmHg)", min_value=70.0, max_value=250.0, value=126.0, step=1.0)
                chol = st.number_input("Total Serum Cholesterol (mg/dL)", min_value=80.0, max_value=500.0, value=205.0, step=1.0)
                
                diabetes_options = list(heart_encoders['Diabetes'].classes_)
                diabetes = st.selectbox("Diagnosed with Diabetes", options=diabetes_options)

            with st.expander("Lifestyle Factors & Secondary Biomarker Assays (Optional)"):
                exp_col1, exp_col2 = st.columns(2)
                
                with exp_col1:
                    st.markdown("<p class='align-section-eyebrow'>Habitual & Circadian Indicators</p>", unsafe_allow_html=True)
                    sleep_hours = st.slider("Average Nightly Sleep (Hours)", min_value=2.0, max_value=14.0, value=7.0, step=0.5)
                    
                    alcohol_options = list(heart_encoders['Alcohol Consumption'].classes_)
                    alcohol_display = [x if x != '0.0' else 'None / Minimal' for x in alcohol_options]
                    alcohol_sel = st.selectbox("Alcohol Consumption Frequency", options=alcohol_display)
                    alcohol = alcohol_options[alcohol_display.index(alcohol_sel)]
                    
                    exercise_options = list(heart_encoders['Exercise Habits'].classes_)
                    exercise = st.selectbox("Physical Exercise Frequency", options=exercise_options)
                    
                    smoking_options = list(heart_encoders['Smoking'].classes_)
                    smoking = st.selectbox("Active Tobacco Smoking", options=smoking_options)
                    
                    stress_options = list(heart_encoders['Stress Level'].classes_)
                    stress = st.selectbox("Self-Reported Stress Level", options=stress_options)
                    
                    sugar_options = list(heart_encoders['Sugar Consumption'].classes_)
                    sugar = st.selectbox("Refined Sugar Intake", options=sugar_options)
                    
                with exp_col2:
                    st.markdown("<p class='align-section-eyebrow'>Circulatory & Inflammatory Biomarkers</p>", unsafe_allow_html=True)
                    trig = st.number_input("Serum Triglyceride Level (mg/dL)", min_value=40.0, max_value=600.0, value=150.0, step=1.0)
                    fbs = st.number_input("Fasting Blood Sugar (mg/dL)", min_value=40.0, max_value=300.0, value=96.0, step=1.0)
                    crp = st.number_input("C-Reactive Protein (CRP) (mg/L)", min_value=0.0, max_value=30.0, value=1.4, step=0.1)
                    homo = st.number_input("Homocysteine Level (µmol/L)", min_value=2.0, max_value=60.0, value=10.2, step=0.1)
                    
                    family_options = list(heart_encoders['Family Heart Disease'].classes_)
                    family = st.selectbox("Family History of Premature CVD", options=family_options)
                    
                    hbp_options = list(heart_encoders['High Blood Pressure'].classes_)
                    hbp = st.selectbox("Hypertension Diagnosis History", options=hbp_options)
                    
                    hdl_options = list(heart_encoders['Low HDL Cholesterol'].classes_)
                    hdl = st.selectbox("Suboptimal Low HDL Level", options=hdl_options)
                    
                    ldl_options = list(heart_encoders['High LDL Cholesterol'].classes_)
                    ldl = st.selectbox("Elevated LDL Cholesterol Assay", options=ldl_options)
                    
            submit_heart = st.form_submit_button("Run Cardiovascular Risk Assessment")
            
        if submit_heart:
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
            
            encoded_vals = [safe_encode(input_dict[col], col, heart_encoders) for col in heart_cols]
            input_df = pd.DataFrame([encoded_vals], columns=heart_cols)
            
            prob = heart_model.predict_proba(input_df)[0]
            pred = heart_model.predict(input_df)[0]
            
            target_classes = list(heart_encoders['Heart Disease Status'].classes_)
            pred_label = target_classes[pred]
            
            yes_index = 0
            for idx, cls in enumerate(target_classes):
                if str(cls).strip().lower() == 'yes':
                    yes_index = idx
                    break
            
            prob_pct = prob[yes_index] * 100
            
            if pred_label.lower() == 'yes':
                card_style = "danger"
                status_title = "Elevated Cardiovascular Risk Detected"
                fill_class = "danger"
                clinical_desc = "The random forest decision-support architecture has detected biomarker and lifestyle indicators consistent with elevated cardiovascular risk. Comprehensive lipid profiling, arterial monitoring, and lifestyle guidance are indicated."
            else:
                card_style = "success"
                status_title = "Normal Cardiovascular Risk Profile"
                fill_class = "success"
                clinical_desc = "The evaluated biometric metrics correspond to low cardiovascular risk parameters. Maintain routine preventive screening and regular physical exercise."
                
            st.markdown(f"""<div class="align-result-card {card_style}">
<p class="align-section-eyebrow">Diagnostic Assessment Result</p>
<h3 class="align-result-status">{status_title}</h3>
<div class="align-meter-wrap">
<div class="align-meter-header">
<span>Cardiovascular Risk Factor Probability</span>
<strong>{prob_pct:.1f}%</strong>
</div>
<div class="align-meter-track">
<div class="align-meter-fill {fill_class}" style="width: {prob_pct}%;"></div>
</div>
</div>
<p class="align-body-text"><strong>Clinical Insight:</strong> {clinical_desc}</p>
</div>""", unsafe_allow_html=True)
            
            st.markdown("<h4 class='align-display-heading' style='font-size:26px !important;'>Personalized Clinical Recommendations</h4>", unsafe_allow_html=True)
            recs = []
            if smoking.lower() == 'yes':
                recs.append("🚬 <strong>Smoking Cessation</strong>: Patient indicates active smoking. Advise enrollment in evidence-based cessation support.")
            if exercise.lower() == 'low':
                recs.append("🏃 <strong>Physical Conditioning</strong>: Low activity recorded. Recommend progressive transition to 150 minutes of moderate aerobic movement weekly.")
            if bmi > 27.0:
                recs.append(f"⚖️ <strong>Body Composition</strong>: Elevated BMI ({bmi:.1f}). Coordinate dietary guidance emphasizing whole, unrefined foods.")
            if bp >= 130.0 or hbp.lower() == 'yes':
                recs.append("🩺 <strong>Arterial Pressure Control</strong>: Systolic blood pressure is elevated. Advise sodium moderation and ambulatory blood pressure logging.")
            if chol >= 240.0 or ldl.lower() == 'yes':
                recs.append("🥑 <strong>Lipid Panel Optimization</strong>: Hypercholesterolemia indicators present. Consider detailed apolipoprotein B testing.")
            if crp > 2.0:
                recs.append(f"🧪 <strong>Systemic Inflammation</strong>: Elevated CRP ({crp:.1f} mg/L). Inspect periodontal, articular, and metabolic stress factors.")
                
            if not recs:
                st.info("✅ All physiological parameters fall within clinically recommended ranges.")
            else:
                for r in recs:
                    st.markdown(f"<div class='align-rec-tile'>{r}</div>", unsafe_allow_html=True)

    elif page == "🩸 Diabetic Readmission Analysis":
        st.markdown("""<div class="align-page-header">
<p class="align-section-eyebrow">Diagnostic Suite 02 &middot; Clinical Decision Support</p>
<h2 class="align-display-heading">Diabetic Hospital <span class="italic">Readmission Analysis</span></h2>
<p class="align-body-text" style="max-width: 680px;">Evaluate the likelihood of inpatient hospital readmission within 30 days of discharge. Our XGBoost predictive engine examines previous utilization, medication titrations, and primary diagnosis codes.</p>
</div>""", unsafe_allow_html=True)
        
        with st.form("diabetes_form"):
            col1, col2 = st.columns(2)
            
            with col1:
                st.markdown("<p class='align-section-eyebrow'>Patient Demographics & Inpatient Duration</p>", unsafe_allow_html=True)
                gender_options = list(diabetes_encoders['gender'].classes_)
                gender = st.selectbox("Biological Sex", options=gender_options)
                
                age_options = list(diabetes_encoders['age'].classes_)
                age = st.selectbox("Age Bracket", options=age_options)
                
                time_in_hospital = st.slider("Length of Hospitalization (Days)", min_value=1, max_value=14, value=3)

            with col2:
                st.markdown("<p class='align-section-eyebrow'>Inpatient Procedures & Glycemic Therapy</p>", unsafe_allow_html=True)
                diag1_options = list(diabetes_encoders['diag_1'].classes_)
                diag1 = st.selectbox("Primary Diagnosis Code (ICD-9)", options=diag1_options, index=diag1_options.index("250") if "250" in diag1_options else 0)
                
                num_lab_procedures = st.number_input("Laboratory Procedures Performed", min_value=1, max_value=120, value=42, step=1)
                
                diabetes_med_options = list(diabetes_encoders['diabetesMed'].classes_)
                diabetes_med = st.selectbox("Diabetes Pharmacotherapy Prescribed", options=diabetes_med_options, index=diabetes_med_options.index("Yes"))

            with st.expander("Admission Context, Prior Hospital Stays & Medication Titrations"):
                exp_col1, exp_col2 = st.columns(2)
                
                with exp_col1:
                    st.markdown("<p class='align-section-eyebrow'>Utilization History</p>", unsafe_allow_html=True)
                    race_options = list(diabetes_encoders['race'].classes_)
                    race = st.selectbox("Ethnicity / Demographic Group", options=race_options)
                    
                    admission_type = st.slider("Admission Type (1: Emergency, 2: Urgent, 3: Elective)", min_value=1, max_value=8, value=1)
                    admission_src = st.slider("Admission Source ID", min_value=1, max_value=25, value=7)
                    discharge_disp = st.slider("Discharge Disposition ID (1: Home)", min_value=1, max_value=28, value=1)
                    
                    num_outpatient = st.number_input("Prior Year Outpatient Visits", min_value=0, max_value=40, value=0, step=1)
                    num_emergency = st.number_input("Prior Year Emergency Visits", min_value=0, max_value=40, value=0, step=1)
                    num_inpatient = st.number_input("Prior Year Inpatient Admissions", min_value=0, max_value=30, value=0, step=1)
                    
                with exp_col2:
                    st.markdown("<p class='align-section-eyebrow'>Diagnoses & Specific Antidiabetic Agents</p>", unsafe_allow_html=True)
                    num_procedures = st.slider("Number of Inpatient Procedures", min_value=0, max_value=6, value=1)
                    num_medications = st.number_input("Distinct Medications Administered", min_value=1, max_value=100, value=16, step=1)
                    num_diagnoses = st.number_input("Total Diagnoses Recorded", min_value=1, max_value=20, value=7, step=1)
                    
                    diag2_options = list(diabetes_encoders['diag_2'].classes_)
                    diag2 = st.selectbox("Secondary Diagnosis Code", options=diag2_options, index=diag2_options.index("250") if "250" in diag2_options else 0)
                    
                    diag3_options = list(diabetes_encoders['diag_3'].classes_)
                    diag3 = st.selectbox("Tertiary Diagnosis Code", options=diag3_options, index=diag3_options.index("250") if "250" in diag3_options else 0)
                    
                    metformin_options = list(diabetes_encoders['metformin'].classes_)
                    metformin = st.selectbox("Metformin Titration", options=metformin_options, index=metformin_options.index("No"))
                    
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
                    
            submit_diabetes = st.form_submit_button("Run Diabetic Readmission Analysis")
            
        if submit_diabetes:
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
            
            encoded_vals = [safe_encode(input_dict[col], col, diabetes_encoders) for col in diabetes_cols]
            input_df = pd.DataFrame([encoded_vals], columns=diabetes_cols)
            
            prob = diabetes_model.predict_proba(input_df)[0]
            pred = diabetes_model.predict(input_df)[0]
            
            target_classes = list(diabetes_encoders['readmitted'].classes_)
            pred_label = target_classes[pred]
            
            prob_less_30 = prob[target_classes.index('<30')] * 100
            prob_more_30 = prob[target_classes.index('>30')] * 100
            prob_no = prob[target_classes.index('NO')] * 100
            
            if pred_label == '<30':
                card_style = "danger"
                status_title = "High Risk: Rapid Readmission Predicted (<30 Days)"
                clinical_desc = "The XGBoost model predicts a high risk of hospital readmission within 30 days of discharge. Transitional follow-up phone calls and nurse visits are strongly indicated."
            elif pred_label == '>30':
                card_style = "warning"
                status_title = "Moderate Risk: Late Readmission Predicted (>30 Days)"
                clinical_desc = "The patient demonstrates indicators for potential long-term readmission beyond 30 days. Recommend standard outpatient scheduling within 14 days."
            else:
                card_style = "success"
                status_title = "Low Risk: Standard Outpatient Discharge (No Readmission Predicted)"
                clinical_desc = "The clinical parameters indicate low readmission risk. Maintain regular primary care follow-up."
                
            st.markdown(f"""<div class="align-result-card {card_style}">
<p class="align-section-eyebrow">Predictive Analytics Result</p>
<h3 class="align-result-status">{status_title}</h3>
<div class="align-meter-wrap">
<div class="align-meter-header">
<span>Rapid 30-Day Readmission Risk (&lt;30 days)</span>
<strong>{prob_less_30:.1f}%</strong>
</div>
<div class="align-meter-track">
<div class="align-meter-fill danger" style="width: {prob_less_30}%;"></div>
</div>
</div>
<div class="align-meter-wrap">
<div class="align-meter-header">
<span>Late Readmission Risk (&gt;30 days)</span>
<strong>{prob_more_30:.1f}%</strong>
</div>
<div class="align-meter-track">
<div class="align-meter-fill warning" style="width: {prob_more_30}%;"></div>
</div>
</div>
<div class="align-meter-wrap">
<div class="align-meter-header">
<span>Safe Discharge Probability (No Readmission)</span>
<strong>{prob_no:.1f}%</strong>
</div>
<div class="align-meter-track">
<div class="align-meter-fill success" style="width: {prob_no}%;"></div>
</div>
</div>
<p class="align-body-text"><strong>Clinical Protocol Insight:</strong> {clinical_desc}</p>
</div>""", unsafe_allow_html=True)
            
            st.markdown("<h4 class='align-display-heading' style='font-size:26px !important;'>Discharge Care Protocol Recommendations</h4>", unsafe_allow_html=True)
            recs = []
            if num_inpatient > 1 or num_emergency > 1:
                recs.append("🏥 <strong>Frequent Hospital Utilization</strong>: High prior year admissions. Assign a designated case manager for transitional coordination.")
            if time_in_hospital >= 5:
                recs.append(f"🛌 <strong>Extended Length of Stay</strong>: {time_in_hospital} days in hospital. Screen for physical deconditioning and schedule physical therapy.")
            if num_medications > 20:
                recs.append(f"💊 <strong>Polypharmacy Oversight</strong>: {num_medications} medications ordered. Recommend comprehensive pharmacist medication reconciliation.")
            if discharge_disp in [3, 4, 5, 22]:
                recs.append("🏠 <strong>Subacute Placement Coordination</strong>: Ensure immediate transfer of care summaries to transitional rehabilitation nursing.")
                
            if not recs:
                st.info("✅ Routine discharge pathway indicated. Standard endocrine outpatient follow-up recommended within 30 days.")
            else:
                for r in recs:
                    st.markdown(f"<div class='align-rec-tile'>{r}</div>", unsafe_allow_html=True)

else:
    st.warning("Please ensure model files exist under the 'models/' directory.")

# --- RICH NAVY SITE FOOTER ---
st.markdown("""<div class="align-site-footer">
<div class="align-footer-container">
<div class="align-footer-top">
<div>
<div class="align-brand-wrap">
<span style="font-family:'Cormorant Garamond', serif; font-size:46px; font-weight:400; color:#FFFFFF; line-height:0.9;">align<span style="color:#7FB3D5;">.</span></span>
</div>
<p class="align-eyebrow text-sky" style="margin-top: 8px;">Health &amp; Clinical Diagnostics &middot; Denver, Colorado</p>
<p style="font-size: 13px; color: rgba(255, 255, 255, 0.75); max-width: 380px; line-height: 1.8; margin-top: 1rem;">Thoughtful, predictive healthcare algorithms.<br/>Supporting clinicians and patients on the path back to balance.</p>
</div>
<div>
<p class="align-eyebrow" style="color: rgba(255, 255, 255, 0.6);">Evidence-Based Support</p>
<span class="align-action-btn primary" style="font-size: 10px; padding: 12px 22px;">Denver Clinical Center Active</span>
</div>
</div>
<div class="align-footer-grid">
<div class="align-footer-col">
<h4>Our Care</h4>
<ul>
<li>Cardiovascular Risk Profiling</li>
<li>Diabetic Readmission Analysis</li>
<li>Metabolic Biomarker Tracking</li>
<li>Transitional Care Protocols</li>
</ul>
</div>
<div class="align-footer-col">
<h4>Clinical Suite</h4>
<ul>
<li>Random Forest Classifier (79.96%)</li>
<li>XGBoost Readmission Engine</li>
<li>Patient Registry Simulator</li>
<li>Decision Support Guidelines</li>
</ul>
</div>
<div class="align-footer-col">
<h4>Practice</h4>
<ul>
<li>Meet Dr. Sarah Kim</li>
<li>Denver Clinical Practice</li>
<li>Board Governance</li>
<li>Patient Testimonials</li>
</ul>
</div>
<div class="align-footer-col">
<h4>Contact &amp; Hours</h4>
<ul>
<li>1250 S. Pearl St., Suite 200</li>
<li>Denver, CO 80210</li>
<li>Mon&ndash;Fri &middot; 9:00 AM &ndash; 5:00 PM MT</li>
<li>(303) 555-0142</li>
</ul>
</div>
</div>
<p class="align-footer-disclaimer">Clinical decision-support software provided for diagnostic assessment and educational review. Algorithm outputs are intended to complement, not replace, certified clinical judgment by a licensed medical practitioner.</p>
<div class="align-footer-bottom">
<span>&copy; 2026 Align Health Diagnostics. All rights reserved.</span>
<span>Denver, Colorado &middot; Secure Clinical Architecture</span>
</div>
</div>
</div>""", unsafe_allow_html=True)
