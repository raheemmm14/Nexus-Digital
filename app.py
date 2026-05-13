import streamlit as st
import os
import sqlite3
import time
import base64
import io
import openpyxl
from openpyxl.styles import Font
from datetime import datetime

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
ASSETS_DIR = os.path.join(BASE_DIR, "assets")
DB_PATH = os.path.join(BASE_DIR, "client_leads.db")
UPLOAD_DIR = os.path.join(BASE_DIR, "uploads")
logo_path = os.path.join(BASE_DIR, "assets", "logo.png")
favicon = logo_path if os.path.exists(logo_path) else "⚡"

# Configure page
st.set_page_config(page_title="Nexus Digital", page_icon=favicon, layout="wide")

# Load custom CSS for Cyber-Industrial theme from utils
from utils import load_cyber_css
load_cyber_css()


# --- Section 1: Hero & Services ---
st.markdown("<br>", unsafe_allow_html=True)
col1, col_logo, col3 = st.columns([2, 1, 2])
with col_logo:
    # Attempt to load the logo if it exists
    if os.path.exists(logo_path):
        st.image(logo_path, use_container_width=True)
    else:
        st.markdown('<div style="color:var(--neon-blue); border:1px solid var(--neon-blue); padding:10px; text-align:center;">[ LOGO HERE ]<br><small>Save as logo.png</small></div>', unsafe_allow_html=True)

st.markdown('<div class="hero-headline">Talent Doesn\'t Open Doors.<br>Presentation Does.</div>', unsafe_allow_html=True)
st.markdown('<div class="hero-subhead">You don\'t lose opportunities because you lack skill—you lose them because your presentation lets you down. We help tech students, graduates, and creative professionals stand out with custom portfolios, ATS-optimized resumes, and powerful web solutions.</div>', unsafe_allow_html=True)

# To simulate a scroll to contact, since streamlit doesn't do smooth scrolling natively easily
# We just use an anchor tag.
st.markdown('<a href="#contact-lead-gen" style="text-decoration: none; display: inline-block; padding: 10px 20px; border: 1px solid var(--neon-blue); color: var(--neon-blue); font-weight: bold; text-transform: uppercase;">GET IN TOUCH [ > ]</a>', unsafe_allow_html=True)

st.markdown("""
<div style="text-align: center; margin: 2rem 0; background-color: var(--card-bg); padding: 15px; border: 1px solid var(--neon-blue); border-radius: 5px; box-shadow: 0 0 10px rgba(0, 243, 255, 0.1);">
    <span style="color: var(--neon-green); font-weight: bold; font-size: 1.1rem; margin: 0 15px;">50+ Projects Delivered</span> <span style="color: var(--neon-blue);">|</span> 
    <span style="color: var(--neon-green); font-weight: bold; font-size: 1.1rem; margin: 0 15px;">98% Client Satisfaction</span> <span style="color: var(--neon-blue);">|</span> 
    <span style="color: var(--neon-green); font-weight: bold; font-size: 1.1rem; margin: 0 15px;">48h Average Turnaround</span>
    <div style="margin-top: 15px; color: var(--text-main); font-size: 0.95em;">
        🛡️ <strong>OUR GUARANTEE:</strong> If you're not fully satisfied, we revise for free.
    </div>
</div>
""", unsafe_allow_html=True)

st.markdown("---")

# --- Section 2: Service Cards ---
st.header("SERVICES_")

col1, col2, col3 = st.columns(3)

with col1:
    st.markdown("""
    <a href="/portfolio_websites" target="_self" style="text-decoration: none; color: inherit;">
        <div class="service-card">
            <h3>[ Portfolio Websites ]</h3>
            <p>Custom-built, SEO-friendly, and interactive.</p>
            <p style='color: var(--neon-green); font-size: 0.9em;'><em>* Lower cost for a limited time</em></p>
        </div>
    </a>
    """, unsafe_allow_html=True)

with col2:
    st.markdown("""
    <a href="/resume_building" target="_self" style="text-decoration: none; color: inherit;">
        <div class="service-card">
            <h3>[ Resume Building ]</h3>
            <p>Tailored for ATS (Applicant Tracking Systems) to get you hired.</p>
            <p style='color: var(--neon-green); font-size: 0.9em;'><em>* Lower cost for a limited time</em></p>
        </div>
    </a>
    """, unsafe_allow_html=True)

with col3:
    st.markdown("""
    <a href="/project_dev" target="_self" style="text-decoration: none; color: inherit;">
        <div class="service-card">
            <h3>[ Project Dev ]</h3>
            <p>Python-based automation scripts and data tools.</p>
            <p style='color: var(--neon-green); font-size: 0.9em;'><em>* Lower cost for a limited time</em></p>
        </div>
    </a>
    """, unsafe_allow_html=True)

st.markdown("---")

# --- Section 3: Resume Integration & Automations ---
st.header("SYS_DATA: RESUME_INTEGRATION_")

col_resume, col_skills = st.columns(2)

with col_resume:
    st.subheader("> LATEST_EXPERIENCE")
    st.code("""
{
  "status": "ACTIVE",
  "role": "Full Stack & AI Developer",
  "recent_projects": [
    "NoteVault & Studio Platform",
    "TechVault Marketplace",
    "AI-Powered Test Case Generator"
  ],
  "focus": "Automating workflows and building premium web apps."
}
    """, language="json")

