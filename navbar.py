import streamlit as st


def top_nav(active_page="dashboard"):

    APP_NAME = "CyberLytics"
    TAGLINE  = "Turning cyberlaw data into actionable insights"

    bg    = "#0b1220"
    text  = "#e6edf7"
    muted = "#94a3b8"
    accent = "#0cc4dd"

    st.markdown(f"""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700&display=swap');

    html, body {{
        background: {bg};
        color: {text};
        font-family: 'Inter', sans-serif;
    }}

    .block-container {{
        max-width: 1200px !important;
        padding-top: 24px;
        padding-left: 20px;
        padding-right: 20px;
    }}

    /* Hide default UI */
    [data-testid="stSidebar"],
    [data-testid="collapsedControl"] {{ display: none !important; }}
    #MainMenu, footer, header {{ visibility: hidden; }}
    [data-testid="stDecoration"] {{ display: none; }}

    /* Wrapper */
    .nav-wrapper {{
        display: flex;
        justify-content: center;
        width: 100%;
    }}

    /* ===== MAIN NAVBAR BOX ===== */
    .nav-card {{
        width: 100%;
        max-width: 1400px;

        margin-bottom: 20px;

        background: rgba(15, 23, 42, 0.95);

        border: 1px solid rgba(255,255,255,0.25);
        border-radius: 10px;

        box-shadow:
            0 0 0 1px rgba(255,255,255,0.05),
            0 12px 30px rgba(0,0,0,0.6);

        display: flex;
        align-items: center;
        justify-content: space-between;

        padding: 14px 20px;
    }}

    /* ===== SECOND BOX (FIXED) ===== */
    .sub-card {{
        width: 100%;
        max-width: 1400px;

        height: 40px;

        margin-top: -10px;
        margin-bottom: 30px;

        background: rgba(15, 23, 42, 0.95);

        border: 1px solid rgba(255,255,255,0.20);
        border-radius: 10px;

        box-shadow:
            0 0 0 1px rgba(255,255,255,0.05),
            0 8px 20px rgba(0,0,0,0.4);

        backdrop-filter: blur(6px);
    }}

    /* Brand */
    .brand {{
        display: flex;
        align-items: center;
        gap: 14px;
    }}

    .brand-logo {{
        width: 52px;
        height: 52px;
        border-radius: 8px;
        background: linear-gradient(135deg,#0cc4dd22,#0cc4dd44);
        border: 1px solid rgba(12,196,221,0.35);
        display: flex;
        align-items: center;
        justify-content: center;
    }}

    .brand-name {{
        font-size: 24px;
        font-weight: 700;
        color: {text};
    }}

    .brand-name span {{
        color: {accent};
    }}

    .brand-tag {{
        font-size: 13px;
        color: {muted};
    }}

    /* Buttons */
    button[kind="secondary"] {{
        font-size: 16px !important;
        font-weight: 500 !important;
        padding: 8px 14px !important;
        border-radius: 8px !important;
        background: transparent !important;
        color: {muted} !important;
        border: 1px solid transparent !important;
        transition: all 0.2s ease !important;
    }}

    button[kind="secondary"]:hover {{
        color: {text} !important;
        background: rgba(255,255,255,0.07) !important;
        border-color: rgba(255,255,255,0.12) !important;
    }}

    .nav-active button[kind="secondary"] {{
        color: {text} !important;
        background: rgba(12,196,221,0.10) !important;
        border-color: rgba(12,196,221,0.30) !important;
        font-weight: 600 !important;
    }}

    /* Mobile fix */
    @media (max-width: 640px) {{
        .brand-tag {{ display: none; }}

        .nav-card {{
            flex-direction: column;
            gap: 12px;
            padding: 12px;
        }}

        button[kind="secondary"] {{
            width: 100% !important;
        }}
    }}
    </style>
    """, unsafe_allow_html=True)

    # ===== NAVBAR =====
    st.markdown('<div class="nav-wrapper"><div class="nav-card">', unsafe_allow_html=True)

    left, right = st.columns([5, 5])

    with left:
        st.markdown(f"""
        <div class="brand">
          <div class="brand-logo">
            <svg width="18" height="18" viewBox="0 0 32 32" fill="none">
              <rect x="2"  y="18" width="5" height="12" rx="1.5" fill="#e63946"/>
              <rect x="9"  y="12" width="5" height="18" rx="1.5" fill="#f4a261"/>
              <rect x="16" y="7"  width="5" height="23" rx="1.5" fill="{accent}"/>
              <rect x="23" y="3"  width="5" height="27" rx="1.5" fill="{accent}" opacity="0.4"/>
            </svg>
          </div>
          <div>
            <div class="brand-name">Cyber<span>Lytics</span></div>
            <div class="brand-tag">{TAGLINE}</div>
          </div>
        </div>
        """, unsafe_allow_html=True)

    with right:
        c1, c2, c3 = st.columns(3)

        with c1:
            st.markdown(f'<div class="{"nav-active" if active_page=="dashboard" else ""}">', unsafe_allow_html=True)
            if st.button("▦ Dashboard", key="nav_dash"):
                st.switch_page("app.py")
            st.markdown("</div>", unsafe_allow_html=True)

        with c2:
            st.markdown(f'<div class="{"nav-active" if active_page=="legal" else ""}">', unsafe_allow_html=True)
            if st.button("🛡 Legal Help", key="nav_legal"):
                st.switch_page("pages/2_Legal_Help_Guide.py")
            st.markdown("</div>", unsafe_allow_html=True)

        with c3:
            st.markdown(f'<div class="{"nav-active" if active_page=="pipeline" else ""}">', unsafe_allow_html=True)
            if st.button("⚙ Pipeline", key="nav_pipeline"):
                st.switch_page("pages/3_Data_Pipeline.py")
            st.markdown("</div>", unsafe_allow_html=True)

    st.markdown('</div></div>', unsafe_allow_html=True)

    # ===== SECOND BOX (NOW WORKING) =====
    st.markdown('''
    <div class="nav-wrapper">
        <div class="sub-card"></div>
    </div>
    ''', unsafe_allow_html=True)

    return "dark"