from crewai import Task

from agents import (
    researcher,
    analyst,
    fact_checker,
    writer,
)


def create_tasks(topic):

    # ========================================================
    # TASK 1 — RESEARCH
    # ========================================================

    research_task = Task(

        description=f"""
        Research the following topic:

        {topic}

        Find accurate and recent information.

        Focus on:
        - Important facts
        - Key concepts
        - Current developments
        - Statistics where available
        - Advantages and disadvantages
        - Important examples
        - Reliable sources

        Use the web search tool.

        Clearly identify useful sources.
        """,

        expected_output="""
        A detailed research summary containing:
        - Key findings
        - Important facts
        - Evidence
        - Source names
        - Source URLs where available
        """,

        agent=researcher,
    )


    # ========================================================
    # TASK 2 — ANALYSIS
    # ========================================================

    analysis_task = Task(

        description=f"""
        Analyze the research collected about:

        {topic}

        Identify:

        - Major findings
        - Important patterns
        - Comparisons
        - Benefits
        - Limitations
        - Practical implications
        - Numerical insights where applicable

        Use the calculator tool when mathematical calculations
        are required.

        Do not invent information.
        """,

        expected_output="""
        A structured analytical summary containing:
        - Major insights
        - Comparisons
        - Calculations if required
        - Practical conclusions
        """,

        agent=analyst,

        context=[research_task],
    )


    # ========================================================
    # TASK 3 — FACT CHECKING
    # ========================================================

    fact_check_task = Task(

        description=f"""
        Fact-check the research and analysis about:

        {topic}

        Verify important claims using reliable web sources.

        Identify:

        - Correct claims
        - Incorrect claims
        - Outdated information
        - Weakly supported claims
        - Claims that require caution

        Use the web search tool.

        Do not introduce unsupported information.
        """,

        expected_output="""
        A fact-checking report containing:
        - Verified claims
        - Questionable claims
        - Corrections
        - Supporting sources
        """,

        agent=fact_checker,

        context=[
            research_task,
            analysis_task
        ],
    )


    # ========================================================
    # TASK 4 — WRITING
    # ========================================================

    writing_task = Task(

        description=f"""
        Write the final research report about:

        {topic}

        Use the research, analysis and fact-checking results.

        The report should contain:

        1. Executive Summary
        2. Introduction
        3. Key Findings
        4. Detailed Analysis
        5. Advantages
        6. Limitations
        7. Practical Applications
        8. Conclusion
        9. Sources

        Write in professional but easy-to-understand English.

        Do not invent facts.

        Clearly distinguish verified information from
        uncertain information.
        """,

        expected_output="""
        A complete professional research report in Markdown format.
        """,

        agent=writer,

        context=[
            research_task,
            analysis_task,
            fact_check_task
        ],
    )


    return [
        research_task,
        analysis_task,
        fact_check_task,
        writing_task
    ]
