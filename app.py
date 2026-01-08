import streamlit as st

st.set_page_config(
    page_title="CampusFlow Pro",
    page_icon="🎓",
    layout="wide",
    initial_sidebar_state="expanded"
)

THEMES = {
    "dark": {
        "bg": "#0d1017",
        "panel": "#0f131d",
        "card": "#131925",
        "border": "#1f2633",
        "text": "#f5f7fb",
        "muted": "#c2c7d2",
        "accent": "#ffffff",
        "subtle": "#1b2030",
        "sidebar": "#0b0d13",
        "track": "#1f2430",
        "fill": "#f7fafc"
    },
    "light": {
        "bg": "#f7f8fb",
        "panel": "#ffffff",
        "card": "#ffffff",
        "border": "#e5e7eb",
        "text": "#0f172a",
        "muted": "#4b5563",
        "accent": "#0f172a",
        "subtle": "#eef1f6",
        "sidebar": "#f5f7fb",
        "track": "#e5e7eb",
        "fill": "#0f172a"
    },
}

if "theme" not in st.session_state:
    st.session_state.theme = "dark"

if "current_page" not in st.session_state:
    st.session_state.current_page = "dashboard"

if "uploaded_file" not in st.session_state:
    st.session_state.uploaded_file = None

if "file_processed" not in st.session_state:
    st.session_state.file_processed = False

colors = THEMES[st.session_state.theme]

st.markdown(
    f"""
<style>
    :root {{
        --bg: {colors['bg']};
        --panel: {colors['panel']};
        --card: {colors['card']};
        --border: {colors['border']};
        --text: {colors['text']};
        --muted: {colors['muted']};
        --accent: {colors['accent']};
        --subtle: {colors['subtle']};
        --sidebar: {colors['sidebar']};
        --track: {colors['track']};
        --fill: {colors['fill']};
    }}

    [data-testid="stAppViewContainer"] {{
        background: var(--bg);
    }}

    .main {{
        padding: 0 1.25rem 2rem 1.25rem;
        background: var(--bg);
    }}

    .header-container {{
        background: var(--panel);
        padding: 2.25rem;
        border-radius: 0px;
        margin-bottom: 1.5rem;
        border: 1px solid var(--border);
    }}

    .header-title {{
        color: var(--accent);
        font-size: 2.5rem;
        font-weight: 700;
        margin: 0;
        line-height: 1.1;
    }}

    .header-subtitle {{
        color: var(--muted);
        font-size: 1.05rem;
        margin-top: 0.5rem;
    }}

    .stat-card {{
        background: var(--card);
        padding: 1.5rem;
        border-radius: 0px;
        border: 1px solid var(--border);
    }}

    .stat-label {{
        color: var(--muted);
        font-size: 0.9rem;
        font-weight: 600;
        letter-spacing: 0.3px;
    }}

    .stat-value {{
        color: var(--accent);
        font-size: 2.1rem;
        font-weight: 700;
        margin: 0.4rem 0;
    }}

    .stat-trend {{
        color: var(--muted);
        font-size: 0.9rem;
    }}

    .task-card {{
        background: var(--card);
        padding: 1.5rem;
        border: 1px solid var(--border);
        margin-bottom: 1rem;
    }}

    .task-title {{
        font-size: 1.05rem;
        font-weight: 600;
        color: var(--accent);
        margin-bottom: 0.35rem;
    }}

    .task-meta {{
        color: var(--muted);
        font-size: 0.9rem;
    }}

    .priority-high {{
        background: var(--accent);
        color: var(--bg);
        padding: 0.25rem 0.75rem;
        font-size: 0.75rem;
        font-weight: 700;
        border: 1px solid var(--accent);
    }}

    .priority-medium {{
        background: transparent;
        color: var(--accent);
        padding: 0.25rem 0.75rem;
        font-size: 0.75rem;
        font-weight: 700;
        border: 1px solid var(--accent);
    }}

    .progress-container {{
        background: var(--track);
        height: 8px;
        overflow: hidden;
        margin-top: 0.5rem;
        border: 1px solid var(--border);
    }}

    .progress-bar {{
        background: var(--fill);
        height: 100%;
        transition: width 0.3s ease;
    }}

    .activity-item {{
        padding: 1rem;
        border-left: 3px solid var(--accent);
        background: var(--card);
        border: 1px solid var(--border);
        margin-bottom: 1rem;
    }}

    [data-testid="stSidebar"] {{
        background: var(--sidebar);
    }}

    [data-testid="stSidebar"] * {{
        color: var(--text) !important;
    }}

    .sidebar-brand {{
        text-align: center;
        margin-bottom: 1.5rem;
    }}

    .sidebar-brand h1 {{
        margin: 0;
        font-size: 1.4rem;
        font-weight: 700;
    }}

    .sidebar-brand p {{
        margin: 0.35rem 0 0 0;
        color: var(--muted);
        font-size: 0.95rem;
    }}

    [data-testid="stSidebar"] [role="radiogroup"] {{
        gap: 0.25rem;
    }}

    [data-testid="stSidebar"] [role="radio"] {{
        background: transparent;
        border: 1px solid transparent;
        padding: 0.55rem 0.75rem;
        border-radius: 0px;
        font-weight: 600;
        width: 100%;
    }}

    [data-testid="stSidebar"] [role="radio"] > div:first-child {{
        display: none;
    }}

    [data-testid="stSidebar"] [aria-checked="true"] {{
        background: var(--card);
        border: 1px solid var(--border);
    }}

    .quick-card {{
        background: var(--card);
        border: 1px solid var(--border);
        padding: 1rem;
        margin-top: 1rem;
    }}

    .quick-row {{
        display: flex;
        justify-content: space-between;
        align-items: center;
        margin-bottom: 0.75rem;
        color: var(--accent);
        font-weight: 700;
    }}

    .quick-muted {{
        color: var(--muted);
        font-weight: 600;
        font-size: 0.9rem;
    }}

    .delta-positive, .delta-negative {{
        padding: 0.1rem 0.35rem;
        border: 1px solid var(--border);
        background: var(--card);
        color: var(--accent);
        font-size: 0.8rem;
        border-radius: 12px;
        margin-left: 0.35rem;
    }}

    .stButton > button {{
        width: 100%;
        background: var(--accent);
        color: {colors['bg']};
        border: 1px solid var(--border);
        border-radius: 0px;
        padding: 0.75rem 1rem;
        font-weight: 700;
    }}

    .stTextInput > div > div input,
    .stSelectbox > div > div,
    .stMultiSelect > div > div,
    .stSlider {{
        background: var(--card);
        color: var(--accent);
        border: 1px solid var(--border);
    }}

    .stSlider [role="slider"] {{
        background: var(--accent);
    }}

    .stMultiSelect div[data-baseweb="tag"] {{
        background: var(--card);
        border: 1px solid var(--border);
        color: var(--accent);
        border-radius: 0px;
    }}
</style>
""",
    unsafe_allow_html=True,
)


