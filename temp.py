import streamlit as st
import pandas as pd
import plotly.graph_objects as go
import plotly.express as px
from plotly.subplots import make_subplots
import requests
from streamlit_lottie import st_lottie

def load_lottieurl(url):
    r = requests.get(url)
    if r.status_code != 200:
        return None
    return r.json()

# Cyber-Law themed animations
lottie_security = load_lottieurl("https://assets10.lottiefiles.com/packages/lf20_m6cu96ic.json") # Shield
lottie_law = load_lottieurl("https://assets5.lottiefiles.com/packages/lf20_fp7svpxm.json") # Gavel/Scales

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
    --navy:    #0a0f1e;
    --navy2:   #111827;
    --navy3:   #1a2540;
    --red:     #e63946;
    --amber:   #f4a261;
    --teal:    #2dd4bf;
    --white:   #f0f4ff;
    --muted:   #8892aa;
    --border:  #1e2d4a;
}

html, body, [data-testid="stAppViewContainer"] {
    background-color: var(--navy) !important;
    color: var(--white) !important;
}

[data-testid="stAppViewContainer"] > .main {
    background-color: var(--navy) !important;
}

[data-testid="block-container"] {
    padding: 0 2rem 4rem 2rem !important;
    max-width: 1400px !important;
}

/* Hide streamlit chrome */
#MainMenu, footer, header { visibility: hidden; }
[data-testid="stDecoration"] { display: none; }

/* Typography */
h1, h2, h3 { font-family: 'Playfair Display', serif !important; }
/* Only apply to text inside your specific containers */
.metric-card div, .metric-card span, .hero-band p, .section-header p {
    font-family: 'IBM Plex Sans', sans-serif !important;
}

/* Metric cards */
.metric-card {
    background: var(--navy3);
    border: 1px solid var(--border);
    border-top: 3px solid var(--red);
    padding: 1.6rem 1.4rem 1.2rem;
    border-radius: 4px;
    position: relative;
    overflow: hidden;
}
.metric-card::before {
    content: '';
    position: absolute;
    top: 0; left: 0; right: 0; bottom: 0;
    background: linear-gradient(135deg, rgba(230,57,70,0.04) 0%, transparent 60%);
    pointer-events: none;
}
.metric-card.teal { border-top-color: var(--teal); }
.metric-card.teal::before { background: linear-gradient(135deg, rgba(45,212,191,0.05) 0%, transparent 60%); }
.metric-card.amber { border-top-color: var(--amber); }
.metric-card.amber::before { background: linear-gradient(135deg, rgba(244,162,97,0.05) 0%, transparent 60%); }

.metric-label {
    font-family: 'IBM Plex Mono', monospace !important;
    font-size: 0.68rem;
    letter-spacing: 0.12em;
    text-transform: uppercase;
    color: var(--muted);
    margin-bottom: 0.5rem;
}
.metric-value {
    font-family: 'Playfair Display', serif !important;
    font-size: 2.8rem;
    font-weight: 900;
    color: var(--red);
    line-height: 1;
    margin-bottom: 0.4rem;
}
.metric-value.teal { color: var(--teal); }
.metric-value.amber { color: var(--amber); }
.metric-value.white { color: var(--white); }
.metric-sub {
    font-family: 'IBM Plex Sans', sans-serif !important;
    font-size: 0.78rem;
    color: var(--muted);
    line-height: 1.4;
}

/* Section headers */
.section-header {
    display: flex;
    align-items: baseline;
    gap: 1rem;
    margin: 3rem 0 1.2rem 0;
    padding-bottom: 0.6rem;
    border-bottom: 1px solid var(--border);
}
.section-number {
    font-family: 'IBM Plex Mono', monospace;
    font-size: 0.7rem;
    color: var(--red);
    letter-spacing: 0.1em;
}
.section-title {
    font-family: 'Playfair Display', serif !important;
    font-size: 1.4rem;
    font-weight: 700;
    color: var(--white);
    margin: 0;
}

