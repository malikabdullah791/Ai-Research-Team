import streamlit as st
from crew import run_research

# -----------------------------
# Page Configuration
# -----------------------------
st.set_page_config(
    page_title="ResearchFlow AI",
    page_icon="🔬",
    layout="wide",
    initial_sidebar_state="collapsed",
)

# -----------------------------
# Custom CSS
# -----------------------------
st.markdown(
    """
    <style>
        /* Main background */
        .stApp {
            background:
                radial-gradient(circle at 10% 10%, rgba(99,102,241,0.12), transparent 25%),
                radial-gradient(circle at 90% 20%, rgba(14,165,233,0.10), transparent 25%),
                #0b1020;
            color: #f8fafc;
        }

        /* Main container */
        .block-container {
            max-width: 1100px;
            padding-top: 2rem;
            padding-bottom: 3rem;
        }

        /* Hero */
        .hero {
            padding: 2.5rem 2rem;
            border-radius: 24px;
            background: linear-gradient(
                135deg,
                rgba(30,41,59,0.95),
                rgba(15,23,42,0.92)
            );
            border: 1px solid rgba(148,163,184,0.15);
            box-shadow: 0 20px 60px rgba(0,0,0,0.30);
            margin-bottom: 1.5rem;
        }

        .hero-badge {
            display: inline-block;
            padding: 0.35rem 0.75rem;
            border-radius: 999px;
            background: rgba(99,102,241,0.15);
            color: #a5b4fc;
            font-size: 0.8rem;
            font-weight: 700;
            margin-bottom: 0.8rem;
        }

        .hero h1 {
            font-size: 3rem;
            line-height: 1.1;
            margin: 0;
            color: #f8fafc;
        }

        .hero p {
            color: #94a3b8;
            font-size: 1.05rem;
            margin-top: 0.8rem;
            max-width: 760px;
        }

        /* Agent cards */
        .agent-card {
            padding: 1rem;
            border-radius: 16px;
            background: rgba(30,41,59,0.65);
            border: 1px solid rgba(148,163,184,0.12);
            min-height: 125px;
        }

        .agent-icon {
            font-size: 1.5rem;
        }

        .agent-name {
            font-weight: 700;
            color: #f8fafc;
            margin-top: 0.4rem;
        }

        .agent-role {
            color: #94a3b8;
            font-size: 0.85rem;
        }

        /* Status */
        .status-box {
            padding: 1rem 1.2rem;
            border-radius: 14px;
            background: rgba(15,23,42,0.8);
            border: 1px solid rgba(99,102,241,0.25);
            margin: 1rem 0;
        }

        .status-label {
            color: #94a3b8;
            font-size: 0.8rem;
            text-transform: uppercase;
            letter-spacing: 0.08em;
        }

        .status-agent {
            color: #a5b4fc;
            font-size: 1.15rem;
            font-weight: 700;
            margin-top: 0.25rem;
        }

        /* Result */
        .result-box {
            padding: 1.5rem;
            border-radius: 20px;
            background: rgba(15,23,42,0.75);
            border: 1px solid rgba(148,163,184,0.14);
        }

        /* Buttons */
        .stButton > button {
            width: 100%;
            border-radius: 12px;
            padding: 0.75rem 1rem;
            font-weight: 700;
            border: none;
        }

        /* Footer */
        .footer {
            text-align: center;
            color: #64748b;
            font-size: 0.8rem;
            margin-top: 2.5rem;
        }
    </style>
    """,
    unsafe_allow_html=True,
)

# -----------------------------
# Hero Section
# -----------------------------
st.markdown(
    """
    <div class="hero">
        <div class="hero-badge">MULTI-AGENT RESEARCH SYSTEM</div>
        <h1>🔬 ResearchFlow AI</h1>
        <p>
            A collaborative AI research team powered by CrewAI and Groq.
            Research, analyze, verify, and write — automatically.
        </p>
    </div>
    """,
    unsafe_allow_html=True,
)

# -----------------------------
# Agent Overview
# -----------------------------
cols = st.columns(4)

agents = [
    ("🔎", "Researcher", "Finds relevant information"),
    ("📊", "Analyst", "Analyzes findings"),
    ("🔍", "Fact Checker", "Verifies important claims"),
    ("✍️", "Writer", "Creates final report"),
]

for col, (icon, name, role) in zip(cols, agents):
    with col:
        st.markdown(
            f"""
            <div class="agent-card">
                <div class="agent-icon">{icon}</div>
                <div class="agent-name">{name}</div>
                <div class="agent-role">{role}</div>
            </div>
            """,
            unsafe_allow_html=True,
        )

st.write("")

# -----------------------------
# Research Input
# -----------------------------
st.markdown("### 🎯 What would you like to research?")

topic = st.text_area(
    "Research topic",
    placeholder=(
        "Example: Impact of EV smart charging on renewable energy "
        "hosting capacity"
    ),
    height=120,
    label_visibility="collapsed",
)

col1, col2 = st.columns([3, 1])

with col1:
    st.caption(
        "Tip: Be specific. A focused research question produces better results."
    )

with col2:
    research_button = st.button(
        "🚀 Start Research",
        type="primary",
        use_container_width=True,
    )

# -----------------------------
# Research Execution
# -----------------------------
if research_button:

    if not topic.strip():
        st.warning("Please enter a research topic first.")
        st.stop()

    st.divider()

    status = st.empty()

    try:
        status.markdown(
            """
            <div class="status-box">
                <div class="status-label">Current Agent</div>
                <div class="status-agent">🔎 Researcher — gathering sources...</div>
            </div>
            """,
            unsafe_allow_html=True,
        )

        result = run_research(
            topic=topic,
            status_callback=lambda message: status.markdown(
                f"""
                <div class="status-box">
                    <div class="status-label">Current Agent</div>
                    <div class="status-agent">{message}</div>
                </div>
                """,
                unsafe_allow_html=True,
            ),
        )

        status.markdown(
            """
            <div class="status-box">
                <div class="status-label">Status</div>
                <div class="status-agent">✅ Research completed</div>
            </div>
            """,
            unsafe_allow_html=True,
        )

        st.markdown("### 📄 Research Report")

        st.markdown(
            '<div class="result-box">',
            unsafe_allow_html=True,
        )

        st.markdown(result)

        st.markdown("</div>", unsafe_allow_html=True)

        st.download_button(
            label="⬇️ Download Report",
            data=result,
            file_name="research_report.md",
            mime="text/markdown",
            use_container_width=True,
        )

    except Exception as e:

        status.empty()

        st.error(
            "Something went wrong while running the research team."
        )

        with st.expander("Technical details"):
            st.exception(e)

# -----------------------------
# Footer
# -----------------------------
st.markdown(
    """
    <div class="footer">
        ResearchFlow AI • CrewAI × Groq × Streamlit
    </div>
    """,
    unsafe_allow_html=True,
)