def render_header(title: str, subtitle: str) -> None:
    st.markdown(
        f"""
        <div class="header-container">
            <h1 class="header-title">{title}</h1>
            <p class="header-subtitle">{subtitle}</p>
        </div>
        """,
        unsafe_allow_html=True,
    )


def render_stat(label: str, value: str, trend: str) -> None:
    st.markdown(
        f"""
        <div class="stat-card">
            <div class="stat-label">{label}</div>
            <div class="stat-value">{value}</div>
            <div class="stat-trend">{trend}</div>
        </div>
        """,
        unsafe_allow_html=True,
    )


def render_tasks() -> None:
    st.markdown("### 📋 Upcoming Tasks")
    
    if st.session_state.file_processed and st.session_state.uploaded_file:
        tasks = [
            {"title": "Review Document Summary", "course": st.session_state.uploaded_file.name[:20], "deadline": "2 days", "priority": "high", "progress": 45},
            {"title": "Complete Flashcard Practice", "course": "Study Materials", "deadline": "4 days", "priority": "medium", "progress": 30},
            {"title": "Follow Study Plan Week 1", "course": "Learning Path", "deadline": "1 week", "priority": "medium", "progress": 15},
        ]
        
        for task in tasks:
            st.markdown(
                f"""
                <div class="task-card">
                    <div style="display: flex; justify-content: space-between; align-items: start;">
                        <div>
                            <div class="task-title">{task['title']}</div>
                            <div class="task-meta">{task['course']} • Due in {task['deadline']}</div>
                        </div>
                        <span class="priority-{task['priority']}">{task['priority'].upper()}</span>
                    </div>
                    <div style="margin-top: 1rem;">
                        <div style="display: flex; justify-content: space-between; font-size: 0.85rem; color: var(--muted);">
                            <span>Progress</span>
                            <span style="font-weight: 700; color: var(--accent);">{task['progress']}%</span>
                        </div>
                        <div class="progress-container">
                            <div class="progress-bar" style="width: {task['progress']}%;"></div>
                        </div>
                    </div>
                </div>
                """,
                unsafe_allow_html=True,
            )
    else:
        st.info("No tasks available. Upload a document to get started.")