/* Callout box */
.callout {
    background: rgba(230, 57, 70, 0.08);
    border-left: 3px solid var(--red);
    padding: 1rem 1.2rem;
    border-radius: 0 4px 4px 0;
    margin: 0.8rem 0;
}
.callout p {
    margin: 0;
    font-size: 0.88rem;
    color: var(--white);
    line-height: 1.6;
}
.callout.teal {
    background: rgba(45,212,191,0.07);
    border-left-color: var(--teal);
}
.callout.amber {
    background: rgba(244,162,97,0.07);
    border-left-color: var(--amber);
}

/* Hero band */
.hero-band {
    background: linear-gradient(135deg, #0d1628 0%, #0a0f1e 100%);
    border: 1px solid var(--border);
    border-left: 4px solid var(--red);
    padding: 2.4rem 2rem;
    margin-bottom: 2rem;
    border-radius: 4px;
}

/* Footer */
.dash-footer {
    margin-top: 4rem;
    padding-top: 1.5rem;
    border-top: 1px solid var(--border);
    font-family: 'IBM Plex Mono', monospace;
    font-size: 0.68rem;
    color: var(--muted);
    letter-spacing: 0.06em;
    text-align: center;
}

/* Tag pills */
.tag {
    display: inline-block;
    background: rgba(230,57,70,0.12);
    border: 1px solid rgba(230,57,70,0.3);
    color: var(--red);
    font-family: 'IBM Plex Mono', monospace;
    font-size: 0.65rem;
    letter-spacing: 0.08em;
    padding: 0.2rem 0.6rem;
    border-radius: 2px;
    margin-right: 0.4rem;
    margin-bottom: 0.4rem;
}

/* Sidebar */
[data-testid="stSidebar"] {
    background: var(--navy2) !important;
    border-right: 1px solid var(--border) !important;
}

/* Plotly chart backgrounds */
.js-plotly-plot { background: transparent !important; }

/* Selectbox */
[data-testid="stSelectbox"] > div {
    background: var(--navy3) !important;
    border-color: var(--border) !important;
    color: var(--white) !important;
}
            
            /* Fix for distorted 3-dot menu text */
[data-testid="stHeaderActionElements"], 
[data-testid="stVirtualizedSlider"],
div[data-baseweb="popover"], 
div[data-baseweb="menu"] {
    font-family: sans-serif !important;
}

div[data-baseweb="popover"] * {
    color: var(--navy) !important; /* Makes text readable against white background */
    line-height: normal !important;
}

            /* Target the 3-dot popup menu and force visibility */
div[data-baseweb="popover"] *, 
div[data-baseweb="menu"] * {
    color: #ffffff !important;
    fill: #ffffff !important; /* Forces icons to be white too */
}

/* Optional: Give the menu a distinct dark background so it pops */
div[data-baseweb="popover"] {
    background-color: #1a2540 !important; /* Matches your --navy3 */
    border: 1px solid #1e2d4a !important; /* Matches your --border */
}

/* Fix for the hover state so you can see what you're selecting */
div[data-baseweb="menu"] li:hover {
    background-color: #e63946 !important; /* Highlights red on hover */
}
            
</style>
""", unsafe_allow_html=True)


# ── Data Loading ───────────────────────────────────────────────────────────────
@st.cache_data
def load_data():
    df = pd.read_excel("Cyberlaw_Women_India_Verified_2024_2026.xlsx", sheet_name="Platform_Case_Data")
    df["conviction_rate_pct"] = (df["cases_convicted"] / df["cases_reported"] * 100).round(2)
    df["chargesheets_rate_pct"] = (df["cases_chargesheeted"] / df["cases_reported"] * 100).round(2)

    trend = pd.read_excel("Cyberlaw_Women_India_Verified_2024_2026.xlsx", sheet_name="NCRP_Yearly_Trend")

    platform_summary = df.groupby("platform").agg(
        cases_reported=("cases_reported", "sum"),
        cases_chargesheeted=("cases_chargesheeted", "sum"),
        cases_convicted=("cases_convicted", "sum"),
        conviction_rate=("conviction_rate_pct", "mean")
    ).round(2).reset_index().sort_values("conviction_rate", ascending=False)

    return df, trend, platform_summary

df, trend, platform_summary = load_data()

# ── Plotly theme ───────────────────────────────────────────────────────────────
NAVY   = "#0a0f1e"
NAVY3  = "#1a2540"
BORDER = "#1e2d4a"
RED    = "#e63946"
AMBER  = "#f4a261"
TEAL   = "#2dd4bf"
WHITE  = "#f0f4ff"
MUTED  = "#8892aa"

CHART_LAYOUT = dict(
    paper_bgcolor="rgba(0,0,0,0)",
    plot_bgcolor="rgba(0,0,0,0)",
    font=dict(family="IBM Plex Sans", color=WHITE, size=12),
    margin=dict(l=10, r=10, t=30, b=10),
    xaxis=dict(gridcolor=BORDER, linecolor=BORDER, tickfont=dict(color=MUTED, size=11)),
    yaxis=dict(gridcolor=BORDER, linecolor=BORDER, tickfont=dict(color=MUTED, size=11)),
    legend=dict(bgcolor="rgba(0,0,0,0)", font=dict(color=MUTED)),
)


# ══════════════════════════════════════════════════════════════════════════════
# HERO HEADER
# ══════════════════════════════════════════════════════════════════════════════
st.markdown("""
<div class="hero-band">
    <div style="font-family:'IBM Plex Mono',monospace;font-size:0.68rem;letter-spacing:0.15em;color:#8892aa;text-transform:uppercase;margin-bottom:0.6rem;">
        Research Dashboard &nbsp;·&nbsp; SP47240003 &nbsp;·&nbsp; 2024–2026
    </div>
    <h1 style="font-family:'Playfair Display',serif;font-size:2.1rem;font-weight:900;color:#f0f4ff;margin:0 0 0.5rem 0;line-height:1.2;">
        Effectiveness of Digital Safety Laws<br>for Women in India
    </h1>
    <p style="font-family:'IBM Plex Sans',sans-serif;color:#8892aa;font-size:0.9rem;margin:0;max-width:680px;line-height:1.6;">
        A data-driven evaluation of cybercrime enforcement outcomes across 11 platforms and 30 crime categories.
        All data sourced from MHA Annual Reports, NCRB Crime in India, NCRP Parliamentary Data, and CERT-In advisories.
    </p>
    <div style="margin-top:1rem;">
        <span class="tag">IT Act 2000</span>
        <span class="tag">IPC / BNS 2023</span>
        <span class="tag">317,534 Cases</span>
        <span class="tag">11 Platforms</span>
        <span class="tag">2024–2025</span>
    </div>
</div>
""", unsafe_allow_html=True)


# ══════════════════════════════════════════════════════════════════════════════
# SECTION 1 — KEY METRICS
# ══════════════════════════════════════════════════════════════════════════════
st.markdown("""
<div class="section-header">
    <span class="section-number">01 —</span>
    <p class="section-title">Enforcement at a Glance</p>
</div>
""", unsafe_allow_html=True)

total_reported   = df["cases_reported"].sum()
total_charged    = df["cases_chargesheeted"].sum()
total_convicted  = df["cases_convicted"].sum()
mean_conv        = df["conviction_rate_pct"].mean()
charge_rate      = total_charged / total_reported * 100
ncrp_growth      = ((76657 - 22188) / 22188 * 100)

c1, c2, c3, c4, c5 = st.columns(5)

with c1:
    st.markdown(f"""
    <div class="metric-card">
        <div class="metric-label">Mean Conviction Rate</div>
        <div class="metric-value">{mean_conv:.2f}%</div>
        <div class="metric-sub">Across all platforms<br>& crime categories</div>
    </div>""", unsafe_allow_html=True)

with c2:
    st.markdown(f"""
    <div class="metric-card amber">
        <div class="metric-label">Chargesheets Filed</div>
        <div class="metric-value amber">{charge_rate:.1f}%</div>
        <div class="metric-sub">Cases reaching<br>prosecution stage</div>
    </div>""", unsafe_allow_html=True)

with c3:
    st.markdown(f"""
    <div class="metric-card teal">
        <div class="metric-label">Total Cases Reported</div>
        <div class="metric-value teal">{total_reported:,}</div>
        <div class="metric-sub">Across 11 platforms<br>2024–2025</div>
    </div>""", unsafe_allow_html=True)

with c4:
    st.markdown(f"""
    <div class="metric-card">
        <div class="metric-label">Total Convictions</div>
        <div class="metric-value white">{total_convicted:,}</div>
        <div class="metric-sub">Out of {total_reported:,}<br>cases reported</div>
    </div>""", unsafe_allow_html=True)

with c5:
    st.markdown(f"""
    <div class="metric-card amber">
        <div class="metric-label">NCRP Growth (2020–25)</div>
        <div class="metric-value amber">+{ncrp_growth:.0f}%</div>
        <div class="metric-sub">Complaints filed by<br>women, 5-year rise</div>
    </div>""", unsafe_allow_html=True)

st.markdown("""
<div class="callout" style="margin-top:1.2rem;">
<p><strong style="color:#e63946;">Key Finding:</strong>
Fewer than <strong style="color:#f0f4ff;">3 in every 100</strong> reported cybercrime cases against women result in a conviction.
Chargesheeting rates (15.9%) are 7× higher than conviction rates (2.24%), pointing to prosecution
and judicial bottlenecks rather than investigative failure alone.</p>
</div>
""", unsafe_allow_html=True)


# ══════════════════════════════════════════════════════════════════════════════
# SECTION 2 — PLATFORM ANALYSIS
# ══════════════════════════════════════════════════════════════════════════════
st.markdown("""
<div class="section-header">
    <span class="section-number">02 —</span>
    <p class="section-title">Platform-Level Enforcement</p>
</div>
""", unsafe_allow_html=True)

col_left, col_right = st.columns([3, 2], gap="large")

with col_left:
    # Horizontal bar chart — conviction rate by platform
    ps = platform_summary.sort_values("conviction_rate")
    colors = [RED if v < 1.5 else AMBER if v < 2.5 else TEAL for v in ps["conviction_rate"]]

    fig = go.Figure()
    fig.add_trace(go.Bar(
        x=ps["conviction_rate"],
        y=ps["platform"],
        orientation="h",
        marker=dict(color=colors, line=dict(width=0)),
        text=[f"{v:.2f}%" for v in ps["conviction_rate"]],
        textposition="outside",
        textfont=dict(color=WHITE, size=11, family="IBM Plex Mono"),
        hovertemplate="<b>%{y}</b><br>Conviction Rate: %{x:.2f}%<extra></extra>",
    ))
    fig.add_vline(x=2.24, line_dash="dot", line_color=MUTED, line_width=1,
                  annotation_text="Mean 2.24%", annotation_font_color=MUTED,
                  annotation_font_size=10)
    layout = dict(**CHART_LAYOUT)
    layout.update(
        height=380,
        title=dict(text="Conviction Rate by Platform (%)", font=dict(color=MUTED, size=12, family="IBM Plex Mono"), x=0),
        xaxis=dict(gridcolor=BORDER, linecolor=BORDER, tickfont=dict(color=MUTED, size=10),
                   title=dict(text="Conviction Rate (%)", font=dict(color=MUTED, size=10)), range=[0, 6.5]),
        yaxis=dict(gridcolor="rgba(0,0,0,0)", linecolor=BORDER, tickfont=dict(color=WHITE, size=11)),
        margin=dict(l=10, r=60, t=40, b=30),
    )
    fig.update_layout(**layout)
    st.plotly_chart(fig, use_container_width=True, config={"displayModeBar": False})

with col_right:
    # Scatter — cases reported vs conviction rate
    fig2 = go.Figure()
    sizes = (platform_summary["cases_reported"] / platform_summary["cases_reported"].max() * 45 + 8).tolist()
    fig2.add_trace(go.Scatter(
        x=platform_summary["cases_reported"],
        y=platform_summary["conviction_rate"],
        mode="markers+text",
        marker=dict(size=sizes, color=TEAL, opacity=0.7,
                    line=dict(color=BORDER, width=1)),
        text=platform_summary["platform"].str.replace(" / ", "/").str.replace("Multiple Platforms", "Multi"),
        textposition="top center",
        textfont=dict(color=MUTED, size=9, family="IBM Plex Sans"),
        hovertemplate="<b>%{text}</b><br>Cases: %{x:,}<br>Conv. Rate: %{y:.2f}%<extra></extra>",
    ))
    layout2 = dict(**CHART_LAYOUT)
    layout2.update(
        height=380,
        title=dict(text="Volume vs. Conviction Rate", font=dict(color=MUTED, size=12, family="IBM Plex Mono"), x=0),
        xaxis=dict(gridcolor=BORDER, linecolor=BORDER, tickfont=dict(color=MUTED, size=9),
                   title=dict(text="Cases Reported", font=dict(color=MUTED, size=10))),
        yaxis=dict(gridcolor=BORDER, linecolor=BORDER, tickfont=dict(color=MUTED, size=10),
                   title=dict(text="Conviction Rate (%)", font=dict(color=MUTED, size=10))),
        margin=dict(l=10, r=10, t=40, b=30),
    )
    fig2.update_layout(**layout2)
    st.plotly_chart(fig2, use_container_width=True, config={"displayModeBar": False})

    st.markdown("""
    <div class="callout teal" style="margin-top:-0.5rem;">
    <p><strong style="color:#2dd4bf;">Scale ≠ Effectiveness.</strong>
    WhatsApp has the highest case volume (88,797) but a conviction rate of only 2.95%.
    Higher reporting does not translate to better enforcement outcomes.</p>
    </div>
    """, unsafe_allow_html=True)


# ══════════════════════════════════════════════════════════════════════════════
# SECTION 3 — CRIME CATEGORIES
# ══════════════════════════════════════════════════════════════════════════════
st.markdown("""
<div class="section-header">
    <span class="section-number">03 —</span>
    <p class="section-title">Crime Categories & Legal Response</p>
</div>
""", unsafe_allow_html=True)

col3a, col3b = st.columns([2, 3], gap="large")

with col3a:
    # Top crime categories by volume — donut
    top_crimes = df.groupby("crime_category")["cases_reported"].sum().sort_values(ascending=False).head(8)
    other = df.groupby("crime_category")["cases_reported"].sum().sort_values(ascending=False).iloc[8:].sum()
    labels = list(top_crimes.index) + ["All Other Categories"]
    values = list(top_crimes.values) + [other]
    short_labels = [l[:28] + "…" if len(l) > 28 else l for l in labels]

    donut_colors = [RED, AMBER, TEAL, "#c77dff", "#4cc9f0", "#f77f00", "#06d6a0", "#118ab2", MUTED]
    fig3 = go.Figure(go.Pie(
        labels=short_labels, values=values,
        hole=0.6,
        marker=dict(colors=donut_colors, line=dict(color=NAVY, width=2)),
        textinfo="percent",
        textfont=dict(size=10, color=WHITE, family="IBM Plex Mono"),
        hovertemplate="<b>%{label}</b><br>%{value:,} cases (%{percent})<extra></extra>",
    ))
    fig3.update_layout(
        paper_bgcolor="rgba(0,0,0,0)", plot_bgcolor="rgba(0,0,0,0)",
        height=360,
        title=dict(text="Case Distribution by Crime Type", font=dict(color=MUTED, size=12, family="IBM Plex Mono"), x=0),
        legend=dict(bgcolor="rgba(0,0,0,0)", font=dict(color=MUTED, size=9, family="IBM Plex Sans"),
                    orientation="v", x=1.01),
        margin=dict(l=0, r=140, t=40, b=10),
        annotations=[dict(text=f"<b>{total_reported//1000}K</b><br><span style='font-size:9'>cases</span>",
                          x=0.5, y=0.5, font=dict(size=14, color=WHITE, family="Playfair Display"),
                          showarrow=False)]
    )
    st.plotly_chart(fig3, use_container_width=True, config={"displayModeBar": False})

with col3b:
    # Conviction rates by crime category — top 12
    crime_conv = df.groupby("crime_category").agg(
        cases_reported=("cases_reported", "sum"),
        cases_convicted=("cases_convicted", "sum")
    ).reset_index()
    crime_conv["conviction_rate"] = (crime_conv["cases_convicted"] / crime_conv["cases_reported"] * 100).round(2)
    crime_conv = crime_conv.sort_values("conviction_rate", ascending=True).tail(12)

    short = [c[:35] + "…" if len(c) > 35 else c for c in crime_conv["crime_category"]]
    bar_colors = [RED if v < 1.5 else AMBER if v < 3.0 else TEAL for v in crime_conv["conviction_rate"]]

    fig4 = go.Figure(go.Bar(
        x=crime_conv["conviction_rate"], y=short,
        orientation="h",
        marker=dict(color=bar_colors),
        text=[f"{v:.2f}%" for v in crime_conv["conviction_rate"]],
        textposition="outside",
        textfont=dict(color=WHITE, size=10, family="IBM Plex Mono"),
        hovertemplate="<b>%{y}</b><br>Conviction Rate: %{x:.2f}%<extra></extra>",
    ))
    layout4 = dict(**CHART_LAYOUT)
    layout4.update(
        height=380,
        title=dict(text="Conviction Rate by Crime Category — Top 12", font=dict(color=MUTED, size=12, family="IBM Plex Mono"), x=0),
        xaxis=dict(gridcolor=BORDER, tickfont=dict(color=MUTED, size=10), range=[0, 7.5],
                   title=dict(text="Conviction Rate (%)", font=dict(color=MUTED, size=10))),
        yaxis=dict(gridcolor="rgba(0,0,0,0)", tickfont=dict(color=WHITE, size=10)),
        margin=dict(l=10, r=60, t=40, b=30),
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
</div>
""", unsafe_allow_html=True)

