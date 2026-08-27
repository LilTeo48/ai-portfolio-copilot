import re

from app.project_data import (
    PROJECTS,
    KNOWN_SKILLS,
    SAMPLE_JOB_DESCRIPTION,
    SKILL_ALIASES,
)


def normalize_skill_name(skill: str) -> str:
    """
    Normalize a skill name to the canonical value used internally.

    Examples:
        Postgres -> postgresql
        Amazon Web Services -> aws
        RESTful APIs -> rest apis
    """
    normalized_skill = skill.strip().lower()

    return SKILL_ALIASES.get(
        normalized_skill,
        normalized_skill,
    )


def analyze_skill_match(
    project_skills: list[str],
    job_skills: list[str],
) -> dict:
    """
    Compare project skills against job skills and calculate
    the percentage of job requirements matched.
    """
    normalized_project_skills = {
        normalize_skill_name(skill)
        for skill in project_skills
    }

    normalized_job_skills = {
        normalize_skill_name(skill)
        for skill in job_skills
    }

    if not normalized_job_skills:
        return {
            "match_score": 0.0,
            "matched_skills": [],
            "missing_skills": [],
        }

    matched_skills = sorted(
        normalized_project_skills
        & normalized_job_skills
    )

    missing_skills = sorted(
        normalized_job_skills
        - normalized_project_skills
    )

    match_score = round(
        (
            len(matched_skills)
            / len(normalized_job_skills)
        )
        * 100,
        2,
    )

    return {
        "match_score": match_score,
        "matched_skills": matched_skills,
        "missing_skills": missing_skills,
    }


def rank_projects(
    projects: list[dict],
    job_skills: list[str],
) -> list[dict]:
    """
    Rank portfolio projects from strongest to weakest
    match for the supplied job skills.

    Project status is preserved so the UI can distinguish
    completed projects from projects that are still in progress.
    """
    rankings = []

    for project in projects:
        analysis = analyze_skill_match(
            project["skills"],
            job_skills,
        )

        ranked_project = {
            "name": project["name"],
            "status": project.get(
                "status",
                "Unknown",
            ),
            "match_score": analysis[
                "match_score"
            ],
            "matched_skills": analysis[
                "matched_skills"
            ],
            "missing_skills": analysis[
                "missing_skills"
            ],
        }

        rankings.append(
            ranked_project
        )

    return sorted(
        rankings,
        key=lambda project: project[
            "match_score"
        ],
        reverse=True,
    )


def extract_skills_from_job_description(
    job_description: str,
    known_skills: list[str],
) -> list[str]:
    """
    Extract recognized technical skills from a job description.

    Common aliases are normalized to canonical skill names.
    """
    found_skills = set()

    searchable_skills = {
        skill.lower(): skill.lower()
        for skill in known_skills
    }

    searchable_skills.update(
        SKILL_ALIASES
    )

    for (
        searchable_skill,
        canonical_skill,
    ) in searchable_skills.items():
        pattern = (
            rf"(?<!\w)"
            rf"{re.escape(searchable_skill)}"
            rf"(?!\w)"
        )

        if re.search(
            pattern,
            job_description,
            re.IGNORECASE,
        ):
            found_skills.add(
                canonical_skill
            )

    return sorted(
        found_skills
    )


def generate_project_recommendation(
    project_analysis: dict,
) -> str:
    """
    Generate a recommendation based on a project's
    current job-description match score.
    """
    project_name = project_analysis[
        "name"
    ]

    match_score = project_analysis[
        "match_score"
    ]

    matched_skills = project_analysis[
        "matched_skills"
    ]

    missing_skills = project_analysis[
        "missing_skills"
    ]

    matched_text = (
        ", ".join(matched_skills)
        if matched_skills
        else "none"
    )

    missing_text = (
        ", ".join(missing_skills)
        if missing_skills
        else "none"
    )

    if match_score >= 75:
        recommendation = (
            "Strong project to feature "
            "for this job."
        )
    elif match_score >= 50:
        recommendation = (
            "Good project to feature, "
            "but it has some skill gaps."
        )
    else:
        recommendation = (
            "Not the strongest project "
            "for this job."
        )

    return (
        f"{project_name}: "
        f"{recommendation} "
        f"Match score: {match_score}%. "
        f"Matched skills: {matched_text}. "
        f"Missing skills: {missing_text}."
    )