def render_activity() -> None:
    st.markdown("### 🕐 Recent Activity")
    
    if st.session_state.file_processed and st.session_state.uploaded_file:
        activities = [
            {"action": "Processed document", "course": st.session_state.uploaded_file.name, "time": "Just now"},
            {"action": "Generated flashcard set", "course": "Study Materials", "time": "Few moments ago"},
            {"action": "Created study plan", "course": "Learning Path", "time": "Few moments ago"},
            {"action": "Generated smart notes", "course": "Summary", "time": "Few moments ago"},
        ]
        
        for activity in activities:
            st.markdown(
                f"""
                <div class="activity-item">
                    <div style="font-weight: 700; color: var(--accent); margin-bottom: 0.25rem;">{activity['action']}</div>
                    <div style="color: var(--muted); font-size: 0.9rem;">{activity['course']}</div>
                    <div style="color: var(--muted); font-size: 0.85rem; margin-top: 0.25rem;">{activity['time']}</div>
                </div>
                """,
                unsafe_allow_html=True,
            )
    else:
        st.info("No recent activity.")


def render_simple_section(title: str) -> None:
    st.markdown(
        f"""
        <div class="header-container">
            <h1 class="header-title">{title}</h1>
        </div>
        """,
        unsafe_allow_html=True,
    )


# Sidebar Navigation
with st.sidebar:
    st.markdown(
        """
        <div class="sidebar-brand">
            <h1>🎓 CampusFlow Pro</h1>
            <p>AI-Powered Academic Suite</p>
        </div>
        """,
        unsafe_allow_html=True,
    )

    nav_labels = [
        "Dashboard",
        "Upload Documents",
        "Study Planner",
        "Smart Notes",
        "Flashcards",
        "Settings",
    ]
    nav_map = {
        "Dashboard": "dashboard",
        "Upload Documents": "upload",
        "Study Planner": "planner",
        "Smart Notes": "notes",
        "Flashcards": "flashcards",
        "Settings": "settings",
    }

    current_label = [k for k, v in nav_map.items() if v == st.session_state.current_page][0]
    selected = st.radio(
        "Navigation",
        nav_labels,
        index=nav_labels.index(current_label),
        label_visibility="collapsed",
        key="nav",
        horizontal=False,
        help=None,
        format_func=lambda x: f"{x}",
    )
    st.session_state.current_page = nav_map[selected]

    st.markdown("---")

    if st.session_state.file_processed and st.session_state.uploaded_file:
        st.markdown(
            """
            <div class="quick-card">
                <div class="quick-muted">Quick Overview</div>
                <div class="quick-row">Active Courses <span class="quick-muted">1</span></div>
                <div class="quick-row">Tasks This Week <span class="quick-muted">3</span></div>
                <div class="quick-row">Study Streak <span class="quick-muted">1 day</span></div>
            </div>
            """,
            unsafe_allow_html=True,
        )
    else:
        st.markdown(
            """
            <div class="quick-card">
                <div class="quick-muted">Quick Overview</div>
                <div class="quick-row">Active Courses <span class="quick-muted">0</span></div>
                <div class="quick-row">Tasks This Week <span class="quick-muted">0</span></div>
                <div class="quick-row">Study Streak <span class="quick-muted">0 days</span></div>
            </div>
            """,
            unsafe_allow_html=True,
        )


# Main Content Area
page = st.session_state.current_page

if page == "dashboard":
    render_header("Welcome back! 👋", "Here's what's happening with your studies today")

    col1, col2, col3, col4 = st.columns(4)
    
    if st.session_state.file_processed and st.session_state.uploaded_file:
        with col1:
            render_stat("Active Tasks", "3", "↑ +3 this week")
        with col2:
            render_stat("Completion Rate", "30%", "↑ +30% vs last week")
        with col3:
            render_stat("Study Hours", "2.5", "This week")
        with col4:
            render_stat("Upcoming Deadlines", "3", "Next 7 days")
    else:
        with col1:
            render_stat("Active Tasks", "0", "")
        with col2:
            render_stat("Completion Rate", "0%", "")
        with col3:
            render_stat("Study Hours", "0", "")
        with col4:
            render_stat("Upcoming Deadlines", "0", "")

    st.markdown("<div style='height: 0.5rem;'></div>", unsafe_allow_html=True)

    left, right = st.columns([2, 1])
    with left:
        render_tasks()
    with right:
        render_activity()

elif page == "upload":
    render_header("Upload Documents", "Upload your syllabus, assignments, or course materials")
    
    uploaded_file = st.file_uploader("Drop your files here or click to browse", type=['pdf', 'docx', 'txt'], label_visibility="visible", key="file_uploader")
    
    if uploaded_file:
        st.session_state.uploaded_file = uploaded_file
        st.success(f"✅ File uploaded: {uploaded_file.name}")
        
        if st.button("🚀 Process Document with AI", use_container_width=True):
            with st.spinner("Processing your document..."):
                import time
                time.sleep(2)
                st.session_state.file_processed = True
                st.success("✨ Document processed successfully!")
                st.balloons()
    elif st.session_state.uploaded_file:
        st.info(f"📄 Current document: {st.session_state.uploaded_file.name}")
        if st.button("🗑️ Remove Document"):
            st.session_state.uploaded_file = None
            st.session_state.file_processed = False
            st.rerun()

