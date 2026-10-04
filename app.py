import streamlit as st

from crew import run_research


# ============================================================
# PAGE CONFIG
# ============================================================

st.set_page_config(
    page_title="ResearchFlow AI",
    page_icon="🧠",
    layout="wide",
    initial_sidebar_state="collapsed",
)


# ============================================================
# CUSTOM CSS
# ============================================================

st.html(
    """
    <style>

    /* Main page */
    .stApp {
        background: #0b1020;
    }

    /* Hero section */
    .hero-box {
        background: linear-gradient(
            135deg,
            #111827 0%,
            #172554 100%
        );

        border: 1px solid #263b63;
        border-radius: 24px;

        padding: 35px 40px;
        margin-bottom: 25px;

        box-shadow: 0 10px 35px rgba(0,0,0,0.25);
    }

    .hero-title {
        font-size: 42px;
        font-weight: 800;
        color: white;
        margin-bottom: 8px;
    }

    .hero-subtitle {
        font-size: 17px;
        color: #b8c4d9;
        line-height: 1.6;
    }

    .hero-badge {
        display: inline-block;

        margin-top: 18px;

        padding: 7px 14px;

        border-radius: 20px;

        background: rgba(59,130,246,0.15);

        border: 1px solid rgba(96,165,250,0.35);

        color: #93c5fd;

        font-size: 13px;

        font-weight: 600;
    }


    /* Agent cards */
    .agent-card {
        background: #111827;

        border: 1px solid #26324a;

        border-radius: 18px;

        padding: 22px 15px;

        min-height: 150px;

        text-align: center;

        box-shadow: 0 8px 25px rgba(0,0,0,0.18);
    }

    .agent-icon {
        font-size: 34px;
        margin-bottom: 8px;
    }

    .agent-name {
        color: white;

        font-size: 17px;

        font-weight: 700;

        margin-bottom: 7px;
    }

    .agent-description {
        color: #9ca3af;

        font-size: 13px;

        line-height: 1.5;
    }


    /* Section headings */
    .section-heading {
        color: white;

        font-size: 25px;

        font-weight: 750;

        margin-top: 25px;

        margin-bottom: 15px;
    }


    /* Pipeline arrow */
    .pipeline-arrow {
        text-align: center;

        color: #64748b;

        font-size: 24px;

        padding-top: 55px;
    }


    /* Research info box */
    .info-box {
        background: #111827;

        border: 1px solid #26324a;

        border-radius: 16px;

        padding: 18px;

        color: #cbd5e1;

        line-height: 1.6;

        margin-top: 20px;
    }

    </style>
    """
)


# ============================================================
# HERO
# ============================================================

st.html(
    """
    <div class="hero-box">

        <div class="hero-title">
            🧠 ResearchFlow AI
        </div>

        <div class="hero-subtitle">
            A Multi-Agent AI Research Team that researches,
            analyzes, verifies, and writes your final report.
        </div>

        <div class="hero-badge">
            ⚡ CrewAI &nbsp;•&nbsp; Groq &nbsp;•&nbsp; Multi-Agent AI
        </div>

    </div>
    """
)


# ============================================================
# AGENT TEAM
# ============================================================

st.markdown(
    '<div class="section-heading">🤖 AI Research Team</div>',
    unsafe_allow_html=True
)


# ============================================================
# AGENT CARDS
# ============================================================

col1, arrow1, col2, arrow2, col3, arrow3, col4 = st.columns(
    [2.2, 0.35, 2.2, 0.35, 2.2, 0.35, 2.2]
)


# ------------------------------------------------------------
# Researcher
# ------------------------------------------------------------

with col1:

    st.html(
        """
        <div class="agent-card">

            <div class="agent-icon">
                🔎
            </div>

            <div class="agent-name">
                Researcher
            </div>

            <div class="agent-description">
                Searches the web and collects
                reliable research evidence.
            </div>

        </div>
        """
    )


# ------------------------------------------------------------
# Arrow
# ------------------------------------------------------------

with arrow1:

    st.html(
        """
        <div class="pipeline-arrow">
            →
        </div>
        """
    )


