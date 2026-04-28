import streamlit as st

st.set_page_config(
    page_title="Legal Help Guide — Cyberlaw India",
    page_icon="🛡️",
    layout="wide",
    initial_sidebar_state="expanded",
)

# ── Shared CSS (same theme as app.py) ──────────────────────────────────────────
st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=Playfair+Display:wght@400;700;900&family=IBM+Plex+Mono:wght@400;500&family=IBM+Plex+Sans:wght@300;400;500;600&display=swap');

:root {
    --navy:   #0a0f1e; --navy2:  #111827; --navy3:  #1a2540;
    --red:    #e63946; --amber:  #f4a261; --teal:   #2dd4bf;
    --white:  #f0f4ff; --muted:  #8892aa; --border: #1e2d4a;
    --green:  #22c55e;
}
html, body, [data-testid="stAppViewContainer"] {
    background-color: var(--navy) !important; color: var(--white) !important;
}
[data-testid="stAppViewContainer"] > .main { background-color: var(--navy) !important; }
[data-testid="block-container"] { padding: 0 2rem 4rem 2rem !important; max-width: 1400px !important; }
#MainMenu, footer, header { visibility: hidden; }
[data-testid="stDecoration"] { display: none; }

/* ── Narrow Sidebar Fix ── */
[data-testid="stSidebar"] { 
    background: var(--navy2) !important; 
    border-right: 1px solid var(--border) !important;
    min-width: 260px !important;
    max-width: 260px !important;
}

