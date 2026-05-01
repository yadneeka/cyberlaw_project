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

    /* ── Sidebar off ── */
    [data-testid="stSidebar"],
    [data-testid="collapsedControl"] {{ display: none !important; }}
    #MainMenu, footer, header {{ visibility: hidden; }}
    [data-testid="stDecoration"] {{ display: none; }}

    /* ── Nav wrapper ── */
    .nav-wrapper {{
        display: flex;
        justify-content: center;
        margin-bottom: 32px;
    }}

   
    /* ===== NAVBAR BOX ===== */
    .nav-card {{
        width: 100%;
        max-width: 1400px;

         height: 35px; 

        margin-bottom: 35px;
        margin-top: 5px;

        background: rgba(15, 23, 42, 0.95);

        border: 1px solid rgba(255,255,255,0.35);
        border-radius: 8px;

        box-shadow:
            0 0 0 1px rgba(255,255,255,0.08),
            0 12px 30px rgba(0,0,0,0.6);

        display: flex;
        align-items: center;
        justify-content: space-between;
    }}

    /* ===== SECOND BOX (NEW) ===== */
    .sub-card {{
        width: 100%;
        max-width: 1100px;

        height: 35px;  /* adjust if needed */

        margin-bottom: 5px;
        margin-top: -80px;
        background: rgba(15, 23, 42, 0.95);

        border: 1px solid rgba(255,255,255,0.35);
        border-radius: 8px;

        box-shadow:
            0 0 0 1px rgba(255,255,255,0.08),
            0 10px 25px rgba(0,0,0,0.5);
    }}

    /* ── Brand ── */
    .brand {{
        display: flex;
        align-items: center;
        gap: 12px;
        flex-shrink: 0;
    }}
    .brand-logo {{
        width: 64px; height: 64px;
        background: linear-gradient(135deg,#0cc4dd22,#0cc4dd44);
        border: 1px solid rgba(12,196,221,0.35);
        border-radius: 8px;
        display: flex; align-items: center; justify-content: center;
    }}
    .brand-name {{
        font-size: 30px; font-weight: 700;
        letter-spacing: -0.3px; color: {text};
        white-space: nowrap;
    }}
    .brand-name span {{ color: {accent}; }}
    .brand-tag {{
        font-size: 18px; color: {muted};
        white-space: nowrap;
    }}

    /* ── Nav buttons (Streamlit override) ── */
    button[kind="secondary"] {{
        font-family: 'Inter', sans-serif !important;
        font-size: 50px !important;
        font-weight: 500 !important;
        padding: 7px 14px !important;
        border-radius: 8px !important;
        background: transparent !important;
        color: {muted} !important;
        border: 1px solid transparent !important;
        transition: all 0.2s ease !important;
        white-space: nowrap !important;
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

    /* ── Mobile: keep row layout ── */
    @media (max-width: 640px) {{
        .brand-tag {{ display: none; }}
        .nav-card  {{ padding: 0 12px; min-height: 54px; }}
        button[kind="secondary"] {{
            font-size: 12px !important;
            padding: 6px 10px !important;
        }}
    }}
    </style>
    """, unsafe_allow_html=True)

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
              <polyline points="4.5,24 11.5,18 18.5,11 25.5,6"
                stroke="white" stroke-width="1.5" fill="none"
                stroke-linecap="round" stroke-linejoin="round" opacity="0.45"/>
              <circle cx="25.5" cy="6" r="2.2" fill="white" opacity="0.85"/>
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
            if st.button("▦  Dashboard", key="nav_dash"):
                st.switch_page("app.py")
            st.markdown("</div>", unsafe_allow_html=True)

        with c2:
            st.markdown(f'<div class="{"nav-active" if active_page=="legal" else ""}">', unsafe_allow_html=True)
            if st.button("🛡  Legal Help", key="nav_legal"):
                st.switch_page("pages/2_Legal_Help_Guide.py")
            st.markdown("</div>", unsafe_allow_html=True)

        with c3:
            st.markdown(f'<div class="{"nav-active" if active_page=="pipeline" else ""}">', unsafe_allow_html=True)
            if st.button("⚙  Pipeline", key="nav_pipeline"):
                st.switch_page("pages/3_Data_Pipeline.py")
            st.markdown("</div>", unsafe_allow_html=True)

    st.markdown('</div></div>', unsafe_allow_html=True)

    return "dark"