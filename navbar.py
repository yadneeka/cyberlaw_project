import streamlit as st


def top_nav(active_page="dashboard"):

    APP_NAME = "CyberLytics"
    TAGLINE = "Turning cyberlaw data into actionable insights"

    bg = "#0b1220"
    glass = "rgba(15, 23, 42, 0.85)"
    text = "#e6edf7"
    muted = "#94a3b8"
    accent = "#0cc4dd"
    border = "rgba(255,255,255,0.08)"

    st.markdown(f"""
    <style>

    html, body {{
        background: {bg};
        color: {text};
        font-family: 'Inter', sans-serif;
    }}

    /* NAVBAR */
    .nav {{
        position: sticky;
        top: 10px;
        z-index: 999;
        display: flex;
        align-items: center;
        justify-content: space-between;
        padding: 10px 14px;
        margin-bottom: 16px;
        background: {glass};
        backdrop-filter: blur(16px);
        border: 1px solid {border};
        border-radius: 14px;
    }}

    /* BRAND */
    .nav-brand-name {{
        font-size: 18px;
        font-weight: 600;
    }}

    .nav-brand-tag {{
        font-size: 11px;
        color: {muted};
    }}

    /* BUTTONS */
    div.stButton > button {{
        background: transparent !important;
        border: none !important;
        color: {muted} !important;
        font-size: 14px !important;
        padding: 6px 10px !important;
        border-radius: 8px !important;
        white-space: nowrap;
    }}

    div.stButton > button:hover {{
        color: {text} !important;
        background: rgba(255,255,255,0.06) !important;
    }}

    .nav-active div.stButton > button {{
        color: {text} !important;
        background: rgba(12,196,221,0.12) !important;
        border: 1px solid rgba(12,196,221,0.25) !important;
    }}

    /* SLIDER */
    .slider {{
        height:2px;
        width:50%;
        background:{accent};
        transition: margin-left 0.35s ease;
    }}

    /* 🔥 MOBILE FIX (HORIZONTAL, NOT STACKED) */
    @media (max-width: 768px) {{

        .nav {{
            padding: 8px 10px;
        }}

        .nav-brand-tag {{
            display: none;
        }}

        .nav-brand-name {{
            font-size: 16px;
        }}

        div.stButton > button {{
            font-size: 13px !important;
            padding: 5px 8px !important;
        }}

    }}

    </style>
    """, unsafe_allow_html=True)

    left_col, right_col = st.columns([5, 3])

    # BRAND
    with left_col:
        st.markdown(f"""
        <div style="display:flex;align-items:center;gap:8px;">
            <svg width="30" height="30" viewBox="0 0 24 24">
                <path d="M4 12L12 4L20 12L12 20Z" stroke="{text}" stroke-width="1.6" fill="none"/>
                <circle cx="12" cy="12" r="2.2" fill="{text}"/>
            </svg>
            <div>
                <div class="nav-brand-name">{APP_NAME}</div>
                <div class="nav-brand-tag">{TAGLINE}</div>
            </div>
        </div>
        """, unsafe_allow_html=True)

    # NAV BUTTONS
    with right_col:
        c1, c2 = st.columns(2)

        with c1:
            st.markdown(f'<div class="{"nav-active" if active_page=="dashboard" else ""}">', unsafe_allow_html=True)
            if st.button("▦ Dashboard", key="nav_dashboard"):
                st.switch_page("app.py")
            st.markdown("</div>", unsafe_allow_html=True)

        with c2:
            st.markdown(f'<div class="{"nav-active" if active_page=="legal" else ""}">', unsafe_allow_html=True)
            if st.button("🛡 Legal Help", key="nav_legal"):
                st.switch_page("pages/2_Legal_Help_Guide.py")
            st.markdown("</div>", unsafe_allow_html=True)

        margin = "0%" if active_page == "dashboard" else "50%"
        st.markdown(f"""
        <div style="display:flex;">
            <div class="slider" style="margin-left:{margin};"></div>
        </div>
        """, unsafe_allow_html=True)

    return "dark"