col4a, col4b = st.columns([3, 1], gap="large")

with col4a:
    yoy = trend["total_complaints_women"].pct_change().fillna(0) * 100

    fig5 = make_subplots(specs=[[{"secondary_y": True}]])
    fig5.add_trace(go.Scatter(
        x=trend["year"], y=trend["total_complaints_women"],
        mode="lines+markers",
        line=dict(color=TEAL, width=3),
        marker=dict(size=9, color=TEAL, line=dict(color=NAVY, width=2)),
        fill="tozeroy",
        fillcolor="rgba(45,212,191,0.07)",
        name="Total Complaints",
        hovertemplate="<b>%{x}</b><br>Complaints: %{y:,}<extra></extra>",
    ), secondary_y=False)

    fig5.add_trace(go.Bar(
        x=trend["year"], y=yoy,
        marker=dict(color=[RED if v > 30 else AMBER for v in yoy], opacity=0.5),
        name="YoY Growth (%)",
        hovertemplate="<b>%{x}</b><br>YoY Growth: %{y:.1f}%<extra></extra>",
    ), secondary_y=True)

    fig5.update_layout(
        paper_bgcolor="rgba(0,0,0,0)", plot_bgcolor="rgba(0,0,0,0)",
        height=340,
        font=dict(family="IBM Plex Sans", color=WHITE, size=12),
        margin=dict(l=10, r=10, t=40, b=10),
        title=dict(text="Women-Targeted Cyber Complaints Filed at NCRP (2020–2025)", font=dict(color=MUTED, size=12, family="IBM Plex Mono"), x=0),
        legend=dict(bgcolor="rgba(0,0,0,0)", font=dict(color=MUTED, size=10), orientation="h", y=-0.15),
        xaxis=dict(gridcolor=BORDER, tickfont=dict(color=MUTED), dtick=1),
    )
    fig5.update_yaxes(gridcolor=BORDER, tickfont=dict(color=MUTED, size=10),
                      title_text="Total Complaints", title_font=dict(color=MUTED, size=10), secondary_y=False)
    fig5.update_yaxes(gridcolor="rgba(0,0,0,0)", tickfont=dict(color=MUTED, size=10),
                      title_text="YoY Growth (%)", title_font=dict(color=MUTED, size=10), secondary_y=True)
    st.plotly_chart(fig5, use_container_width=True, config={"displayModeBar": False})