# ------------------------------------------------------------
# Analyst
# ------------------------------------------------------------

with col2:

    st.html(
        """
        <div class="agent-card">

            <div class="agent-icon">
                📊
            </div>

            <div class="agent-name">
                Analyst
            </div>

            <div class="agent-description">
                Analyzes findings, comparisons
                and numerical information.
            </div>

        </div>
        """
    )


# ------------------------------------------------------------
# Arrow
# ------------------------------------------------------------

with arrow2:

    st.html(
        """
        <div class="pipeline-arrow">
            →
        </div>
        """
    )


# ------------------------------------------------------------
# Fact Checker
# ------------------------------------------------------------

with col3:

    st.html(
        """
        <div class="agent-card">

            <div class="agent-icon">
                🔍
            </div>

            <div class="agent-name">
                Fact Checker
            </div>

            <div class="agent-description">
                Verifies important claims
                and identifies weak evidence.
            </div>

        </div>
        """
    )


# ------------------------------------------------------------
# Arrow
# ------------------------------------------------------------

with arrow3:

    st.html(
        """
        <div class="pipeline-arrow">
            →
        </div>
        """
    )


# ------------------------------------------------------------
# Writer
# ------------------------------------------------------------

with col4:

    st.html(
        """
        <div class="agent-card">

            <div class="agent-icon">
                ✍️
            </div>

            <div class="agent-name">
                Writer
            </div>

            <div class="agent-description">
                Converts everything into
                a professional research report.
            </div>

        </div>
        """
    )


# ============================================================
# RESEARCH INPUT
# ============================================================

st.markdown(
    '<div class="section-heading">🔬 What do you want to research?</div>',
    unsafe_allow_html=True
)


topic = st.text_area(
    label="Research topic",
    placeholder=(
        "Example:\n"
        "How can artificial intelligence improve "
        "renewable energy integration in modern power systems?"
    ),
    height=130,
    label_visibility="collapsed",
)


# ============================================================
# QUICK EXAMPLES
# ============================================================

st.caption(
    "💡 Example topics: AI in power systems • EV smart charging • "
    "Renewable energy • Battery technology • Agentic AI"
)


# ============================================================
# START BUTTON
# ============================================================

start_button = st.button(
    "🚀 Start AI Research",
    type="primary",
    use_container_width=True,
)


# ============================================================
# RUN RESEARCH
# ============================================================

if start_button:

    if not topic.strip():

        st.warning(
            "⚠️ Please enter a research topic first."
        )

    else:

        st.divider()

        st.markdown(
            '<div class="section-heading">⚙️ Research Progress</div>',
            unsafe_allow_html=True
        )


        # ----------------------------------------------------
        # Progress display
        # ----------------------------------------------------

        with st.status(
            "🧠 ResearchFlow AI is working...",
            expanded=True
        ) as progress:

            st.write(
                "🔎 Researcher → Searching for information..."
            )

            try:

                result = run_research(topic)

                st.write(
                    "📊 Analyst → Analyzing findings..."
                )

                st.write(
                    "🔍 Fact Checker → Verifying important claims..."
                )

                st.write(
                    "✍️ Writer → Preparing final report..."
                )

                progress.update(
                    label="✅ Research completed successfully!",
                    state="complete",
                    expanded=False,
                )


            except Exception as error:

                progress.update(
                    label="❌ Research failed",
                    state="error",
                    expanded=True,
                )

                st.error(
                    "An error occurred while running the AI research team."
                )

                st.exception(error)

                st.stop()


        # ====================================================
        # FINAL REPORT
        # ====================================================

        st.markdown(
            '<div class="section-heading">📄 Final Research Report</div>',
            unsafe_allow_html=True
        )


        st.markdown(
            result
        )


        # ====================================================
        # DOWNLOAD
        # ====================================================

        st.download_button(
            label="⬇️ Download Research Report",
            data=result,
            file_name="research_report.md",
            mime="text/markdown",
            use_container_width=True,
        )


# ============================================================
# FOOTER
# ============================================================

st.divider()

st.caption(
    "ResearchFlow AI • Multi-Agent Research System • "
    "Built with CrewAI + Groq + Streamlit"
)
