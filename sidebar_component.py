
import streamlit as st
import streamlit.components.v1 as components

DARK = {
    "navy": "#0a0f1e",
    "navy2": "#111827",
    "navy3": "#1a2540",
    "teal": "#2dd4bf",
    "white": "#f0f4ff",
}

THEME = DARK


def inject_sidebar(active_page="dashboard"):

    dash_active = "nav-active" if active_page == "dashboard" else ""
    legal_active = "nav-active" if active_page == "legal" else ""

    components.html(
        """
<!DOCTYPE html>
<html>
<head>
<style>

:root {{
    --sb-w: 260px;
    --bg: {DARK["navy"]};
    --card: {DARK["navy3"]};
    --text: {DARK["white"]};
    --teal: {DARK["teal"]};
}}

[data-theme="light"] {{
    --bg: #f4f6fb;
    --card: #dde4f0;
    --text: #0f172a;
    --teal: #0d9488;
}}

body {{
    margin:0;
}}

#toggle-btn {{
    position: fixed;
    top: 14px;
    left: 14px;
    z-index: 9999;
    background: var(--card);
    padding: 10px;
    border-radius: 6px;
    cursor: pointer;
}}

#sidebar {{
    position: fixed;
    top: 0;
    left: -260px;
    width: var(--sb-w);
    height: 100%;
    background: var(--card);
    transition: left 0.3s ease;
    z-index: 9998;
    padding-top: 60px;
}}

#sidebar.open {{
    left: 0;
}}

#overlay {{
    position: fixed;
    inset: 0;
    background: rgba(0,0,0,0.5);
    display: none;
    z-index: 9997;
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
</head>

<body>

<div id="toggle-btn">☰</div>
<div id="overlay"></div>

<div id="sidebar">
    <div class="nav">
        <a class="{dash_active}" href="/">Dashboard</a>
        <a class="{legal_active}" href="/Legal_Help_Guide">Legal Help</a>

        <hr>

        <a onclick="scrollToSection('section-01')">Section 1</a>
        <a onclick="scrollToSection('section-02')">Section 2</a>

        <hr>

        <label style="padding:10px; display:block;">
            Theme
            <input type="checkbox" id="themeToggle">
        </label>
    </div>
</div>

<script>

function initSidebar() {{
    const btn = document.getElementById("toggle-btn");
    const sidebar = document.getElementById("sidebar");
    const overlay = document.getElementById("overlay");
    const themeToggle = document.getElementById("themeToggle");

    if (!btn || !sidebar) return;

    // Toggle sidebar
    btn.onclick = () => {{
        sidebar.classList.toggle("open");
        overlay.classList.toggle("show");
    }};

    overlay.onclick = () => {{
        sidebar.classList.remove("open");
        overlay.classList.remove("show");
    }};

    // Theme
    const saved = localStorage.getItem("theme") || "dark";
    document.documentElement.setAttribute("data-theme", saved);
    themeToggle.checked = saved === "light";

    themeToggle.onchange = () => {{
        const theme = themeToggle.checked ? "light" : "dark";
        localStorage.setItem("theme", theme);
        document.documentElement.setAttribute("data-theme", theme);
    }};
}

// Smooth scroll
window.scrollToSection = function(id) {{
    const el = window.parent.document.getElementById(id);
    if (el) {{
        el.scrollIntoView({{behavior: "smooth"}});
    }}
}};

// INIT (IMPORTANT)
setTimeout(initSidebar, 300);

// Re-init after Streamlit rerender
const observer = new MutationObserver(() => {{
    initSidebar();
}});
observer.observe(document.body, {{childList:true, subtree:true}});

</script>

</body>
</html>
""",
        height=0,
    )

