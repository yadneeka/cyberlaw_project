
import streamlit as st

DARK = {
    "navy": "#0a0f1e",
    "navy3": "#1a2540",
    "teal": "#2dd4bf",
    "white": "#f0f4ff",
}


def inject_sidebar(active_page="dashboard"):

    dash_active = "nav-active" if active_page == "dashboard" else ""
    legal_active = "nav-active" if active_page == "legal" else ""

    st.markdown(f"""
<style>

/* THEME */
:root {{
    --bg: {DARK["navy"]};
    --card: {DARK["navy3"]};
    --text: {DARK["white"]};
    --teal: {DARK["teal"]};
}}

/* BUTTON (FIXED + ALWAYS VISIBLE) */
#toggle-btn {{
    position: fixed;
    top: 14px;
    left: 14px;
    z-index: 99999;
    background: var(--card);
    padding: 10px;
    border-radius: 6px;
    cursor: pointer;
}}

/* SIDEBAR */
#sidebar {{
    position: fixed;
    top: 0;
    left: -260px;
    width: 260px;
    height: 100%;
    background: var(--card);
    transition: left 0.3s ease;
    z-index: 99998;
    padding-top: 60px;
}}

#sidebar.open {{
    left: 0;
}}

/* OVERLAY */
#overlay {{
    position: fixed;
    inset: 0;
    background: rgba(0,0,0,0.5);
    z-index: 99997;
    display: none;
}}

#overlay.show {{
    display: block;
}}

.nav a {{
    display: block;
    padding: 12px;
    color: var(--text);
    text-decoration: none;
}}

.nav a.nav-active {{
    color: var(--teal);
}}

</style>

<div id="toggle-btn">☰</div>
<div id="overlay"></div>

<div id="sidebar">
    <div class="nav">
        <a class="{dash_active}" href="/">Dashboard</a>
        <a class="{legal_active}" href="/Legal_Help_Guide">Legal Help</a>

        <hr>

        <a onclick="scrollToSection('section-01')">Section 1</a>
        <a onclick="scrollToSection('section-02')">Section 2</a>
    </div>
</div>

<script>

const btn = document.getElementById("toggle-btn");
const sidebar = document.getElementById("sidebar");
const overlay = document.getElementById("overlay");

btn.onclick = () => {{
    sidebar.classList.toggle("open");
    overlay.classList.toggle("show");
}};

overlay.onclick = () => {{
    sidebar.classList.remove("open");
    overlay.classList.remove("show");
}};

window.scrollToSection = function(id) {{
    const el = document.getElementById(id);
    if (el) el.scrollIntoView({{behavior:"smooth"}});
}};

</script>
""", unsafe_allow_html=True)