with col4b:
    st.markdown("<div style='height:0.5rem'></div>", unsafe_allow_html=True)
    for year, val in zip(trend["year"], trend["total_complaints_women"]):
        yoy_val = trend.loc[trend["year"] == year, "total_complaints_women"].values[0]
        prev = trend.loc[trend["year"] == year - 1, "total_complaints_women"]
        growth = ""
        if len(prev) > 0:
            g = (yoy_val - prev.values[0]) / prev.values[0] * 100
            arrow = "▲" if g > 0 else "▼"
            color = RED if g > 30 else AMBER if g > 15 else TEAL
            growth = f'<span style="color:{color};font-size:0.75rem"> {arrow}{g:.0f}%</span>'
        st.markdown(f"""
        <div style="display:flex;justify-content:space-between;align-items:baseline;
                    padding:0.5rem 0;border-bottom:1px solid {BORDER};">
            <span style="font-family:'IBM Plex Mono',monospace;font-size:0.8rem;color:{MUTED};">{int(year)}</span>
            <span style="font-family:'Playfair Display',serif;font-size:1.05rem;color:{WHITE};">{val:,}{growth}</span>
        </div>
        """, unsafe_allow_html=True)

    st.markdown(f"""
    <div class="callout" style="margin-top:1rem;">
    <p><strong style="color:{RED};">+245%</strong> growth in 5 years.
    2025 alone saw a <strong style="color:{WHITE};">58.5% spike</strong> — the largest single-year jump recorded.</p>
    </div>
    """, unsafe_allow_html=True)


