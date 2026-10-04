from crewai import Task

from agents import (
    researcher,
    analyst,
    fact_checker,
    writer,
)


def create_tasks(topic: str):

    # -----------------------------
    # Research Task
    # -----------------------------
    research_task = Task(
        description=f"""
        Research the following topic:

        {topic}

        Use the web search tool extensively.

        Find:
        1. Important background information
        2. Current developments
        3. Important facts and statistics
        4. Different perspectives
        5. Relevant organizations, studies, or credible sources

        Prefer recent and authoritative sources.

        Return structured research findings with source names
        and URLs where available.
        """,
        expected_output="""
        A structured research brief containing:
        - Key findings
        - Important facts
        - Evidence
        - Source names
        - Source URLs
        """,
        agent=researcher,
    )

    # -----------------------------
    # Analysis Task
    # -----------------------------
    analysis_task = Task(
        description=f"""
        Analyze the research findings about:

        {topic}

        Identify:
        - Major trends
        - Important relationships
        - Advantages and disadvantages
        - Key implications
        - Numerical insights where relevant

        Use the calculator tool whenever a numerical calculation
        is actually required.

        Do not invent data.
        """,
        expected_output="""
        A clear analytical summary containing:
        - Major insights
        - Comparisons
        - Trends
        - Implications
        - Any useful calculations
        """,
        agent=analyst,
        context=[research_task],
    )

    # -----------------------------
    # Fact Check Task
    # -----------------------------
    fact_check_task = Task(
        description=f"""
        Fact-check the research and analysis about:

        {topic}

        Use the web search tool to independently verify
        the most important factual claims.

        Pay special attention to:
        - Numbers
        - Dates
        - Statistics
        - Technical claims
        - Current information

        Identify claims that are strongly supported and claims
        that should be treated cautiously.
        """,
        expected_output="""
        A fact-checking report containing:
        - Verified claims
        - Claims needing caution
        - Corrections if necessary
        - Supporting source names and URLs
        """,
        agent=fact_checker,
        context=[research_task, analysis_task],
    )

    # -----------------------------
    # Writing Task
    # -----------------------------
    writing_task = Task(
        description=f"""
        Write the final research report about:

        {topic}

        Use ONLY the research, analysis, and fact-checking information
        provided by the previous agents.

        Structure the report as:

        # Research Report

        ## Executive Summary

        ## Introduction

        ## Key Findings

        ## Detailed Analysis

        ## Fact-Checked Evidence

        ## Challenges and Limitations

        ## Conclusion

        ## Sources

        Write professionally and clearly.

        Do not invent references, statistics, quotations, or facts.
        Preserve source URLs supplied by previous agents.
        """,
        expected_output="""
        A polished Markdown research report with clear headings,
        concise paragraphs, useful bullet points, and a Sources section.
        """,
        agent=writer,
        context=[
            research_task,
            analysis_task,
            fact_check_task,
        ],
    )

    return [
        research_task,
        analysis_task,
        fact_check_task,
        writing_task,
    ]
