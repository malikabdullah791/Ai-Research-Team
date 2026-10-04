import streamlit as st

from crew import run_research


# ============================================================
# PAGE CONFIG
# ============================================================

st.set_page_config(
    page_title="ResearchFlow AI",
    page_icon="🧠",
    layout="wide"
)


# ============================================================
# CUSTOM CSS
# ============================================================

st.markdown(
    """
    <style>

    .main {
        background-color: #0e1117;
    }

    .hero {
        padding: 30px;
        border-radius: 20px;
        background: linear-gradient(
            135deg,
            #111827,
            #172554
        );
        border: 1px solid #26324a;
        margin-bottom: 25px;
    }

    .hero-title {
        font-size: 42px;
        font-weight: 800;
        margin-bottom: 5px;
    }

    .hero-subtitle {
        font-size: 18px;
        color: #b8c1d1;
    }

    .agent-card {
        padding: 18px;
        border-radius: 15px;
        background: #151b26;
        border: 1px solid #26324a;
        text-align: center;
        min-height: 130px;
    }

    .agent-icon {
        font-size: 30px;
    }

    .agent-name {
        font-size: 17px;
        font-weight: 700;
        margin-top: 8px;
    }

    .agent-description {
        font-size: 13px;
        color: #9ca3af;
        margin-top: 5px;
    }

    .section-title {
        font-size: 25px;
        font-weight: 700;
        margin-top: 25px;
        margin-bottom: 10px;
    }

    </style>
    """,
    unsafe_allow_html=True
)


# ============================================================
# HERO
# ============================================================

st.markdown(
    """
    <div class="hero">

        <div class="hero-title">
            🧠 ResearchFlow AI
        </div>

        <div class="hero-subtitle">
            A Multi-Agent AI Research Team powered by CrewAI + Groq
        </div>

    </div>
    """,
    unsafe_allow_html=True
)


# ============================================================
# AGENT PIPELINE
# ============================================================

st.markdown(
    '<div class="section-title">🤖 AI Research Team</div>',
    unsafe_allow_html=True
)

col1, col2, col3, col4 = st.columns(4)


with col1:

    st.markdown(
        """
        <div class="agent-card">

            <div class="agent-icon">🔎</div>

            <div class="agent-name">
                Researcher
            </div>

            <div class="agent-description">
                Searches the web and collects evidence
            </div>

        </div>
        """,
        unsafe_allow_html=True
    )


with col2:

    st.markdown(
        """
        <div class="agent-card">

            <div class="agent-icon">📊</div>

            <div class="agent-name">
                Analyst
            </div>

            <div class="agent-description">
                Analyzes findings and calculations
            </div>

        </div>
        """,
        unsafe_allow_html=True
    )


with col3:

    st.markdown(
        """
        <div class="agent-card">

            <div class="agent-icon">🔍</div>

            <div class="agent-name">
                Fact Checker
            </div>

            <div class="agent-description">
                Verifies important claims
            </div>

        </div>
        """,
        unsafe_allow_html=True
    )


with col4:

    st.markdown(
        """
        <div class="agent-card">

            <div class="agent-icon">✍️</div>

            <div class="agent-name">
                Writer
            </div>

            <div class="agent-description">
                Creates the final research report
            </div>

        </div>
        """,
        unsafe_allow_html=True
    )


# ============================================================
# INPUT
# ============================================================

st.markdown(
    '<div class="section-title">🔬 Research Topic</div>',
    unsafe_allow_html=True
)


topic = st.text_area(
    "Enter your research topic",
    placeholder=(
        "Example: How can AI improve renewable energy "
        "integration in modern power systems?"
    ),
    height=120
)


# ============================================================
# RUN
# ============================================================

if st.button(
    "🚀 Start AI Research",
    use_container_width=True
):

    if not topic.strip():

        st.warning(
            "Please enter a research topic first."
        )

    else:

        st.info(
            "🤖 Research team is starting..."
        )

        try:

            with st.status(
                "🧠 AI Research Team is working...",
                expanded=True
            ) as status:

                st.write(
                    "🔎 Researcher is searching for information..."
                )

                result = run_research(topic)

                status.update(
                    label="✅ Research completed!",
                    state="complete",
                    expanded=False
                )


            # =================================================
            # RESULT
            # =================================================

            st.markdown(
                '<div class="section-title">📄 Final Research Report</div>',
                unsafe_allow_html=True
            )

            st.markdown(result)


            # =================================================
            # DOWNLOAD
            # =================================================

            st.download_button(
                label="⬇️ Download Report",
                data=result,
                file_name="research_report.md",
                mime="text/markdown",
                use_container_width=True
            )


        except Exception as e:

            st.error(
                "❌ Something went wrong."
            )

            st.code(
                str(e)
            )
