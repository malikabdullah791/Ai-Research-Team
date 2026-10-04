import os

from crewai import Crew, Process

from agents import (
    researcher,
    analyst,
    fact_checker,
    writer,
)

from tasks import create_tasks


def run_research(topic: str, status_callback=None):

    if not os.getenv("GROQ_API_KEY"):
        raise ValueError(
            "GROQ_API_KEY is missing. Add it to Streamlit Secrets."
        )

    if not os.getenv("SERPER_API_KEY"):
        raise ValueError(
            "SERPER_API_KEY is missing. Add it to Streamlit Secrets."
        )

    tasks = create_tasks(topic)

    # -----------------------------
    # Status updates
    # -----------------------------
    if status_callback:
        status_callback("🔎 Researcher — searching the web...")

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

    # Note:
    # CrewAI itself controls task execution.
    # Streamlit receives the main status updates here.
    if status_callback:
        status_callback("📊 Analyst — analyzing research findings...")

    result = crew.kickoff()

    if status_callback:
        status_callback("🔍 Fact Checker — verifying important claims...")

    if status_callback:
        status_callback("✍️ Writer — preparing the final report...")

    return str(result)
