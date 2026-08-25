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


analyze_button = st.button(
    "Analyze Portfolio",
    type="primary",
)


if analyze_button:
    if not job_description.strip():
        st.warning("Enter a job description before analyzing.")
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

    st.write(", ".join(job_skills))

    rankings = rank_projects(
        PROJECTS,
        job_skills,
    )

    st.subheader("Project Rankings")

    for index, project in enumerate(rankings, start=1):
        with st.container(border=True):
            st.markdown(
                f"### {index}. {project['name']}"
            )

            score = project["match_score"]

            col1, col2 = st.columns(2)

            with col1:
                st.metric(
                    "Current Match",
                    f"{score}%",
                )

            with col2:
                projected_score = calculate_projected_score(
                    project
                )

                st.metric(
                    "Potential Match",
                    f"{projected_score}%",
                )

            st.progress(score / 100)

            st.markdown("**Recommendation**")

            st.write(
                generate_project_recommendation(project)
            )

            st.markdown("**Matched Skills**")

            if project["matched_skills"]:
                st.write(
                    ", ".join(project["matched_skills"])
                )
            else:
                st.write("None")

            st.markdown("**Missing Skills**")

            if project["missing_skills"]:
                st.write(
                    ", ".join(project["missing_skills"])
                )
            else:
                st.write("None")

            partial_scores = (
                calculate_partial_upgrade_scores(project)
            )

            if partial_scores:
                st.markdown("**Individual Skill Upgrades**")

                for upgrade in partial_scores:
                    st.write(
                        f"Add **{upgrade['skill']}** "
                        f"→ {upgrade['projected_score']}%"
                    )

            suggestions = (
                generate_improvement_suggestions(project)
            )

            st.markdown("**Improvement Suggestions**")

            if suggestions:
                for suggestion in suggestions:
                    st.write(f"- {suggestion}")
            else:
                st.success(
                    "No major skill gaps detected."
                )