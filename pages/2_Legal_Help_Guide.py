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
[data-testid="stSidebar"] { background: var(--navy2) !important; border-right: 1px solid var(--border) !important; }

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


# ── SIDEBAR ────────────────────────────────────────────────────────────────────
with st.sidebar:
    st.markdown("""
    <div style="padding:1.2rem 0 0.5rem 0;">
      <div style="font-family:'IBM Plex Mono',monospace;font-size:0.6rem;
                  color:#2dd4bf;letter-spacing:0.15em;text-transform:uppercase;
                  margin-bottom:0.5rem;">Navigation</div>
      <div style="font-family:'Playfair Display',serif;font-size:1.1rem;
                  font-weight:700;color:#f0f4ff;margin-bottom:1.2rem;">Legal Help Guide</div>
    </div>
    <hr style="border-color:#1e2d4a;margin:0 0 1rem 0;">
    """, unsafe_allow_html=True)

    sections = [
        ("08", "Know Your Rights", "#know-your-rights"),
        ("09", "How to File a Complaint", "#how-to-file"),
        ("10", "Get Help Now", "#get-help"),
    ]
    for num, label, _ in sections:
        st.markdown(f"""
        <div style="display:flex;align-items:center;gap:0.7rem;
                    padding:0.55rem 0.6rem;border-radius:5px;margin-bottom:0.3rem;
                    background:rgba(45,212,191,0.05);border:1px solid rgba(45,212,191,0.1);">
          <span style="font-family:'IBM Plex Mono',monospace;font-size:0.6rem;
                       color:#2dd4bf;min-width:1.4rem;">{num}</span>
          <span style="font-family:'IBM Plex Sans',sans-serif;font-size:0.82rem;
                       color:#f0f4ff;">{label}</span>
        </div>""", unsafe_allow_html=True)

    st.markdown("""
    <hr style="border-color:#1e2d4a;margin:1.2rem 0 1rem 0;">
    <div style="font-family:'IBM Plex Mono',monospace;font-size:0.62rem;
                color:#8892aa;line-height:1.7;">
      🆘 <strong style="color:#e63946;">Emergency:</strong> 112<br>
      👩 Women's Helpline: 1091<br>
      🌐 Cyber Cell: 1930<br>
      📋 NCW: 7827-170-170
    </div>
    <hr style="border-color:#1e2d4a;margin:1rem 0;">
    <div style="font-family:'IBM Plex Mono',monospace;font-size:0.58rem;
                color:#8892aa;letter-spacing:0.04em;line-height:1.6;">
      SP47240003 · Yadneeka Jadhav<br>
      Guide: Prof. Kirti Garud<br>
      Research Project 2024–2026
    </div>
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
    # IT Act
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
    # IPC / BNS
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
    # BNS 2023 new provisions
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

# ── Render table using divs (Streamlit strips <table> tags) ───────────────────
# Header row
st.markdown("""
<div style="display:grid;grid-template-columns:150px 200px 1fr 200px 110px;
            gap:0;background:var(--navy3);border-radius:6px 6px 0 0;
            border:1px solid var(--border);border-bottom:2px solid var(--teal);
            padding:0.7rem 0.9rem;">
  <div style="font-family:'IBM Plex Mono',monospace;font-size:0.68rem;
              letter-spacing:0.1em;text-transform:uppercase;color:var(--teal);padding-right:0.5rem;">Section</div>
  <div style="font-family:'IBM Plex Mono',monospace;font-size:0.68rem;
              letter-spacing:0.1em;text-transform:uppercase;color:var(--teal);padding-right:0.5rem;">Crime Type</div>
  <div style="font-family:'IBM Plex Mono',monospace;font-size:0.68rem;
              letter-spacing:0.1em;text-transform:uppercase;color:var(--teal);padding-right:0.5rem;">What It Means + Examples</div>
  <div style="font-family:'IBM Plex Mono',monospace;font-size:0.68rem;
              letter-spacing:0.1em;text-transform:uppercase;color:var(--teal);padding-right:0.5rem;">Maximum Punishment</div>
  <div style="font-family:'IBM Plex Mono',monospace;font-size:0.68rem;
              letter-spacing:0.1em;text-transform:uppercase;color:var(--teal);">Applies To</div>
</div>
""", unsafe_allow_html=True)

for i, law in enumerate(filtered_laws):
    gt_class = "all" if law["gender_specific"] == "All" else ""
    bns_text = (
        f'<span style="font-family:\'IBM Plex Mono\',monospace;font-size:0.75rem;color:#2dd4bf;font-weight:600;">{law["bns_equiv"]}</span>'
        if law["bns_equiv"] != "—"
        else '<span style="color:#8892aa;font-size:0.75rem;">—</span>'
    )
    row_bg = "rgba(26,37,64,0.5)" if i % 2 == 1 else "transparent"
    gender_color = "#e63946" if law["gender_specific"] == "Women" else ("#f4a261" if law["gender_specific"] == "All" else "#2dd4bf")
    gender_bg   = "rgba(230,57,70,0.15)" if law["gender_specific"] == "Women" else ("rgba(244,162,97,0.12)" if law["gender_specific"] == "All" else "rgba(45,212,191,0.1)")
    gender_border= "rgba(230,57,70,0.35)" if law["gender_specific"] == "Women" else ("rgba(244,162,97,0.35)" if law["gender_specific"] == "All" else "rgba(45,212,191,0.4)")

    st.markdown(f"""
    <div style="display:grid;grid-template-columns:150px 200px 1fr 200px 110px;
                gap:0;background:{row_bg};
                border-left:1px solid var(--border);border-right:1px solid var(--border);
                border-bottom:1px solid var(--border);
                padding:0.75rem 0.9rem;
                transition:background 0.15s;"
         onmouseover="this.style.background='rgba(45,212,191,0.04)'"
         onmouseout="this.style.background='{row_bg}'">
      <div style="padding-right:0.8rem;vertical-align:top;">
        <span style="font-family:'IBM Plex Mono',monospace;font-size:0.78rem;
                     color:#f4a261;font-weight:600;white-space:nowrap;">{law["section"]}</span><br>
        <span style="font-size:0.68rem;color:#8892aa;font-family:'IBM Plex Mono',monospace;">BNS: </span>{bns_text}
      </div>
      <div style="padding-right:0.8rem;vertical-align:top;">
        <strong style="color:#f0f4ff;font-family:'IBM Plex Sans',sans-serif;font-size:0.83rem;">{law["crime"]}</strong><br>
        <span style="color:#8892aa;font-size:0.78rem;font-family:'IBM Plex Sans',sans-serif;">{law["law_type"]}</span>
      </div>
      <div style="padding-right:0.8rem;vertical-align:top;line-height:1.55;">
        <span style="color:#f0f4ff;font-family:'IBM Plex Sans',sans-serif;font-size:0.83rem;">{law["plain_english"]}</span>
        <br>
        <span style="color:#8892aa;font-size:0.77rem;font-style:italic;font-family:'IBM Plex Sans',sans-serif;">
          Examples: {law["examples"]}
        </span>
      </div>
      <div style="padding-right:0.8rem;font-size:0.78rem;color:#8892aa;
                  font-family:'IBM Plex Sans',sans-serif;line-height:1.5;">{law["punishment"]}</div>
      <div>
        <span style="display:inline-block;background:{gender_bg};
                     border:1px solid {gender_border};color:{gender_color};
                     font-family:'IBM Plex Mono',monospace;font-size:0.6rem;
                     padding:0.12rem 0.45rem;border-radius:3px;white-space:nowrap;">
          {law["gender_specific"]}
        </span>
      </div>
    </div>
    """, unsafe_allow_html=True)

# Closing border radius bottom
st.markdown('<div style="height:6px;background:var(--navy3);border:1px solid var(--border);border-top:none;border-radius:0 0 6px 6px;"></div>', unsafe_allow_html=True)

st.markdown("""
<div class="callout amber" style="margin-top:1rem;">
  <p>&#9888;&#65039; <strong>Important:</strong> Multiple laws can apply to the same incident. For example, 
  a revenge porn case can be filed under IT Act §67A (sexually explicit material), IPC §354C (voyeurism), 
  and BNS §308 (extortion) simultaneously. A lawyer or NGO counsellor can help identify which combination 
  gives the strongest case.</p>
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

st.markdown("""
<p style="font-family:'IBM Plex Sans',sans-serif;font-size:0.9rem;color:#8892aa;margin-bottom:1.5rem;line-height:1.6;">
There are four ways to report cybercrime in India. You can use more than one method — filing in multiple places strengthens your case. 
<strong style="color:#f0f4ff;">You do not need a lawyer to file the initial complaint.</strong>
</p>
""", unsafe_allow_html=True)

method_tab1, method_tab2, method_tab3, method_tab4 = st.tabs([
    "🌐  Method 1: NCRP Online",
    "🏢  Method 2: Local Cyber Cell",
    "👩‍⚖️  Method 3: NCW Online",
    "📧  Method 4: Email to SP Cyber"
])

with method_tab1:
    st.markdown("""
    <div style="padding:0.5rem 0 1rem 1.5rem;">
    <p style="font-family:'IBM Plex Sans',sans-serif;font-size:0.88rem;color:#8892aa;margin-bottom:1.2rem;">
    The <strong style="color:#f0f4ff;">National Cyber Crime Reporting Portal (NCRP)</strong> at 
    <a href="https://cybercrime.gov.in" target="_blank" style="color:#2dd4bf;">cybercrime.gov.in</a> 
    is India's official online complaint system. You can file from home, 24/7, without visiting a police station.
    It is the fastest route and is directly routed to the cyber cell of your state.
    </p>
    """, unsafe_allow_html=True)

    steps_m1 = [
        ("Go to the portal", "Visit <a href='https://cybercrime.gov.in' target='_blank' style='color:#2dd4bf;'>cybercrime.gov.in</a>. Click <strong>'File a Complaint'</strong>. You do not need to register first for an anonymous complaint, but registering lets you track the status.",
         "Use a laptop or desktop browser if possible — the mobile site works but the desktop version is easier to navigate."),
        ("Choose your crime category", "Select <strong>'Women / Child Related Crime'</strong> for most cases on this dashboard. If your case is financial fraud (investment scam, UPI fraud), select <strong>'Financial Fraud'</strong> instead.",
         "If unsure which category fits, use the Legal Reference table in Section 08 above to identify your applicable law first."),
        ("Fill in the complaint form", "Provide: your name and contact details (kept confidential), date and time of the incident, platform where it occurred (WhatsApp, Instagram, etc.), description of what happened in your own words. Upload any evidence you have.",
         "Write the description in plain, factual language. Dates, times, and platform names matter more than legal terms at this stage."),
        ("Collect your evidence first", "Before filing, screenshot or save: offensive messages/posts (with timestamps visible), the profile URL or phone number of the accused, any transaction records if money was involved, witness names if any.",
         "On mobile, take a screen recording — it captures the URL in the address bar which a screenshot alone may miss."),
        ("Submit and note your complaint ID", "After submitting, you will receive a <strong>complaint acknowledgement number</strong>. Save it — you will need it to track progress and follow up.",
         "Follow up after 15 days if you have not received a response. Use the 'Track Your Complaint' option on the same portal."),
    ]

    for i, (title, body, tip) in enumerate(steps_m1, 1):
        st.markdown(f"""
        <div class="step-card" style="margin-left:1rem;">
          <div class="step-num">{i}</div>
          <div style="margin-left:0.8rem;">
            <div class="step-title">{title}</div>
            <p class="step-body">{body}</p>
            <div class="step-tip">💡 Tip: {tip}</div>
          </div>
        </div>""", unsafe_allow_html=True)

    st.markdown("</div>", unsafe_allow_html=True)

with method_tab2:
    st.markdown("""
    <div style="padding:0.5rem 0 1rem 1.5rem;">
    <p style="font-family:'IBM Plex Sans',sans-serif;font-size:0.88rem;color:#8892aa;margin-bottom:1.2rem;">
    Every district in India has a <strong style="color:#f0f4ff;">Cyber Crime Cell</strong> — a specialised police unit 
    for cybercrime. Walking in person is recommended when you have physical evidence (a device, printed screenshots) 
    or when you need an FIR (First Information Report) to be filed immediately.
    </p>
    """, unsafe_allow_html=True)

    steps_m2 = [
        ("Find your nearest cyber cell", "Search Google for '<em>[your city] cyber crime cell address</em>' or call <strong>1930</strong> (National Cybercrime Helpline) and ask for your nearest cyber cell location.",
         "In Maharashtra, the Cyber Cell is part of the Crime Branch. Pune has a dedicated Cyber Crime Cell at the Crime Branch office, Shivajinagar."),
        ("Carry everything with you", "Bring: government-issued ID (Aadhaar/PAN), your mobile/laptop if the crime happened on the device, printed screenshots of evidence (or the device itself), written summary of the incident (dates, what happened, accused details if known).",
         "Write a brief summary in advance — 1 page, factual, chronological. This makes the officer's job easier and shows you are prepared."),
        ("Request a written complaint acknowledgement", "When you submit your complaint at the counter, ask the officer for a <strong>complaint acknowledgement receipt</strong> in writing. This is your right. If they refuse, note the officer's name and badge number.",
         "If the officer tells you this is not a cognizable offence or refuses to take the complaint, you can approach the Superintendent of Police directly or use Method 4 (email to SP Cyber)."),
        ("Request an FIR if appropriate", "If the crime is serious (threats, sexual content, financial loss over ₹1 lakh), request that an <strong>FIR be registered</strong>, not just a complaint. An FIR triggers a formal investigation and is stronger than a complaint.",
         "Under Section 154 of CrPC (now BNSS), the police are legally obligated to register an FIR for cognizable offences. Cyberstalking, NCII distribution, and sextortion are all cognizable."),
        ("Follow up in writing", "After 30 days with no update, send a written follow-up to the Cyber Cell (email or registered post) referencing your complaint number and requesting a status update.",
         "Keep a copy of every communication with the police. If the investigation stalls, you can approach the Magistrate under Section 156(3) of CrPC / BNSS to order the police to investigate."),
    ]

    for i, (title, body, tip) in enumerate(steps_m2, 1):
        st.markdown(f"""
        <div class="step-card" style="margin-left:1rem;">
          <div class="step-num">{i}</div>
          <div style="margin-left:0.8rem;">
            <div class="step-title">{title}</div>
            <p class="step-body">{body}</p>
            <div class="step-tip">💡 Tip: {tip}</div>
          </div>
        </div>""", unsafe_allow_html=True)

    st.markdown("</div>", unsafe_allow_html=True)

with method_tab3:
    st.markdown("""
    <div style="padding:0.5rem 0 1rem 1.5rem;">
    <p style="font-family:'IBM Plex Sans',sans-serif;font-size:0.88rem;color:#8892aa;margin-bottom:1.2rem;">
    The <strong style="color:#f0f4ff;">National Commission for Women (NCW)</strong> accepts online complaints 
    about cybercrimes against women at 
    <a href="https://ncwapps.nic.in/onlinecomplaintsv2/' target='_blank' style='color:#2dd4bf;">ncwapps.nic.in</a>. 
    NCW can intervene with police if your complaint is being ignored and can refer your case to state commissions.
    </p>
    """, unsafe_allow_html=True)

    steps_m3 = [
        ("Go to the NCW complaint portal", "Visit <a href='https://ncwapps.nic.in/onlinecomplaintsv2/' target='_blank' style='color:#2dd4bf;'>ncwapps.nic.in/onlinecomplaintsv2/</a>. Select <strong>'Cybercrime'</strong> as your complaint category.",
         "NCW is particularly effective when police have refused to register your complaint or when you need institutional pressure applied on state authorities."),
        ("Provide complete details", "Include: your state and district, police station jurisdiction, whether you have already filed with NCRP or cyber cell (and your complaint number if yes), description of the incident.",
         "Mentioning that you have already filed with NCRP or the Cyber Cell strengthens the NCW complaint — it shows you have exhausted primary channels."),
        ("NCW follow-up process", "NCW will forward your complaint to the concerned State Women's Commission and the police. You will receive a reference number. NCW holds regular review meetings with state police on pending women's cybercrime cases.",
         "NCW complaints are more effective for systemic pressure than for speedy resolution of individual cases. Use it alongside, not instead of, NCRP."),
    ]

    for i, (title, body, tip) in enumerate(steps_m3, 1):
        st.markdown(f"""
        <div class="step-card" style="margin-left:1rem;">
          <div class="step-num">{i}</div>
          <div style="margin-left:0.8rem;">
            <div class="step-title">{title}</div>
            <p class="step-body">{body}</p>
            <div class="step-tip">💡 Tip: {tip}</div>
          </div>
        </div>""", unsafe_allow_html=True)

    st.markdown("</div>", unsafe_allow_html=True)

with method_tab4:
    st.markdown("""
    <div style="padding:0.5rem 0 1rem 1.5rem;">
    <p style="font-family:'IBM Plex Sans',sans-serif;font-size:0.88rem;color:#8892aa;margin-bottom:1.2rem;">
    If the local Cyber Cell refuses your complaint or is unresponsive, you can escalate directly to the 
    <strong style="color:#f0f4ff;">Superintendent of Police (Cyber)</strong> of your district or state. 
    A written email creates a paper trail and triggers a duty to respond.
    </p>
    """, unsafe_allow_html=True)

    steps_m4 = [
        ("Find the SP Cyber email for your state", "Each state police has a Cyber Crime nodal officer. Search '<em>[your state] SP Cyber Crime email</em>' or visit your state police website. Maharashtra: <strong>cybercrime@mahapolice.gov.in</strong>. For other states, the NCRP helpline (1930) can provide the correct email.",
         "Always CC your complaint to the District Superintendent of Police as well — this ensures the email does not get lost in a large inbox."),
        ("Write a clear complaint email", """Use this structure:<br><br>
        <strong>Subject:</strong> Cybercrime Complaint — [Your Name] — [Crime Type] — Ref: [NCRP number if any]<br><br>
        <strong>Body:</strong><br>
        Para 1: Who you are, when and where the incident occurred.<br>
        Para 2: What exactly happened (factual, chronological).<br>
        Para 3: Laws you believe apply (use Section 08 of this guide).<br>
        Para 4: What action you are requesting (FIR registration, platform data preservation, accused identification).<br>
        Para 5: Previous complaints filed and their reference numbers.<br><br>
        Attach: screenshots, complaint acknowledgements, any evidence.""",
         "Keep the email under one page of body text. Attach evidence as a single PDF if possible — easier for officers to handle than multiple files."),
        ("Request data preservation urgently", "In the email, explicitly request that the police issue a <strong>data preservation notice</strong> to the platform (WhatsApp, Instagram, etc.) immediately. Platforms delete data after 90 days — this is time-critical.",
         "Under Section 67C of the IT Act, platforms are legally required to preserve data when asked by law enforcement. Mentioning this in your email signals legal awareness."),
        ("Send via registered email and post", "Send the email and simultaneously send a printed copy by <strong>India Post Registered Letter</strong> to the SP Cyber's office address. The postal acknowledgement is admissible evidence that your complaint was received.",
         "Keep the email in your sent folder and take a screenshot of the sent timestamp. If you need to escalate to the High Court later, this proves the date of complaint."),
    ]

    for i, (title, body, tip) in enumerate(steps_m4, 1):
        st.markdown(f"""
        <div class="step-card" style="margin-left:1rem;">
          <div class="step-num">{i}</div>
          <div style="margin-left:0.8rem;">
            <div class="step-title">{title}</div>
            <p class="step-body">{body}</p>
            <div class="step-tip">💡 Tip: {tip}</div>
          </div>
        </div>""", unsafe_allow_html=True)

    st.markdown("</div>", unsafe_allow_html=True)

st.markdown("""
<div class="callout green" style="margin-top:1.2rem;">
  <p>✅ <strong>Use all four methods if your case is serious.</strong> Filing with NCRP, the Cyber Cell, NCW, 
  and SP Cyber simultaneously — each referencing the others' complaint numbers — demonstrates seriousness, 
  creates multiple accountability threads, and makes it harder for any single office to ignore your case.</p>
</div>
""", unsafe_allow_html=True)


# ══════════════════════════════════════════════════════════════════════════════
# SECTION 10 — GET HELP NOW
# ══════════════════════════════════════════════════════════════════════════════
st.markdown("""
<div class="section-header" style="margin-top:3.5rem;">
  <span class="section-number">10 —</span>
  <p class="section-title">Get Help Now: Organisations & Helplines</p>
</div>""", unsafe_allow_html=True)

st.markdown("""
<p style="font-family:'IBM Plex Sans',sans-serif;font-size:0.9rem;color:#8892aa;margin-bottom:1.5rem;line-height:1.6;">
You do not have to navigate this alone. These organisations provide free legal support, counselling, 
and victim assistance specifically for cybercrime cases in India.
</p>
""", unsafe_allow_html=True)

# ── Emergency row ─────────────────────────────────────────────────────────────
st.markdown("""
<div style="display:flex;gap:1rem;margin-bottom:1.5rem;flex-wrap:wrap;">
  <div style="background:rgba(230,57,70,0.1);border:1px solid rgba(230,57,70,0.4);border-radius:6px;padding:1rem 1.5rem;min-width:160px;text-align:center;">
    <div style="font-family:'IBM Plex Mono',monospace;font-size:0.63rem;color:#8892aa;letter-spacing:0.1em;text-transform:uppercase;margin-bottom:0.3rem;">Emergency</div>
    <div class="hotline">112</div>
    <div style="font-family:'IBM Plex Sans',sans-serif;font-size:0.75rem;color:#8892aa;margin-top:0.3rem;">National Emergency</div>
  </div>
  <div style="background:rgba(230,57,70,0.1);border:1px solid rgba(230,57,70,0.4);border-radius:6px;padding:1rem 1.5rem;min-width:160px;text-align:center;">
    <div style="font-family:'IBM Plex Mono',monospace;font-size:0.63rem;color:#8892aa;letter-spacing:0.1em;text-transform:uppercase;margin-bottom:0.3rem;">Women's Helpline</div>
    <div class="hotline">1091</div>
    <div style="font-family:'IBM Plex Sans',sans-serif;font-size:0.75rem;color:#8892aa;margin-top:0.3rem;">24/7 Nationwide</div>
  </div>
  <div style="background:rgba(45,212,191,0.08);border:1px solid rgba(45,212,191,0.3);border-radius:6px;padding:1rem 1.5rem;min-width:160px;text-align:center;">
    <div style="font-family:'IBM Plex Mono',monospace;font-size:0.63rem;color:#8892aa;letter-spacing:0.1em;text-transform:uppercase;margin-bottom:0.3rem;">Cybercrime Helpline</div>
    <div class="hotline" style="color:#2dd4bf;border-color:rgba(45,212,191,0.4);background:rgba(45,212,191,0.1);">1930</div>
    <div style="font-family:'IBM Plex Sans',sans-serif;font-size:0.75rem;color:#8892aa;margin-top:0.3rem;">NCRP — 24/7</div>
  </div>
  <div style="background:rgba(244,162,97,0.08);border:1px solid rgba(244,162,97,0.3);border-radius:6px;padding:1rem 1.5rem;min-width:160px;text-align:center;">
    <div style="font-family:'IBM Plex Mono',monospace;font-size:0.63rem;color:#8892aa;letter-spacing:0.1em;text-transform:uppercase;margin-bottom:0.3rem;">NCW Helpline</div>
    <div class="hotline" style="color:#f4a261;border-color:rgba(244,162,97,0.4);background:rgba(244,162,97,0.1);">7827-170-170</div>
    <div style="font-family:'IBM Plex Sans',sans-serif;font-size:0.75rem;color:#8892aa;margin-top:0.3rem;">National Commission for Women</div>
  </div>
</div>
""", unsafe_allow_html=True)

# ── Organisation cards ────────────────────────────────────────────────────────
orgs = [
    {
        "name": "iCall — TISS",
        "focus": "Mental Health & Cyber Harassment Support",
        "color": "",
        "desc": "Free, confidential psychological counselling for cybercrime victims. Based at Tata Institute of Social Sciences, Mumbai. Provides both phone and online counselling. Particularly helpful for sextortion, cyberstalking, and deepfake trauma cases.",
        "contact": "📞 9152987821",
        "link": "https://icallhelpline.org",
        "link_text": "icallhelpline.org",
    },
    {
        "name": "Internet Freedom Foundation",
        "focus": "Legal Aid & Digital Rights Policy",
        "color": "amber",
        "desc": "India's leading digital rights organisation. Provides legal support for cybercrime victims, publishes policy research, and advocates for law reform. Their Access to Justice project specifically tracks cybercrime enforcement gaps.",
        "contact": "✉️ hello@internetfreedom.in",
        "link": "https://internetfreedom.in",
        "link_text": "internetfreedom.in",
    },
    {
        "name": "Cyber Peace Foundation",
        "focus": "Cybercrime Awareness & Reporting Support",
        "color": "",
        "desc": "Works with government, law enforcement, and citizens on cybercrime awareness and prevention. Provides a free cyber helpdesk for victims and runs digital literacy programmes specifically for women across India.",
        "contact": "✉️ contact@cyberpeace.org",
        "link": "https://cyberpeace.org",
        "link_text": "cyberpeace.org",
    },
    {
        "name": "Point of View",
        "focus": "Image-Based Abuse & Gender + Technology",
        "color": "amber",
        "desc": "Mumbai-based NGO specialising in gender, sexuality, and digital rights. Provides direct support for victims of morphed image abuse, revenge porn, and non-consensual intimate image distribution (NCII). Also trains police and judiciary.",
        "contact": "✉️ info@pointofview.org",
        "link": "https://pointofview.org",
        "link_text": "pointofview.org",
    },
    {
        "name": "National Commission for Women",
        "focus": "Official Government Body — Complaint Escalation",
        "color": "red",
        "desc": "Statutory body under the Government of India. Accepts cybercrime complaints against women and can intervene with state police. Filing with NCW adds institutional pressure when local police are unresponsive.",
        "contact": "📞 7827-170-170 | ncwapps.nic.in",
        "link": "https://ncwapps.nic.in/onlinecomplaintsv2/",
        "link_text": "File complaint online",
    },
    {
        "name": "IT for Change",
        "focus": "Gender, Technology & Policy Research",
        "color": "red",
        "desc": "Bangalore-based organisation working at the intersection of technology, gender, and governance. Publishes accessible policy research and supports grassroots organisations working with women on digital safety. Can amplify NGO findings.",
        "contact": "✉️ itfc@itforchange.net",
        "link": "https://itforchange.net",
        "link_text": "itforchange.net",
    },
]

cols = st.columns(3)
for i, org in enumerate(orgs):
    with cols[i % 3]:
        st.markdown(f"""
        <div class="help-card {org['color']}">
          <div class="help-org">{org['name']}</div>
          <div class="help-focus">{org['focus']}</div>
          <div class="help-desc">{org['desc']}</div>
          <div class="help-contact">
            {org['contact']}<br>
            <a href="{org['link']}" target="_blank">{org['link_text']}</a>
          </div>
        </div>
        <div style="margin-bottom:1rem;"></div>
        """, unsafe_allow_html=True)


# ── FOOTER ────────────────────────────────────────────────────────────────────
st.markdown("""
<div class="dash-footer">
    DATA SOURCES: IT Act 2000 (MeitY) &nbsp;·&nbsp; BNS 2023 (Ministry of Law) &nbsp;·&nbsp;
    NCRB Crime in India 2024 &nbsp;·&nbsp; NCW India &nbsp;·&nbsp; NCRP cybercrime.gov.in
    <br><br>
    Yadneeka Sanjay Jadhav (SP47240003) &nbsp;·&nbsp; Guide: Prof. Kirti Garud &nbsp;·&nbsp;
    Research Project 2024–2026 &nbsp;·&nbsp;
    <a href="https://github.com/yadneeka/cyberlaw_project" target="_blank"
       style="color:#2dd4bf;text-decoration:none;">GitHub</a>
</div>
""", unsafe_allow_html=True)