# ══════════════════════════════════════════════════════════════════════════════
# SECTION 5 — AI CRIMES SPOTLIGHT
# ══════════════════════════════════════════════════════════════════════════════
st.markdown("""
<div class="section-header">
    <span class="section-number">05 —</span>
    <p class="section-title">Emerging Threat — AI-Enabled Crimes</p>
</div>
""", unsafe_allow_html=True)

ai_crimes = df[df["platform"].str.contains("AI|Deepfake|deepfake", case=False, na=False) |
               df["crime_category"].str.contains("AI|Deepfake|deepfake|Voice", case=False, na=False)].copy()

col5a, col5b, col5c = st.columns([1, 1, 2], gap="large")

with col5a:
    ai_total = ai_crimes["cases_reported"].sum()
    ai_conv  = (ai_crimes["cases_convicted"].sum() / ai_total * 100) if ai_total > 0 else 0
    st.markdown(f"""
    <div class="metric-card" style="height:100%;">
        <div class="metric-label">AI Crime Conviction Rate</div>
        <div class="metric-value" style="font-size:3.4rem;">{ai_conv:.2f}%</div>
        <div class="metric-sub">{ai_total:,} cases reported<br>across AI-enabled categories</div>
    </div>""", unsafe_allow_html=True)

with col5b:
    lowest = df.nsmallest(1, "conviction_rate_pct").iloc[0]
    st.markdown(f"""
    <div class="metric-card" style="height:100%;">
        <div class="metric-label">Lowest Single Category</div>
        <div class="metric-value" style="font-size:3.4rem;">{lowest['conviction_rate_pct']:.2f}%</div>
        <div class="metric-sub">{lowest['crime_category']}<br><span style="color:#e63946;">{lowest['platform']}</span></div>
    </div>""", unsafe_allow_html=True)

