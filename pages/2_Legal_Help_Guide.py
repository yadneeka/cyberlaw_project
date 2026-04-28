import streamlit as st

st.set_page_config(
    page_title="Legal Help Guide — Cyberlaw India",
    page_icon="🛡️",
    layout="wide",
    initial_sidebar_state="expanded",
)

# ── Shared CSS & Sidebar Width Fix ────────────────────────────────────────────
st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=Playfair+Display:wght@400;700;900&family=IBM+Plex+Mono:wght@400;500&family=IBM+Plex+Sans:wght@300;400;500;600&display=swap');

:root {
    --navy:   #0a0f1e; --navy2:  #111827; --navy3:  #1a2540;
    --red:    #e63946; --amber:  #f4a261; --teal:   #2dd4bf;
    --white:  #f0f4ff; --muted:  #8892aa; --border: #1e2d4a;
    --green:  #22c55e;
}

/* Sidebar Width Constraint */
[data-testid="stSidebar"] {
    min-width: 240px !important;
    max-width: 240px !important;
    background-color: var(--navy2) !important;
}

html, body, [data-testid="stAppViewContainer"] {
    background-color: var(--navy) !important; color: var(--white) !important;
}
[data-testid="stAppViewContainer"] > .main { background-color: var(--navy) !important; }
[data-testid="block-container"] { padding: 0 2rem 4rem 2rem !important; max-width: 1400px !important; }
#MainMenu, footer, header { visibility: hidden; }

/* Law table styling */
.law-table { width:100%; border-collapse:collapse; margin-top:0.5rem; background: var(--navy); }
.law-table th {
    background:var(--navy3); color:var(--teal);
    font-family:'IBM Plex Mono',monospace; font-size:0.7rem; 
    padding:0.8rem; border-bottom:2px solid var(--teal); text-align:left;
}
.law-table td {
    padding:0.8rem; border-bottom:1px solid var(--border);
    font-family:'IBM Plex Sans',sans-serif; font-size:0.85rem;
    color:var(--white); vertical-align:top;
}
.section-code { color:var(--amber); font-family:'IBM Plex Mono',monospace; font-weight:bold; }
.gender-tag {
    background:rgba(230,57,70,0.15); color:var(--red);
    padding:2px 6px; border-radius:3px; font-size:0.7rem;
}
.gender-tag.all { background:rgba(244,162,97,0.15); color:var(--amber); }

/* Hero Band */
.hero-band {
    background: linear-gradient(135deg, #0d1628 0%, #0a0f1e 100%);
    border: 1px solid var(--border); border-left: 4px solid var(--teal);
    padding: 2rem; margin-bottom: 2rem; border-radius: 6px;
}
</style>
""", unsafe_allow_html=True)

# ── HERO ───────────────────────────────────────────────────────────────────────
st.markdown("""
<div class="hero-band">
  <div style="font-family:'IBM Plex Mono',monospace;font-size:0.7rem;color:#2dd4bf;margin-bottom:0.5rem;">08 — LEGAL REFERENCE</div>
  <div style="font-family:'Playfair Display',serif;font-size:2rem;font-weight:900;color:#f0f4ff;margin-bottom:0.5rem;">Know Your Rights.</div>
  <div style="font-family:'IBM Plex Sans',sans-serif;font-size:0.95rem;color:#8892aa;max-width:700px;">
    Use the table below to find which law applies to your situation. IT Act sections are India's main cyber law, 
    while BNS replaces the old IPC.
  </div>
</div>
""", unsafe_allow_html=True)

# ── Filter Logic ──────────────────────────────────────────────────────────────
col1, col2 = st.columns([2, 3])
with col1:
    law_filter = st.selectbox("Filter by Law Type", ["All Laws", "IT Act 2000", "IPC (Old Law)", "BNS 2023 (New Law)"])
with col2:
    search = st.text_input("Search by crime or keyword", placeholder="e.g. stalking, hacking...")

# ── Data ──────────────────────────────────────────────────────────────────────
LAWS = [
    {"law": "IT Act 2000", "sec": "Section 66C", "crime": "Identity Theft", "desc": "Someone pretending to be you online using your name/photo.", "punish": "Up to 3 yrs + fine", "tag": "All"},
    {"law": "IT Act 2000", "sec": "Section 66E", "crime": "Privacy Violation", "desc": "Capturing or sharing intimate images without consent.", "punish": "Up to 3 yrs + 2L fine", "tag": "Women"},
    {"law": "IT Act 2000", "sec": "Section 67A", "crime": "Sexually Explicit Material", "desc": "Publishing/sharing sexually explicit content online (Revenge Porn).", "punish": "Up to 5 yrs + 10L fine", "tag": "Women"},
    {"law": "IPC (Old Law)", "sec": "Section 354D", "crime": "Cyberstalking", "desc": "Repeatedly following/monitoring a woman online against her will.", "punish": "Up to 3 yrs", "tag": "Women"},
    {"law": "BNS 2023 (New Law)", "sec": "BNS §308", "crime": "Extortion (Online)", "desc": "Threatening to release private info unless money is paid.", "punish": "Up to 10 yrs + fine", "tag": "All"}
]

# Apply Filters
filtered = [l for l in LAWS if (law_filter == "All Laws" or l['law'] == law_filter) and (search.lower() in l['crime'].lower() or search.lower() in l['desc'].lower())]

# ── Render Table Correctly ────────────────────────────────────────────────────
table_html = """
<table class="law-table">
    <thead>
        <tr>
            <th>Section</th>
            <th>Crime</th>
            <th>Description</th>
            <th>Punishment</th>
            <th>Applies To</th>
        </tr>
    </thead>
    <tbody>
"""

for l in filtered:
    tag_class = "gender-tag all" if l['tag'] == "All" else "gender-tag"
    table_html += f"""
        <tr>
            <td><span class="section-code">{l['sec']}</span><br><small style="color:#8892aa">{l['law']}</small></td>
            <td><strong>{l['crime']}</strong></td>
            <td>{l['desc']}</td>
            <td>{l['punish']}</td>
            <td><span class="{tag_class}">{l['tag']}</span></td>
        </tr>
    """

table_html += "</tbody></table>"

st.markdown(table_html, unsafe_allow_html=True)

# ── Footer ────────────────────────────────────────────────────────────────────
st.markdown(f'<div style="margin-top:3rem; color:#8892aa; font-size:0.7rem; text-align:center;">Yadneeka Sanjay Jadhav (SP47240003) | Guide: Prof. Kirti Garud</div>', unsafe_allow_html=True)