import streamlit as st
import pandas as pd
import plotly.graph_objects as go
from plotly.subplots import make_subplots
from sidebar_component import inject_sidebar

# Call this immediately after st.set_page_config
inject_sidebar(active_page="dashboard") # or "legal guide"

st.set_page_config(layout="wide", initial_sidebar_state="expanded")

# ── Page config ────────────────────────────────────────────────────────────────
st.set_page_config(
    page_title="Digital Safety Laws for Women in India",
    page_icon="⚖️",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# ── Global CSS ─────────────────────────────────────────────────────────────────
st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=Playfair+Display:wght@400;700;900&family=IBM+Plex+Mono:wght@400;500&family=IBM+Plex+Sans:wght@300;400;500;600&display=swap');

:root {
    --navy:   #0a0f1e;
    --navy2:  #111827;
    --navy3:  #1a2540;
    --red:    #e63946;
    --amber:  #f4a261;
    --teal:   #2dd4bf;
    --white:  #f0f4ff;
    --muted:  #8892aa;
    --border: #1e2d4a;
}

html, body, [data-testid="stAppViewContainer"] {
    background-color: var(--navy) !important;
    color: var(--white) !important;
}
[data-testid="stAppViewContainer"] > .main { background-color: var(--navy) !important; }
[data-testid="block-container"] { padding: 0 2rem 4rem 2rem !important; max-width: 1400px !important; }
#MainMenu, footer, header { visibility: hidden; }
[data-testid="stDecoration"] { display: none; }

@keyframes fadeSlideIn {
    from { opacity: 0; transform: translateY(18px); }
    to   { opacity: 1; transform: translateY(0); }
}
.hero-band {
    background: linear-gradient(135deg, #0d1628 0%, #0a0f1e 100%);
    border: 1px solid var(--border);
    border-left: 4px solid var(--red);
    padding: 2.6rem 2.2rem;
    margin-bottom: 2rem;
    border-radius: 6px;
    animation: fadeSlideIn 0.7s ease both;
    position: relative;
    overflow: hidden;
}
.hero-band::after {
    content: '⚖';
    position: absolute; right: 2rem; top: 50%;
    transform: translateY(-50%);
    font-size: 7rem; opacity: 0.04; pointer-events: none;
}

@keyframes cardIn {
    from { opacity: 0; transform: translateY(12px); }
    to   { opacity: 1; transform: translateY(0); }
}
.metric-card {
    background: var(--navy3);
    border: 1px solid var(--border);
    border-top: 3px solid var(--red);
    padding: 1.6rem 1.4rem 1.2rem;
    border-radius: 6px;
    position: relative; overflow: hidden;
    transition: transform 0.25s ease, box-shadow 0.25s ease, border-color 0.25s ease;
    animation: cardIn 0.5s ease both;
    cursor: default;
}
.metric-card:hover {
    transform: translateY(-6px);
    box-shadow: 0 12px 32px rgba(0,0,0,0.4);
    border-color: var(--muted);
}
.metric-card::before {
    content: '';
    position: absolute; top: 0; left: 0; right: 0; bottom: 0;
    background: linear-gradient(135deg, rgba(230,57,70,0.05) 0%, transparent 60%);
    pointer-events: none;
}
.metric-card.teal  { border-top-color: var(--teal); }
.metric-card.teal::before  { background: linear-gradient(135deg, rgba(45,212,191,0.06) 0%, transparent 60%); }
.metric-card.amber { border-top-color: var(--amber); }
.metric-card.amber::before { background: linear-gradient(135deg, rgba(244,162,97,0.06) 0%, transparent 60%); }

.metric-label {
    font-family: 'IBM Plex Mono', monospace !important;
    font-size: 0.65rem; letter-spacing: 0.13em; text-transform: uppercase;
    color: var(--muted); margin-bottom: 0.5rem;
}
.metric-value {
    font-family: 'Playfair Display', serif !important;
    font-size: 2.8rem; font-weight: 900; color: var(--red);
    line-height: 1; margin-bottom: 0.4rem;
}
.metric-value.teal  { color: var(--teal); }
.metric-value.amber { color: var(--amber); }
.metric-value.white { color: var(--white); }
.metric-sub {
    font-family: 'IBM Plex Sans', sans-serif !important;
    font-size: 0.77rem; color: var(--muted); line-height: 1.4;
}

.section-header {
    display: flex; align-items: baseline; gap: 1rem;
    margin: 3rem 0 1.2rem 0; padding-bottom: 0.7rem;
    border-bottom: 1px solid var(--border);
}
.section-number { font-family: 'IBM Plex Mono', monospace; font-size: 0.7rem; color: var(--red); letter-spacing: 0.1em; }
.section-title  { font-family: 'Playfair Display', serif !important; font-size: 1.4rem; font-weight: 700; color: var(--white); margin: 0; }

@keyframes pulse-border {
    0%, 100% { border-left-color: var(--red); }
    50%       { border-left-color: rgba(230,57,70,0.4); }
}
.callout {
    background: rgba(230,57,70,0.08); border-left: 4px solid var(--red);
    padding: 1rem 1.2rem; border-radius: 0 6px 6px 0; margin: 0.8rem 0;
    animation: pulse-border 3s ease infinite;
}
.callout p { margin: 0; font-size: 0.88rem; color: var(--white); line-height: 1.6; font-family: 'IBM Plex Sans', sans-serif !important; }
.callout.teal  { background: rgba(45,212,191,0.07);  border-left-color: var(--teal);  animation: none; }
.callout.amber { background: rgba(244,162,97,0.07);  border-left-color: var(--amber); animation: none; }

.tag {
    display: inline-block;
    background: rgba(230,57,70,0.12); border: 1px solid rgba(230,57,70,0.3);
    color: var(--red); font-family: 'IBM Plex Mono', monospace;
    font-size: 0.65rem; letter-spacing: 0.08em;
    padding: 0.22rem 0.65rem; border-radius: 3px;
    margin-right: 0.4rem; margin-bottom: 0.4rem;
    transition: background 0.2s, color 0.2s;
}
.tag:hover { background: rgba(230,57,70,0.25); color: var(--white); }

.insight-box {
    background: var(--navy3); border: 1px solid var(--border);
    border-radius: 6px; padding: 1rem 1.2rem; margin-bottom: 0.6rem;
    transition: border-color 0.2s;
}
.insight-box:hover { border-color: var(--teal); }
.insight-title { font-family: 'IBM Plex Mono', monospace; font-size: 0.65rem; text-transform: uppercase; letter-spacing: 0.1em; color: var(--teal); margin-bottom: 0.3rem; }
.insight-text  { font-family: 'IBM Plex Sans', sans-serif; font-size: 0.83rem; color: var(--white); line-height: 1.5; margin: 0; }

.prog-row { margin-bottom: 0.7rem; }
.prog-label { display: flex; justify-content: space-between; margin-bottom: 0.25rem; }
.prog-name  { font-family: 'IBM Plex Sans', sans-serif; font-size: 0.82rem; color: var(--white); }
.prog-val   { font-family: 'IBM Plex Mono', monospace; font-size: 0.78rem; color: var(--teal); }
.prog-track { background: var(--border); border-radius: 3px; height: 6px; overflow: hidden; }
.prog-fill  { height: 100%; border-radius: 3px; }

.dash-footer {
    margin-top: 4rem; padding-top: 1.5rem;
    border-top: 1px solid var(--border);
    font-family: 'IBM Plex Mono', monospace; font-size: 0.65rem;
    color: var(--muted); letter-spacing: 0.06em; text-align: center;
}

[data-testid="stSidebar"] { background: var(--navy2) !important; border-right: 1px solid var(--border) !important; }
[data-testid="stSelectbox"] > div { background: var(--navy3) !important; border-color: var(--border) !important; }
.js-plotly-plot { background: transparent !important; }
div[data-baseweb="popover"] { background-color: #1a2540 !important; border: 1px solid #1e2d4a !important; }
div[data-baseweb="popover"] *, div[data-baseweb="menu"] * { color: #ffffff !important; }
div[data-baseweb="menu"] li:hover { background-color: #e63946 !important; }
</style>
""", unsafe_allow_html=True)


# ── Data loading ───────────────────────────────────────────────────────────────
EXCEL_FILE = "Cyberlaw_Women_India_Verified_2024_2026.xlsx"

def _get_file_mtime():
    import os
    try:    return os.path.getmtime(EXCEL_FILE)
    except: return 0

@st.cache_data
def load_data(_mtime):
    df = pd.read_excel(EXCEL_FILE, sheet_name="Platform_Case_Data")
    df["conviction_rate_pct"]   = (df["cases_convicted"]     / df["cases_reported"] * 100).round(2)
    df["chargesheets_rate_pct"] = (df["cases_chargesheeted"] / df["cases_reported"] * 100).round(2)
    trend = pd.read_excel(EXCEL_FILE, sheet_name="NCRP_Yearly_Trend")
    platform_summary = df.groupby("platform").agg(
        cases_reported      =("cases_reported",    "sum"),
        cases_chargesheeted =("cases_chargesheeted","sum"),
        cases_convicted     =("cases_convicted",   "sum"),
        conviction_rate     =("conviction_rate_pct","mean")
    ).round(2).reset_index().sort_values("conviction_rate", ascending=False)
    return df, trend, platform_summary

df, trend, platform_summary = load_data(_mtime=_get_file_mtime())

# ── Colour constants ───────────────────────────────────────────────────────────
NAVY   = "#0a0f1e";  NAVY3  = "#1a2540";  BORDER = "#1e2d4a"
RED    = "#e63946";  AMBER  = "#f4a261";  TEAL   = "#2dd4bf"
WHITE  = "#f0f4ff";  MUTED  = "#8892aa"

BASE_LAYOUT = dict(
    paper_bgcolor="rgba(0,0,0,0)", plot_bgcolor="rgba(0,0,0,0)",
    font=dict(family="IBM Plex Sans", color=WHITE, size=12),
    margin=dict(l=10, r=10, t=40, b=10),
    xaxis=dict(gridcolor=BORDER, linecolor=BORDER, tickfont=dict(color=MUTED, size=11)),
    yaxis=dict(gridcolor=BORDER, linecolor=BORDER, tickfont=dict(color=MUTED, size=11)),
    legend=dict(bgcolor="rgba(0,0,0,0)", font=dict(color=MUTED)),
)

total_reported  = df["cases_reported"].sum()
total_charged   = df["cases_chargesheeted"].sum()
total_convicted = df["cases_convicted"].sum()
mean_conv       = df["conviction_rate_pct"].mean()
charge_rate     = total_charged / total_reported * 100
n_platforms     = df["platform"].nunique()
n_crimes        = df["crime_category"].nunique()


# ══════════════════════════════════════════════════════════════════════════════
# HERO
# ══════════════════════════════════════════════════════════════════════════════
st.markdown(f"""
<div class="hero-band">
    <div style="font-family:'IBM Plex Mono',monospace;font-size:0.66rem;letter-spacing:0.16em;
                color:#8892aa;text-transform:uppercase;margin-bottom:0.7rem;">
        Research Dashboard &nbsp;·&nbsp; SP47240003 &nbsp;·&nbsp; 2024–2026
    </div>
    <h1 style="font-family:'Playfair Display',serif;font-size:2.2rem;font-weight:900;
               color:#f0f4ff;margin:0 0 0.6rem 0;line-height:1.2;">
        Effectiveness of Digital Safety Laws<br>for Women in India
    </h1>
    <p style="font-family:'IBM Plex Sans',sans-serif;color:#8892aa;font-size:0.9rem;
              margin:0 0 1.1rem 0;max-width:700px;line-height:1.7;">
        A data-driven evaluation of cybercrime enforcement outcomes across
        <strong style="color:#f0f4ff;">{n_platforms} platforms</strong> and
        <strong style="color:#f0f4ff;">{n_crimes} crime categories</strong>.
        All data sourced exclusively from MHA Annual Reports, NCRB Crime in India,
        NCRP Parliamentary Data, and CERT-In advisories.
    </p>
    <div>
        <span class="tag">IT Act 2000</span>
        <span class="tag">IPC / BNS 2023</span>
        <span class="tag">{total_reported:,} Cases</span>
        <span class="tag">{n_platforms} Platforms</span>
        <span class="tag">2024–2025</span>
    </div>
</div>
""", unsafe_allow_html=True)


# ══════════════════════════════════════════════════════════════════════════════
# SECTION 1 — METRIC CARDS
# ══════════════════════════════════════════════════════════════════════════════
st.markdown("""
<div class="section-header">
    <span class="section-number">01 —</span>
    <p class="section-title">Enforcement at a Glance</p>
</div>""", unsafe_allow_html=True)

c1, c2, c3, c4, c5 = st.columns(5)
with c1:
    st.markdown(f"""<div class="metric-card">
        <div class="metric-label">Mean Conviction Rate</div>
        <div class="metric-value">{mean_conv:.2f}%</div>
        <div class="metric-sub">Across all platforms<br>& crime categories</div>
    </div>""", unsafe_allow_html=True)
with c2:
    st.markdown(f"""<div class="metric-card amber">
        <div class="metric-label">Chargesheet Rate</div>
        <div class="metric-value amber">{charge_rate:.1f}%</div>
        <div class="metric-sub">Cases reaching<br>prosecution stage</div>
    </div>""", unsafe_allow_html=True)
with c3:
    st.markdown(f"""<div class="metric-card teal">
        <div class="metric-label">Total Cases Reported</div>
        <div class="metric-value teal">{total_reported:,}</div>
        <div class="metric-sub">Across {n_platforms} platforms<br>2024–2025</div>
    </div>""", unsafe_allow_html=True)
with c4:
    st.markdown(f"""<div class="metric-card">
        <div class="metric-label">Total Convictions</div>
        <div class="metric-value white">{total_convicted:,}</div>
        <div class="metric-sub">Out of {total_reported:,}<br>cases reported</div>
    </div>""", unsafe_allow_html=True)
with c5:
    st.markdown(f"""<div class="metric-card amber">
        <div class="metric-label">NCRP Growth 2020–25</div>
        <div class="metric-value amber">+245%</div>
        <div class="metric-sub">Women-targeted complaints<br>5-year rise</div>
    </div>""", unsafe_allow_html=True)

st.markdown("""
<div class="callout" style="margin-top:1.2rem;">
<p><strong style="color:#e63946;">Key Finding:</strong>
Fewer than <strong style="color:#f0f4ff;">3 in every 100</strong> reported cybercrime cases against women
result in a conviction. The chargesheet rate (15.9%) is 7× the conviction rate (2.24%) —
pointing squarely at <strong style="color:#f0f4ff;">prosecution and judicial bottlenecks</strong>,
not investigative failure.</p>
</div>""", unsafe_allow_html=True)


# ══════════════════════════════════════════════════════════════════════════════
# SECTION 2 — PLATFORM ANALYSIS
# ══════════════════════════════════════════════════════════════════════════════
st.markdown("""
<div class="section-header">
    <span class="section-number">02 —</span>
    <p class="section-title">Platform-Level Enforcement</p>
</div>""", unsafe_allow_html=True)

col_left, col_right = st.columns([3, 2], gap="large")

with col_left:
    ps = platform_summary.sort_values("conviction_rate")
    colors = [RED if v < 1.5 else AMBER if v < 2.5 else TEAL for v in ps["conviction_rate"]]
    fig = go.Figure()
    fig.add_trace(go.Bar(
        x=ps["conviction_rate"], y=ps["platform"],
        orientation="h",
        marker=dict(color=colors, line=dict(width=0)),
        text=[f"{v:.2f}%" for v in ps["conviction_rate"]],
        textposition="outside",
        textfont=dict(color=WHITE, size=11, family="IBM Plex Mono"),
        hovertemplate="<b>%{y}</b><br>Conviction Rate: %{x:.2f}%<extra></extra>",
    ))
    fig.add_vline(x=mean_conv, line_dash="dot", line_color=MUTED, line_width=1.5,
                  annotation_text=f"Mean {mean_conv:.2f}%",
                  annotation_font_color=MUTED, annotation_font_size=10,
                  annotation_position="top right")
    layout = dict(**BASE_LAYOUT)
    layout.update(
        height=420,
        title=dict(text="Conviction Rate by Platform  (hover for details)",
                   font=dict(color=MUTED, size=12, family="IBM Plex Mono"), x=0),
        xaxis=dict(gridcolor=BORDER, linecolor=BORDER, tickfont=dict(color=MUTED, size=10),
                   title=dict(text="Conviction Rate (%)", font=dict(color=MUTED, size=10)), range=[0, 7]),
        yaxis=dict(gridcolor="rgba(0,0,0,0)", linecolor=BORDER, tickfont=dict(color=WHITE, size=11)),
        margin=dict(l=10, r=70, t=45, b=30),
    )
    fig.update_layout(**layout)
    st.plotly_chart(fig, use_container_width=True, config={"displayModeBar": False})

with col_right:
    ps2 = platform_summary.copy().reset_index(drop=True)
    ps2["short_name"] = (ps2["platform"]
                         .str.replace("Multiple Platforms", "Multi-Platform")
                         .str.replace(" / ", "/"))
    max_cases = ps2["cases_reported"].max()
    sizes_map = {row["platform"]: (row["cases_reported"] / max_cases * 55 + 12)
                 for _, row in ps2.iterrows()}

    # ── Per-platform label offsets (ax, ay) chosen to avoid overlaps
    # ax/ay are pixel offsets from the marker centre; arrowhead=0 → clean line
    label_offsets = {
        "WhatsApp":           (45, -30),
        "Facebook":           (45,  25),
        "Instagram":          (-55, -25),
        "Telegram":           (45,   0),
        "Multiple Platforms": (-70, -28),
        "Snapchat":           (-60,  15),
        "YouTube":            (-60,  15),
        "OLX/Quikr":          (-65,   0),
        "ShareChat/Moj":      (50,   15),
        "AI Tools (Undisclosed)": (50, -18),
        "X (Twitter)":        (-65, -18),
        "Tinder":             (-55,  18),
        "CyberDome/Kerala":   (50,  -15),
    }

    fig2 = go.Figure()

    # ── Plot markers only (no text in trace)
    for _, row in ps2.iterrows():
        dot_color = RED if row["conviction_rate"] < 1.5 else AMBER if row["conviction_rate"] < 2.5 else TEAL
        fig2.add_trace(go.Scatter(
            x=[row["cases_reported"]],
            y=[row["conviction_rate"]],
            mode="markers",
            marker=dict(
                size=sizes_map[row["platform"]],
                color=dot_color, opacity=0.80,
                line=dict(color=BORDER, width=1.5)
            ),
            hovertemplate=(
                f"<b>{row['short_name']}</b><br>"
                f"Cases Reported: {row['cases_reported']:,}<br>"
                f"Convicted: {row['cases_convicted']:,}<br>"
                f"Conv. Rate: {row['conviction_rate']:.2f}%<extra></extra>"
            ),
            showlegend=False,
        ))

    # ── Annotations for labels (offset arrows, no arrowhead)
    annotations = []
    for _, row in ps2.iterrows():
        ax, ay = label_offsets.get(row["platform"], (45, -20))
        annotations.append(dict(
            x=row["cases_reported"],
            y=row["conviction_rate"],
            text=row["short_name"],
            showarrow=True,
            arrowhead=0,
            arrowwidth=1,
            arrowcolor="rgba(136,146,170,0.45)",
            ax=ax, ay=ay,
            font=dict(color=WHITE, size=10, family="IBM Plex Sans"),
            bgcolor="rgba(10,15,30,0.72)",
            borderpad=3,
        ))

    layout2 = dict(**BASE_LAYOUT)
    layout2.update(
        height=450,
        title=dict(text="Volume vs. Conviction Rate  (bubble = case volume)",
                   font=dict(color=MUTED, size=12, family="IBM Plex Mono"), x=0),
        xaxis=dict(gridcolor=BORDER, linecolor=BORDER, tickfont=dict(color=MUTED, size=10),
                   title=dict(text="Cases Reported", font=dict(color=MUTED, size=10))),
        yaxis=dict(gridcolor=BORDER, linecolor=BORDER, tickfont=dict(color=MUTED, size=10),
                   title=dict(text="Conviction Rate (%)", font=dict(color=MUTED, size=10))),
        margin=dict(l=10, r=20, t=45, b=40),
        annotations=annotations,
    )
    fig2.update_layout(**layout2)
    st.plotly_chart(fig2, use_container_width=True, config={"displayModeBar": False})

    st.markdown("""
    <div class="callout teal">
    <p><strong style="color:#2dd4bf;">Scale ≠ Effectiveness.</strong>
    WhatsApp leads in volume (88,797 cases) but convicts at only 2.95%.
    AI Tools record the lowest rate (0.68%) — revealing a structural
    enforcement gap, not a reporting one.</p>
    </div>""", unsafe_allow_html=True)


# ══════════════════════════════════════════════════════════════════════════════
# SECTION 3 — CRIME CATEGORIES
# ══════════════════════════════════════════════════════════════════════════════
st.markdown("""
<div class="section-header">
    <span class="section-number">03 —</span>
    <p class="section-title">Crime Categories & Legal Response</p>
</div>""", unsafe_allow_html=True)

col3a, col3b = st.columns([2, 3], gap="large")

with col3a:
    top_crimes  = df.groupby("crime_category")["cases_reported"].sum().sort_values(ascending=False).head(8)
    other_val   = df.groupby("crime_category")["cases_reported"].sum().sort_values(ascending=False).iloc[8:].sum()
    labels      = list(top_crimes.index) + ["All Other Categories"]
    values      = list(top_crimes.values) + [other_val]
    donut_colors= [RED, AMBER, TEAL, "#c77dff", "#4cc9f0", "#f77f00", "#06d6a0", "#118ab2", MUTED]
    # Short labels only on slice (percentage only keeps slices clean)
    fig3 = go.Figure(go.Pie(
        labels=labels, values=values, hole=0.60,
        marker=dict(colors=donut_colors, line=dict(color=NAVY, width=2)),
        textinfo="percent",
        textposition="inside",
        insidetextorientation="radial",
        textfont=dict(size=9, color=WHITE, family="IBM Plex Mono"),
        hovertemplate="<b>%{label}</b><br>%{value:,} cases — %{percent}<extra></extra>",
        pull=[0.05 if i == 0 else 0 for i in range(len(labels))],
        showlegend=False,
    ))
    fig3.update_layout(
        paper_bgcolor="rgba(0,0,0,0)", plot_bgcolor="rgba(0,0,0,0)",
        height=340,
        title=dict(text="Case Distribution by Crime Type",
                   font=dict(color=MUTED, size=12, family="IBM Plex Mono"), x=0),
        margin=dict(l=10, r=10, t=40, b=10),
        annotations=[dict(
            text=f"<b>{total_reported//1000}K</b><br><span style='font-size:10px'>total cases</span>",
            x=0.5, y=0.5,
            font=dict(size=15, color=WHITE, family="Playfair Display"),
            showarrow=False
        )]
    )
    st.plotly_chart(fig3, use_container_width=True, config={"displayModeBar": False})

    # ── Custom HTML legend below the chart (decoupled from Plotly layout engine)
    legend_html = "<div style='display:flex;flex-wrap:wrap;gap:0.35rem 1.1rem;margin-top:0.1rem;'>"
    for lbl, color in zip(labels, donut_colors):
        short = lbl[:34] + "…" if len(lbl) > 34 else lbl
        legend_html += (
            f"<div style='display:flex;align-items:center;gap:0.35rem;'>"
            f"<span style='display:inline-block;width:10px;height:10px;border-radius:2px;"
            f"background:{color};flex-shrink:0;'></span>"
            f"<span style='font-family:IBM Plex Sans,sans-serif;font-size:0.72rem;"
            f"color:{MUTED};'>{short}</span></div>"
        )
    legend_html += "</div>"
    st.markdown(legend_html, unsafe_allow_html=True)

with col3b:
    crime_conv = df.groupby("crime_category").agg(
        cases_reported =("cases_reported", "sum"),
        cases_convicted=("cases_convicted","sum")
    ).reset_index()
    crime_conv["conviction_rate"] = (crime_conv["cases_convicted"] / crime_conv["cases_reported"] * 100).round(2)
    crime_conv = crime_conv.sort_values("conviction_rate", ascending=True).tail(14)
    short       = [c[:38] + "…" if len(c) > 38 else c for c in crime_conv["crime_category"]]
    bar_colors2 = [RED if v < 1.5 else AMBER if v < 3.0 else TEAL for v in crime_conv["conviction_rate"]]

    fig4 = go.Figure(go.Bar(
        x=crime_conv["conviction_rate"], y=short,
        orientation="h",
        marker=dict(color=bar_colors2, opacity=0.9),
        text=[f"{v:.2f}%" for v in crime_conv["conviction_rate"]],
        textposition="outside",
        textfont=dict(color=WHITE, size=10, family="IBM Plex Mono"),
        hovertemplate="<b>%{y}</b><br>Conviction Rate: %{x:.2f}%<extra></extra>",
    ))
    layout4 = dict(**BASE_LAYOUT)
    layout4.update(
        height=420,
        title=dict(text="Conviction Rate by Crime Category — Top 14",
                   font=dict(color=MUTED, size=12, family="IBM Plex Mono"), x=0),
        xaxis=dict(gridcolor=BORDER, tickfont=dict(color=MUTED, size=10), range=[0, 8],
                   title=dict(text="Conviction Rate (%)", font=dict(color=MUTED, size=10))),
        yaxis=dict(gridcolor="rgba(0,0,0,0)", tickfont=dict(color=WHITE, size=10)),
        margin=dict(l=10, r=70, t=45, b=30),
    )
    fig4.update_layout(**layout4)
    st.plotly_chart(fig4, use_container_width=True, config={"displayModeBar": False})


# ══════════════════════════════════════════════════════════════════════════════
# SECTION 4 — NCRP TREND
# ══════════════════════════════════════════════════════════════════════════════
st.markdown("""
<div class="section-header">
    <span class="section-number">04 —</span>
    <p class="section-title">Rising Tide — NCRP Complaints 2020–2025</p>
</div>""", unsafe_allow_html=True)

col4a, col4b = st.columns([3, 1], gap="large")

with col4a:
    yoy  = trend["total_complaints_women"].pct_change().fillna(0) * 100
    fig5 = make_subplots(specs=[[{"secondary_y": True}]])
    fig5.add_trace(go.Scatter(
        x=trend["year"], y=trend["total_complaints_women"],
        mode="lines+markers",
        line=dict(color=TEAL, width=3, shape="spline"),
        marker=dict(size=10, color=TEAL, line=dict(color=NAVY, width=2.5)),
        fill="tozeroy", fillcolor="rgba(45,212,191,0.07)",
        name="Total Complaints",
        hovertemplate="<b>%{x}</b><br>Complaints: %{y:,}<extra></extra>",
    ), secondary_y=False)
    fig5.add_trace(go.Bar(
        x=trend["year"], y=yoy,
        marker=dict(color=[RED if v > 30 else AMBER for v in yoy], opacity=0.55),
        name="YoY Growth (%)",
        hovertemplate="<b>%{x}</b><br>YoY Growth: %{y:.1f}%<extra></extra>",
    ), secondary_y=True)
    fig5.update_layout(
        paper_bgcolor="rgba(0,0,0,0)", plot_bgcolor="rgba(0,0,0,0)",
        height=340, font=dict(family="IBM Plex Sans", color=WHITE, size=12),
        margin=dict(l=10, r=10, t=45, b=10),
        title=dict(text="Women-Targeted Cyber Complaints at NCRP (2020–2025)",
                   font=dict(color=MUTED, size=12, family="IBM Plex Mono"), x=0),
        legend=dict(bgcolor="rgba(0,0,0,0)", font=dict(color=MUTED, size=10), orientation="h", y=-0.18),
        xaxis=dict(gridcolor=BORDER, tickfont=dict(color=MUTED), dtick=1),
    )
    fig5.update_yaxes(gridcolor=BORDER, tickfont=dict(color=MUTED, size=10),
                      title_text="Total Complaints", title_font=dict(color=MUTED, size=10), secondary_y=False)
    fig5.update_yaxes(gridcolor="rgba(0,0,0,0)", tickfont=dict(color=MUTED, size=10),
                      title_text="YoY Growth (%)", title_font=dict(color=MUTED, size=10), secondary_y=True)
    st.plotly_chart(fig5, use_container_width=True, config={"displayModeBar": False})

with col4b:
    st.markdown("<div style='height:0.4rem'></div>", unsafe_allow_html=True)
    prev_val = None
    for _, row in trend.iterrows():
        yr, val = int(row["year"]), int(row["total_complaints_women"])
        growth_html = ""
        if prev_val:
            g = (val - prev_val) / prev_val * 100
            color = RED if g > 30 else AMBER if g > 15 else TEAL
            growth_html = f'<span style="color:{color};font-size:0.72rem;"> ▲{g:.0f}%</span>'
        prev_val = val
        st.markdown(f"""
        <div style="display:flex;justify-content:space-between;align-items:baseline;
                    padding:0.55rem 0;border-bottom:1px solid {BORDER};">
            <span style="font-family:'IBM Plex Mono',monospace;font-size:0.78rem;color:{MUTED};">{yr}</span>
            <span style="font-family:'Playfair Display',serif;font-size:1.05rem;color:{WHITE};">{val:,}{growth_html}</span>
        </div>""", unsafe_allow_html=True)
    st.markdown(f"""
    <div class="callout" style="margin-top:1rem;">
    <p><strong style="color:{RED};">+245%</strong> in 5 years.
    The 2025 spike (+58.5%) is the largest single-year jump on record.</p>
    </div>""", unsafe_allow_html=True)


# ══════════════════════════════════════════════════════════════════════════════
# SECTION 5 — AI CRIMES SPOTLIGHT
# ══════════════════════════════════════════════════════════════════════════════
st.markdown("""
<div class="section-header">
    <span class="section-number">05 —</span>
    <p class="section-title">Emerging Threat — AI-Enabled Crimes</p>
</div>""", unsafe_allow_html=True)

ai_crimes = df[
    df["platform"].str.contains("AI|Deepfake|deepfake", case=False, na=False) |
    df["crime_category"].str.contains("AI|Deepfake|deepfake|Voice", case=False, na=False)
].copy()
ai_total = ai_crimes["cases_reported"].sum()
ai_conv  = (ai_crimes["cases_convicted"].sum() / ai_total * 100) if ai_total > 0 else 0
lowest   = df.nsmallest(1, "conviction_rate_pct").iloc[0]

col5a, col5b, col5c = st.columns([1, 1, 2], gap="large")

with col5a:
    st.markdown(f"""<div class="metric-card">
        <div class="metric-label">AI Crime Conviction Rate</div>
        <div class="metric-value" style="font-size:3.2rem;">{ai_conv:.2f}%</div>
        <div class="metric-sub">{ai_total:,} cases reported<br>across AI-enabled categories</div>
    </div>""", unsafe_allow_html=True)

with col5b:
    st.markdown(f"""<div class="metric-card">
        <div class="metric-label">Lowest Single Category</div>
        <div class="metric-value" style="font-size:3.2rem;">{lowest['conviction_rate_pct']:.2f}%</div>
        <div class="metric-sub">{lowest['crime_category']}<br>
        <span style="color:#e63946;">{lowest['platform']}</span></div>
    </div>""", unsafe_allow_html=True)

with col5c:
    ai_df = df[df["crime_category"].str.contains(
        "AI|Deepfake|deepfake|Voice|Morphed", case=False, na=False)].copy()
    ai_df = ai_df.sort_values("conviction_rate_pct")
    if not ai_df.empty:
        gradient = [f"rgba(230,57,70,{0.45 + i * 0.1})" for i in range(len(ai_df))]
        fig6 = go.Figure(go.Bar(
            x=ai_df["conviction_rate_pct"],
            y=[c[:42] for c in ai_df["crime_category"]],
            orientation="h",
            marker=dict(color=gradient),
            text=[f"{v:.2f}%" for v in ai_df["conviction_rate_pct"]],
            textposition="outside",
            textfont=dict(color=WHITE, size=11, family="IBM Plex Mono"),
            hovertemplate="<b>%{y}</b><br>Conviction Rate: %{x:.2f}%<extra></extra>",
        ))
        layout6 = dict(**BASE_LAYOUT)
        layout6.update(
            height=240,
            title=dict(text="AI-Enabled Crime — Conviction Rates",
                       font=dict(color=MUTED, size=12, family="IBM Plex Mono"), x=0),
            xaxis=dict(gridcolor=BORDER, tickfont=dict(color=MUTED, size=10), range=[0, 4.5]),
            yaxis=dict(gridcolor="rgba(0,0,0,0)", tickfont=dict(color=WHITE, size=10)),
            margin=dict(l=10, r=75, t=45, b=20),
        )
        fig6.update_layout(**layout6)
        st.plotly_chart(fig6, use_container_width=True, config={"displayModeBar": False})

st.markdown(f"""
<div class="callout">
<p><strong style="color:{RED};">Legal Blind Spot:</strong>
AI-enabled crimes — deepfake pornography, voice cloning fraud, AI sextortion — record the lowest conviction
rates in the dataset. <strong style="color:{WHITE};">No dedicated legal provision exists</strong>
for AI voice cloning under the IT Act or BNS 2023.
CyberDome specialized units achieve 5.53%, showing
<strong style="color:{WHITE};">dedicated enforcement cells outperform general police by 8×</strong>
on technology crimes.</p>
</div>""", unsafe_allow_html=True)


# ══════════════════════════════════════════════════════════════════════════════
# SECTION 6 — KEY INSIGHTS PANEL
# ══════════════════════════════════════════════════════════════════════════════
st.markdown("""
<div class="section-header">
    <span class="section-number">06 —</span>
    <p class="section-title">Key Insights</p>
</div>""", unsafe_allow_html=True)

ins1, ins2, ins3 = st.columns(3, gap="large")

with ins1:
    st.markdown("""
    <div class="insight-box">
        <div class="insight-title">⚖ Enforcement Gap</div>
        <p class="insight-text">The chargesheet rate (15.9%) is 7× the conviction rate (2.24%).
        Cases are registered and investigated — but not reaching verdict stage.
        Judicial backlog and prosecution quality are the primary bottlenecks.</p>
    </div>
    <div class="insight-box">
        <div class="insight-title">📡 Platform Accountability</div>
        <p class="insight-text">WhatsApp dominates case volume but not outcomes.
        Specialized units (CyberDome, Kerala) achieve 5.53% — more than double the national mean —
        proving that targeted institutional focus works.</p>
    </div>""", unsafe_allow_html=True)

with ins2:
    st.markdown("""
    <div class="insight-box">
        <div class="insight-title">🤖 AI Crime Lag</div>
        <p class="insight-text">AI voice cloning (0.61%) and deepfake sextortion sit at the bottom
        of conviction rates. Neither the IT Act 2000 nor BNS 2023 has a dedicated provision
        for AI-generated abuse — a critical legislative gap as these crimes surge.</p>
    </div>
    <div class="insight-box">
        <div class="insight-title">📈 Surge Not Slowing</div>
        <p class="insight-text">NCRP complaints grew 245% in 5 years. The 2025 jump (+58.5%)
        is the steepest on record. Enforcement capacity has not kept pace with the
        growth in reporting.</p>
    </div>""", unsafe_allow_html=True)

with ins3:
    max_rate = platform_summary["conviction_rate"].max()
    st.markdown(f"""
    <div style="background:{NAVY3};border:1px solid {BORDER};border-radius:6px;padding:1.2rem;">
        <div style="font-family:'IBM Plex Mono',monospace;font-size:0.65rem;text-transform:uppercase;
                    letter-spacing:0.1em;color:{MUTED};margin-bottom:1rem;">
            Platform Conviction Rates
        </div>""", unsafe_allow_html=True)
    for _, row in platform_summary.sort_values("conviction_rate", ascending=False).iterrows():
        pct       = row["conviction_rate"] / max_rate * 100
        bar_color = RED if row["conviction_rate"] < 1.5 else AMBER if row["conviction_rate"] < 2.5 else TEAL
        short     = row["platform"][:22] + "…" if len(row["platform"]) > 22 else row["platform"]
        st.markdown(f"""
        <div class="prog-row">
            <div class="prog-label">
                <span class="prog-name">{short}</span>
                <span class="prog-val">{row['conviction_rate']:.2f}%</span>
            </div>
            <div class="prog-track">
                <div class="prog-fill" style="width:{pct:.0f}%;background:{bar_color};"></div>
            </div>
        </div>""", unsafe_allow_html=True)
    st.markdown("</div>", unsafe_allow_html=True)


# ══════════════════════════════════════════════════════════════════════════════
# SECTION 7 — DATA EXPLORER
# ══════════════════════════════════════════════════════════════════════════════
# ══════════════════════════════════════════════════════════════════════════════

st.markdown("""
<div class="section-header">
    <span class="section-number">07 —</span>
    <p class="section-title">Data Explorer</p>
</div>""", unsafe_allow_html=True)

# 1. Simplified layout with only two columns for filters
col_f1, col_f2 = st.columns(2)
with col_f1:
    platform_filter = st.selectbox("Filter by Platform",
                                   ["All Platforms"] + sorted(df["platform"].unique().tolist()))
with col_f2:
    crime_filter = st.selectbox("Filter by Crime Type",
                                ["All Crime Types"] + sorted(df["crime_category"].unique().tolist()))

# 2. Filter logic (removed sort_by logic)
filtered = df.copy()
if platform_filter != "All Platforms":
    filtered = filtered[filtered["platform"] == platform_filter]
if crime_filter != "All Crime Types":
    filtered = filtered[filtered["crime_category"] == crime_filter]

st.markdown(f"""<div style="font-family:'IBM Plex Mono',monospace;font-size:0.7rem;color:{MUTED};
                margin-bottom:0.6rem;letter-spacing:0.06em;">
    Showing {len(filtered)} of {len(df)} rows
</div>""", unsafe_allow_html=True)

# 3. Display table
display_df = filtered[[
    "platform","crime_category","cases_reported","cases_chargesheeted",
    "cases_convicted","conviction_rate_pct","laws_invoked"
]].rename(columns={
    "platform":"Platform","crime_category":"Crime Category",
    "cases_reported":"Reported","cases_chargesheeted":"Chargesheeted",
    "cases_convicted":"Convicted","conviction_rate_pct":"Conv. Rate %",
    "laws_invoked":"Laws Invoked"
})

st.dataframe(
    display_df, use_container_width=True, height=400, # Increased height slightly
    column_config={
        "Conv. Rate %":  st.column_config.ProgressColumn("Conv. Rate %",  min_value=0, max_value=6, format="%.2f%%"),
        "Reported":      st.column_config.NumberColumn("Reported",      format="%d"),
        "Convicted":     st.column_config.NumberColumn("Convicted",     format="%d"),
        "Chargesheeted": st.column_config.NumberColumn("Chargesheeted", format="%d"),
    }
)
# ══════════════════════════════════════════════════════════════════════════════
# FOOTER
# ══════════════════════════════════════════════════════════════════════════════
st.markdown("""
<div class="dash-footer">
    DATA SOURCES: MHA Annual Report 2023–24 &nbsp;·&nbsp; NCRB Crime in India 2024 &nbsp;·&nbsp;
    NCRP Parliamentary Data 2024–25 &nbsp;·&nbsp; CERT-In Annual Report 2024–25
    <br><br>
    Yadneeka Sanjay Jadhav (SP47240003) &nbsp;·&nbsp; Guide: Prof. Kirti Garud &nbsp;·&nbsp;
    Research Project 2024–2026 &nbsp;·&nbsp; All data from official Government of India publications
</div>""", unsafe_allow_html=True)
