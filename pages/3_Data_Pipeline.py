import streamlit as st
from navbar import top_nav

st.set_page_config(
    page_title="CyberLytics | Data Pipeline",
    page_icon="⚙️",
    layout="wide",
    initial_sidebar_state="collapsed",
)

top_nav("pipeline")


# ── Design tokens ──────────────────────────────────────────────────────────────
BG     = "#0b1220"
CARD   = "#111c35"
CARD2  = "#162040"
TEXT   = "#e6edf7"
MUTED  = "#94a3b8"
BORDER = "rgba(255,255,255,0.08)"
ACCENT = "#0cc4dd"
GREEN  = "#22c55e"
AMBER  = "#f4a261"
RED    = "#e63946"

# ── HERO CARD ───────────────────────────────────────────────────────────────
st.markdown(f"""
<div style="
background: linear-gradient(135deg, rgba(12,196,221,0.08), rgba(12,196,221,0.02));
border:1px solid {BORDER};
border-left:4px solid {ACCENT};
border-radius:14px;
padding:2rem 2.2rem;
margin-bottom:2.5rem;
position:relative;
overflow:hidden;
">

<div style="
font-family:'IBM Plex Mono',monospace;
font-size:.65rem;
letter-spacing:.12em;
color:{ACCENT};
margin-bottom:.6rem;
text-transform:uppercase;
">
DATA PIPELINE · MLflow · TRACEABILITY
</div>

<h1 style="
font-size:clamp(1.8rem,3vw,2.4rem);
margin:0 0 .6rem;
color:{TEXT};
font-weight:700;
">
From Raw Data → Verified Insights
</h1>

<p style="
color:{MUTED};
font-size:.95rem;
max-width:600px;
line-height:1.6;
margin-bottom:1rem;
">
A reproducible pipeline that transforms government cybercrime datasets into 
traceable, auditable insights using Python, MLflow, and Streamlit.
</p>

<div style="display:flex;gap:8px;flex-wrap:wrap;">
<span style="padding:6px 10px;border:1px solid {BORDER};border-radius:6px;font-size:.7rem;">Excel Dataset</span>
<span style="padding:6px 10px;border:1px solid {BORDER};border-radius:6px;font-size:.7rem;">Python Processing</span>
<span style="padding:6px 10px;border:1px solid {BORDER};border-radius:6px;font-size:.7rem;">MLflow Tracking</span>
<span style="padding:6px 10px;border:1px solid {BORDER};border-radius:6px;font-size:.7rem;">Git Versioning</span>
<span style="padding:6px 10px;border:1px solid {BORDER};border-radius:6px;font-size:.7rem;">Streamlit Dashboard</span>
</div>

</div>
""", unsafe_allow_html=True)

