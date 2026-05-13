import streamlit as st
import os

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
logo_path = os.path.join(BASE_DIR, "assets", "logo.png")
favicon = logo_path if os.path.exists(logo_path) else "⚡"

st.set_page_config(page_title="Resume Building - Nexus Digital", page_icon=favicon, layout="wide")
from utils import load_cyber_css, render_return_button
load_cyber_css()
render_return_button()


st.markdown('<div class="hero-headline">RESUME BUILDING</div>', unsafe_allow_html=True)
st.markdown('<div class="hero-subhead">Tailored for ATS (Applicant Tracking Systems) to get you hired.</div>', unsafe_allow_html=True)

st.markdown("---")

col1, col2 = st.columns([2, 1])

with col1:
    st.subheader("> SHOWCASE_")
    
    import base64
    
    # Path to assets folder
    ASSETS_DIR = os.path.join(BASE_DIR, "assets")
    
    resumes_data = [
        {"path": os.path.join(ASSETS_DIR, "Sayyed_Raheem_Resume.jpg"), "name": "The Executive", "score": 96},
        {"path": os.path.join(ASSETS_DIR, "Sayyed_Raheem_Resume_2.jpg"), "name": "The Technologist", "score": 92},
        {"path": os.path.join(ASSETS_DIR, "Sayyed_Raheem_Resume_3.jpg"), "name": "The Minimalist", "score": 98},
        {"path": os.path.join(ASSETS_DIR, "resume 4_page-0001.jpg"), "name": "The Classic Professional", "score": 99},
    ]

    def get_base64_of_bin_file(bin_file):
        if os.path.exists(bin_file):
            with open(bin_file, 'rb') as f:
                return base64.b64encode(f.read()).decode()
        return ""

    valid_resumes = []
    for res in resumes_data:
        b64 = get_base64_of_bin_file(res["path"])
        if b64:
            valid_resumes.append({**res, "b64": b64})
        else:
            st.error(f"⚠️ Could not find file: {os.path.basename(res['path'])} in the assets folder.")

    num_resumes = len(valid_resumes)
    st.info(f"Successfully loaded {num_resumes} out of {len(resumes_data)} resumes from the assets directory.")

    if num_resumes > 0:
        total_duration = num_resumes * 4
        
        if num_resumes > 1:
            vis = (4.0 / total_duration) * 100
            fade_in = 5
            visible_end = vis - 5
            fade_out = vis
            
            keyframes = f"""
            @keyframes swipeAnim {{
                0% {{ opacity: 0; transform: translateX(30px); }}
                {fade_in}% {{ opacity: 1; transform: translateX(0); }}
                {visible_end}% {{ opacity: 1; transform: translateX(0); }}
                {fade_out}% {{ opacity: 0; transform: translateX(-30px); }}
                100% {{ opacity: 0; transform: translateX(-30px); }}
            }}
            """
        else:
            keyframes = """
            @keyframes swipeAnim {
                0% { opacity: 1; transform: translateX(0); }
                100% { opacity: 1; transform: translateX(0); }
            }
            """
            total_duration = 8

        slides_html = ""
        for i, res in enumerate(valid_resumes):
            delay = i * 4
            slides_html += f"""<div class="carousel-slide" style="animation-delay: {delay}s;">
    <img src="data:image/jpeg;base64,{res['b64']}" class="carousel-img" alt="{res['name']}">
    <div class="ats-badge">🛡️ ATS Match Score: {res['score']}%<br><span style="font-size: 0.8em; color: var(--text-main); text-shadow: none;">Template {i+1}: {res['name']}</span></div>
</div>"""

        carousel_html = f"""<style>
.carousel-container {{
    position: relative;
    width: 100%;
    margin: 0 auto 20px auto;
    height: 900px;
    overflow: hidden;
    border: 2px solid var(--neon-blue);
    border-radius: 10px;
    background-color: rgba(20, 20, 20, 0.8);
    box-shadow: 0 0 15px rgba(0, 243, 255, 0.1);
}}
.carousel-slide {{
    position: absolute;
    top: 0;
    left: 0;
    width: 100%;
    height: 100%;
    opacity: 0;
    animation: swipeAnim {total_duration}s infinite;
    display: flex;
    flex-direction: column;
    align-items: center;
    justify-content: flex-start;
    padding: 20px;
    box-sizing: border-box;
}}
{keyframes}
.carousel-img {{
    width: 100%;
    height: auto;
    max-height: calc(100% - 100px);
    object-fit: contain;
    border: 1px solid var(--grid-color);
    box-shadow: 0 4px 8px rgba(0,0,0,0.5);
    border-radius: 5px;
}}
.ats-badge {{
    margin-top: 15px;
    background: rgba(0, 0, 0, 0.7);
    padding: 10px 20px;
    border-radius: 5px;
    border: 1px solid var(--neon-green);
    color: var(--neon-green);
    font-weight: bold;
    font-size: 1.1rem;
    text-shadow: 0 0 5px var(--neon-green);
    text-align: center;
}}
</style>
<div class="carousel-container">
{slides_html}
</div>"""
        st.markdown(carousel_html, unsafe_allow_html=True)
    else:
        st.warning("Resume images not found. Please upload them to the 'assets' folder.")
        
    st.markdown("""
    **WHY CHOOSE THIS SERVICE:**
    - Guaranteed ATS parsing compatibility
    - Keyword optimization for specific roles
    - Professional, sleek formatting
    - Tailored cover letter included
    """)

with col2:
    st.subheader("> PRICING_")
    st.markdown("""
    <div class="service-card" style="text-align: center;">
        <h2 style="color: var(--neon-green) !important; font-size: 3rem; margin: 10px 0;">₹700</h2>
        <p style="color: var(--text-muted);">Standard rate for full resume optimization.</p>
        <hr>
        <p style="font-size: 0.9em;"><em>* Lower cost for a limited time</em></p>
    </div>
    """, unsafe_allow_html=True)
    
    st.markdown("<br>", unsafe_allow_html=True)
    st.markdown('<a href="/#contact-lead-gen" target="_self" style="display: block; text-align: center; padding: 15px; border: 1px solid var(--neon-blue); color: #000; background-color: var(--neon-blue); font-weight: bold; text-transform: uppercase; text-decoration: none;">INITIALIZE PROJECT &rarr;</a>', unsafe_allow_html=True)

st.markdown("---")
st.markdown("""
<div style="text-align: center; padding: 30px 0; margin-top: 20px; border-top: 1px solid rgba(255,255,255,0.05); font-family: 'Fira Code', monospace; font-size: 0.85rem; color: #888; opacity: 0.6;">
    &copy; 2026 Nexus Digital. All rights reserved.<br>
    Engineered for Excellence.<br><br>
    <span style="background: linear-gradient(135deg, #00f3ff, #39ff14); -webkit-background-clip: text; -webkit-text-fill-color: transparent; background-clip: text; font-weight: 800; font-size: 1rem; letter-spacing: 2px; font-family: 'Inter', sans-serif;">NEXUS GROUP</span>
</div>
""", unsafe_allow_html=True)
