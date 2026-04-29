"""
sidebar_component.py
────────────────────
Shared custom sidebar + light/dark mode for the Cyberlaw India dashboard.
Import and call inject_sidebar(active_page) at the TOP of each page,
before any other st.markdown() calls.

Usage:
    from sidebar_component import inject_sidebar, THEME
    inject_sidebar(active_page="dashboard")   # or "legal"

After calling inject_sidebar(), use THEME dict for Python-side colour logic.
"""

import streamlit as st
import streamlit.components.v1 as components

# ── Python-side colour constants (dark mode defaults, overridden by JS on client)
DARK = {
    "navy":   "#0a0f1e", "navy2":  "#111827", "navy3":  "#1a2540",
    "red":    "#e63946", "amber":  "#f4a261", "teal":   "#2dd4bf",
    "white":  "#f0f4ff", "muted":  "#8892aa", "border": "#1e2d4a",
    "green":  "#22c55e",
}
LIGHT = {
    "navy":   "#f4f6fb", "navy2":  "#e8edf5", "navy3":  "#dde4f0",
    "red":    "#c0202d", "amber":  "#b85c10", "teal":   "#0d9488",
    "white":  "#0f172a", "muted":  "#4a5568", "border": "#c5cfe0",
    "green":  "#16a34a",
}
# Python code always uses dark constants; JS swaps CSS vars on the client.
THEME = DARK


