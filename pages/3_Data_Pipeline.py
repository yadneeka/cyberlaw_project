
import streamlit as st
from navbar import top_nav

# ------------------ PAGE CONFIG ------------------
st.set_page_config(page_title="Cyberlytics | Data Pipeline", layout="wide")

# ------------------ NAVBAR ------------------
top_nav("pipeline")

# ------------------ THEME ------------------
theme = st.session_state.get("theme", "dark")

if theme == "dark":
    card = "#1a2540"
    text = "#f0f4ff"
    muted = "#8892aa"
    border = "#1e2d4a"
else:
    card = "#ffffff"
    text = "#0f172a"
    muted = "#4a5568"
    border = "#e5e7eb"

# ------------------ HEADER ------------------
st.markdown("""
<h1 style="margin-bottom:0;">🔄 Data Pipeline</h1>
<p style="margin-top:5px;color:#8892aa;">
End-to-end flow from raw cybercrime data to actionable insights
</p>
""", unsafe_allow_html=True)

st.markdown("---")

# ------------------ PIPELINE FLOW ------------------
st.markdown("### ⚙️ Pipeline Flow")

st.markdown(f"""
<div style="display:flex;gap:10px;flex-wrap:wrap;align-items:center;">

<div style="padding:10px 16px;background:{card};border-radius:8px;">📊 Excel</div>
➡️
<div style="padding:10px 16px;background:{card};border-radius:8px;">🐍 Python</div>
➡️
<div style="padding:10px 16px;background:{card};border-radius:8px;">📈 MLflow</div>
➡️
<div style="padding:10px 16px;background:{card};border-radius:8px;">🌐 Git</div>
➡️
<div style="padding:10px 16px;background:{card};border-radius:8px;">📊 Dashboard</div>

</div>
""", unsafe_allow_html=True)

st.markdown("---")

# ------------------ STEP CARDS ------------------
st.markdown("### 🧱 Pipeline Components")

col1, col2, col3, col4, col5 = st.columns(5)

def card_block(title, desc):
    st.markdown(f"""
    <div style="
    background:{card};
    padding:15px;
    border-radius:10px;
    border:1px solid {border};
    min-height:140px;">
    <b>{title}</b>
    <p style="color:{muted};font-size:13px;">
    {desc}
    </p>
    </div>
    """, unsafe_allow_html=True)

with col1:
    card_block("Excel", "Raw cybercrime case records collected from structured datasets.")

with col2:
    card_block("Python", "Data cleaning, preprocessing, and feature extraction for analysis.")

with col3:
    card_block("MLflow", "Tracks experiments, model performance, and ensures reproducibility.")

with col4:
    card_block("Git", "Version control for code and pipeline updates.")

with col5:
    card_block("Streamlit", "Interactive dashboard for visualization and insights.")

st.markdown("---")

# ------------------ DATA PROCESSING ------------------
st.markdown("### ⚙️ Data Processing")

col1, col2 = st.columns(2)

with col1:
    st.markdown("""
- Duplicate removal  
- Missing value handling  
- Data normalization  
- Structured formatting  
""")

with col2:
    st.markdown("""
- Feature extraction  
- Crime classification  
- Aggregation for insights  
- Time-based grouping  
""")

st.markdown("---")

# ------------------ MLFLOW ------------------
st.markdown("### 🤖 MLflow Integration")

col1, col2, col3 = st.columns(3)

col1.metric("Latest Run", "v1.2")
col2.metric("Model Accuracy", "82%")
col3.metric("Experiments Logged", "15+")

st.info("MLflow enables experiment tracking, reproducibility, and performance monitoring.")

st.markdown("---")

# ------------------ DATA TRUST ------------------
st.markdown("### 🔍 Data Integrity & Trust")

st.success("✔ Data validated from reliable cybercrime sources")
st.info("✔ Preprocessing ensures consistency and removes anomalies")
st.info("✔ Version control maintains data integrity")
st.info("✔ MLflow guarantees reproducibility")

st.markdown("---")

# ------------------ BENEFITS ------------------
st.markdown("### 🚀 System Benefits")

col1, col2 = st.columns(2)

with col1:
    st.markdown("""
- Reproducible pipeline  
- Scalable architecture  
""")

with col2:
    st.markdown("""
- Transparent data flow  
- Easy maintenance & updates  
""")

st.markdown("---")

# ------------------ CALL TO ACTION ------------------
st.markdown(f"""
<div style="
padding:15px;
border-left:4px solid #2dd4bf;
background:{card};
border-radius:6px;">
<b>Cyberlytics Insight:</b> This pipeline ensures traceability from raw data ingestion to final insights, enabling reliable cybercrime analysis.
</div>
""", unsafe_allow_html=True)
