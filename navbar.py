import streamlit as st


def top_nav(active_page="dashboard"):
    """
    CyberLytics top navbar.
    - Entire visual layout is pure CSS flexbox (flex-wrap:nowrap) — never
      stacks on mobile regardless of Streamlit's column behaviour.
    - Real st.buttons are rendered off-screen and repositioned over the HTML
      nav links via JavaScript, so clicks always fire the correct action.
    - Returns resolved theme string ("dark" | "light").
    """

    TAGLINE = "Turning cyberlaw data into actionable insights"

    # ── Theme init ─────────────────────────────────────────────────────────────
    if "theme" not in st.session_state:
        st.session_state.theme = "dark"
    theme = st.session_state.theme

    # ── Colour tokens ──────────────────────────────────────────────────────────
    if theme == "dark":
        BG, NAV_BG  = "#0b1220", "rgba(11,18,32,0.93)"
        TEXT, MUTED = "#e6edf7", "#94a3b8"
        ACCENT      = "#0cc4dd"
        BORDER      = "rgba(255,255,255,0.09)"
        BTN_ACT     = "rgba(12,196,221,0.13)"
        BTN_BD      = "rgba(12,196,221,0.30)"
        HOVER_BG    = "rgba(255,255,255,0.05)"
        PILL_BG     = "rgba(255,255,255,0.06)"
        PILL_ACT    = "rgba(255,255,255,0.13)"
        SUN_C, MOON_C = "#f4a261", "#e6edf7"
        DROP_BG     = "#1a2540"
    else:
        BG, NAV_BG  = "#f4f6fb", "rgba(244,246,251,0.93)"
        TEXT, MUTED = "#0f172a", "#64748b"
        ACCENT      = "#0891b2"
        BORDER      = "rgba(0,0,0,0.10)"
        BTN_ACT     = "rgba(8,145,178,0.10)"
        BTN_BD      = "rgba(8,145,178,0.30)"
        HOVER_BG    = "rgba(0,0,0,0.05)"
        PILL_BG     = "rgba(0,0,0,0.06)"
        PILL_ACT    = "rgba(0,0,0,0.11)"
        SUN_C, MOON_C = "#f59e0b", "#64748b"
        DROP_BG     = "#ffffff"

    is_dash  = active_page == "dashboard"
    is_legal = active_page == "legal"

    def _link_style(active):
        if active:
            return (f"color:{TEXT};background:{BTN_ACT};"
                    f"border:1px solid {BTN_BD};font-weight:600;")
        return f"color:{MUTED};border:1px solid transparent;"

    def _pill_style(active):
        return (f"background:{PILL_ACT};opacity:1;" if active
                else "background:transparent;opacity:0.50;")

    # ── SVGs ──────────────────────────────────────────────────────────────────
    logo = f"""<svg width="28" height="28" viewBox="0 0 32 32" fill="none">
  <rect x="2"  y="18" width="5" height="12" rx="1.5" fill="#e63946"/>
  <rect x="9"  y="12" width="5" height="18" rx="1.5" fill="#f4a261"/>
  <rect x="16" y="7"  width="5" height="23" rx="1.5" fill="{ACCENT}"/>
  <rect x="23" y="3"  width="5" height="27" rx="1.5" fill="{ACCENT}" opacity="0.40"/>
  <polyline points="4.5,24 11.5,18 18.5,11 25.5,6"
    stroke="white" stroke-width="1.5" fill="none"
    stroke-linecap="round" stroke-linejoin="round" opacity="0.45"/>
  <circle cx="25.5" cy="6" r="2.2" fill="white" opacity="0.85"/>
</svg>"""

    sun = f"""<svg width="14" height="14" viewBox="0 0 24 24" fill="none">
  <circle cx="12" cy="12" r="4" stroke="{SUN_C}" stroke-width="2"/>
  <path d="M12 2v2M12 20v2M4.22 4.22l1.42 1.42M18.36 18.36l1.42 1.42
           M2 12h2M20 12h2M4.22 19.78l1.42-1.42M18.36 5.64l1.42-1.42"
        stroke="{SUN_C}" stroke-width="2" stroke-linecap="round"/>
</svg>"""

    moon = f"""<svg width="14" height="14" viewBox="0 0 24 24" fill="none">
  <path d="M21 12.79A9 9 0 1 1 11.21 3 7 7 0 0 0 21 12.79z"
        stroke="{MOON_C}" stroke-width="2"
        stroke-linecap="round" stroke-linejoin="round"/>
</svg>"""

    # ── All CSS ────────────────────────────────────────────────────────────────
    st.markdown(f"""
<style>
@import url('https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700&display=swap');

/* ── App background ── */
html, body,
[data-testid="stAppViewContainer"],
[data-testid="stAppViewContainer"] > .main {{
    background-color: {BG} !important;
    color: {TEXT} !important;
    font-family: 'Inter', sans-serif;
    transition: background-color 0.3s, color 0.3s;
}}

/* ── Hide Streamlit chrome ── */
[data-testid="stSidebar"],
[data-testid="collapsedControl"] {{ display: none !important; }}
#MainMenu, footer, header {{ visibility: hidden; }}
[data-testid="stDecoration"] {{ display: none; }}

/* ── Block padding ── */
[data-testid="block-container"] {{
    padding: 0 0.75rem 4rem !important;
    max-width: 1440px !important;
}}
@media (min-width: 600px) {{
    [data-testid="block-container"] {{ padding: 0 1.25rem 4rem !important; }}
}}
@media (min-width: 1024px) {{
    [data-testid="block-container"] {{ padding: 0 2rem 4rem !important; }}
}}

/* ══════════════════════════════════════════
   NAVBAR — always a single horizontal row
   ══════════════════════════════════════════ */
#cl-nav {{
    position: sticky;
    top: 8px;
    z-index: 9999;
    display: flex;
    flex-direction: row;    /* ← key: never column */
    flex-wrap: nowrap;      /* ← key: never wraps  */
    align-items: center;
    justify-content: space-between;
    padding: 8px 12px;
    margin-bottom: 18px;
    background: {NAV_BG};
    backdrop-filter: blur(18px);
    -webkit-backdrop-filter: blur(18px);
    border: 1px solid {BORDER};
    border-radius: 14px;
    gap: 6px;
    box-sizing: border-box;
    transition: background 0.3s, border-color 0.3s;
}}

/* ── Brand ── */
#cl-brand {{
    display: flex;
    align-items: center;
    gap: 8px;
    flex-shrink: 0;
    min-width: 0;
}}
#cl-brand-text {{ display: flex; flex-direction: column; min-width: 0; }}
#cl-brand-name {{
    font-size: clamp(13px, 3.5vw, 17px);
    font-weight: 700;
    color: {TEXT};
    white-space: nowrap;
    letter-spacing: -0.3px;
    line-height: 1.15;
}}
#cl-brand-name span {{ color: {ACCENT}; }}
#cl-tagline {{
    font-size: clamp(9px, 1.6vw, 11px);
    color: {MUTED};
    white-space: nowrap;
    overflow: hidden;
    text-overflow: ellipsis;
    max-width: 30ch;
    display: block;
}}
/* Hide tagline on very small screens to save space */
@media (max-width: 440px) {{
    #cl-tagline {{ display: none; }}
}}

/* ── Centre group: links + slider ── */
#cl-centre {{
    display: flex;
    flex-direction: column;
    align-items: center;
    flex-shrink: 0;
}}
#cl-links {{
    display: flex;
    flex-direction: row;   /* row always */
    align-items: center;
    gap: 3px;
}}
.cl-link {{
    display: flex;
    align-items: center;
    gap: 5px;
    padding: clamp(4px,1.2vw,7px) clamp(7px,2vw,13px);
    border-radius: 9px;
    font-size: clamp(11px, 2vw, 13.5px);
    font-weight: 500;
    cursor: pointer;
    white-space: nowrap;
    transition: all 0.2s ease;
    text-decoration: none !important;
    box-sizing: border-box;
}}
.cl-link:hover {{
    color: {TEXT} !important;
    background: {HOVER_BG} !important;
}}

/* ── Animated underline slider ── */
#cl-slider-track {{
    height: 2px;
    width: 100%;
    margin-top: 3px;
    position: relative;
}}
#cl-slider {{
    position: absolute;
    height: 2px;
    width: 50%;
    background: {ACCENT};
    border-radius: 2px;
    transition: left 0.35s cubic-bezier(0.4,0,0.2,1);
    left: {'0%' if is_dash else '50%'};
}}

/* ── Theme pill ── */
#cl-pill {{
    display: flex;
    flex-direction: row;   /* row always */
    align-items: center;
    background: {PILL_BG};
    border: 1px solid {BORDER};
    border-radius: 20px;
    padding: 3px;
    gap: 2px;
    flex-shrink: 0;
}}
.cl-pill-opt {{
    display: flex;
    align-items: center;
    justify-content: center;
    width: clamp(24px,4.5vw,30px);
    height: clamp(20px,4vw,26px);
    border-radius: 16px;
    cursor: pointer;
    transition: background 0.2s, opacity 0.2s;
}}

/* ── Hide the raw Streamlit button row ── */
#cl-btn-row {{
    position: fixed !important;
    left: -9999px !important;
    top: -9999px !important;
    opacity: 0 !important;
    pointer-events: none !important;
    width: 1px !important;
    height: 1px !important;
    overflow: hidden !important;
}}

/* ── Selectbox / dropdown theme ── */
[data-testid="stSelectbox"] > div {{
    background: rgba(255,255,255,0.04) !important;
    border-color: {BORDER} !important;
    color: {TEXT} !important;
}}
div[data-baseweb="popover"] {{
    background-color: {DROP_BG} !important;
    border: 1px solid {BORDER} !important;
}}
div[data-baseweb="popover"] *,
div[data-baseweb="menu"] * {{ color: {TEXT} !important; }}
div[data-baseweb="menu"] li:hover {{
    background-color: {ACCENT} !important;
    color: white !important;
}}
</style>

<!-- ══ NAVBAR HTML ══ -->
<div id="cl-nav">

  <div id="cl-brand">
    {logo}
    <div id="cl-brand-text">
      <div id="cl-brand-name">Cyber<span>Lytics</span></div>
      <span id="cl-tagline">{TAGLINE}</span>
    </div>
  </div>

  <div id="cl-centre">
    <div id="cl-links">
      <a class="cl-link" id="cl-dash"
         style="{_link_style(is_dash)}">⊞&nbsp;Dashboard</a>
      <a class="cl-link" id="cl-legal"
         style="{_link_style(is_legal)}">🛡&nbsp;Legal&nbsp;Help</a>
    </div>
    <div id="cl-slider-track"><div id="cl-slider"></div></div>
  </div>

  <div id="cl-pill">
    <div class="cl-pill-opt" id="cl-sun"
         style="{_pill_style(theme == 'light')}" title="Light mode">{sun}</div>
    <div class="cl-pill-opt" id="cl-moon"
         style="{_pill_style(theme == 'dark')}" title="Dark mode">{moon}</div>
  </div>

</div>
""", unsafe_allow_html=True)

    # ── Streamlit buttons — rendered in a hidden div, positioned by JS ─────────
    with st.container():
        st.markdown('<div id="cl-btn-row">', unsafe_allow_html=True)
        c1, c2, c3, c4 = st.columns(4)
        with c1:
            if st.button("Dashboard", key="__nav_dash__"):
                if not is_dash:
                    st.switch_page("app.py")
        with c2:
            if st.button("Legal Help", key="__nav_legal__"):
                if not is_legal:
                    st.switch_page("pages/2_Legal_Help_Guide.py")
        with c3:
            if st.button("☀ Light", key="__theme_light__"):
                st.session_state.theme = "light"
                st.rerun()
        with c4:
            if st.button("☽ Dark", key="__theme_dark__"):
                st.session_state.theme = "dark"
                st.rerun()
        st.markdown('</div>', unsafe_allow_html=True)

    # ── JS: position the hidden buttons over their HTML counterparts ───────────
    st.markdown(f"""
<script>
(function() {{
    var PAIRS = [
        ['cl-dash',  '__nav_dash__'],
        ['cl-legal', '__nav_legal__'],
        ['cl-sun',   '__theme_light__'],
        ['cl-moon',  '__theme_dark__'],
    ];

    function findBtn(key) {{
        /* Streamlit renders button text as the key's label; find by aria-label
           or by iterating all buttons in the parent frame */
        var doc = window.parent.document;
        var all = doc.querySelectorAll('button[kind="secondary"], button');
        for (var b of all) {{
            if (b.getAttribute('data-testid') === key) return b;
            if (b.innerText) {{
                var t = b.innerText.trim();
                if (key === '__nav_dash__'    && t === 'Dashboard')  return b;
                if (key === '__nav_legal__'   && t === 'Legal Help') return b;
                if (key === '__theme_light__' && t.includes('Light')) return b;
                if (key === '__theme_dark__'  && t.includes('Dark'))  return b;
            }}
        }}
        return null;
    }}

    function overlay() {{
        var doc = window.parent.document;
        PAIRS.forEach(function(pair) {{
            var htmlEl = doc.getElementById(pair[0]);
            var btn    = findBtn(pair[1]);
            if (!htmlEl || !btn) return;

            var r = htmlEl.getBoundingClientRect();
            /* Create or reuse an invisible overlay div */
            var overId = 'cl-over-' + pair[0];
            var over = doc.getElementById(overId);
            if (!over) {{
                over = doc.createElement('div');
                over.id = overId;
                over.style.cssText = [
                    'position:fixed',
                    'z-index:99999',
                    'cursor:pointer',
                    'background:transparent',
                    'overflow:hidden',
                    '-webkit-tap-highlight-color:transparent',
                ].join(';');
                /* Clone the button inside the overlay */
                over.style.opacity = '0';
                over.appendChild(btn.cloneNode(true));
                doc.body.appendChild(over);

                /* Forward click to the real Streamlit button */
                over.addEventListener('click', function(e) {{
                    e.preventDefault();
                    btn.click();
                }});
                /* Touch support */
                over.addEventListener('touchend', function(e) {{
                    e.preventDefault();
                    btn.click();
                }}, {{passive: false}});
            }}
            over.style.left   = r.left   + 'px';
            over.style.top    = r.top    + 'px';
            over.style.width  = r.width  + 'px';
            over.style.height = r.height + 'px';
        }});
    }}

    /* Run immediately, after DOM settles, and on resize */
    setTimeout(overlay, 150);
    setTimeout(overlay, 500);
    setTimeout(overlay, 1200);
    window.parent.addEventListener('resize',      overlay, {{passive: true}});
    window.parent.addEventListener('scroll',      overlay, {{passive: true}});
    window.parent.addEventListener('orientationchange', function() {{
        setTimeout(overlay, 300);
    }});
}})();
</script>
""", unsafe_allow_html=True)

    return theme