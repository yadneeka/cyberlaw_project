import streamlit as st


def top_nav(active_page="dashboard"):

    APP_NAME = "CyberLytics"
    TAGLINE = "Turning cyberlaw data into actionable insights"

    # ── DESIGN TOKENS ─────────────────────────
    bg = "#0b1220"
    glass = "rgba(15, 23, 42, 0.85)"
    text = "#e6edf7"
    muted = "#94a3b8"
    accent = "#0cc4dd"
    border = "rgba(255,255,255,0.08)"

    st.markdown(f"""
    <style>

    @import url('https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600&display=swap');

    /* ── GLOBAL RESET ── */
    html, body {{
        background: {bg};
        color: {text};
        font-family: 'Inter', sans-serif;
        -webkit-text-size-adjust: 100%;
        -webkit-tap-highlight-color: transparent;
    }}

    /* ── STREAMLIT OVERRIDES ── */
    [data-testid="block-container"] {{
        padding: 0 1rem 4rem 1rem !important;
    }}
    @media (min-width: 768px) {{
        [data-testid="block-container"] {{
            padding: 0 2rem 4rem 2rem !important;
        }}
    }}

    /* ── FLOATING NAVBAR ── */
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
        -webkit-backdrop-filter: blur(16px);
        border: 1px solid {border};
        border-radius: 14px;
        transition: box-shadow 0.3s ease;
        min-height: 56px;
    }}
    .nav:hover {{
        box-shadow: 0 10px 30px rgba(0,0,0,0.4);
    }}

    /* ── BRAND BLOCK ── */
    .nav-brand {{
        display: flex;
        align-items: center;
        gap: 10px;
        flex-shrink: 0;
    }}
    .nav-brand-text {{
        display: flex;
        flex-direction: column;
    }}
    .nav-brand-name {{
        font-size: 18px;
        font-weight: 600;
        color: {text};
        line-height: 1.1;
    }}
    .nav-brand-tag {{
        font-size: 11px;
        color: {muted};
        display: none;          /* hidden on mobile */
    }}
    @media (min-width: 540px) {{
        .nav-brand-tag {{ display: block; }}
        .nav-brand-name {{ font-size: 20px; }}
    }}

    /* ── NAV LINKS (desktop) ── */
    .nav-links {{
        display: flex;
        align-items: center;
        gap: 4px;
    }}

    /* ── NAV BUTTON ── */
    div.stButton > button,
    button[data-testid="baseButton-secondary"],
    button[data-testid="baseButton-primary"] {{
        background: transparent !important;
        border: none !important;
        color: {muted} !important;
        font-size: 14px !important;
        font-weight: 500 !important;
        padding: 8px 14px !important;
        border-radius: 8px !important;
        transition: color 0.2s ease, background 0.2s ease !important;
        cursor: pointer !important;
        min-height: 40px !important;
        /* touch-friendly */
        min-width: 44px !important;
        touch-action: manipulation !important;
    }}
    div.stButton > button:hover {{
        color: {text} !important;
        background: rgba(255,255,255,0.06) !important;
    }}

    /* Active page button */
    .nav-active div.stButton > button {{
        color: {text} !important;
        font-weight: 600 !important;
        background: rgba(12, 196, 221, 0.12) !important;
        border: 1px solid rgba(12, 196, 221, 0.25) !important;
    }}

    /* ── SLIDER UNDERLINE ── */
    .nav-slider-wrap {{
        display: flex;
        height: 2px;
        margin-top: 4px;
    }}
    .slider {{
        height: 2px;
        width: 50%;
        background: {accent};
        border-radius: 2px;
        transition: margin-left 0.35s ease;
    }}

    /* ── HERO BAND MOBILE FIX ── */
    .hero-band h1 {{
        font-size: clamp(1.4rem, 5vw, 2.2rem) !important;
    }}
    .hero-band {{
        padding: clamp(1.2rem, 4vw, 2.6rem) clamp(1rem, 3vw, 2.2rem) !important;
    }}

    /* ── METRIC CARDS MOBILE ── */
    .metric-value {{
        font-size: clamp(1.8rem, 5vw, 2.8rem) !important;
    }}

    /* ── TABLES: horizontal scroll on mobile ── */
    [data-testid="stDataFrame"],
    .law-table-wrap {{
        overflow-x: auto !important;
        -webkit-overflow-scrolling: touch !important;
        max-width: 100% !important;
        display: block !important;
    }}
    .law-table {{
        min-width: 600px;   /* keep columns readable; scrolls on small screens */
    }}

    /* ── STEP CARDS: fix overflow on narrow screens ── */
    .step-card {{
        margin-left: 0.5rem !important;
        overflow: hidden !important;
    }}
    .step-num {{
        left: -0.8rem !important;
    }}

    /* ── HELP CARDS: ensure full-width on mobile ── */
    .help-card {{
        height: auto !important;
        margin-bottom: 0.8rem;
    }}

    /* ── EMERGENCY HOTLINE ROW: single column on mobile ── */
    .hotline-row {{
        display: flex;
        gap: 0.75rem;
        flex-wrap: wrap;
    }}
    .hotline-box {{
        flex: 1 1 140px;
        min-width: 130px;
    }}

    /* ── CALLOUTS: readable on narrow screens ── */
    .callout p {{
        font-size: clamp(0.8rem, 2.5vw, 0.88rem) !important;
    }}

    /* ── FOOTER: wrap on mobile ── */
    .dash-footer {{
        font-size: clamp(0.58rem, 1.8vw, 0.65rem) !important;
        padding: 1.2rem 0.5rem 2rem 0.5rem !important;
        word-break: break-word;
    }}

    /* ── SECTION TITLE: responsive ── */
    .section-title {{
        font-size: clamp(1.1rem, 3.5vw, 1.4rem) !important;
    }}

    /* ── PLOTLY: ensure charts don't overflow ── */
    .js-plotly-plot {{
        max-width: 100% !important;
        overflow: hidden !important;
    }}

    /* ── INSIGHT BOXES ── */
    .insight-box {{
        margin-bottom: 0.8rem;
    }}

    /* ── PROGRESS BARS: wrap labels ── */
    .prog-name {{
        font-size: clamp(0.73rem, 2vw, 0.82rem) !important;
        word-break: break-word;
    }}

    </style>
    """, unsafe_allow_html=True)

    # ── NAVBAR HTML ─────────────────────────────────────────────────────────────
    # Logo SVG + Brand name (always visible)
    # Nav buttons + active slider rendered via Streamlit columns
    # (Pure HTML nav buttons can't trigger st.switch_page)

    left_col, right_col = st.columns([5, 3])

    with left_col:
        st.markdown(f"""
        <div class="nav-brand" style="display:flex;align-items:center;gap:10px;padding:6px 0;">
            <svg width="36" height="36" viewBox="0 0 24 24" style="flex-shrink:0;">
                <path d="M4 12L12 4L20 12L12 20Z" stroke="{text}" stroke-width="1.6" fill="none"/>
                <circle cx="12" cy="12" r="2.2" fill="{text}"/>
            </svg>
            <div class="nav-brand-text">
                <div class="nav-brand-name">{APP_NAME}</div>
                <div class="nav-brand-tag">{TAGLINE}</div>
            </div>
        </div>
        """, unsafe_allow_html=True)

    with right_col:
        btn1_col, btn2_col = st.columns(2)

        with btn1_col:
            is_active = active_page == "dashboard"
            st.markdown(f'<div class="{"nav-active" if is_active else ""}">', unsafe_allow_html=True)
            if st.button("▦ Dashboard", key="nav_dashboard"):
                st.switch_page("app.py")
            st.markdown("</div>", unsafe_allow_html=True)

        with btn2_col:
            is_active = active_page == "legal"
            st.markdown(f'<div class="{"nav-active" if is_active else ""}">', unsafe_allow_html=True)
            if st.button("🛡 Legal Help", key="nav_legal"):
                st.switch_page("pages/2_Legal_Help_Guide.py")
            st.markdown("</div>", unsafe_allow_html=True)

        # Animated underline slider
        margin = "0%" if active_page == "dashboard" else "50%"
        st.markdown(f"""
        <div class="nav-slider-wrap">
            <div class="slider" style="margin-left:{margin};"></div>
        </div>
        """, unsafe_allow_html=True)

    return "dark"