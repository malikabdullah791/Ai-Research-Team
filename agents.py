import os

from crewai import Agent, LLM

from tools import web_search_tool, calculator


# -----------------------------
# LLM
# -----------------------------
llm = LLM(
    model="groq/openai/gpt-oss-120b",
    api_key=os.getenv("GROQ_API_KEY"),
    temperature=0.2,
)


# -----------------------------
# 1. Research Agent
# -----------------------------
researcher = Agent(
    role="Senior Researcher",
    goal=(
        "Find accurate, relevant, recent, and high-quality information "
        "about the research topic."
    ),
    backstory=(
        "You are an experienced research analyst. "
        "You search the web carefully, compare sources, "
        "identify useful evidence, and avoid unsupported claims."
    ),
    tools=[web_search_tool],
    llm=llm,
    verbose=True,
    allow_delegation=False,
)


# -----------------------------
# 2. Analysis Agent
# -----------------------------
analyst = Agent(
    role="Research Analyst",
    goal=(
        "Analyze the research findings, identify patterns, "
        "compare evidence, and extract meaningful insights."
    ),
    backstory=(
        "You are a analytical researcher who converts raw research "
        "into clear findings. You use calculations when numerical "
        "reasoning is required."
    ),
    tools=[calculator],
    llm=llm,
    verbose=True,
    allow_delegation=False,
)


# -----------------------------
# 3. Fact Checker
# -----------------------------
fact_checker = Agent(
    role="Fact Checking Specialist",
    goal=(
        "Verify important claims and identify information that "
        "may be inaccurate, outdated, weakly supported, or misleading."
    ),
    backstory=(
        "You are a meticulous fact checker. You independently "
        "search for supporting evidence and clearly identify "
        "claims that require caution."
    ),
    tools=[web_search_tool],
    llm=llm,
    verbose=True,
    allow_delegation=False,
)


# -----------------------------
# 4. Report Writer
# -----------------------------
writer = Agent(
    role="Senior Research Writer",
    goal=(
        "Transform the research, analysis, and verification findings "
        "into a professional, well-structured research report."
    ),
    backstory=(
        "You are an experienced technical writer. "
        "You communicate complex information clearly and logically "
        "without inventing facts."
    ),
    tools=[],
    llm=llm,
    verbose=True,
    allow_delegation=False,
)