# ── Global CSS ─────────────────────────────────────────────────────────────────
st.markdown(f"""
<style>
@import url('https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700&family=IBM+Plex+Mono:wght@400;500&display=swap');

:root {{
  --bg:{BG}; --card:{CARD}; --card2:{CARD2};
  --text:{TEXT}; --muted:{MUTED}; --border:{BORDER};
  --accent:{ACCENT}; --green:{GREEN}; --amber:{AMBER}; --red:{RED};
}}

html,body,[data-testid="stAppViewContainer"],
[data-testid="stAppViewContainer"]>.main {{
  background:var(--bg) !important;
  color:var(--text) !important;
  font-family:'Inter',sans-serif;
}}
[data-testid="block-container"] {{
  padding:0 1.25rem 5rem !important;
  max-width:1200px !important;
}}
[data-testid="stMetric"] {{ display:none !important; }}

/* ── Animations ── */
@keyframes fadeUp {{
  from {{ opacity:0; transform:translateY(14px); }}
  to   {{ opacity:1; transform:translateY(0);    }}
}}
@keyframes pulseGlow {{
  0%,100% {{ box-shadow:0 0 0 0 rgba(12,196,221,0); }}
  50%     {{ box-shadow:0 0 20px 5px rgba(12,196,221,0.20); }}
}}
.s1 {{ animation:fadeUp .55s ease both; }}
.s2 {{ animation:fadeUp .55s .10s ease both; }}
.s3 {{ animation:fadeUp .55s .18s ease both; }}
.s4 {{ animation:fadeUp .55s .26s ease both; }}
.s5 {{ animation:fadeUp .55s .34s ease both; }}


/* ══ PIPELINE FLOW ══ */
.pipeline-wrap {{
  display:flex; flex-direction:row; align-items:stretch; overflow-x:auto;
  -webkit-overflow-scrolling:touch; padding-bottom:8px; margin-top: 1.5rem;
  gap:0;
}}
.pipe-step {{
  flex:1; min-width:120px; display:flex; flex-direction:column;
  align-items:center; position:relative; cursor:default;
}}
.pipe-step:not(:last-child)::after {{
  content:''; position:absolute; top:27px; right:-1px;
  width:calc(100% - 54px + 2px); height:2px;
  background:linear-gradient(90deg,var(--accent),rgba(12,196,221,.15));
  transform:translateX(27px); z-index:0; pointer-events:none;
}}
.pipe-icon {{
  width:54px; height:54px; border-radius:13px;
  display:flex; align-items:center; justify-content:center;
  position:relative; z-index:1; margin-bottom:13px;
  border:1px solid var(--border);
  transition:border-color .25s, transform .25s, box-shadow .25s;
}}
.pipe-step:hover .pipe-icon {{
  border-color:var(--accent); transform:translateY(-4px);
  animation:pulseGlow 2.5s ease infinite;
}}
.pipe-num  {{ font-family:'IBM Plex Mono',monospace; font-size:.59rem;
              letter-spacing:.1em; color:var(--accent); margin-bottom:4px; }}
.pipe-name {{ font-size:.81rem; font-weight:600; color:var(--text);
              text-align:center; margin-bottom:3px; }}
.pipe-desc {{ font-size:.7rem; color:var(--muted); text-align:center;
              line-height:1.45; max-width:108px; }}

/* ══ COMPONENT CARDS ══ */
.comp-card {{
  background:var(--card); border:1px solid var(--border); border-radius:12px;
  padding:1.35rem 1.25rem; height:100%; box-sizing:border-box; position:relative;
  overflow:hidden;
  transition:transform .22s, box-shadow .22s, border-color .22s;
}}
.comp-card::before {{
  content:''; position:absolute; top:0; left:0; right:0; height:2px;
  background:linear-gradient(90deg,var(--accent),transparent);
  opacity:0; transition:opacity .25s;
}}
.comp-card:hover {{
  transform:translateY(-5px);
  box-shadow:0 16px 40px rgba(0,0,0,.35),0 0 0 1px rgba(12,196,221,.18);
  border-color:rgba(12,196,221,.25);
}}
.comp-card:hover::before {{ opacity:1; }}
.comp-icon {{ width:34px; height:34px; border-radius:9px; display:flex;
              align-items:center; justify-content:center;
              font-size:1rem; margin-bottom:.9rem; }}
.comp-name {{ font-size:.88rem; font-weight:600; color:var(--text); margin-bottom:.4rem; }}
.comp-desc {{ font-size:.76rem; color:var(--muted); line-height:1.6; }}

/* ══ PROCESSING CARDS ══ */
.proc-card {{ background:var(--card); border:1px solid var(--border);
              border-radius:12px; padding:1.4rem 1.5rem; height:100%; }}
.proc-title {{ font-family:'IBM Plex Mono',monospace; font-size:.83rem;
               letter-spacing:.1em; text-transform:uppercase; color:var(--accent);
               margin-bottom:1rem; }}
.proc-item {{ display:flex; align-items:flex-start; gap:10px; padding:.52rem 0;
              border-bottom:1px solid var(--border); font-size:.83rem;
              color:var(--text); line-height:1.45; }}
.proc-item:last-child {{ border-bottom:none; }}
.proc-dot {{ width:5px; height:5px; border-radius:50%; background:var(--accent);
             flex-shrink:0; margin-top:7px; opacity:.65; }}

/* ══ KPI CARDS ══ */
.kpi-card {{
  background:var(--card); border:1px solid var(--border); border-radius:12px;
  padding:1.4rem 1.35rem; position:relative; overflow:hidden;
  transition:transform .22s, box-shadow .22s;
}}
.kpi-card:hover {{ transform:translateY(-4px); box-shadow:0 12px 32px rgba(0,0,0,.3); }}
.kpi-label {{ font-family:'IBM Plex Mono',monospace; font-size:.62rem;
              letter-spacing:.1em; text-transform:uppercase;
              color:var(--muted); margin-bottom:.5rem; }}
.kpi-value {{ font-size:2rem; font-weight:700; letter-spacing:-1px;
              line-height:1; margin-bottom:.4rem; }}
.kpi-sub   {{ font-size:.73rem; color:var(--muted); line-height:1.4; }}
.kpi-bar   {{ position:absolute; bottom:0; left:0; right:0; height:3px; border-radius:0 0 12px 12px; }}

/* ══ TRUST GRID ══ */
.trust-grid {{
  display:grid; grid-template-columns:repeat(auto-fit,minmax(255px,1fr)); gap:1rem;
}}
.trust-item {{
  background:var(--card); border:1px solid var(--border); border-radius:10px;
  padding:1.05rem 1.15rem; display:flex; align-items:flex-start; gap:11px;
  transition:border-color .2s, transform .2s;
}}
.trust-item:hover {{ border-color:rgba(34,197,94,.3); transform:translateX(3px); }}
.trust-check {{
  width:26px; height:26px; border-radius:7px;
  background:rgba(34,197,94,.12); border:1px solid rgba(34,197,94,.25);
  display:flex; align-items:center; justify-content:center;
  flex-shrink:0; font-size:.8rem; color:{GREEN};
}}
.trust-text {{ font-size:.83rem; color:var(--text); line-height:1.55; }}
.trust-text strong {{ color:{GREEN}; font-weight:600; }}

/* ══ CALLOUT ══ */
.callout-insight {{
  background:linear-gradient(135deg,rgba(12,196,221,.07),rgba(12,196,221,.02));
  border:1px solid rgba(12,196,221,.2); border-left:3px solid var(--accent);
  border-radius:10px; padding:1.2rem 1.4rem; margin-top:2.5rem;
  display:flex; gap:13px; align-items:flex-start;
}}
.callout-ico {{ font-size:.95rem; flex-shrink:0; margin-top:1px; opacity:.75; }}
.callout-body {{ font-size:.86rem; color:var(--text); line-height:1.65; }}
.callout-body strong {{ color:var(--accent); }}

/* ══ MOBILE ══ */
@media (max-width:640px) {{
  .pipe-step {{ min-width:95px; }}
  .pipe-icon {{ width:44px; height:44px; border-radius:11px; }}
  .pipe-step:not(:last-child)::after {{
    top:22px; width:calc(100% - 44px + 2px); transform:translateX(22px);
  }}
  .pipe-name {{ font-size:.72rem; }}
  .pipe-desc {{ font-size:.64rem; }}
  .kpi-value {{ font-size:1.65rem; }}
  .ph-title  {{ font-size:1.45rem; }}
}}

/* ══ SECTION HEADINGS (PROMINENT) ══ */
.sl {{
        font-family: 'IBM Plex Mono', monospace;
  font-size: 1.65rem;
  letter-spacing: 0.10em;
  text-transform: uppercase;
  color: var(--accent);
  margin-bottom: 6px;
  opacity: 0.9;
}}

.st {{
  font-size: 1.02rem;
  font-weight: 700;
  color: var(--text);
  margin-bottom: 1.4rem;
  position: relative;
  display: inline-block;
}}

/* subtle glow accent */
.st::after {{
  content: '';
  position: absolute;
  left: 0;
  bottom: -6px;
  width: 40%;
  height: 2px;
  background: linear-gradient(90deg, var(--accent), transparent);
  opacity: 0.6;
}}

/* spacing wrapper */
.section-wrap {{
  margin-top: 2.8rem;
}}</style>
""", unsafe_allow_html=True)


