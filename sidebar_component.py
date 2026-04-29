
import streamlit as st
import streamlit.components.v1 as components

DARK = {
    "navy": "#0a0f1e",
    "navy3": "#1a2540",
    "teal": "#2dd4bf",
    "white": "#f0f4ff",
}

THEME = DARK


def inject_sidebar(active_page="dashboard"):

    dash_active = "nav-active" if active_page == "dashboard" else ""
    legal_active = "nav-active" if active_page == "legal" else ""

    # ✅ STEP 1: Inject CSS variables (SAFE f-string)
    st.markdown(f"""
    <style>
    :root {{
        --bg: {DARK["navy"]};
        --card: {DARK["navy3"]};
        --text: {DARK["white"]};
        --teal: {DARK["teal"]};
    }}
    </style>
    """, unsafe_allow_html=True)

    # ✅ STEP 2: PURE HTML + JS (NO f-string → no crash)
    components.html("""
<!DOCTYPE html>
<html>
<head>
<style>

#toggle-btn {
    position: fixed;
    top: 14px;
    left: 14px;
    z-index: 10001;
    background: var(--card);
    padding: 10px;
    border-radius: 6px;
    cursor: pointer;
}

#sidebar {
    position: fixed;
    top: 0;
    left: -260px;
    width: 260px;
    height: 100%;
    background: var(--card);
    transition: left 0.3s ease;
    z-index: 10000;
    padding-top: 60px;
}

#sidebar.open {
    left: 0;
}

#overlay {
    position: fixed;
    inset: 0;
    background: rgba(0,0,0,0.5);
    z-index: 9999;
    display: none;
    pointer-events: none;
}

#overlay.show {
    display: block;
    pointer-events: auto;
}

.nav a {
    display: block;
    padding: 12px;
    color: var(--text);
    text-decoration: none;
}

.nav a.nav-active {
    color: var(--teal);
}

</style>
</head>

<body>

<div id="toggle-btn">☰</div>
<div id="overlay"></div>

<div id="sidebar">
    <div class="nav">
        <a href="/">Dashboard</a>
        <a href="/Legal_Help_Guide">Legal Help</a>

        <hr>

        <a onclick="scrollToSection('section-01')">Section 1</a>
        <a onclick="scrollToSection('section-02')">Section 2</a>

        <hr>

        <label style="padding:10px;">
            Theme
            <input type="checkbox" id="themeToggle">
        </label>
    </div>
</div>

<script>

function initSidebar() {
    const btn = document.getElementById("toggle-btn");
    const sidebar = document.getElementById("sidebar");
    const overlay = document.getElementById("overlay");

    if (!btn || !sidebar || !overlay) return;

    btn.onclick = () => {
        const isOpen = sidebar.classList.contains("open");

        if (isOpen) {
            sidebar.classList.remove("open");
            overlay.classList.remove("show");
        } else {
            sidebar.classList.add("open");
            overlay.classList.add("show");
        }
    };

    overlay.onclick = () => {
        sidebar.classList.remove("open");
        overlay.classList.remove("show");
    };
}

// scroll
window.scrollToSection = function(id) {
    const el = window.parent.document.getElementById(id);
    if (el) el.scrollIntoView({ behavior: "smooth" });
};

// init
setTimeout(initSidebar, 300);

// fix rerender
const observer = new MutationObserver(() => {
    initSidebar();
});
observer.observe(document.body, { childList: true, subtree: true });

</script>

</body>
</html>
""", height=0)
