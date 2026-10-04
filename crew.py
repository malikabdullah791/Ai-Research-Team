import os

from crewai import Crew, Process

from agents import (
    researcher,
    analyst,
    fact_checker,
    writer,
)

from tasks import create_tasks


def run_research(topic):

    # ========================================================
    # CHECK API KEYS
    # ========================================================

    if not os.getenv("GROQ_API_KEY"):
        raise ValueError(
            "GROQ_API_KEY is missing."
        )

    if not os.getenv("SERPER_API_KEY"):
        raise ValueError(
            "SERPER_API_KEY is missing."
        )


    # ========================================================
    # CREATE TASKS
    # ========================================================

    tasks = create_tasks(topic)


    # ========================================================
    # CREATE CREW
    # ========================================================

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


    # ========================================================
    # RUN CREW
    # ========================================================

    result = crew.kickoff()


    return str(result)
