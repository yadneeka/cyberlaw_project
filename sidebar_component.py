
"""
Shared custom sidebar + light/dark mode for the Cyberlaw India dashboard.
Import and call inject_sidebar(active_page) at the TOP of each page.

Usage:
    from sidebar_component import inject_sidebar, THEME
    inject_sidebar(active_page="dashboard")   # or "legal"
"""

import streamlit as st
import streamlit.components.v1 as components


# ─────────────────────────────────────────────────────────────
# THEME CONSTANTS
# ─────────────────────────────────────────────────────────────
DARK = {
    "navy": "#0a0f1e",
    "navy2": "#111827",
    "navy3": "#1a2540",
    "red": "#e63946",
    "amber": "#f4a261",
    "teal": "#2dd4bf",
    "white": "#f0f4ff",
    "muted": "#8892aa",
    "border": "#1e2d4a",
    "green": "#22c55e",
}

LIGHT = {
    "navy": "#f4f6fb",
    "navy2": "#e8edf5",
    "navy3": "#dde4f0",
    "red": "#c0202d",
    "amber": "#b85c10",
    "teal": "#0d9488",
    "white": "#0f172a",
    "muted": "#4a5568",
    "border": "#c5cfe0",
    "green": "#16a34a",
}

THEME = DARK


# ─────────────────────────────────────────────────────────────
# MAIN FUNCTION
# ─────────────────────────────────────────────────────────────
def inject_sidebar(active_page: str = "dashboard"):
    # ── Fix default sidebar width & button ──
    st.markdown(
        f"""
        <style>
        [data-testid="stSidebar"] {{
            min-width: 250px !important;
            max-width: 250px !important;
            background-color: {DARK['navy2']} !important;
        }}
        [data-testid="stSidebarCollapsedControl"] {{
            display: flex !important;
            z-index: 9999 !important;
        }}
        </style>
        """,
        unsafe_allow_html=True,
    )

    # ── Inject JS safely (NO f-string conflicts) ──
    components.html(
        """
        <script>
        window.scrollToSection = function(id) {
            const el = document.getElementById(id);
            if (el) {
                el.scrollIntoView({behavior: 'smooth'});
            }
        };

        function applyTheme(theme) {
            document.documentElement.setAttribute('data-theme', theme);
        }

        const saved = localStorage.getItem("theme") || "dark";
        applyTheme(saved);
        </script>
        """,
        height=0,
    )

    # ── Hide default sidebar ──
    st.markdown(
        """
        <style>
        [data-testid="stSidebar"] {display:none;}
        </style>
        """,
        unsafe_allow_html=True,
    )

    dash_active = "nav-active" if active_page == "dashboard" else ""
    legal_active = "nav-active" if active_page == "legal" else ""

    # ─────────────────────────────────────────────
    # MAIN SIDEBAR HTML
    # ─────────────────────────────────────────────
    st.markdown(
        f"""
<style>
:root {{
    --sb-w: 260px;
    --bg: #0a0f1e;
    --card: #1a2540;
    --text: #f0f4ff;
    --muted: #8892aa;
    --teal: #2dd4bf;
}}

body {{
    background: var(--bg);
    color: var(--text);
}}

#sidebar {{
    position: fixed;
    top: 0;
    left: -260px;
    width: var(--sb-w);
    height: 100%;
    background: var(--card);
    transition: 0.3s;
    z-index: 999;
}}

#sidebar.open {{
    left: 0;
}}

.toggle-btn {{
    position: fixed;
    top: 10px;
    left: 10px;
    z-index: 1000;
    cursor: pointer;
    background: var(--card);
    padding: 10px;
}}

.nav {{
    padding: 20px;
}}

.nav a {{
    display: block;
    padding: 10px;
    color: var(--text);
    text-decoration: none;
}}

.nav a.nav-active {{
    color: var(--teal);
}}

</style>

<div class="toggle-btn" onclick="toggleSidebar()">☰</div>

<div id="sidebar">
    <div class="nav">
        <a class="{dash_active}" href="/">Dashboard</a>
        <a class="{legal_active}" href="/Legal_Help_Guide">Legal Help</a>

        <hr>

        <a onclick="scrollToSection('section-01')">Section 1</a>
        <a onclick="scrollToSection('section-02')">Section 2</a>

        <hr>

        <label>
            Theme
            <input type="checkbox" onchange="toggleTheme(this.checked)">
        </label>
    </div>
</div>

<script>
function toggleSidebar() {{
    document.getElementById("sidebar").classList.toggle("open");
}}

function toggleTheme(isLight) {{
    const theme = isLight ? "light" : "dark";
    localStorage.setItem("theme", theme);
    document.documentElement.setAttribute("data-theme", theme);
}}
</script>
        """,
        unsafe_allow_html=True,
    )

