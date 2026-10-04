import os
from crewai import Agent, LLM

from tools import web_search_tool, calculator_tool


# ============================================================
# GROQ LLM
# ============================================================

GROQ_API_KEY = os.getenv("GROQ_API_KEY")

if not GROQ_API_KEY:
    raise ValueError(
        "GROQ_API_KEY is missing. Add it in Streamlit Secrets."
    )


llm = LLM(
    model="groq/openai/gpt-oss-120b",
    api_key=GROQ_API_KEY,
    temperature=0.2,
)


# ============================================================
# 1. RESEARCHER
# ============================================================

researcher = Agent(
    role="Senior Researcher",

    goal=(
        "Research the user's topic using reliable and recent "
        "web sources. Collect important facts, evidence, statistics "
        "and source information."
    ),

    backstory=(
        "You are an experienced research specialist. "
        "You investigate topics carefully, compare information "
        "from multiple sources and avoid unsupported claims."
    ),

    tools=[web_search_tool],

    llm=llm,

    verbose=True,

    allow_delegation=False,
)


# ============================================================
# 2. ANALYST
# ============================================================

analyst = Agent(
    role="Research Analyst",

    goal=(
        "Analyze the research findings, identify important patterns, "
        "compare evidence and produce useful insights."
    ),

    backstory=(
        "You are a professional analytical researcher. "
        "You transform raw research into meaningful conclusions "
        "and use calculations whenever numerical reasoning is needed."
    ),

    tools=[calculator_tool],

    llm=llm,

    verbose=True,

    allow_delegation=False,
)


# ============================================================
# 3. FACT CHECKER
# ============================================================

fact_checker = Agent(
    role="Fact Checking Specialist",

    goal=(
        "Verify important claims from the research and identify "
        "information that may be inaccurate, outdated or weakly supported."
    ),

    backstory=(
        "You are a meticulous fact checker. "
        "You independently verify important claims using reliable "
        "web sources and clearly identify questionable information."
    ),

    tools=[web_search_tool],

    llm=llm,

    verbose=True,

    allow_delegation=False,
)


# ============================================================
# 4. WRITER
# ============================================================

writer = Agent(
    role="Senior Research Writer",

    goal=(
        "Create a professional, clear and well-structured research "
        "report from the research, analysis and fact-checking results."
    ),

    backstory=(
        "You are an experienced technical writer. "
        "You communicate complex information in simple, logical "
        "and professional language without inventing facts."
    ),

    llm=llm,

    verbose=True,

    allow_delegation=False,
)