def generate_improvement_suggestions(
    project_analysis: dict,
) -> list[str]:
    """
    Generate actionable recommendations for the
    skills missing from a portfolio project.
    """
    suggestion_map = {
        "aws": (
            "Deploy the project to AWS and "
            "document the deployment architecture."
        ),
        "rest apis": (
            "Add or document REST API endpoints "
            "and include example requests."
        ),
        "docker": (
            "Containerize the project with Docker "
            "and add setup instructions."
        ),
        "postgresql": (
            "Add PostgreSQL persistence and "
            "document the database schema."
        ),
        "sql": (
            "Add SQL queries that demonstrate "
            "analytics or business insights."
        ),
        "fastapi": (
            "Expose the project through "
            "FastAPI endpoints."
        ),
        "python": (
            "Add Python-based backend or "
            "automation functionality."
        ),
    }

    missing_skills = project_analysis[
        "missing_skills"
    ]

    suggestions = []

    for skill in missing_skills:
        suggestion = suggestion_map.get(
            skill,
            (
                "Add a project feature that "
                f"demonstrates {skill}."
            ),
        )

        suggestions.append(
            suggestion
        )

    return suggestions


def calculate_projected_score(
    project_analysis: dict,
) -> float:
    """
    Calculate the projected match score if all
    currently missing skills were added.
    """
    matched_skills = project_analysis[
        "matched_skills"
    ]

    missing_skills = project_analysis[
        "missing_skills"
    ]

    total_skills = (
        len(matched_skills)
        + len(missing_skills)
    )

    if total_skills == 0:
        return 0.0

    return 100.0


def calculate_partial_upgrade_scores(
    project_analysis: dict,
) -> list[dict]:
    """
    Calculate the projected match score for adding
    each missing skill individually.
    """
    matched_skills = project_analysis[
        "matched_skills"
    ]

    missing_skills = project_analysis[
        "missing_skills"
    ]

    total_skills = (
        len(matched_skills)
        + len(missing_skills)
    )

    if total_skills == 0:
        return []

    upgrade_scores = []

    for skill in missing_skills:
        projected_matched_count = (
            len(matched_skills) + 1
        )

        projected_score = round(
            (
                projected_matched_count
                / total_skills
            )
            * 100,
            2,
        )

        upgrade_scores.append(
            {
                "skill": skill,
                "projected_score": (
                    projected_score
                ),
            }
        )

    return upgrade_scores


def get_job_description_from_user() -> str:
    """
    Collect a multi-line job description from
    terminal input.

    Submit an empty line to finish.
    """
    print(
        "\nPaste the job description below."
    )

    print(
        "Press Enter on an empty line "
        "when finished.\n"
    )

    lines = []

    while True:
        line = input()

        if not line.strip():
            break

        lines.append(
            line
        )

    return "\n".join(
        lines
    ).strip()


if __name__ == "__main__":
    projects = PROJECTS
    known_skills = KNOWN_SKILLS

    job_description = (
        get_job_description_from_user()
    )

    if not job_description:
        print(
            "\nNo job description entered."
        )

        print(
            "Using the sample job "
            "description instead."
        )

        job_description = (
            SAMPLE_JOB_DESCRIPTION
        )

    job_skills = (
        extract_skills_from_job_description(
            job_description,
            known_skills,
        )
    )

    print(
        "Extracted job skills:",
        job_skills,
    )

    rankings = rank_projects(
        projects,
        job_skills,
    )

    print(
        "\nProject Recommendations:"
    )

    for project in rankings:
        recommendation = (
            generate_project_recommendation(
                project
            )
        )

        print(
            recommendation
        )

    print(
        "\nImprovement Suggestions:"
    )

    for project in rankings:
        print(
            f"\n{project['name']}"
        )

        print(
            f"Status: "
            f"{project['status']}"
        )

        suggestions = (
            generate_improvement_suggestions(
                project
            )
        )

        projected_score = (
            calculate_projected_score(
                project
            )
        )

        partial_scores = (
            calculate_partial_upgrade_scores(
                project
            )
        )

        print(
            f"Current score: "
            f"{project['match_score']}% "
            f"-> Projected score: "
            f"{projected_score}%"
        )

        if partial_scores:
            print(
                "Individual skill upgrades:"
            )

            for upgrade in partial_scores:
                print(
                    f"- Add "
                    f"{upgrade['skill']} "
                    f"-> "
                    f"{upgrade['projected_score']}%"
                )

        if not suggestions:
            print(
                "- No major skill gaps detected."
            )
        else:
            for suggestion in suggestions:
                print(
                    f"- {suggestion}"
                )

    print(
        "\nProject Rankings:"
    )

    for index, project in enumerate(
        rankings,
        start=1,
    ):
        print(
            f"{index}. "
            f"{project['name']} "
            f"[{project['status']}] "
            f"- "
            f"{project['match_score']}%"
        )