with col5c:
    # AI crimes comparison bar
    ai_df = df[df["crime_category"].str.contains("AI|Deepfake|deepfake|Voice|Morphed", case=False, na=False)].copy()
    ai_df = ai_df.sort_values("conviction_rate_pct")

    if not ai_df.empty:
        fig6 = go.Figure(go.Bar(
            x=ai_df["conviction_rate_pct"],
            y=[c[:40] for c in ai_df["crime_category"]],
            orientation="h",
            marker=dict(color=RED, opacity=0.85),
            text=[f"{v:.2f}%" for v in ai_df["conviction_rate_pct"]],
            textposition="outside",
            textfont=dict(color=WHITE, size=11, family="IBM Plex Mono"),
        ))
        layout6 = dict(**CHART_LAYOUT)
        layout6.update(
            height=220,
            title=dict(text="AI-Enabled Crime Conviction Rates", font=dict(color=MUTED, size=12, family="IBM Plex Mono"), x=0),
            xaxis=dict(gridcolor=BORDER, tickfont=dict(color=MUTED, size=10), range=[0, 4]),
            yaxis=dict(gridcolor="rgba(0,0,0,0)", tickfont=dict(color=WHITE, size=10)),
            margin=dict(l=10, r=70, t=40, b=20),
        )
        fig6.update_layout(**layout6)
        st.plotly_chart(fig6, use_container_width=True, config={"displayModeBar": False})

