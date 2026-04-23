Effectiveness of Digital Safety Laws for Women in India (2024–2026)


🔗 Click Here to Access the Live Dashboard : https://cyberlawproject.streamlit.app/

⚖️ The Problem Statement: The "Enforcement Gap"
Despite the rise in digital literacy and reporting mechanisms, a significant gap remains between cybercrime reporting and legal outcomes. This research analyzed 324,567 cases across 13 digital platforms to evaluate the effectiveness of the IT Act 2000 and BNS 2023.

Key Findings:

The 7x Bottleneck: While the national chargesheet rate stands at 15.9%, the conviction rate is only 2.24%. This indicates that cases are being successfully investigated and brought to court, but they are failing at the prosecution and judicial stages.

Platform Disparity: Large-scale platforms like WhatsApp account for high case volumes but show lower conviction rates (2.95%) compared to specialized enforcement units like Kerala's CyberDome (5.53%).

Legislative Lags: Emerging threats like AI-enabled deepfakes and voice cloning show the lowest conviction rates (sub-1%) due to a lack of dedicated legal provisions.

🛠️ Tool Rationale & Architecture
This project utilizes a structured DevOps pipeline to ensure the research is reproducible and accessible to non-technical stakeholders.

📈 MLflow for Traceability
Why: In academic research, data integrity is paramount. MLflow was chosen as the audit layer to track every iteration of the dataset.

Impact: Every change in platform-level metrics is logged as an "experiment," providing a timestamped, traceable history that proves the data hasn't been tampered with and ensures findings are reproducible.

🎨 Streamlit for Accessibility
Why: Traditional research often remains trapped in PDFs or complex spreadsheets. Streamlit was selected to transform raw data into an interactive advocacy tool.

Impact: By hosting the findings on a web-accessible dashboard, NGOs and policymakers can filter data by platform or crime category in real-time, allowing them to identify specific legal blind spots without needing any programming knowledge.

📂 Project Structure
app.py: The core Streamlit application logic.

Cyberlaw_Women_India_Verified_2024_2026.xlsx: The verified dataset curated from MHA, NCRB, and CERT-In reports.

cyberlaw_case_tracking.ipynb: The data processing and MLflow logging pipeline.

requirements.txt: Environment dependencies for cloud deployment.

🏛️ Data Sources & Credibility
All data displayed in this project is aggregated from verified Government of India publications:

MHA (Ministry of Home Affairs) Annual Reports 2023–24

NCRB (National Crime Records Bureau) Crime in India 2024

NCRP (National Cybercrime Reporting Portal) Parliamentary Data 2024–25

CERT-In Annual Advisories 2024–25