# ── PAGE HEADER ────────────────────────────────────────────────────────────────
st.markdown("""
<div class="ph s1">
  <div class="ph-label">11 — Infrastructure</div>
  <h1 class="ph-title">Data Pipeline</h1>
  <p class="ph-sub">End-to-end traceability from raw government datasets to
  NGO-accessible visualisations — reproducible, versioned, and auditable at
  every stage.</p>
</div>
""", unsafe_allow_html=True)


# ── PIPELINE FLOW ──────────────────────────────────────────────────────────────
st.markdown('<div class="s2"><div class="sl">Pipeline</div><div class="st">End-to-End Flow</div>', unsafe_allow_html=True)

pipe_steps = [
    ("01", "Excel",      "Structured MHA / NCRB source data",
     f"rgba(244,162,97,.15)", f"rgba(244,162,97,.4)",
     f'<svg width="22" height="22" viewBox="0 0 24 24" fill="none"><rect x="3" y="3" width="18" height="18" rx="2" stroke="{AMBER}" stroke-width="1.8"/><path d="M3 9h18M9 3v18" stroke="{AMBER}" stroke-width="1.8"/><path d="M7 13l2.5 2.5L16.5 8" stroke="{AMBER}" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round"/></svg>'),
    ("02", "Python",     "Clean · transform · validate",
     f"rgba(12,196,221,.12)", f"rgba(12,196,221,.35)",
     f'<svg width="22" height="22" viewBox="0 0 24 24" fill="none"><rect x="3" y="3" width="18" height="18" rx="3" stroke="{ACCENT}" stroke-width="1.8"/><path d="M8 12h8M12 8v8" stroke="{ACCENT}" stroke-width="1.8" stroke-linecap="round"/></svg>'),
    ("03", "MLflow",     "Track · log · reproduce",
     f"rgba(34,197,94,.12)", f"rgba(34,197,94,.35)",
     f'<svg width="22" height="22" viewBox="0 0 24 24" fill="none"><path d="M3 17l4-8 4 5 3-3 4 6" stroke="{GREEN}" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round"/><circle cx="7" cy="9" r="1.5" fill="{GREEN}"/><circle cx="11" cy="14" r="1.5" fill="{GREEN}"/><circle cx="14" cy="11" r="1.5" fill="{GREEN}"/><circle cx="18" cy="17" r="1.5" fill="{GREEN}"/></svg>'),
    ("04", "Git",        "Version · audit · deploy",
     f"rgba(230,57,70,.12)", f"rgba(230,57,70,.35)",
     f'<svg width="22" height="22" viewBox="0 0 24 24" fill="none"><circle cx="6" cy="6" r="2.5" stroke="{RED}" stroke-width="1.8"/><circle cx="18" cy="6" r="2.5" stroke="{RED}" stroke-width="1.8"/><circle cx="12" cy="18" r="2.5" stroke="{RED}" stroke-width="1.8"/><path d="M8.5 6h7M6 8.5v7M15.5 7.5l-3.5 8.5" stroke="{RED}" stroke-width="1.8" stroke-linecap="round"/></svg>'),
    ("05", "Dashboard",  "Visualise · publish · share",
     f"rgba(12,196,221,.12)", f"rgba(12,196,221,.35)",
     f'<svg width="22" height="22" viewBox="0 0 24 24" fill="none"><rect x="2" y="3" width="20" height="14" rx="2" stroke="{ACCENT}" stroke-width="1.8"/><path d="M8 17v3M16 17v3M5 20h14" stroke="{ACCENT}" stroke-width="1.8" stroke-linecap="round"/><rect x="5" y="7" width="3" height="6" rx="1" fill="{ACCENT}" opacity=".3"/><rect x="10" y="9" width="3" height="4" rx="1" fill="{ACCENT}" opacity=".5"/><rect x="15" y="6" width="3" height="7" rx="1" fill="{ACCENT}" opacity=".75"/></svg>'),
]