st.markdown(f"""
<div class="callout" style="margin-top:0.5rem;">
<p><strong style="color:{RED};">Legal Blind Spot:</strong>
AI-enabled crimes — deepfake pornography, voice cloning fraud, and AI sextortion — record the lowest conviction
rates in this dataset. No dedicated legal provision exists for AI voice cloning under the current IT Act or BNS 2023 framework.
CyberDome-type specialized units show 5.53% conviction rates, suggesting that <strong style="color:{WHITE};">
dedicated enforcement cells significantly outperform general law enforcement</strong> for technology-enabled crimes.</p>
</div>
""", unsafe_allow_html=True)


# ══════════════════════════════════════════════════════════════════════════════
# SECTION 6 — DATA EXPLORER
# ══════════════════════════════════════════════════════════════════════════════
st.markdown("""
<div class="section-header">
    <span class="section-number">06 —</span>
    <p class="section-title">Data Explorer</p>
</div>
""", unsafe_allow_html=True)

col_f1, col_f2 = st.columns(2)
with col_f1:
    platform_filter = st.selectbox("Filter by Platform", ["All Platforms"] + sorted(df["platform"].unique().tolist()))
with col_f2:
    sort_by = st.selectbox("Sort by", ["conviction_rate_pct ↓", "cases_reported ↓", "cases_convicted ↓"])

filtered = df.copy()
if platform_filter != "All Platforms":
    filtered = filtered[filtered["platform"] == platform_filter]

sort_col = sort_by.split(" ")[0]
filtered = filtered.sort_values(sort_col, ascending=False)

display_cols = ["platform", "crime_category", "cases_reported", "cases_chargesheeted",
                "cases_convicted", "conviction_rate_pct", "laws_invoked"]
display_df = filtered[display_cols].rename(columns={
    "platform": "Platform",
    "crime_category": "Crime Category",
    "cases_reported": "Reported",
    "cases_chargesheeted": "Chargesheeted",
    "cases_convicted": "Convicted",
    "conviction_rate_pct": "Conv. Rate %",
    "laws_invoked": "Laws Invoked"
})

st.dataframe(
    display_df,
    use_container_width=True,
    height=320,
    column_config={
        "Conv. Rate %": st.column_config.ProgressColumn(
            "Conv. Rate %", min_value=0, max_value=6, format="%.2f%%"
        ),
        "Reported": st.column_config.NumberColumn("Reported", format="%d"),
        "Convicted": st.column_config.NumberColumn("Convicted", format="%d"),
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
</div>
""", unsafe_allow_html=True)