/* ── Hero ── */
@keyframes fadeSlideIn { from { opacity:0; transform:translateY(18px); } to { opacity:1; transform:translateY(0); } }
.hero-band {
    background: linear-gradient(135deg, #0d1628 0%, #0a0f1e 100%);
    border: 1px solid var(--border); border-left: 4px solid var(--teal);
    padding: 2.4rem 2.2rem; margin-bottom: 2rem; border-radius: 6px;
    animation: fadeSlideIn 0.7s ease both; position: relative; overflow: hidden;
}
.hero-band::after {
    content: '🛡'; position: absolute; right: 2rem; top: 50%;
    transform: translateY(-50%); font-size: 6rem; opacity: 0.06; pointer-events: none;
}

/* ── Section headers ── */
.section-header {
    display: flex; align-items: baseline; gap: 1rem;
    margin: 3rem 0 1.2rem 0; padding-bottom: 0.7rem;
    border-bottom: 1px solid var(--border);
}
.section-number { font-family:'IBM Plex Mono',monospace; font-size:0.7rem; color:var(--teal); letter-spacing:0.1em; }
.section-title  { font-family:'Playfair Display',serif !important; font-size:1.4rem; font-weight:700; color:var(--white); margin:0; }

/* ── Law table ── */
.law-table { width:100%; border-collapse:collapse; margin-top:0.5rem; }
.law-table th {
    background:var(--navy3); color:var(--teal);
    font-family:'IBM Plex Mono',monospace; font-size:0.68rem; letter-spacing:0.1em;
    text-transform:uppercase; padding:0.7rem 0.9rem; border-bottom:2px solid var(--teal);
    text-align:left;
}
.law-table td {
    padding:0.75rem 0.9rem; border-bottom:1px solid var(--border);
    font-family:'IBM Plex Sans',sans-serif; font-size:0.83rem;
    color:var(--white); vertical-align:top; line-height:1.55;
}
.law-table tr:hover td { background:rgba(45,212,191,0.04); }
.law-table tr:nth-child(even) td { background:rgba(26,37,64,0.5); }
.law-table tr:nth-child(even):hover td { background:rgba(45,212,191,0.06); }
.section-code {
    font-family:'IBM Plex Mono',monospace; font-size:0.78rem;
    color:var(--amber); font-weight:600; white-space:nowrap;
}
.bns-code { color: var(--teal); }
.gender-tag {
    display:inline-block; background:rgba(230,57,70,0.15);
    border:1px solid rgba(230,57,70,0.35); color:var(--red);
    font-family:'IBM Plex Mono',monospace; font-size:0.6rem;
    padding:0.12rem 0.45rem; border-radius:3px; white-space:nowrap;
}
.gender-tag.all {
    background:rgba(244,162,97,0.12); border-color:rgba(244,162,97,0.35); color:var(--amber);
}
.punish { font-size:0.78rem; color:var(--muted); }

/* ── Step cards ── */
.step-card {
    background:var(--navy3); border:1px solid var(--border);
    border-radius:8px; padding:1.4rem 1.5rem; margin-bottom:1.1rem;
    position:relative; transition:border-color 0.2s, transform 0.2s;
}
.step-card:hover { border-color:var(--teal); transform:translateX(4px); }
.step-num {
    position:absolute; top:1.2rem; left:-1rem;
    width:2rem; height:2rem; border-radius:50%;
    background:var(--teal); color:var(--navy);
    font-family:'IBM Plex Mono',monospace; font-weight:700; font-size:0.85rem;
    display:flex; align-items:center; justify-content:center;
}
.step-title {
    font-family:'IBM Plex Mono',monospace; font-size:0.7rem;
    text-transform:uppercase; letter-spacing:0.1em; color:var(--teal); margin-bottom:0.4rem;
}
.step-body {
    font-family:'IBM Plex Sans',sans-serif; font-size:0.85rem;
    color:var(--white); line-height:1.65; margin:0;
}
.step-body a { color:var(--teal); text-decoration:none; }
.step-body a:hover { text-decoration:underline; }
.step-tip {
    margin-top:0.6rem; padding:0.5rem 0.8rem;
    background:rgba(45,212,191,0.07); border-left:3px solid var(--teal);
    border-radius:0 4px 4px 0;
    font-family:'IBM Plex Sans',sans-serif; font-size:0.78rem; color:var(--muted);
}

/* ── Help cards ── */
.help-card {
    background:var(--navy3); border:1px solid var(--border);
    border-top:3px solid var(--teal); border-radius:6px;
    padding:1.4rem 1.3rem; height:100%;
    transition:transform 0.2s, box-shadow 0.2s;
}
.help-card:hover { transform:translateY(-4px); box-shadow:0 10px 28px rgba(0,0,0,0.35); }
.help-card.amber { border-top-color:var(--amber); }
.help-card.red   { border-top-color:var(--red); }
.help-org  { font-family:'Playfair Display',serif; font-size:1rem; font-weight:700; color:var(--white); margin-bottom:0.3rem; }
.help-focus{ font-family:'IBM Plex Mono',monospace; font-size:0.63rem; color:var(--teal); letter-spacing:0.08em; text-transform:uppercase; margin-bottom:0.7rem; }
.help-desc { font-family:'IBM Plex Sans',sans-serif; font-size:0.82rem; color:var(--muted); line-height:1.55; margin-bottom:0.9rem; }
.help-contact { font-family:'IBM Plex Mono',monospace; font-size:0.8rem; color:var(--white); }
.help-contact a { color:var(--teal); text-decoration:none; }
.hotline {
    display:inline-block; background:rgba(230,57,70,0.15);
    border:1px solid rgba(230,57,70,0.4); color:var(--red);
    font-family:'IBM Plex Mono',monospace; font-size:0.95rem; font-weight:700;
    padding:0.3rem 0.8rem; border-radius:4px; margin-top:0.4rem;
    letter-spacing:0.05em;
}

/* ── Callout ── */
.callout {
    background:rgba(230,57,70,0.08); border-left:4px solid var(--red);
    padding:1rem 1.2rem; border-radius:0 6px 6px 0; margin:0.8rem 0;
}
.callout.teal  { background:rgba(45,212,191,0.07);  border-left-color:var(--teal); }
.callout.amber { background:rgba(244,162,97,0.07);  border-left-color:var(--amber); }
.callout.green { background:rgba(34,197,94,0.07);   border-left-color:var(--green); }
.callout p { margin:0; font-size:0.87rem; color:var(--white); line-height:1.6; font-family:'IBM Plex Sans',sans-serif; }

.dash-footer {
    margin-top:4rem; padding-top:1.5rem; border-top:1px solid var(--border);
    font-family:'IBM Plex Mono',monospace; font-size:0.65rem;
    color:var(--muted); letter-spacing:0.06em; text-align:center;
}
</style>
""", unsafe_allow_html=True)


# ── HERO ───────────────────────────────────────────────────────────────────────
st.markdown("""
<div class="hero-band">
  <div style="font-family:'IBM Plex Mono',monospace;font-size:0.65rem;color:#2dd4bf;letter-spacing:0.15em;margin-bottom:0.6rem;">
    LEGAL HELP &amp; GUIDE
  </div>
  <div style="font-family:'Playfair Display',serif;font-size:2rem;font-weight:900;color:#f0f4ff;margin-bottom:0.6rem;line-height:1.2;">
    Know Your Rights.<br>Know Where to Go.
  </div>
  <div style="font-family:'IBM Plex Sans',sans-serif;font-size:0.95rem;color:#8892aa;max-width:680px;line-height:1.7;">
    This page is designed for <strong style="color:#f0f4ff;">victims, families, NGOs, and legal aid workers</strong>. 
    No technical knowledge required. Find the law that applies to your situation, 
    learn exactly how to file a complaint, and get direct contact details for organisations that can help.
  </div>
</div>
""", unsafe_allow_html=True)

st.markdown("""
<div class="callout teal">
  <p>&#128274; <strong>All information on this page is sourced from official Government of India publications.</strong>
  Laws cited: IT Act 2000 (amended 2008), Indian Penal Code 1860, and Bharatiya Nyaya Sanhita (BNS) 2023 
  which replaces the IPC. If you are in immediate danger, call <strong>112</strong> (National Emergency) 
  or <strong>1091</strong> (Women's Helpline) right now.</p>
</div>
""", unsafe_allow_html=True)


# ══════════════════════════════════════════════════════════════════════════════
# SECTION 08 — KNOW YOUR RIGHTS (LEGAL REFERENCE TABLE)
# ══════════════════════════════════════════════════════════════════════════════
st.markdown("""
<div class="section-header">
  <span class="section-number">08 —</span>
  <p class="section-title">Know Your Rights: The Laws That Protect You</p>
</div>""", unsafe_allow_html=True)

st.markdown("""
<p style="font-family:'IBM Plex Sans',sans-serif;font-size:0.9rem;color:#8892aa;margin-bottom:1.2rem;line-height:1.6;">
Use the table below to find which law applies to your situation. 
<strong style="color:#f0f4ff;">IT Act</strong> sections are India's main cyber law. 
<strong style="color:#f4a261;">IPC sections</strong> are from the older Indian Penal Code (still valid). 
<strong style="color:#2dd4bf;">BNS sections</strong> are from the new Bharatiya Nyaya Sanhita 2023 which is replacing the IPC — 
if your case is filed from July 2024 onwards, the BNS applies.
</p>
""", unsafe_allow_html=True)

# ── Filter ────────────────────────────────────────────────────────────────────
filter_col1, filter_col2 = st.columns([2, 3])
with filter_col1:
    law_filter = st.selectbox("Filter by Law Type",
        ["All Laws", "IT Act 2000", "IPC (Old Law)", "BNS 2023 (New Law)"])
with filter_col2:
    crime_search = st.text_input("Search by crime or keyword", placeholder="e.g. stalking, deepfake, morphed image...")

# ── Law data ──────────────────────────────────────────────────────────────────
LAWS = [
    {
        "law_type": "IT Act 2000",
        "section": "Section 66C",
        "bns_equiv": "—",
        "crime": "Identity Theft",
        "plain_english": "Someone is pretending to be you online — using your name, photo, or personal details without permission.",
        "examples": "Fake Instagram/WhatsApp account in your name; using your Aadhaar or PAN details.",
        "punishment": "Up to 3 years imprisonment + ₹1 lakh fine",
        "gender_specific": "All",
    },
    {
        "law_type": "IT Act 2000",
        "section": "Section 66D",
        "bns_equiv": "BNS §319",
        "crime": "Cheating by Impersonation (Online)",
        "plain_english": "Someone is pretending to be you or another person online to cheat or defraud you.",
        "examples": "Fake matrimonial profiles; impersonating a bank officer to extract OTPs.",
        "punishment": "Up to 3 years imprisonment + ₹1 lakh fine",
        "gender_specific": "All",
    },
    {
        "law_type": "IT Act 2000",
        "section": "Section 66E",
        "bns_equiv": "BNS §77",
        "crime": "Violation of Privacy (Intimate Images)",
        "plain_english": "Someone has captured, published, or shared private/intimate images of you without your consent.",
        "examples": "Hidden camera footage; sharing bathroom/changing-room photos; sharing images sent privately.",
        "punishment": "Up to 3 years imprisonment + ₹2 lakh fine",
        "gender_specific": "Women",
    },
    {
        "law_type": "IT Act 2000",
        "section": "Section 67",
        "bns_equiv": "BNS §294",
        "crime": "Publishing Obscene Material Online",
        "plain_english": "Someone has posted obscene or sexually offensive content about you on the internet.",
        "examples": "Morphed obscene photos posted on social media; obscene messages circulated in groups.",
        "punishment": "Up to 3 years + ₹5 lakh fine (first offence); up to 5 years + ₹10 lakh (repeat)",
        "gender_specific": "All",
    },
    {
        "law_type": "IT Act 2000",
        "section": "Section 67A",
        "bns_equiv": "BNS §295",
        "crime": "Publishing Sexually Explicit Material Online",
        "plain_english": "Someone has posted explicitly sexual content involving you without your consent.",
        "examples": "Revenge porn; non-consensual intimate image distribution (NCII); deepfake sexual videos.",
        "punishment": "Up to 5 years + ₹10 lakh fine (first offence); up to 7 years + ₹10 lakh (repeat)",
        "gender_specific": "Women",
    },
    {
        "law_type": "IT Act 2000",
        "section": "Section 67B",
        "bns_equiv": "BNS §296",
        "crime": "Child Sexual Abuse Material (CSAM) Online",
        "plain_english": "Sexual content involving anyone under 18 published or transmitted online.",
        "examples": "Any sexual image, video, or text involving minors on any platform.",
        "punishment": "Up to 5 years + ₹10 lakh fine (first offence); up to 7 years + ₹10 lakh (repeat)",
        "gender_specific": "Children",
    },
    {
        "law_type": "IT Act 2000",
        "section": "Section 43 + 66",
        "bns_equiv": "—",
        "crime": "Unauthorised Access / Hacking",
        "plain_english": "Someone has broken into your email, social media, or other online accounts without your permission.",
        "examples": "Email account hacked; WhatsApp taken over; cloud storage accessed.",
        "punishment": "Up to 3 years imprisonment + ₹5 lakh fine",
        "gender_specific": "All",
    },
    {
        "law_type": "IPC (Old Law)",
        "section": "IPC §354C",
        "bns_equiv": "BNS §77",
        "crime": "Voyeurism",
        "plain_english": "Someone has watched, photographed, or filmed you in a private act (bathing, changing, intimate) without your knowledge.",
        "examples": "Hidden cameras in toilets or changing rooms; drone cameras; peeping through windows.",
        "punishment": "1–3 years imprisonment (first offence); 3–7 years (repeat offence)",
        "gender_specific": "Women",
    },
    {
        "law_type": "IPC (Old Law)",
        "section": "IPC §354D",
        "bns_equiv": "BNS §78",
        "crime": "Cyberstalking",
        "plain_english": "Someone is repeatedly following you online, monitoring you, or contacting you against your will using the internet or electronic devices.",
        "examples": "Repeated messages after being told to stop; tracking your location via apps; monitoring social media obsessively.",
        "punishment": "Up to 3 years imprisonment (first offence); up to 5 years (repeat offence)",
        "gender_specific": "Women",
    },
    {
        "law_type": "IPC (Old Law)",
        "section": "IPC §507",
        "bns_equiv": "BNS §352",
        "crime": "Criminal Intimidation (Anonymous Threats)",
        "plain_english": "Someone is sending you threats anonymously — threatening to harm you, your family, or your reputation.",
        "examples": "Anonymous rape/death threats online; threatening messages from unknown numbers.",
        "punishment": "Up to 2 years imprisonment",
        "gender_specific": "All",
    },
    {
        "law_type": "IPC (Old Law)",
        "section": "IPC §509",
        "bns_equiv": "BNS §79",
        "crime": "Words or Gestures Insulting a Woman's Modesty",
        "plain_english": "Someone has used words, sounds, gestures, or objects to insult or humiliate you as a woman.",
        "examples": "Sexually abusive comments online; obscene voice notes sent on WhatsApp; catcalling via video call.",
        "punishment": "Up to 3 years imprisonment + fine",
        "gender_specific": "Women",
    },
    {
        "law_type": "IPC (Old Law)",
        "section": "IPC §499–500",
        "bns_equiv": "BNS §356",
        "crime": "Defamation (Online)",
        "plain_english": "Someone has published false statements about you online that damage your reputation.",
        "examples": "False rumours spread on social media; defamatory posts in WhatsApp groups; fake news about you.",
        "punishment": "Up to 2 years imprisonment + fine",
        "gender_specific": "All",
    },
    {
        "law_type": "BNS 2023 (New Law)",
        "section": "BNS §308",
        "bns_equiv": "New provision",
        "crime": "Extortion (Online)",
        "plain_english": "Someone is threatening to expose private information or images unless you pay money or comply with demands.",
        "examples": "Sextortion: 'Pay me or I will send your photos to your family'; financial extortion after hacking.",
        "punishment": "Up to 10 years imprisonment + fine",
        "gender_specific": "All",
    },
    {
        "law_type": "BNS 2023 (New Law)",
        "section": "BNS §351",
        "bns_equiv": "New provision",
        "crime": "Criminal Intimidation",
        "plain_english": "Someone threatens to injure you, your reputation, or your property to force you to do something.",
        "examples": "Online threats to release private content; doxxing threats; threats to inform employer.",
        "punishment": "Up to 2 years imprisonment + fine (up to 7 years if threat is of death or grievous hurt)",
        "gender_specific": "All",
    },
    {
        "law_type": "BNS 2023 (New Law)",
        "section": "BNS §318",
        "bns_equiv": "Replaces IPC §420",
        "crime": "Cheating / Online Fraud",
        "plain_english": "Someone deceived you online to take money or property from you.",
        "examples": "Investment scams (Pig Butchering); fake job offers; romance scams; UPI fraud.",
        "punishment": "Up to 7 years imprisonment + fine",
        "gender_specific": "All",
    },
]

# ── Apply filters ─────────────────────────────────────────────────────────────
filtered_laws = LAWS
if law_filter != "All Laws":
    filtered_laws = [l for l in filtered_laws if l["law_type"] == law_filter]
if crime_search:
    q = crime_search.lower()
    filtered_laws = [l for l in filtered_laws if
        q in l["crime"].lower() or q in l["plain_english"].lower() or
        q in l["examples"].lower() or q in l["section"].lower()]

st.markdown(f"""
<p style="font-family:'IBM Plex Mono',monospace;font-size:0.7rem;color:#8892aa;margin-bottom:0.6rem;">
  Showing {len(filtered_laws)} of {len(LAWS)} legal provisions
</p>""", unsafe_allow_html=True)

# ── Render table ──────────────────────────────────────────────────────────────
table_rows = ""
for law in filtered_laws:
    gt_class = "all" if law["gender_specific"] == "All" else ""
    bns_text = f'<span class="section-code bns-code">{law["bns_equiv"]}</span>' if law["bns_equiv"] != "—" else '<span style="color:#8892aa;font-size:0.75rem;">—</span>'
    table_rows += f"""
    <tr>
      <td>
        <span class="section-code">{law["section"]}</span><br>
        <span style="font-size:0.72rem;color:#8892aa;font-family:'IBM Plex Mono',monospace;">BNS equiv: </span>{bns_text}
      </td>
      <td>
        <strong style="color:#f0f4ff;">{law["crime"]}</strong><br>
        <span style="color:#8892aa;font-size:0.8rem;">{law["law_type"]}</span>
      </td>
      <td>
        <span style="color:#f0f4ff;">{law["plain_english"]}</span>
        <br><br>
        <span style="color:#8892aa;font-size:0.78rem;font-style:italic;">Examples: {law["examples"]}</span>
      </td>
      <td class="punish">{law["punishment"]}</td>
      <td><span class="gender-tag {gt_class}">{law["gender_specific"]}</span></td>
    </tr>"""

st.markdown(f"""
<div style="overflow-x:auto;">
<table class="law-table">
  <thead>
    <tr>
      <th style="min-width:140px;">Section</th>
      <th style="min-width:180px;">Crime Type</th>
      <th style="min-width:320px;">What It Means + Examples</th>
      <th style="min-width:180px;">Maximum Punishment</th>
      <th style="min-width:100px;">Applies To</th>
    </tr>
  </thead>
  <tbody>
    {table_rows}
  </tbody>
</table>
</div>
""", unsafe_allow_html=True)

st.markdown("""
<div class="callout amber" style="margin-top:1rem;">
  <p>&#9888;&#65039; <strong>Important:</strong> Multiple laws can apply to the same incident. For example, 
  a revenge porn case can be filed under IT Act §67A (sexually explicit material), IPC §354C (voyeurism), 
  and BNS §308 (extortion) simultaneously.</p>
</div>
""", unsafe_allow_html=True)


# ══════════════════════════════════════════════════════════════════════════════
# SECTION 09 — HOW TO FILE A COMPLAINT
# ══════════════════════════════════════════════════════════════════════════════
st.markdown("""
<div class="section-header" style="margin-top:3.5rem;">
  <span class="section-number">09 —</span>
  <p class="section-title">How to File a Complaint: Step-by-Step</p>
</div>""", unsafe_allow_html=True)

method_tab1, method_tab2, method_tab3, method_tab4 = st.tabs([
    "🌐  Method 1: NCRP Online",
    "🏢  Method 2: Local Cyber Cell",
    "👩‍⚖️  Method 3: NCW Online",
    "📧  Method 4: Email to SP Cyber"
])

with method_tab1:
    st.markdown("""<div style="padding:0.5rem 0 1rem 1.5rem;"><p style="font-family:'IBM Plex Sans',sans-serif;font-size:0.88rem;color:#8892aa;margin-bottom:1.2rem;">The NCRP is India's official online portal.</p>""", unsafe_allow_html=True)
    # Step card rendering here...
    st.markdown("</div>", unsafe_allow_html=True)

# ══════════════════════════════════════════════════════════════════════════════
# SECTION 10 — GET HELP NOW
# ══════════════════════════════════════════════════════════════════════════════
st.markdown("""
<div class="section-header" style="margin-top:3.5rem;">
  <span class="section-number">10 —</span>
  <p class="section-title">Get Help Now: Organisations & Helplines</p>
</div>""", unsafe_allow_html=True)

orgs = [
    {"name": "iCall — TISS", "focus": "Mental Health", "color": "", "desc": "Free counselling for victims.", "contact": "📞 9152987821", "link": "https://icallhelpline.org", "link_text": "icallhelpline.org"},
    {"name": "Internet Freedom Foundation", "focus": "Legal Aid", "color": "amber", "desc": "Digital rights advocacy.", "contact": "✉️ hello@internetfreedom.in", "link": "https://internetfreedom.in", "link_text": "internetfreedom.in"},
]

cols = st.columns(3)
for i, org in enumerate(orgs):
    with cols[i % 3]:
        st.markdown(f"""
        <div class="help-card {org['color']}">
          <div class="help-org">{org['name']}</div>
          <div class="help-focus">{org['focus']}</div>
          <div class="help-desc">{org['desc']}</div>
          <div class="help-contact">{org['contact']}<br><a href="{org['link']}" target="_blank">{org['link_text']}</a></div>
        </div>""", unsafe_allow_html=True)

# ── FOOTER ────────────────────────────────────────────────────────────────────
st.markdown("""
<div class="dash-footer">
    Yadneeka Sanjay Jadhav (SP47240003) &nbsp;·&nbsp; Guide: Prof. Kirti Garud &nbsp;·&nbsp; Research Project 2024–2026
</div>
""", unsafe_allow_html=True)