import streamlit as st

def load_cyber_css():
    st.markdown("""
    <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.4.0/css/all.min.css">
    <style>
        /* Global Styles */
        :root {
            --bg-color: #0d0d0d;
            --grid-color: #1a1a1a;
            --neon-blue: #00f3ff;
            --neon-green: #39ff14;
            --text-main: #e0e0e0;
            --text-muted: #888888;
            --card-bg: rgba(20, 20, 20, 0.8);
        }
        
        .stApp {
            background-color: var(--bg-color);
            background-image: 
                linear-gradient(var(--grid-color) 1px, transparent 1px),
                linear-gradient(90deg, var(--grid-color) 1px, transparent 1px);
            background-size: 30px 30px;
            color: var(--text-main);
            font-family: 'Courier New', Courier, monospace;
        }
        
        h1, h2, h3 {
            color: var(--neon-blue) !important;
            text-transform: uppercase;
            letter-spacing: 2px;
            text-shadow: 0 0 5px var(--neon-blue);
        }
        
        /* Headers specific */
        .hero-headline {
            font-size: 3rem;
            font-weight: bold;
            color: var(--neon-blue);
            text-shadow: 0 0 10px rgba(0, 243, 255, 0.5);
            margin-bottom: 0.5rem;
            text-align: center;
        }
        .hero-subhead {
            font-size: 1.5rem;
            color: var(--text-main);
            margin-bottom: 2rem;
            text-align: center;
        }
        
        /* Service Cards */
        .service-card {
            background-color: var(--card-bg);
            border: 1px solid var(--neon-blue);
            border-radius: 5px;
            padding: 20px;
            margin: 10px 0;
            box-shadow: 0 0 10px rgba(0, 243, 255, 0.1);
            transition: all 0.3s ease;
        }
        .service-card:hover {
            box-shadow: 0 0 20px rgba(57, 255, 20, 0.3);
            border-color: var(--neon-green);
            transform: translateY(-5px);
        }
        
        /* Buttons */
        .stButton>button {
            background-color: transparent !important;
            color: var(--neon-blue) !important;
            border: 1px solid var(--neon-blue) !important;
            border-radius: 0 !important;
            text-transform: uppercase;
            letter-spacing: 1px;
            font-weight: bold;
            transition: all 0.3s ease;
        }
        .stButton>button:hover {
            background-color: var(--neon-blue) !important;
            color: #000 !important;
            box-shadow: 0 0 15px var(--neon-blue) !important;
        }
        
        /* Progress Bars */
        .stProgress > div > div > div > div {
            background-color: var(--neon-green);
        }
        
        /* Contact Form */
        div[data-baseweb="input"] > div, div[data-baseweb="textarea"] > div, div[data-baseweb="select"] > div {
            background-color: rgba(20, 20, 20, 0.8);
            border: 1px solid var(--neon-blue);
        }
        
        hr {
            border-color: var(--neon-blue);
            opacity: 0.3;
        }
        
        /* Anchor for jump */
        .anchor {
            display: block;
            position: relative;
            top: -100px; /* Offset for sticky headers if any */
            visibility: hidden;
        }

        /* Hide Streamlit Sidebar for Custom Navigation */
        [data-testid="stSidebar"] {
            display: none;
        }
        [data-testid="collapsedControl"] {
            display: none;
        }
        
        /* Custom Return Link */
        .return-link {
            display: inline-block;
            margin-bottom: 20px;
            padding: 8px 15px;
            border: 1px solid var(--neon-blue);
            color: var(--neon-blue) !important;
            text-decoration: none !important;
            font-weight: bold;
            transition: all 0.3s ease;
        }
        .return-link:hover {
            background-color: var(--neon-blue);
            color: #000 !important;
            box-shadow: 0 0 10px var(--neon-blue);
        }
        
        /* Showcase Image styling */
        .showcase-img {
            border: 2px solid var(--grid-color);
            border-radius: 5px;
            padding: 5px;
            background: var(--card-bg);
            transition: all 0.3s ease;
        }
        .showcase-img:hover {
            border-color: var(--neon-green);
            box-shadow: 0 0 15px rgba(57, 255, 20, 0.3);
        }
    </style>
    """, unsafe_allow_html=True)

def render_return_button():
    st.markdown('<a href="/" target="_self" class="return-link"><i class="fas fa-arrow-left"></i> RETURN TO MAIN SEC</a>', unsafe_allow_html=True)
