import re
def analyze_skill_match(
    project_skills: list[str],
    job_skills: list[str],
) -> dict:
    """
    Analyze how well a project's skills match a job's required skills.
    """
    if not job_skills:
        return {
            "match_score": 0.0,
            "matched_skills": [],
            "missing_skills": [],
        }

    project_set = {skill.lower().strip() for skill in project_skills}
    job_set = {skill.lower().strip() for skill in job_skills}

    matched_skills = sorted(project_set.intersection(job_set))
    missing_skills = sorted(job_set.difference(project_set))

    match_score = round(
        (len(matched_skills) / len(job_set)) * 100,
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
    Rank portfolio projects by how well their skills match a job.
    """
    ranked_projects = []

    for project in projects:
        analysis = analyze_skill_match(
            project["skills"],
            job_skills,
        )

        ranked_projects.append(
            {
                "name": project["name"],
                "match_score": analysis["match_score"],
                "matched_skills": analysis["matched_skills"],
                "missing_skills": analysis["missing_skills"],
            }
        )

    return sorted(
        ranked_projects,
        key=lambda project: project["match_score"],
        reverse=True,
    )

def extract_skills_from_job_description(
    job_description: str,
    known_skills: list[str],
) -> list[str]:
    """
    Extract known skills that appear in a job description.
    """
    found_skills = []

    for skill in known_skills:
        pattern = rf"(?<!\w){re.escape(skill)}(?!\w)"

        if re.search(pattern, job_description, re.IGNORECASE):
            found_skills.append(skill.lower())

    return sorted(set(found_skills))

if __name__ == "__main__":
    projects = [
        {
            "name": "Spotify Analytics Backend",
            "skills": [
                "Python",
                "FastAPI",
                "PostgreSQL",
                "Docker",
            ],
        },
        {
            "name": "E-Commerce Database System",
            "skills": [
                "Python",
                "PostgreSQL",
                "SQL",
            ],
        },
        {
            "name": "IT Asset Tracker",
            "skills": [
                "Python",
                "SQLite",
                "Streamlit",
                "Pandas",
            ],
        },
    ]

    job_description = """
    We are looking for a backend engineer with experience in
    Python, FastAPI, PostgreSQL, Docker, AWS, and REST APIs.
    """

    known_skills = [
        "Python",
        "FastAPI",
        "PostgreSQL",
        "Docker",
        "AWS",
        "REST APIs",
        "SQL",
        "SQLite",
        "Streamlit",
        "Pandas",
    ]

    job_skills = extract_skills_from_job_description(
        job_description,
        known_skills,
    )

    print("Extracted job skills:", job_skills)

    rankings = rank_projects(projects, job_skills)

    for index, project in enumerate(rankings, start=1):
        print(
            f"{index}. {project['name']} "
            f"- {project['match_score']}%"
        )