import streamlit as st


def top_nav(active_page="dashboard"):

    APP_NAME = "CyberLytics"
    TAGLINE = "Turning cyberlaw data into actionable insights"

    # ── DESIGN TOKENS ─────────────────────────
    bg = "#0b1220"
    glass = "rgba(15, 23, 42, 0.7)"
    text = "#e6edf7"
    muted = "#94a3b8"
    accent = "#0cc4dd"
    border = "rgba(255,255,255,0.06)"

    # ── GLOBAL STYLE ───────────────────────────
    st.markdown(f"""
    <style>

    @import url('https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600&display=swap');

    html, body {{
        background: {bg};
        color: {text};
        font-family: 'Inter', sans-serif;
    }}

    /* ── FLOATING NAVBAR ── */
    .nav {{
        position: sticky;
        top: 10px;
        z-index: 999;

        display:flex;
        align-items:center;
        justify-content:space-between;

        padding:12px 20px;
        margin-bottom:20px;

        background: {glass};
        backdrop-filter: blur(14px);
        border:1px solid {border};
        border-radius:14px;

        transition: all 0.3s ease;
    }}

    .nav:hover {{
        box-shadow: 0 10px 30px rgba(0,0,0,0.4);
    }}

    /* ── NAV BUTTON ── */
div.stButton > button,
button[data-testid="baseButton-secondary"],
button[data-testid="baseButton-primary"] {{
        background: transparent !important;
        border: none !important;
        color: {muted} !important;
         font-size: 28px !important;   /* increase */
        font-weight: 500;
         padding: 10px 18px;     
        border-radius: 8px;
        transition: all 0.25s ease;
    }}

    div.stButton > button:hover {{
        color: {text} !important;
        transform: translateY(-1px);
    }}

    .active div.stButton > button {{
        color: {text} !important;
        font-weight: 600;
    }}

    /* ── SLIDER ── */
    .slider {{
        height:2px;
        background:{accent};
        border-radius:2px;
        transition: all 0.35s ease;
    }}

    </style>
    """, unsafe_allow_html=True)

    # ── NAVBAR CONTAINER ─────────────────────
    st.markdown('<div class="nav">', unsafe_allow_html=True)

    left, center, right = st.columns([4, 4, 1])

    # ── BRAND ───────────────────────────────
    with left:

        l1, l2 = st.columns([1, 6])

        # CLEAN LOGO
        with l1:
            st.markdown(f"""
            <svg width="45" height="45" viewBox="0 0 24 24">
                <path d="M4 12L12 4L20 12L12 20Z" stroke="{text}" stroke-width="1.6"/>
                <circle cx="12" cy="12" r="2.2" fill="{text}"/>
            </svg>
            """, unsafe_allow_html=True)

        with l2:
            st.markdown(f"<div style='font-size:25px;font-weight:600'>{APP_NAME}</div>", unsafe_allow_html=True)
            st.markdown(f"<div style='font-size:20px;color:{muted}'>{TAGLINE}</div>", unsafe_allow_html=True)

    # ── CENTER NAV ───────────────────────────
    with center:

        c1, c2 = st.columns([1, 1])

        # DASHBOARD
        with c1:
            st.markdown(f'<div class="{"active" if active_page=="dashboard" else ""}">', unsafe_allow_html=True)
            if st.button("▦ Dashboard"):
                st.switch_page("app.py")
            st.markdown("</div>", unsafe_allow_html=True)

        # LEGAL HELP
        with c2:
            st.markdown(f'<div class="{"active" if active_page=="legal" else ""}">', unsafe_allow_html=True)
            if st.button("🛡 Legal Help"):
                st.switch_page("pages/2_Legal_Help_Guide.py")
            st.markdown("</div>", unsafe_allow_html=True)

        # ── SLIDER POSITION ──
        if active_page == "dashboard":
            st.markdown('<div class="slider" style="width:50%"></div>', unsafe_allow_html=True)
        else:
            st.markdown('<div class="slider" style="width:50%; margin-left:50%"></div>', unsafe_allow_html=True)

    st.markdown('</div>', unsafe_allow_html=True)

    return "dark"