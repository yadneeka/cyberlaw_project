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
        padding: 8px 12px;
        margin-bottom: 16px;
        background: {glass};
        backdrop-filter: blur(14px);
        border: 1px solid {border};
        border-radius: 14px;
    }}

    /* BRAND */
    .brand {{
        display: flex;
        align-items: center;
        gap: 8px;
    }}

    .brand-name {{
        font-size: 16px;
        font-weight: 600;
    }}

    .brand-tag {{
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

    .active div.stButton > button {{
        color: {text} !important;
        background: rgba(12,196,221,0.12) !important;
        border: 1px solid rgba(12,196,221,0.25) !important;
    }}

    /* MOBILE FIX (keep horizontal) */
    @media (max-width: 768px) {{

        .brand-tag {{
            display: none;
        }}

        div.stButton > button {{
            font-size: 12px !important;
            padding: 5px 8px !important;
        }}

    }}

    </style>
    """, unsafe_allow_html=True)

    # ── NAVBAR ─────────────────────────

    left, right = st.columns([5, 3])

    # LOGO + BRAND
    with left:
        st.markdown(f"""
        <div class="brand">
            <svg width="28" height="28" viewBox="0 0 24 24">
                <path d="M4 12L12 4L20 12L12 20Z"
                      stroke="{text}" stroke-width="1.5" fill="none"/>
                <circle cx="12" cy="12" r="2" fill="{text}"/>
            </svg>
            <div>
                <div class="brand-name">{APP_NAME}</div>
                <div class="brand-tag">{TAGLINE}</div>
            </div>
        </div>
        """, unsafe_allow_html=True)

    # NAV BUTTONS (HORIZONTAL ALWAYS)
    with right:
        c1, c2 = st.columns(2)

        with c1:
            st.markdown(f'<div class="{"active" if active_page=="dashboard" else ""}">', unsafe_allow_html=True)
            if st.button("▦ Dashboard"):
                st.switch_page("app.py")
            st.markdown("</div>", unsafe_allow_html=True)

        with c2:
            st.markdown(f'<div class="{"active" if active_page=="legal" else ""}">', unsafe_allow_html=True)
            if st.button("🛡 Legal Help"):
                st.switch_page("pages/2_Legal_Help_Guide.py")
            st.markdown("</div>", unsafe_allow_html=True)

    return "dark"