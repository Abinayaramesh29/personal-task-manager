import streamlit as st
from datetime import datetime, timedelta
import plotly.graph_objects as go
import plotly.express as px

# Page Configuration
st.set_page_config(
    page_title="CampusFlow Pro",
    page_icon="🎓",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Custom CSS for Production-Ready Styling
st.markdown("""
<style>
    /* Main Container */
    .main {
        padding: 0rem 1rem;
    }
    
    /* Header Styling */
    .header-container {
        background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
        padding: 2rem;
        border-radius: 15px;
        margin-bottom: 2rem;
        box-shadow: 0 10px 30px rgba(0,0,0,0.1);
    }
    
    .header-title {
        color: white;
        font-size: 2.5rem;
        font-weight: 700;
        margin: 0;
    }
    
    .header-subtitle {
        color: rgba(255,255,255,0.9);
        font-size: 1.1rem;
        margin-top: 0.5rem;
    }
    
    /* Stats Cards */
    .stat-card {
        background: white;
        padding: 1.5rem;
        border-radius: 12px;
        box-shadow: 0 4px 6px rgba(0,0,0,0.07);
        border-left: 4px solid;
        transition: transform 0.2s;
    }
    
    .stat-card:hover {
        transform: translateY(-5px);
        box-shadow: 0 8px 15px rgba(0,0,0,0.1);
    }
    
    .stat-value {
        font-size: 2rem;
        font-weight: 700;
        margin: 0.5rem 0;
    }
    
    .stat-label {
        color: #64748b;
        font-size: 0.9rem;
        font-weight: 500;
        text-transform: uppercase;
        letter-spacing: 0.5px;
    }
    
    .stat-trend {
        color: #10b981;
        font-size: 0.85rem;
        font-weight: 600;
    }
    
    /* Task Cards */
    .task-card {
        background: white;
        padding: 1.5rem;
        border-radius: 12px;
        margin-bottom: 1rem;
        box-shadow: 0 2px 8px rgba(0,0,0,0.08);
        border-left: 4px solid #667eea;
    }
    
    .task-title {
        font-size: 1.1rem;
        font-weight: 600;
        color: #1e293b;
        margin-bottom: 0.5rem;
    }
    
    .task-meta {
        color: #64748b;
        font-size: 0.9rem;
    }
    
    /* Priority Badges */
    .priority-high {
        background: #fee2e2;
        color: #dc2626;
        padding: 0.25rem 0.75rem;
        border-radius: 20px;
        font-size: 0.75rem;
        font-weight: 600;
    }
    
    .priority-medium {
        background: #fef3c7;
        color: #d97706;
        padding: 0.25rem 0.75rem;
        border-radius: 20px;
        font-size: 0.75rem;
        font-weight: 600;
    }
    
    .priority-low {
        background: #d1fae5;
        color: #059669;
        padding: 0.25rem 0.75rem;
        border-radius: 20px;
        font-size: 0.75rem;
        font-weight: 600;
    }
    
    /* Upload Area */
    .upload-area {
        border: 2px dashed #cbd5e1;
        border-radius: 12px;
        padding: 3rem;
        text-align: center;
        background: #f8fafc;
        transition: all 0.3s;
    }
    
    .upload-area:hover {
        border-color: #667eea;
        background: #f1f5f9;
    }
    
    /* Sidebar Styling */
    .css-1d391kg {
        background: linear-gradient(180deg, #667eea 0%, #764ba2 100%);
    }
    
    /* Button Styling */
    .stButton>button {
        background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
        color: white;
        border: none;
        border-radius: 8px;
        padding: 0.75rem 2rem;
        font-weight: 600;
        transition: all 0.3s;
    }
    
    .stButton>button:hover {
        transform: translateY(-2px);
        box-shadow: 0 8px 20px rgba(102,126,234,0.4);
    }
    
    /* Progress Bar */
    .progress-container {
        background: #e2e8f0;
        border-radius: 10px;
        height: 8px;
        overflow: hidden;
        margin: 0.5rem 0;
    }
    
    .progress-bar {
        background: linear-gradient(90deg, #667eea 0%, #764ba2 100%);
        height: 100%;
        border-radius: 10px;
        transition: width 0.3s;
    }
    
    /* Activity Item */
    .activity-item {
        padding: 1rem;
        border-left: 3px solid #667eea;
        margin-bottom: 1rem;
        background: #f8fafc;
        border-radius: 0 8px 8px 0;
    }
</style>
""", unsafe_allow_html=True)

# Initialize session state
if 'uploaded_file' not in st.session_state:
    st.session_state.uploaded_file = None
if 'processed' not in st.session_state:
    st.session_state.processed = False

# Sidebar Navigation
with st.sidebar:
    st.markdown("<h1 style='color: white; text-align: center;'>🎓 CampusFlow Pro</h1>", unsafe_allow_html=True)
    st.markdown("<p style='color: rgba(255,255,255,0.8); text-align: center; margin-bottom: 2rem;'>AI-Powered Academic Suite</p>", unsafe_allow_html=True)
    
    page = st.radio(
        "Navigation",
        ["📊 Dashboard", "📤 Upload Documents", "📅 Study Planner", "📝 Smart Notes", "🧠 Flashcards", "⚙️ Settings"],
        label_visibility="collapsed"
    )
    
    st.markdown("---")
    
    # Quick Stats in Sidebar
    st.markdown("### Quick Overview")
    st.metric("Active Courses", "4", delta="1 new")
    st.metric("Tasks This Week", "12", delta="-3")
    st.metric("Study Streak", "7 days", delta="2 days")

# Main Content Area
if "Dashboard" in page:
    # Header
    st.markdown("""
    <div class="header-container">
        <h1 class="header-title">Welcome back! 👋</h1>
        <p class="header-subtitle">Here's what's happening with your studies today</p>
    </div>
    """, unsafe_allow_html=True)
    
    # Stats Row
    col1, col2, col3, col4 = st.columns(4)
    
    with col1:
        st.markdown("""
        <div class="stat-card" style="border-left-color: #3b82f6;">
            <div class="stat-label">Active Tasks</div>
            <div class="stat-value" style="color: #3b82f6;">12</div>
            <div class="stat-trend">↑ +3 this week</div>
        </div>
        """, unsafe_allow_html=True)
    
    with col2:
        st.markdown("""
        <div class="stat-card" style="border-left-color: #10b981;">
            <div class="stat-label">Completion Rate</div>
            <div class="stat-value" style="color: #10b981;">87%</div>
            <div class="stat-trend">↑ +5% vs last week</div>
        </div>
        """, unsafe_allow_html=True)
    
    with col3:
        st.markdown("""
        <div class="stat-card" style="border-left-color: #8b5cf6;">
            <div class="stat-label">Study Hours</div>
            <div class="stat-value" style="color: #8b5cf6;">24.5</div>
            <div class="stat-trend">This week</div>
        </div>
        """, unsafe_allow_html=True)
    
    with col4:
        st.markdown("""
        <div class="stat-card" style="border-left-color: #f59e0b;">
            <div class="stat-label">Upcoming Deadlines</div>
            <div class="stat-value" style="color: #f59e0b;">5</div>
            <div class="stat-trend">Next 7 days</div>
        </div>
        """, unsafe_allow_html=True)
    
    st.markdown("<br>", unsafe_allow_html=True)
    
    # Main Content Grid
    col_left, col_right = st.columns([2, 1])
    
    with col_left:
        st.markdown("### 📋 Upcoming Tasks")
        
        tasks = [
            {"title": "Machine Learning Assignment", "course": "CS 401", "deadline": "2 days", "priority": "high", "progress": 65},
            {"title": "Database Design Project", "course": "CS 305", "deadline": "4 days", "priority": "medium", "progress": 40},
            {"title": "Algorithm Analysis", "course": "CS 402", "deadline": "1 week", "priority": "medium", "progress": 80},
            {"title": "Final Exam Preparation", "course": "CS 301", "deadline": "2 weeks", "priority": "low", "progress": 20}
        ]
        
        for task in tasks:
            priority_class = f"priority-{task['priority']}"
            st.markdown(f"""
            <div class="task-card">
                <div style="display: flex; justify-content: space-between; align-items: start;">
                    <div>
                        <div class="task-title">{task['title']}</div>
                        <div class="task-meta">{task['course']} • Due in {task['deadline']}</div>
                    </div>
                    <span class="{priority_class}">{task['priority'].upper()}</span>
                </div>
                <div style="margin-top: 1rem;">
                    <div style="display: flex; justify-content: space-between; font-size: 0.85rem; color: #64748b; margin-bottom: 0.5rem;">
                        <span>Progress</span>
                        <span style="font-weight: 600; color: #1e293b;">{task['progress']}%</span>
                    </div>
                    <div class="progress-container">
                        <div class="progress-bar" style="width: {task['progress']}%;"></div>
                    </div>
                </div>
            </div>
            """, unsafe_allow_html=True)
        
        # Study Hours Chart
        st.markdown("### 📈 Study Hours This Week")
        
        days = ['Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat', 'Sun']
        hours = [3.5, 4.2, 2.8, 5.1, 3.9, 4.5, 0.5]
        
        fig = go.Figure(data=[
            go.Bar(
                x=days,
                y=hours,
                marker=dict(
                    color=hours,
                    colorscale='Purples',
                    line=dict(color='rgb(102,126,234)', width=2)
                ),
                text=hours,
                textposition='outside'
            )
        ])
        
        fig.update_layout(
            height=300,
            margin=dict(l=0, r=0, t=10, b=0),
            plot_bgcolor='rgba(0,0,0,0)',
            paper_bgcolor='rgba(0,0,0,0)',
            yaxis=dict(showgrid=True, gridcolor='rgba(0,0,0,0.05)'),
            xaxis=dict(showgrid=False)
        )
        
        st.plotly_chart(fig, use_container_width=True)
    
    with col_right:
        st.markdown("### 🕐 Recent Activity")
        
        activities = [
            {"action": "Completed flashcard set", "course": "Data Structures", "time": "2 hours ago"},
            {"action": "Generated study plan", "course": "Algorithms", "time": "5 hours ago"},
            {"action": "Uploaded syllabus", "course": "Machine Learning", "time": "1 day ago"},
            {"action": "Finished assignment", "course": "Database Systems", "time": "2 days ago"}
        ]
        
        for activity in activities:
            st.markdown(f"""
            <div class="activity-item">
                <div style="font-weight: 600; color: #1e293b; margin-bottom: 0.25rem;">{activity['action']}</div>
                <div style="color: #64748b; font-size: 0.9rem;">{activity['course']}</div>
                <div style="color: #94a3b8; font-size: 0.8rem; margin-top: 0.25rem;">{activity['time']}</div>
            </div>
            """, unsafe_allow_html=True)
        
        # Course Distribution
        st.markdown("<br>", unsafe_allow_html=True)
        st.markdown("### 📚 Course Load")
        
        courses = ['CS 401', 'CS 305', 'CS 402', 'CS 301']
        tasks_count = [5, 3, 2, 2]
        
        fig2 = go.Figure(data=[go.Pie(
            labels=courses,
            values=tasks_count,
            hole=.4,
            marker=dict(colors=['#667eea', '#764ba2', '#f093fb', '#4facfe'])
        )])
        
        fig2.update_layout(
            height=250,
            margin=dict(l=0, r=0, t=0, b=0),
            showlegend=True,
            legend=dict(orientation="h", yanchor="bottom", y=-0.2, xanchor="center", x=0.5)
        )
        
        st.plotly_chart(fig2, use_container_width=True)

elif "Upload" in page:
    st.markdown("""
    <div class="header-container">
        <h1 class="header-title">📤 Upload Documents</h1>
        <p class="header-subtitle">Upload your syllabus, assignments, or course materials</p>
    </div>
    """, unsafe_allow_html=True)
    
    # Upload Area
    st.markdown("""
    <div class="upload-area">
        <div style="font-size: 3rem; margin-bottom: 1rem;">📄</div>
        <h3>Drop your files here</h3>
        <p style="color: #64748b; margin: 1rem 0;">or click to browse from your computer</p>
    </div>
    """, unsafe_allow_html=True)
    
    uploaded_file = st.file_uploader("", type=['pdf'], label_visibility="collapsed")
    
    if uploaded_file:
        st.session_state.uploaded_file = uploaded_file
        st.success(f"✅ File uploaded: {uploaded_file.name}")
        
        col1, col2, col3 = st.columns([1, 2, 1])
        with col2:
            if st.button("🚀 Process Document with AI", use_container_width=True):
                with st.spinner("Processing your document..."):
                    import time
                    time.sleep(2)
                    st.session_state.processed = True
                    st.success("✨ Document processed successfully!")
                    st.balloons()

elif "Planner" in page:
    st.markdown("""
    <div class="header-container">
        <h1 class="header-title">📅 Study Planner</h1>
        <p class="header-subtitle">AI-generated personalized study schedules</p>
    </div>
    """, unsafe_allow_html=True)
    
    st.info("📝 Upload a document to generate your personalized study plan")

elif "Notes" in page:
    st.markdown("""
    <div class="header-container">
        <h1 class="header-title">📝 Smart Notes</h1>
        <p class="header-subtitle">AI-powered summaries and insights</p>
    </div>
    """, unsafe_allow_html=True)
    
    st.info("📝 Upload a document to generate smart notes and summaries")

elif "Flashcards" in page:
    st.markdown("""
    <div class="header-container">
        <h1 class="header-title">🧠 Flashcards</h1>
        <p class="header-subtitle">Auto-generated flashcards for active recall</p>
    </div>
    """, unsafe_allow_html=True)
    
    st.info("📝 Upload a document to generate flashcards automatically")

elif "Settings" in page:
    st.markdown("""
    <div class="header-container">
        <h1 class="header-title">⚙️ Settings</h1>
        <p class="header-subtitle">Customize your CampusFlow Pro experience</p>
    </div>
    """, unsafe_allow_html=True)
    
    st.subheader("API Configuration")
    api_key = st.text_input("Gemini API Key", type="password", help="Enter your Google Gemini API key")
    
    st.subheader("Preferences")
    st.selectbox("Theme", ["Light", "Dark", "Auto"])
    st.slider("Default Study Session Duration (minutes)", 25, 120, 50, 5)
    st.multiselect("Notification Preferences", ["Email", "Push", "In-App"], default=["In-App"])
    
    if st.button("💾 Save Settings"):
        st.success("Settings saved successfully!")

# Footer
st.markdown("---")
st.markdown("""
<div style="text-align: center; color: #64748b; padding: 1rem;">
    <p>CampusFlow Pro v2.0 | Powered by Gemini 2.0 Flash | Made with ❤️ for students</p>
</div>