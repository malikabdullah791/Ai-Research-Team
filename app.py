import os

from crewai import Agent, LLM

from tools import web_search_tool, calculator_tool


# ============================================================
# GROQ API KEY
# ============================================================

GROQ_API_KEY = os.getenv("GROQ_API_KEY")

if not GROQ_API_KEY:
    raise ValueError(
        "GROQ_API_KEY is missing. "
        "Please add it to Streamlit Secrets."
    )


# ============================================================
# GROQ LLM
# ============================================================

llm = LLM(
    model="groq/qwen/qwen3.8-27b",
    api_key=GROQ_API_KEY,
    temperature=0.2,
)


# ============================================================
# 1. RESEARCHER
# ============================================================

researcher = Agent(

    role="Senior Researcher",

    goal="""
    Research the user's topic using reliable and recent
    web sources.

    Collect:
    - Important facts
    - Evidence
    - Statistics
    - Recent developments
    - Relevant examples
    - Source information

    Always use the web search tool when research is required.
    Do not invent sources.
    """,

    backstory="""
    You are an experienced research specialist.

    You carefully search the internet, compare information
    from different sources and collect reliable evidence.

    You never pretend to have accessed a webpage unless the
    web search tool actually returned information about it.
    """,

    tools=[
        web_search_tool
    ],

    llm=llm,

    verbose=True,

    allow_delegation=False,
)


# ============================================================
# 2. ANALYST
# ============================================================

analyst = Agent(

    role="Research Analyst",

    goal="""
    Analyze the research findings and convert raw information
    into useful insights.

    Identify:
    - Patterns
    - Comparisons
    - Advantages
    - Limitations
    - Practical implications
    - Numerical insights
    """,

    backstory="""
    You are a professional analytical researcher.

    You carefully examine research findings and produce
    logical conclusions.

    When mathematical calculations are required, use the
    calculator tool.
    """,

    tools=[
        calculator_tool
    ],

    llm=llm,

    verbose=True,

    allow_delegation=False,
)


# ============================================================
# 3. FACT CHECKER
# ============================================================

fact_checker = Agent(

    role="Fact Checking Specialist",

    goal="""
    Verify important claims from the research.

    Check:
    - Accuracy
    - Reliability
    - Current relevance
    - Supporting evidence
    - Potentially misleading claims
    """,

    backstory="""
    You are a meticulous fact-checking specialist.

    You independently verify important claims using the
    available web search tool.

    Clearly identify information that is verified,
    questionable or unsupported.
    """,

    tools=[
        web_search_tool
    ],

    llm=llm,

    verbose=True,

    allow_delegation=False,
)


# ============================================================
# 4. WRITER
# ============================================================

writer = Agent(

    role="Senior Research Writer",

    goal="""
    Convert the research, analysis and fact-checking results
    into a professional research report.
    """,

    backstory="""
    You are an experienced technical writer.

    You write clear, professional and logically structured
    reports.

    You must not invent facts, statistics or sources.
    """,

    tools=[],

    llm=llm,

    verbose=True,

    allow_delegation=False,
)