def inject_sidebar(active_page: str = "dashboard"):
    """
    Injects:
    1. CSS variables for dark/light mode + all shared styles
    2. Custom HTML sidebar (fixed, slides in/out)
    3. Hamburger button (top-left, always visible)
    4. Light/dark toggle (inside sidebar)
    5. JS that resizes Streamlit's main block when sidebar opens/closes
    6. Mobile / touch support
    """

    # Hide Streamlit's own sidebar completely
    hide_streamlit_sidebar = """
    <style>
      [data-testid="stSidebar"],
      [data-testid="collapsedControl"],
      button[kind="header"] { display: none !important; }
    </style>
    """
    st.markdown(hide_streamlit_sidebar, unsafe_allow_html=True)

    # ── Determine active nav items
    dash_active  = "nav-active" if active_page == "dashboard" else ""
    legal_active = "nav-active" if active_page == "legal"     else ""

    sidebar_html = f"""
<!-- ═══════════════════════════════════════════════════════════════════
     CYBERLAW INDIA — Custom Sidebar + Theme System
     ═══════════════════════════════════════════════════════════════════ -->
<style>
@import url('https://fonts.googleapis.com/css2?family=Playfair+Display:wght@400;700;900&family=IBM+Plex+Mono:wght@400;500&family=IBM+Plex+Sans:wght@300;400;500;600&display=swap');

/* ── CSS Variable sets ─────────────────────────────────────────────── */
:root {{
  --sb-w: 260px;
  /* DARK theme defaults */
  --navy:   #0a0f1e; --navy2:  #111827; --navy3:  #1a2540;
  --red:    #e63946; --amber:  #f4a261; --teal:   #2dd4bf;
  --white:  #f0f4ff; --muted:  #8892aa; --border: #1e2d4a;
  --green:  #22c55e;
  --page-bg:      var(--navy);
  --card-bg:      var(--navy3);
  --sidebar-bg:   var(--navy2);
  --text-primary: var(--white);
  --text-muted:   var(--muted);
  --border-col:   var(--border);
}}
[data-theme="light"] {{
  --navy:   #f4f6fb; --navy2:  #e8edf5; --navy3:  #dde4f0;
  --red:    #c0202d; --amber:  #b85c10; --teal:   #0d9488;
  --white:  #0f172a; --muted:  #4a5568; --border: #c5cfe0;
  --green:  #16a34a;
  --page-bg:      #f4f6fb;
  --card-bg:      #dde4f0;
  --sidebar-bg:   #e8edf5;
  --text-primary: #0f172a;
  --text-muted:   #4a5568;
  --border-col:   #c5cfe0;
}}

/* ── Global overrides ──────────────────────────────────────────────── */
html, body,
[data-testid="stAppViewContainer"],
[data-testid="stAppViewContainer"] > .main,
section.main {{
  background-color: var(--page-bg) !important;
  color: var(--text-primary) !important;
  transition: background-color 0.3s ease, color 0.3s ease;
}}
[data-testid="block-container"] {{
  padding: 0 2rem 4rem 2rem !important;
  max-width: 1400px !important;
  transition: margin-left 0.32s cubic-bezier(.4,0,.2,1);
}}
#MainMenu, footer, header {{ visibility: hidden; }}
[data-testid="stDecoration"] {{ display: none; }}

/* ── Hamburger button ──────────────────────────────────────────────── */
#sb-toggle {{
  position: fixed;
  top: 14px; left: 14px;
  z-index: 2001;
  width: 40px; height: 40px;
  border-radius: 8px;
  background: var(--navy3);
  border: 1px solid var(--border-col);
  cursor: pointer;
  display: flex; flex-direction: column;
  align-items: center; justify-content: center;
  gap: 5px;
  transition: background 0.2s, border-color 0.2s, transform 0.15s;
  box-shadow: 0 2px 12px rgba(0,0,0,0.25);
  -webkit-tap-highlight-color: transparent;
}}
#sb-toggle:hover {{ background: var(--navy2); border-color: var(--teal); transform: scale(1.06); }}
#sb-toggle.open  {{ border-color: var(--teal); background: rgba(45,212,191,0.1); }}
.sb-line {{
  width: 18px; height: 2px;
  background: var(--text-primary);
  border-radius: 2px;
  transition: transform 0.28s ease, opacity 0.2s ease, width 0.2s ease;
  transform-origin: center;
}}
#sb-toggle.open .sb-line:nth-child(1) {{ transform: translateY(7px) rotate(45deg); }}
#sb-toggle.open .sb-line:nth-child(2) {{ opacity: 0; width: 0; }}
#sb-toggle.open .sb-line:nth-child(3) {{ transform: translateY(-7px) rotate(-45deg); }}

/* ── Sidebar panel ─────────────────────────────────────────────────── */
#custom-sidebar {{
  position: fixed;
  top: 0; left: 0;
  height: 100vh;
  width: var(--sb-w);
  background: var(--sidebar-bg);
  border-right: 1px solid var(--border-col);
  z-index: 2000;
  transform: translateX(calc(-1 * var(--sb-w)));
  transition: transform 0.32s cubic-bezier(.4,0,.2,1), background 0.3s, border-color 0.3s;
  overflow-y: auto;
  overflow-x: hidden;
  display: flex; flex-direction: column;
  box-shadow: 4px 0 24px rgba(0,0,0,0.3);
  -webkit-overflow-scrolling: touch;
}}
#custom-sidebar.open {{
  transform: translateX(0);
}}
/* scrollbar */
#custom-sidebar::-webkit-scrollbar {{ width: 4px; }}
#custom-sidebar::-webkit-scrollbar-thumb {{ background: var(--border-col); border-radius: 2px; }}

/* ── Overlay (mobile) ──────────────────────────────────────────────── */
#sb-overlay {{
  display: none;
  position: fixed; inset: 0;
  background: rgba(0,0,0,0.5);
  z-index: 1999;
  opacity: 0;
  transition: opacity 0.3s ease;
}}
#sb-overlay.visible {{ display: block; }}
#sb-overlay.opaque  {{ opacity: 1; }}

/* ── Sidebar internals ─────────────────────────────────────────────── */
.sb-brand {{
  padding: 1.4rem 1.2rem 0.8rem;
  border-bottom: 1px solid var(--border-col);
}}
.sb-brand-tag {{
  font-family: 'IBM Plex Mono', monospace;
  font-size: 0.55rem; letter-spacing: 0.18em;
  color: var(--teal); text-transform: uppercase; margin-bottom: 0.35rem;
}}
.sb-brand-title {{
  font-family: 'Playfair Display', serif;
  font-size: 0.95rem; font-weight: 700;
  color: var(--text-primary); line-height: 1.3;
}}
.sb-section-label {{
  font-family: 'IBM Plex Mono', monospace;
  font-size: 0.55rem; letter-spacing: 0.18em; text-transform: uppercase;
  color: var(--text-muted); padding: 1rem 1.2rem 0.4rem;
}}
.sb-nav-item {{
  display: flex; align-items: center; gap: 0.75rem;
  padding: 0.65rem 1.2rem;
  border-left: 3px solid transparent;
  cursor: pointer;
  text-decoration: none;
  transition: background 0.18s, border-color 0.18s;
  -webkit-tap-highlight-color: transparent;
}}
.sb-nav-item:hover {{
  background: rgba(45,212,191,0.07);
  border-left-color: rgba(45,212,191,0.4);
}}
.sb-nav-item.nav-active {{
  background: rgba(45,212,191,0.1);
  border-left-color: var(--teal);
}}
.sb-nav-icon {{
  font-size: 1rem; width: 1.2rem; text-align: center; flex-shrink: 0;
}}
.sb-nav-text {{
  font-family: 'IBM Plex Sans', sans-serif;
  font-size: 0.82rem; color: var(--text-primary);
}}
.sb-nav-item.nav-active .sb-nav-text {{ color: var(--teal); font-weight: 600; }}
.sb-nav-sub {{
  font-family: 'IBM Plex Mono', monospace;
  font-size: 0.58rem; color: var(--text-muted); letter-spacing: 0.06em;
}}

/* Jump anchors (on same page) */
.sb-anchor-item {{
  display: flex; align-items: center; gap: 0.65rem;
  padding: 0.45rem 1.2rem 0.45rem 2.2rem;
  cursor: pointer;
  border-left: 3px solid transparent;
  transition: background 0.15s;
  -webkit-tap-highlight-color: transparent;
}}
.sb-anchor-item:hover {{ background: rgba(45,212,191,0.05); border-left-color: rgba(45,212,191,0.25); }}
.sb-anchor-dot {{
  width: 5px; height: 5px; border-radius: 50%;
  background: var(--teal); flex-shrink: 0; opacity: 0.6;
}}
.sb-anchor-text {{
  font-family: 'IBM Plex Mono', monospace;
  font-size: 0.66rem; color: var(--text-muted); letter-spacing: 0.04em;
}}

/* ── Theme toggle ──────────────────────────────────────────────────── */
.sb-theme-row {{
  display: flex; align-items: center; justify-content: space-between;
  padding: 0.8rem 1.2rem;
  border-top: 1px solid var(--border-col);
  margin-top: auto;
}}
.sb-theme-label {{
  font-family: 'IBM Plex Mono', monospace;
  font-size: 0.65rem; color: var(--text-muted); letter-spacing: 0.08em;
}}
.theme-toggle-wrap {{
  display: flex; align-items: center; gap: 0.5rem;
}}
.theme-icon {{ font-size: 0.85rem; }}
.theme-switch {{
  position: relative; width: 38px; height: 20px; cursor: pointer;
  -webkit-tap-highlight-color: transparent;
}}
.theme-switch input {{ opacity: 0; width: 0; height: 0; }}
.theme-slider {{
  position: absolute; inset: 0;
  background: var(--border-col);
  border-radius: 20px;
  transition: background 0.3s;
}}
.theme-slider::before {{
  content: '';
  position: absolute;
  height: 14px; width: 14px;
  left: 3px; bottom: 3px;
  background: var(--text-muted);
  border-radius: 50%;
  transition: transform 0.3s, background 0.3s;
}}
.theme-switch input:checked + .theme-slider {{ background: rgba(45,212,191,0.3); }}
.theme-switch input:checked + .theme-slider::before {{
  transform: translateX(18px);
  background: var(--teal);
}}

/* ── Emergency strip ────────────────────────────────────────────────── */
.sb-emergency {{
  margin: 0.6rem 1rem;
  background: rgba(230,57,70,0.08);
  border: 1px solid rgba(230,57,70,0.25);
  border-radius: 6px; padding: 0.7rem 0.9rem;
}}
.sb-emerg-title {{
  font-family: 'IBM Plex Mono', monospace;
  font-size: 0.55rem; letter-spacing: 0.12em; text-transform: uppercase;
  color: var(--red); margin-bottom: 0.45rem;
}}
.sb-emerg-line {{
  font-family: 'IBM Plex Mono', monospace;
  font-size: 0.7rem; color: var(--text-primary);
  display: flex; justify-content: space-between;
  margin-bottom: 0.2rem; line-height: 1.5;
}}
.sb-emerg-num {{ color: var(--red); font-weight: 700; }}

/* ── Meta ───────────────────────────────────────────────────────────── */
.sb-meta {{
  padding: 0.6rem 1.2rem 1rem;
  border-top: 1px solid var(--border-col);
}}
.sb-meta-text {{
  font-family: 'IBM Plex Mono', monospace;
  font-size: 0.58rem; color: var(--text-muted);
  letter-spacing: 0.04em; line-height: 1.75;
}}

/* ── Main content shift ─────────────────────────────────────────────── */
.main-shifted {{
  margin-left: var(--sb-w) !important;
}}

/* ── Mobile ─────────────────────────────────────────────────────────── */
@media (max-width: 768px) {{
  :root {{ --sb-w: 80vw; }}
  .main-shifted {{ margin-left: 0 !important; }}
  [data-testid="block-container"] {{ padding: 0 1rem 4rem 1rem !important; }}
}}

/* ── Shared component styles (both pages share these) ──────────────── */
@keyframes fadeSlideIn {{
  from {{ opacity: 0; transform: translateY(18px); }}
  to   {{ opacity: 1; transform: translateY(0); }}
}}
@keyframes pulse-border {{
  0%, 100% {{ border-left-color: var(--red); }}
  50%       {{ border-left-color: rgba(230,57,70,0.35); }}
}}
.hero-band {{
  background: linear-gradient(135deg, var(--navy3) 0%, var(--navy) 100%);
  border: 1px solid var(--border-col); border-left: 4px solid var(--red);
  padding: 2.6rem 2.2rem; margin-bottom: 2rem; border-radius: 6px;
  animation: fadeSlideIn 0.7s ease both;
  position: relative; overflow: hidden;
}}
.section-header {{
  display: flex; align-items: baseline; gap: 1rem;
  margin: 3rem 0 1.2rem 0; padding-bottom: 0.7rem;
  border-bottom: 1px solid var(--border-col);
}}
.section-number {{ font-family: 'IBM Plex Mono', monospace; font-size: 0.7rem; color: var(--red); letter-spacing: 0.1em; }}
.section-title  {{ font-family: 'Playfair Display', serif !important; font-size: 1.4rem; font-weight: 700; color: var(--text-primary); margin: 0; }}
.callout {{
  background: rgba(230,57,70,0.08); border-left: 4px solid var(--red);
  padding: 1rem 1.2rem; border-radius: 0 6px 6px 0; margin: 0.8rem 0;
  animation: pulse-border 3s ease infinite;
}}
.callout p {{ margin: 0; font-size: 0.88rem; color: var(--text-primary); line-height: 1.6; font-family: 'IBM Plex Sans', sans-serif !important; }}
.callout.teal  {{ background: rgba(45,212,191,0.07);  border-left-color: var(--teal);  animation: none; }}
.callout.amber {{ background: rgba(244,162,97,0.07);  border-left-color: var(--amber); animation: none; }}
.callout.green {{ background: rgba(34,197,94,0.07);   border-left-color: var(--green); animation: none; }}
.tag {{
  display: inline-block;
  background: rgba(230,57,70,0.12); border: 1px solid rgba(230,57,70,0.3);
  color: var(--red); font-family: 'IBM Plex Mono', monospace;
  font-size: 0.65rem; letter-spacing: 0.08em;
  padding: 0.22rem 0.65rem; border-radius: 3px;
  margin-right: 0.4rem; margin-bottom: 0.4rem;
}}
.metric-card {{
  background: var(--card-bg); border: 1px solid var(--border-col);
  border-top: 3px solid var(--red); padding: 1.6rem 1.4rem 1.2rem;
  border-radius: 6px; transition: transform 0.25s, box-shadow 0.25s, border-color 0.25s;
}}
.metric-card:hover {{ transform: translateY(-6px); box-shadow: 0 12px 32px rgba(0,0,0,0.25); }}
.metric-card.teal  {{ border-top-color: var(--teal); }}
.metric-card.amber {{ border-top-color: var(--amber); }}
.metric-label {{ font-family: 'IBM Plex Mono', monospace !important; font-size: 0.65rem; letter-spacing: 0.13em; text-transform: uppercase; color: var(--text-muted); margin-bottom: 0.5rem; }}
.metric-value {{ font-family: 'Playfair Display', serif !important; font-size: 2.8rem; font-weight: 900; color: var(--red); line-height: 1; margin-bottom: 0.4rem; }}
.metric-value.teal  {{ color: var(--teal); }}
.metric-value.amber {{ color: var(--amber); }}
.metric-value.white {{ color: var(--text-primary); }}
.metric-sub {{ font-family: 'IBM Plex Sans', sans-serif !important; font-size: 0.77rem; color: var(--text-muted); line-height: 1.4; }}
.insight-box {{ background: var(--card-bg); border: 1px solid var(--border-col); border-radius: 6px; padding: 1rem 1.2rem; margin-bottom: 0.6rem; transition: border-color 0.2s; }}
.insight-box:hover {{ border-color: var(--teal); }}
.insight-title {{ font-family: 'IBM Plex Mono', monospace; font-size: 0.65rem; text-transform: uppercase; letter-spacing: 0.1em; color: var(--teal); margin-bottom: 0.3rem; }}
.insight-text  {{ font-family: 'IBM Plex Sans', sans-serif; font-size: 0.83rem; color: var(--text-primary); line-height: 1.5; margin: 0; }}
.prog-row {{ margin-bottom: 0.7rem; }}
.prog-label {{ display: flex; justify-content: space-between; margin-bottom: 0.25rem; }}
.prog-name  {{ font-family: 'IBM Plex Sans', sans-serif; font-size: 0.82rem; color: var(--text-primary); }}
.prog-val   {{ font-family: 'IBM Plex Mono', monospace; font-size: 0.78rem; color: var(--teal); }}
.prog-track {{ background: var(--border-col); border-radius: 3px; height: 6px; overflow: hidden; }}
.prog-fill  {{ height: 100%; border-radius: 3px; }}
.dash-footer {{
  margin-top: 4rem; padding-top: 1.5rem; border-top: 1px solid var(--border-col);
  font-family: 'IBM Plex Mono', monospace; font-size: 0.65rem;
  color: var(--text-muted); letter-spacing: 0.06em; text-align: center;
}}
/* Legal page extras */
.hero-band.legal {{ border-left-color: var(--teal); }}
.step-card {{ background: var(--card-bg); border: 1px solid var(--border-col); border-radius: 8px; padding: 1.4rem 1.5rem; margin-bottom: 1.1rem; position: relative; transition: border-color 0.2s, transform 0.2s; }}
.step-card:hover {{ border-color: var(--teal); transform: translateX(4px); }}
.step-num {{ position: absolute; top: 1.2rem; left: -1rem; width: 2rem; height: 2rem; border-radius: 50%; background: var(--teal); color: var(--navy); font-family: 'IBM Plex Mono', monospace; font-weight: 700; font-size: 0.85rem; display: flex; align-items: center; justify-content: center; }}
.step-title {{ font-family: 'IBM Plex Mono', monospace; font-size: 0.7rem; text-transform: uppercase; letter-spacing: 0.1em; color: var(--teal); margin-bottom: 0.4rem; }}
.step-body {{ font-family: 'IBM Plex Sans', sans-serif; font-size: 0.85rem; color: var(--text-primary); line-height: 1.65; margin: 0; }}
.step-tip {{ margin-top: 0.6rem; padding: 0.5rem 0.8rem; background: rgba(45,212,191,0.07); border-left: 3px solid var(--teal); border-radius: 0 4px 4px 0; font-family: 'IBM Plex Sans', sans-serif; font-size: 0.78rem; color: var(--text-muted); }}
.help-card {{ background: var(--card-bg); border: 1px solid var(--border-col); border-top: 3px solid var(--teal); border-radius: 6px; padding: 1.4rem 1.3rem; height: 100%; transition: transform 0.2s, box-shadow 0.2s; }}
.help-card:hover {{ transform: translateY(-4px); box-shadow: 0 10px 28px rgba(0,0,0,0.2); }}
.help-card.amber {{ border-top-color: var(--amber); }}
.help-card.red   {{ border-top-color: var(--red); }}
.help-org   {{ font-family: 'Playfair Display', serif; font-size: 1rem; font-weight: 700; color: var(--text-primary); margin-bottom: 0.3rem; }}
.help-focus {{ font-family: 'IBM Plex Mono', monospace; font-size: 0.63rem; color: var(--teal); letter-spacing: 0.08em; text-transform: uppercase; margin-bottom: 0.7rem; }}
.help-desc  {{ font-family: 'IBM Plex Sans', sans-serif; font-size: 0.82rem; color: var(--text-muted); line-height: 1.55; margin-bottom: 0.9rem; }}
.help-contact {{ font-family: 'IBM Plex Mono', monospace; font-size: 0.8rem; color: var(--text-primary); }}
.help-contact a {{ color: var(--teal); text-decoration: none; }}
.hotline {{ display: inline-block; background: rgba(230,57,70,0.15); border: 1px solid rgba(230,57,70,0.4); color: var(--red); font-family: 'IBM Plex Mono', monospace; font-size: 0.95rem; font-weight: 700; padding: 0.3rem 0.8rem; border-radius: 4px; margin-top: 0.4rem; letter-spacing: 0.05em; }}
/* Plotly dark/light */
.js-plotly-plot {{ background: transparent !important; }}
[data-theme="light"] .js-plotly-plot .bg {{ fill: #f4f6fb !important; }}
/* Selectbox theming */
[data-testid="stSelectbox"] > div {{ background: var(--card-bg) !important; border-color: var(--border-col) !important; color: var(--text-primary) !important; }}
div[data-baseweb="popover"] {{ background-color: var(--navy3) !important; border: 1px solid var(--border-col) !important; }}
div[data-baseweb="popover"] *, div[data-baseweb="menu"] * {{ color: var(--text-primary) !important; }}
div[data-baseweb="menu"] li:hover {{ background-color: var(--red) !important; }}
/* Dataframe */
[data-testid="stDataFrame"] {{ border: 1px solid var(--border-col) !important; border-radius: 6px; overflow: hidden; }}
/* Top padding for hamburger button */
[data-testid="block-container"] {{ padding-top: 3.5rem !important; }}
</style>

<!-- ── Overlay ── -->
<div id="sb-overlay" onclick="closeSidebar()"></div>

<!-- ── Hamburger ── -->
<button id="sb-toggle" onclick="toggleSidebar()" aria-label="Toggle menu" aria-expanded="false">
  <div class="sb-line"></div>
  <div class="sb-line"></div>
  <div class="sb-line"></div>
</button>

<!-- ── Sidebar panel ── -->
<nav id="custom-sidebar" role="navigation" aria-label="Main navigation">

  <!-- Brand -->
  <div class="sb-brand">
    <div class="sb-brand-tag">⚖ Cyberlaw India</div>
    <div class="sb-brand-title">Digital Safety Laws<br>for Women in India</div>
  </div>

  <!-- Pages nav -->
  <div class="sb-section-label">Pages</div>
  <a class="sb-nav-item {dash_active}" href="/" onclick="closeSidebar()">
    <span class="sb-nav-icon">📊</span>
    <div>
      <div class="sb-nav-text">Main Dashboard</div>
      <div class="sb-nav-sub">Enforcement analytics</div>
    </div>
  </a>
  <a class="sb-nav-item {legal_active}" href="/Legal_Help_Guide" onclick="closeSidebar()">
    <span class="sb-nav-icon">🛡️</span>
    <div>
      <div class="sb-nav-text">Legal Help Guide</div>
      <div class="sb-nav-sub">Know your rights</div>
    </div>
  </a>

  <!-- Section anchors — shown depending on active page -->
  {"<!-- Dashboard anchors -->" if active_page == "dashboard" else ""}
  {"".join([f'''
  <div class="sb-anchor-item" onclick="scrollToSection('{sid}'); closeSidebar();">
    <div class="sb-anchor-dot"></div>
    <span class="sb-anchor-text">{label}</span>
  </div>''' for sid, label in [
    ("section-01","01 — Enforcement at a Glance"),
    ("section-02","02 — Platform Analysis"),
    ("section-03","03 — Crime Breakdown"),
    ("section-04","04 — Yearly Trend"),
    ("section-05","05 — Enforcement Gaps"),
    ("section-06","06 — Key Insights"),
    ("section-07","07 — Data Explorer"),
  ]]) if active_page == "dashboard" else ""}

  {"<!-- Legal anchors -->" if active_page == "legal" else ""}
  {"".join([f'''
  <div class="sb-anchor-item" onclick="scrollToSection('{sid}'); closeSidebar();">
    <div class="sb-anchor-dot" style="background:var(--teal)"></div>
    <span class="sb-anchor-text">{label}</span>
  </div>''' for sid, label in [
    ("section-08","08 — Know Your Rights"),
    ("section-09","09 — How to File"),
    ("section-10","10 — Get Help Now"),
  ]]) if active_page == "legal" else ""}

  <!-- Emergency strip -->
  <div style="margin-top: 1rem;">
    <div class="sb-section-label">Emergency Helplines</div>
    <div class="sb-emergency">
      <div class="sb-emerg-title">🆘 Call Now</div>
      <div class="sb-emerg-line"><span>National Emergency</span><span class="sb-emerg-num">112</span></div>
      <div class="sb-emerg-line"><span>Women's Helpline</span><span class="sb-emerg-num">1091</span></div>
      <div class="sb-emerg-line"><span>Cyber Cell</span><span class="sb-emerg-num">1930</span></div>
      <div class="sb-emerg-line"><span>NCW</span><span class="sb-emerg-num">7827-170-170</span></div>
    </div>
  </div>

  <!-- Spacer -->
  <div style="flex:1; min-height: 1rem;"></div>

  <!-- Meta -->
  <div class="sb-meta">
    <div class="sb-meta-text">
      SP47240003 · Yadneeka Jadhav<br>
      Guide: Prof. Kirti Garud<br>
      Research Project 2024–2026<br>
      <a href="https://github.com/yadneeka/cyberlaw_project"
         style="color:var(--teal);text-decoration:none;" target="_blank">GitHub ↗</a>
    </div>
  </div>

  <!-- Theme toggle -->
  <div class="sb-theme-row">
    <span class="sb-theme-label">Theme</span>
    <div class="theme-toggle-wrap">
      <span class="theme-icon">🌙</span>
      <label class="theme-switch" title="Toggle light/dark mode">
        <input type="checkbox" id="theme-checkbox" onchange="toggleTheme(this.checked)">
        <span class="theme-slider"></span>
      </label>
      <span class="theme-icon">☀️</span>
    </div>
  </div>

</nav>

<script>
(function() {{
  /* ── State ── */
  var isOpen = false;
  var isMobile = window.innerWidth <= 768;

  /* ── Restore theme from localStorage ── */
  var savedTheme = localStorage.getItem('cyberlaw-theme') || 'dark';
  applyTheme(savedTheme);
  var checkbox = document.getElementById('theme-checkbox');
  if (checkbox) checkbox.checked = (savedTheme === 'light');

  /* ── Sidebar toggle ── */
  window.toggleSidebar = function() {{
    isOpen ? closeSidebar() : openSidebar();
  }};

  window.openSidebar = function() {{
    isOpen = true;
    var sb = document.getElementById('custom-sidebar');
    var btn = document.getElementById('sb-toggle');
    var overlay = document.getElementById('sb-overlay');
    sb.classList.add('open');
    btn.classList.add('open');
    btn.setAttribute('aria-expanded', 'true');
    isMobile = window.innerWidth <= 768;
    if (isMobile) {{
      overlay.classList.add('visible');
      setTimeout(function(){{ overlay.classList.add('opaque'); }}, 10);
    }} else {{
      shiftMain(true);
    }}
  }};

  window.closeSidebar = function() {{
    isOpen = false;
    var sb = document.getElementById('custom-sidebar');
    var btn = document.getElementById('sb-toggle');
    var overlay = document.getElementById('sb-overlay');
    sb.classList.remove('open');
    btn.classList.remove('open');
    btn.setAttribute('aria-expanded', 'false');
    overlay.classList.remove('opaque');
    setTimeout(function(){{ overlay.classList.remove('visible'); }}, 300);
    shiftMain(false);
  }};

  function shiftMain(open) {{
    // Find Streamlit's block container and shift it
    var targets = [
      document.querySelector('[data-testid="block-container"]'),
      document.querySelector('section.main'),
      document.querySelector('.main'),
    ];
    var sbW = getComputedStyle(document.documentElement).getPropertyValue('--sb-w').trim();
    targets.forEach(function(el) {{
      if (!el) return;
      el.style.transition = 'margin-left 0.32s cubic-bezier(.4,0,.2,1)';
      el.style.marginLeft  = open ? sbW : '0px';
    }});
  }}

  /* ── Keyboard: Escape to close ── */
  document.addEventListener('keydown', function(e) {{
    if (e.key === 'Escape' && isOpen) closeSidebar();
  }});

  /* ── Touch swipe to close (mobile) ── */
  var touchStartX = 0;
  document.addEventListener('touchstart', function(e) {{
    touchStartX = e.changedTouches[0].screenX;
  }}, {{passive: true}});
  document.addEventListener('touchend', function(e) {{
    var dx = e.changedTouches[0].screenX - touchStartX;
    if (isOpen && dx < -60) closeSidebar();
    if (!isOpen && dx > 60 && touchStartX < 30) openSidebar();
  }}, {{passive: true}});

  /* ── Resize handler ── */
  window.addEventListener('resize', function() {{
    isMobile = window.innerWidth <= 768;
    if (isMobile && isOpen) {{
      document.getElementById('sb-overlay').classList.add('visible', 'opaque');
      shiftMain(false);
    }} else if (!isMobile && isOpen) {{
      document.getElementById('sb-overlay').classList.remove('visible', 'opaque');
      shiftMain(true);
    }}
  }});

  /* ── Section scroll ── */
  window.scrollToSection = function(sectionId) {{
    // Streamlit renders section headers as plain text inside divs;
    // we use a data attribute strategy: look for divs with matching id,
    // or fallback to text search on section-number spans.
    var el = document.getElementById(sectionId);
    if (!el) {{
      // Search by section-number text content
      var spans = document.querySelectorAll('.section-number');
      var prefix = sectionId.replace('section-', '').replace('-', ' —');
      for (var i = 0; i < spans.length; i++) {{
        if (spans[i].textContent.trim().startsWith(prefix.split('—')[0].trim())) {{
          el = spans[i].closest('.section-header') || spans[i].parentElement;
          break;
        }}
      }}
    }}
    if (el) {{
      el.scrollIntoView({{behavior: 'smooth', block: 'start'}});
    }}
  }};

  /* ── Theme toggle ── */
  window.toggleTheme = function(isLight) {{
    var theme = isLight ? 'light' : 'dark';
    applyTheme(theme);
    localStorage.setItem('cyberlaw-theme', theme);
  }};

  function applyTheme(theme) {{
    document.documentElement.setAttribute('data-theme', theme);
    // Also apply to Streamlit's root elements
    var roots = [document.body, document.documentElement,
                 document.querySelector('[data-testid="stAppViewContainer"]')];
    roots.forEach(function(el) {{
      if (el) el.setAttribute('data-theme', theme);
    }});
  }}

  /* Re-apply theme when Streamlit re-renders */
  var observer = new MutationObserver(function() {{
    var theme = localStorage.getItem('cyberlaw-theme') || 'dark';
    applyTheme(theme);
  }});
  observer.observe(document.body, {{childList: true, subtree: false}});

}})();
</script>
"""
    st.markdown(sidebar_html, unsafe_allow_html=True)