html = '<div class="pipeline-wrap">'
for num, name, desc, ibg, ibd, isvg in pipe_steps:
    html += f"""<div class="pipe-step">
      <div class="pipe-icon" style="background:{ibg};border-color:{ibd};">{isvg}</div>
      <div class="pipe-num">{num}</div>
      <div class="pipe-name">{name}</div>
      <div class="pipe-desc">{desc}</div>
    </div>"""
html += "</div></div>"
st.markdown(html, unsafe_allow_html=True)


# ── COMPONENT CARDS ────────────────────────────────────────────────────────────
st.markdown('<div class="s3" style="margin-top:2.8rem;"><div class="sl">Components</div><div class="st">Pipeline Layers</div></div>', unsafe_allow_html=True)

comps = [
    ("📊", f"rgba(244,162,97,.12)", "Excel Dataset",
     "Three-sheet workbook — platform stats, crime categories, verified source URLs. "
     "All records cross-checked against MHA and NCRB annual reports."),
    ("🐍", f"rgba(12,196,221,.10)", "Python / Pandas",
     "Data cleaning, type coercion, derived column computation "
     "(conviction_rate_pct). openpyxl read-only; no formula dependency."),
    ("📈", f"rgba(34,197,94,.10)", "MLflow Tracking",
     "Runs logged to SQLite backend under experiment _v3. "
     "Single-pass logging with pre-run cleanup prevents stale duplicates."),
    ("🔀", f"rgba(230,57,70,.10)", "Git / GitHub",
     "Full repo history per pipeline layer. Commit messages trace every "
     "data and model change for end-to-end auditability."),
    ("📡", f"rgba(12,196,221,.10)", "Streamlit Cloud",
     "Public NGO-accessible URL. Cache keyed to file mod-time ensures "
     "the dashboard always reflects the latest validated dataset."),
]

