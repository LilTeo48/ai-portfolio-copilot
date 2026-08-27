import streamlit as st

from app.project_data import (
    PROJECTS,
    KNOWN_SKILLS,
    SAMPLE_JOB_DESCRIPTION,
)
from app.project_matcher import (
    calculate_partial_upgrade_scores,
    calculate_projected_score,
    extract_skills_from_job_description,
    generate_improvement_suggestions,
    generate_project_recommendation,
    rank_projects,
)


def format_skill_name(skill: str) -> str:
    display_names = {
        "aws": "AWS",
        "fastapi": "FastAPI",
        "postgresql": "PostgreSQL",
        "rest apis": "REST APIs",
        "sql": "SQL",
        "sqlite": "SQLite",
        "streamlit": "Streamlit",
        "pandas": "Pandas",
        "python": "Python",
        "docker": "Docker",
        "javascript": "JavaScript",
        "typescript": "TypeScript",
    }

    normalized_skill = skill.strip().lower()

    return display_names.get(
        normalized_skill,
        skill.strip().title(),
    )


def display_project_status(status: str) -> None:
    if status == "Completed":
        st.success("✅ Completed")
    elif status == "In Progress":
        st.info("🚧 In Progress")
    else:
        st.warning("⚠️ Status Unknown")


st.set_page_config(
    page_title="AI Portfolio Copilot",
    page_icon="🚀",
    layout="wide",
)


st.title("🚀 AI Portfolio Copilot")

st.write(
    "Paste a job description and discover which portfolio projects "
    "best match the role, which skills are missing, and what to improve."
)


job_description = st.text_area(
    "Job Description",
    value=SAMPLE_JOB_DESCRIPTION.strip(),
    height=220,
    placeholder="Paste a job description here...",
)


with st.expander("➕ Add a Custom Portfolio Project"):
    custom_project_name = st.text_input(
        "Project Name",
        placeholder="Example: AI Resume Analyzer",
    )

    custom_project_status = st.selectbox(
        "Project Status",
        options=[
            "Completed",
            "In Progress",
        ],
    )

    custom_project_skills = st.text_input(
        "Project Skills",
        placeholder="Python, FastAPI, PostgreSQL, Docker",
    )

    include_custom_project = st.checkbox(
        "Include custom project in analysis",
    )


analyze_button = st.button(
    "Analyze Portfolio",
    type="primary",
)


if analyze_button:
    if not job_description.strip():
        st.warning(
            "Enter a job description before analyzing."
        )
        st.stop()

    job_skills = extract_skills_from_job_description(
        job_description,
        KNOWN_SKILLS,
    )

    if not job_skills:
        st.warning(
            "No recognized skills were found in the job description."
        )
        st.stop()

    st.subheader("Detected Job Skills")

    st.write(
        ", ".join(
            format_skill_name(skill)
            for skill in job_skills
        )
    )

    projects_to_analyze = list(PROJECTS)

    if include_custom_project:
        if not custom_project_name.strip():
            st.warning(
                "Enter a project name before including a custom project."
            )
            st.stop()

        custom_skills = [
            skill.strip()
            for skill in custom_project_skills.split(",")
            if skill.strip()
        ]

        if not custom_skills:
            st.warning(
                "Enter at least one skill for the custom project."
            )
            st.stop()

        projects_to_analyze.append(
            {
                "name": custom_project_name.strip(),
                "status": custom_project_status,
                "skills": custom_skills,
            }
        )

    rankings = rank_projects(
        projects_to_analyze,
        job_skills,
    )

    st.subheader("Project Rankings")

    best_project = rankings[0]

    st.success(
        f"🏆 Best Project to Feature: "
        f"{best_project['name']} "
        f"({best_project['match_score']}% match)"
    )

    for index, project in enumerate(
        rankings,
        start=1,
    ):
        with st.container(border=True):
            st.markdown(
                f"### {index}. {project['name']}"
            )

            display_project_status(
                project.get(
                    "status",
                    "Unknown",
                )
            )

            score = project["match_score"]

            col1, col2 = st.columns(2)

            with col1:
                st.metric(
                    "Current Match",
                    f"{score}%",
                )

            with col2:
                projected_score = (
                    calculate_projected_score(
                        project
                    )
                )

                st.metric(
                    "Potential Match",
                    f"{projected_score}%",
                )

            st.progress(
                score / 100
            )

            st.markdown(
                "**Recommendation**"
            )

            st.write(
                generate_project_recommendation(
                    project
                )
            )

            st.markdown(
                "**Matched Skills**"
            )

            if project["matched_skills"]:
                st.write(
                    ", ".join(
                        format_skill_name(skill)
                        for skill in project["matched_skills"]
                    )
                )
            else:
                st.write("None")

            st.markdown(
                "**Missing Skills**"
            )

            if project["missing_skills"]:
                st.write(
                    ", ".join(
                        format_skill_name(skill)
                        for skill in project["missing_skills"]
                    )
                )
            else:
                st.write("None")

            partial_scores = (
                calculate_partial_upgrade_scores(
                    project
                )
            )

            if partial_scores:
                st.markdown(
                    "**Individual Skill Upgrades**"
                )

                for upgrade in partial_scores:
                    st.write(
                        f"Add "
                        f"**{format_skill_name(upgrade['skill'])}** "
                        f"→ "
                        f"{upgrade['projected_score']}%"
                    )

            suggestions = (
                generate_improvement_suggestions(
                    project
                )
            )

            st.markdown(
                "**Improvement Suggestions**"
            )

            if suggestions:
                for suggestion in suggestions:
                    st.write(
                        f"- {suggestion}"
                    )
            else:
                st.success(
                    "No major skill gaps detected."
                )