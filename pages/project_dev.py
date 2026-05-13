import streamlit as st
import os
from utils import load_cyber_css, render_return_button

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
logo_path = os.path.join(BASE_DIR, "assets", "logo.png")
favicon = logo_path if os.path.exists(logo_path) else "⚡"

st.set_page_config(page_title="Project Dev - Nexus Digital", page_icon=favicon, layout="wide")
load_cyber_css()
render_return_button()

st.markdown('<div class="hero-headline">PROJECT DEVELOPMENT</div>', unsafe_allow_html=True)
st.markdown('<div class="hero-subhead">Python-based automation scripts, web scraping, and data tools.</div>', unsafe_allow_html=True)

st.markdown("---")

col1, col2 = st.columns([2, 1])

with col1:
    st.subheader("> SHOWCASE_")
    
    st.markdown("### Health AI Assistant")
    
    import os
    BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    ASSETS_DIR = os.path.join(BASE_DIR, "assets")
    
    img_1 = os.path.join(ASSETS_DIR, "health_ai_1.png")
    img_2 = os.path.join(ASSETS_DIR, "health_ai_2.png")
    img_3 = os.path.join(ASSETS_DIR, "health_ai_3.png")
    img_4 = os.path.join(ASSETS_DIR, "health_ai_4.png")
    
    import base64
    def get_base64_of_bin_file(bin_file):
        if os.path.exists(bin_file):
            with open(bin_file, 'rb') as f:
                return base64.b64encode(f.read()).decode()
        return ""

    img_data = [
        {"path": img_1, "caption": "Main Interface & Upload"},
        {"path": img_2, "caption": "Diagnosis Overview"},
        {"path": img_3, "caption": "Medications & Surgery Assessment"},
        {"path": img_4, "caption": "Lifestyle Changes Analysis"}
    ]

    valid_imgs = []
    for item in img_data:
        b64 = get_base64_of_bin_file(item["path"])
        if b64:
            valid_imgs.append({"b64": b64, "caption": item["caption"]})

    if valid_imgs:
        imgs_html = ""
        for img in valid_imgs:
            imgs_html += f'''<div style="display:inline-block; text-align:center; margin-right:30px; vertical-align:top;">
<img src="data:image/png;base64,{img['b64']}" style="height:350px; width:auto; border:1px solid var(--grid-color); border-radius:5px; box-shadow:0 4px 8px rgba(0,0,0,0.5); object-fit:contain;">
<div style="color:var(--neon-green); margin-top:15px; font-weight:bold; font-size:1.1rem; text-shadow:0 0 5px var(--neon-green);">{img['caption']}</div>
</div>'''
        
        # Duplicate for infinite seamless scroll
        track_html = imgs_html + imgs_html

        marquee_html = f"""<style>
.marquee-container {{
    width: 100%;
    overflow: hidden;
    white-space: nowrap;
    border: 2px solid var(--neon-blue);
    padding: 20px 10px;
    background-color: rgba(20, 20, 20, 0.8);
    box-shadow: 0 0 15px rgba(0, 243, 255, 0.1);
    border-radius: 10px;
    position: relative;
    margin-bottom: 20px;
}}
.marquee-track {{
    display: inline-block;
    animation: marquee 25s linear infinite;
}}
.marquee-track:hover {{
    animation-play-state: paused;
}}
@keyframes marquee {{
    0% {{ transform: translateX(0); }}
    100% {{ transform: translateX(-50%); }}
}}
</style>
<div class="marquee-container">
<div class="marquee-track">
{track_html}
</div>
</div>"""
        st.markdown(marquee_html, unsafe_allow_html=True)
    else:
        st.warning("Project images not found in the 'assets' folder.")
        
    st.markdown("""
    **PROJECT HIGHLIGHTS (Health AI Assistant):**
    - **AI Integration**: Powered by Google Gemini API for advanced medical report analysis.
    - **Symptom Checker**: Users can describe symptoms in natural language for preliminary diagnosis overviews.
    - **Report Analysis**: Supports uploading images or text reports (PDF, JPG, PNG) for automated breakdown.
    - **Comprehensive Output**: Generates detailed insights including diagnosis overviews, suggested lifestyle changes, and critical medical disclaimers.
    - **Framework**: Built entirely on Streamlit for a fast, responsive user interface.
    """)

with col2:
    st.subheader("> PRICING_")
    st.markdown("""
    <div class="service-card" style="text-align: center;">
        <h2 style="color: var(--neon-blue) !important; font-size: 2.5rem; margin: 10px 0;">CUSTOM</h2>
        <p style="color: var(--text-muted);">Pricing scales depending on project scope and complexity.</p>
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