ccols = st.columns(5, gap="small")
for i, (icon, ibg, name, desc) in enumerate(comps):
    with ccols[i]:
        st.markdown(f"""
        <div class="comp-card">
          <div class="comp-icon" style="background:{ibg};">{icon}</div>
          <div class="comp-name">{name}</div>
          <div class="comp-desc">{desc}</div>
        </div>
        """, unsafe_allow_html=True)


# ── DATA PROCESSING ────────────────────────────────────────────────────────────
st.markdown('<div class="s4" style="margin-top:2.8rem;"><div class="sl">Processing</div><div class="st">Data Operations</div></div>', unsafe_allow_html=True)

pc1, pc2 = st.columns(2, gap="medium")

with pc1:
    st.markdown("""
    <div class="proc-card">
      <div class="proc-title">Ingestion &amp; Cleaning</div>
      <div class="proc-item"><div class="proc-dot"></div>Duplicate record removal across all sheets</div>
      <div class="proc-item"><div class="proc-dot"></div>Missing value imputation with source flagging</div>
      <div class="proc-item"><div class="proc-dot"></div>Type normalisation — dates, numerics, categoricals</div>
      <div class="proc-item"><div class="proc-dot"></div>Schema enforcement before downstream export</div>
    </div>
    """, unsafe_allow_html=True)

with pc2:
    st.markdown("""
    <div class="proc-card">
      <div class="proc-title">Feature Engineering</div>
      <div class="proc-item"><div class="proc-dot"></div>conviction_rate_pct computed in Python, not Excel</div>
      <div class="proc-item"><div class="proc-dot"></div>Platform-level and crime-type aggregation</div>
      <div class="proc-item"><div class="proc-dot"></div>Year-over-year delta columns for trend analysis</div>
      <div class="proc-item"><div class="proc-dot"></div>IPC → BNS 2023 section mapping and tagging</div>
    </div>
    """, unsafe_allow_html=True)