with col_skills:
    st.subheader("> SKILL_METRICS")
    st.markdown("**Python**")
    st.progress(90)
    st.markdown("**Streamlit**")
    st.progress(85)
    st.markdown("**SQL / Database (Supabase)**")
    st.progress(80)
    st.markdown("**AI SDKs (Gemini)**")
    st.progress(75)

st.markdown("---")



# --- Section 4: Contact & Lead Gen ---
st.markdown('<a id="contact-lead-gen" class="anchor"></a>', unsafe_allow_html=True)
st.header("CONTACT_ & LEAD_GEN_")
st.write("Ready to upgrade your digital presence? Initialize a connection.")

st.markdown("""
<link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.4.0/css/all.min.css">
<div style="margin-bottom: 1rem;">
    <strong style="color: var(--neon-blue);">COMMS_LINKS:</strong><br>
    <i class="fas fa-envelope" style="color: var(--neon-blue); margin-right: 5px;"></i> <a href="mailto:sayyedraheem994@gmail.com" style="color: var(--text-main); text-decoration: none; transition: color 0.3s;" onmouseover="this.style.color='var(--neon-green)'" onmouseout="this.style.color='var(--text-main)'">sayyedraheem994@gmail.com</a> &nbsp;|&nbsp; 
    <i class="fas fa-mobile-alt" style="color: var(--neon-blue); margin-right: 5px;"></i> <span style="color: var(--text-main);">+91 6303554891</span> &nbsp;|&nbsp; 
    <i class="fab fa-instagram" style="color: var(--neon-blue); margin-right: 5px;"></i> <a href="https://instagram.com/raheemmm.lala" style="color: var(--text-main); text-decoration: none; transition: color 0.3s;" onmouseover="this.style.color='var(--neon-green)'" onmouseout="this.style.color='var(--text-main)'">raheemmm.lala</a>
</div>
""", unsafe_allow_html=True)

st.subheader("BOOKING_TERMINAL")
with st.form("contact_form", clear_on_submit=True):
    name = st.text_input("NAME_")
    email = st.text_input("EMAIL_")
    
    col_code, col_phone = st.columns([1, 3])
    with col_code:
        country_code = st.selectbox("CODE_", [
            "🇮🇳 +91", "🇺🇸 +1", "🇬🇧 +44", "🇦🇺 +61", "🇦🇪 +971", 
            "🇸🇦 +966", "🇩🇪 +49", "🇫🇷 +33", "🇯🇵 +81", "🇨🇳 +86", 
            "🇧🇷 +55", "🇲🇽 +52", "🇿🇦 +27", "🇷🇺 +7", "🇵🇰 +92", 
            "🇧🇩 +880", "🌎 Other"
        ])
    with col_phone:
        phone = st.text_input("PHONE_NUMBER_")
        
    service = st.selectbox("SERVICE_REQUIRED_", ["Portfolio Website", "Resume Building & Optimization", "Project Development"])
    message = st.text_area("PROJECT_DETAILS_")
    uploaded_file = st.file_uploader("ATTACH_REFERENCE_FILE_ (Optional)", type=["pdf", "png", "jpg", "jpeg", "docx", "txt"])
    st.caption("💡 *Note: You can attach your resume here to have your portfolio website customized according to your specific skillset and experience.*")
    
    submitted = st.form_submit_button("SUBMIT_REQUEST")
    if submitted:
        if name and email:
            full_phone = f"{country_code.split(' ')[1] if 'Other' not in country_code else ''} {phone}".strip()
            
            # Handle file upload
            final_message = message
            if uploaded_file is not None:
                upload_dir = UPLOAD_DIR
                os.makedirs(upload_dir, exist_ok=True)
                safe_filename = f"{int(time.time())}_{uploaded_file.name}"
                file_path = os.path.join(upload_dir, safe_filename)
                
                with open(file_path, "wb") as f:
                    f.write(uploaded_file.getbuffer())
                
                final_message += f"\\n\\n[Attached File: {safe_filename}]"
                
            # Save to database
            try:
                db_path = DB_PATH
                conn = sqlite3.connect(db_path)
                cursor = conn.cursor()
                cursor.execute('''
                    INSERT INTO client_inquiries (name, email, phone_number, service_required, requirements)
                    VALUES (?, ?, ?, ?, ?)
                ''', (name, email, full_phone, service, final_message))
                conn.commit()
                conn.close()
                st.success(f"REQUEST_RECEIVED. Database updated. Transmitting confirmation to {email}...")
                st.balloons()
            except Exception as e:
                st.error(f"SYSTEM_ERROR: Could not save to database. {e}")
        else:
            st.error("ERROR: NAME and EMAIL are required fields.")

st.markdown("---")
st.markdown("""
<div style="text-align: center; padding: 30px 0; margin-top: 20px; border-top: 1px solid rgba(255,255,255,0.05); font-family: 'Fira Code', monospace; font-size: 0.85rem; color: #888; opacity: 0.6;">
    &copy; 2026 Nexus Digital. All rights reserved.<br>
    Engineered for Excellence.<br><br>
    <span style="background: linear-gradient(135deg, #00f3ff, #39ff14); -webkit-background-clip: text; -webkit-text-fill-color: transparent; background-clip: text; font-weight: 800; font-size: 1rem; letter-spacing: 2px; font-family: 'Inter', sans-serif;">NEXUS GROUP</span>
</div>
""", unsafe_allow_html=True)