elif page == "planner":
    render_header("Study Planner", "AI-generated personalized study schedules")
    
    if st.session_state.uploaded_file and st.session_state.file_processed:
        st.success(f"📄 Document: {st.session_state.uploaded_file.name}")
        
        st.markdown("### 📅 Generated Study Plan")
        st.markdown("""
        <div class="task-card">
            <div class="task-title">Week 1: Introduction & Fundamentals</div>
            <div class="task-meta">Days 1-3: Review core concepts</div>
            <div style="margin-top: 0.5rem;" class="task-meta">Days 4-7: Practice problems and exercises</div>
        </div>
        
        <div class="task-card">
            <div class="task-title">Week 2: Advanced Topics</div>
            <div class="task-meta">Days 8-10: Deep dive into complex areas</div>
            <div style="margin-top: 0.5rem;" class="task-meta">Days 11-14: Project work and implementation</div>
        </div>
        
        <div class="task-card">
            <div class="task-title">Week 3: Review & Assessment</div>
            <div class="task-meta">Days 15-18: Comprehensive review</div>
            <div style="margin-top: 0.5rem;" class="task-meta">Days 19-21: Mock tests and final preparation</div>
        </div>
        """, unsafe_allow_html=True)
    else:
        st.info("📝 Upload and process a document to generate your personalized study plan")

elif page == "notes":
    render_header("Smart Notes", "AI-powered summaries and insights")
    
    if st.session_state.uploaded_file and st.session_state.file_processed:
        st.success(f"📄 Document: {st.session_state.uploaded_file.name}")
        
        st.markdown("### 📝 Key Insights")
        st.markdown("""
        <div class="activity-item">
            <div style="font-weight: 700; color: var(--accent); margin-bottom: 0.25rem;">Main Concepts</div>
            <div style="color: var(--muted); font-size: 0.95rem;">Core principles and fundamental ideas extracted from the document</div>
        </div>
        
        <div class="activity-item">
            <div style="font-weight: 700; color: var(--accent); margin-bottom: 0.25rem;">Important Definitions</div>
            <div style="color: var(--muted); font-size: 0.95rem;">Key terms and their meanings identified in the material</div>
        </div>
        
        <div class="activity-item">
            <div style="font-weight: 700; color: var(--accent); margin-bottom: 0.25rem;">Summary</div>
            <div style="color: var(--muted); font-size: 0.95rem;">Concise overview of the document's main topics and takeaways</div>
        </div>
        """, unsafe_allow_html=True)
        
        st.markdown("### 💡 Suggestions")
        st.info("Focus on understanding the core concepts before moving to advanced topics")
    else:
        st.info("📝 Upload and process a document to generate smart notes and summaries")

elif page == "flashcards":
    render_header("Flashcards", "Auto-generated flashcards for active recall")
    
    if st.session_state.uploaded_file and st.session_state.file_processed:
        st.success(f"📄 Document: {st.session_state.uploaded_file.name}")
        
        st.markdown("### 🧠 Generated Flashcards")
        
        flashcards = [
            {"front": "What is the main concept?", "back": "The fundamental principle discussed in the document"},
            {"front": "Define the key term", "back": "A crucial definition from the material"},
            {"front": "Explain the process", "back": "Step-by-step explanation of the methodology"}
        ]
        
        for i, card in enumerate(flashcards, 1):
            with st.expander(f"Flashcard {i}: {card['front']}"):
                st.markdown(f"""
                <div class="task-card">
                    <div class="task-title">Question</div>
                    <div style="color: var(--muted); margin: 0.5rem 0;">{card['front']}</div>
                    <div class="task-title" style="margin-top: 1rem;">Answer</div>
                    <div style="color: var(--muted); margin: 0.5rem 0;">{card['back']}</div>
                </div>
                """, unsafe_allow_html=True)
        
        st.markdown("---")
        col1, col2 = st.columns(2)
        with col1:
            st.button("📥 Download Flashcards", use_container_width=True)
        with col2:
            st.button("🔄 Generate More", use_container_width=True)
    else:
        st.info("📝 Upload and process a document to generate flashcards automatically")

elif page == "settings":
    render_header("Settings", "Customize your CampusFlow Pro experience")

    st.subheader("API Configuration")
    st.text_input("Gemini API Key", type="password")

    st.subheader("Preferences")
    theme_choice = st.selectbox("Theme", ["Light", "Dark"], index=0 if st.session_state.theme == "light" else 1)
    st.slider("Default Study Session Duration (minutes)", 25, 120, 50, 5)
    st.multiselect("Notification Preferences", ["In-App"], default=["In-App"])

    if theme_choice.lower() != st.session_state.theme:
        st.session_state.theme = theme_choice.lower()
        st.rerun()
