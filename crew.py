# ============================================================
# IMPORTANT GROQ + CREWAI COMPATIBILITY FIX
# ============================================================

# CrewAI currently adds an Anthropic-specific
# "cache_breakpoint" field to messages.
#
# Groq does not accept this field.
#
# This patch disables that marker before it reaches Groq.

try:
    import crewai.llms.cache as crewai_cache

    crewai_cache.mark_cache_breakpoint = lambda message: message

except Exception:
    pass


# ============================================================
# IMPORTS
# ============================================================

import os

from crewai import Crew, Process

from agents import (
    researcher,
    analyst,
    fact_checker,
    writer,
)

from tasks import create_tasks


# ============================================================
# RUN RESEARCH
# ============================================================

def run_research(topic: str):

    # --------------------------------------------------------
    # Check API keys
    # --------------------------------------------------------

    if not os.getenv("GROQ_API_KEY"):
        raise ValueError(
            "GROQ_API_KEY is missing. "
            "Please add it to Streamlit Secrets."
        )

    if not os.getenv("SERPER_API_KEY"):
        raise ValueError(
            "SERPER_API_KEY is missing. "
            "Please add it to Streamlit Secrets."
        )


    # --------------------------------------------------------
    # Create tasks
    # --------------------------------------------------------

    tasks = create_tasks(topic)


    # --------------------------------------------------------
    # Create Crew
    # --------------------------------------------------------

    crew = Crew(

        agents=[
            researcher,
            analyst,
            fact_checker,
            writer,
        ],

        tasks=tasks,

        process=Process.sequential,

        verbose=True,
    )


    # --------------------------------------------------------
    # Start research
    # --------------------------------------------------------

    result = crew.kickoff()


    return str(result)