# ── MLFLOW KPIs ────────────────────────────────────────────────────────────────
st.markdown('<div class="s5" style="margin-top:2.8rem;"><div class="sl">MLflow</div><div class="st">Experiment Tracking</div></div>', unsafe_allow_html=True)

kpi_cols = st.columns(4, gap="medium")
kpis = [
    ("Active Experiment",  "v3",    "Cyberlaw_Case_Tracker_v3",  ACCENT),
    ("Data Quality Score", "97%",   "Across all 3 workbook sheets", GREEN),
    ("Runs Logged",        "15+",   "Clean, deduplicated entries",  AMBER),
    ("Backend Store",      "SQLite","D:\\cyberlaw_proj\\mlflow.db", MUTED),
]

for i, (label, val, sub, color) in enumerate(kpis):
    with kpi_cols[i]:
        st.markdown(f"""
        <div class="kpi-card">
          <div class="kpi-label">{label}</div>
          <div class="kpi-value" style="color:{color};">{val}</div>
          <div class="kpi-sub">{sub}</div>
          <div class="kpi-bar" style="background:{color};opacity:.30;"></div>
        </div>
        """, unsafe_allow_html=True)


# ── SYSTEM INTEGRITY ──────────────────────────────────────────────────────────
st.markdown('<div style="margin-top:2.8rem;"><div class="sl">Guarantees</div><div class="st">System Integrity Layer</div>', unsafe_allow_html=True)

trust = [
    ("All records sourced exclusively from <strong>MHA Annual Reports</strong>, NCRB Crime in India, NCRP Parliamentary Data, and CERT-In advisories."),
    ("<strong>No Excel formula dependency</strong> — all derived columns recomputed in Python to eliminate openpyxl silent read errors."),
    ("<strong>MLflow experiment versioning</strong> (suffix _v3) avoids soft-delete conflicts; each run logged in a single pass to prevent duplicates."),
    ("<strong>File modification time</strong> used as Streamlit cache key — the dashboard always reflects the latest validated dataset."),
    ("<strong>Git commit history</strong> provides a full audit trail from raw ingestion to the published dashboard."),
    ("All source URLs <strong>verified and stored</strong> in sheet 3 — NGOs can inspect primary evidence without leaving the interface."),
]

thtml = '<div class="trust-grid">'
for item in trust:
    thtml += f'<div class="trust-item"><div class="trust-check">✓</div><div class="trust-text">{item}</div></div>'
thtml += "</div></div>"
st.markdown(thtml, unsafe_allow_html=True)


# ── CLOSING CALLOUT ────────────────────────────────────────────────────────────
st.markdown(f"""
<div class="callout-insight">
  <div class="callout-ico">◈</div>
  <div class="callout-body">
    <strong>Pipeline design principle:</strong> Every transformation is explicit,
    every source is cited, and every run is logged — so any finding surfaced by
    the dashboard can be traced back, step by step, to a specific government
    document. This makes the research defensible in both academic and policy contexts.
  </div>
</div>
""", unsafe_allow_html=True)

# ── FOOTER ─────────────────────────────────────────────────────────────────────
st.markdown(f"""
<div style="margin-top:4rem;padding-top:1.5rem;border-top:1px solid {BORDER};
  font-family:'IBM Plex Mono',monospace;font-size:.63rem;color:{MUTED};
  letter-spacing:.05em;text-align:center;line-height:2;">
  DATA SOURCES: MHA Annual Reports &nbsp;·&nbsp; NCRB Crime in India 2024
  &nbsp;·&nbsp; NCRP Parliamentary Data &nbsp;·&nbsp; CERT-In Advisories
  <br>
  Yadneeka Sanjay Jadhav (SP47240003) &nbsp;·&nbsp;
  Guide: Prof. Kirti Garud &nbsp;·&nbsp; Research Project 2024–2026
</div>
""", unsafe_allow_html=True)