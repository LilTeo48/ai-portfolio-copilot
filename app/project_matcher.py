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

def generate_project_recommendation(project_analysis: dict) -> str:
    """
    Generate a simple recommendation explaining why a project
    is or is not a strong match for a job.
    """
    name = project_analysis["name"]
    score = project_analysis["match_score"]
    matched_skills = project_analysis["matched_skills"]
    missing_skills = project_analysis["missing_skills"]

    matched_text = ", ".join(matched_skills) if matched_skills else "none"
    missing_text = ", ".join(missing_skills) if missing_skills else "none"

    if score >= 75:
        recommendation = "Strong project to feature."
    elif score >= 50:
        recommendation = "Good project to feature, but it has some skill gaps."
    else:
        recommendation = "Not the strongest project for this job."

    return (
        f"{name}: {recommendation} "
        f"Match score: {score}%. "
        f"Matched skills: {matched_text}. "
        f"Missing skills: {missing_text}."
    ) 

def generate_improvement_suggestions(project_analysis: dict) -> list[str]:
    """
    Generate actionable improvement suggestions based on missing skills.
    """
    missing_skills = project_analysis["missing_skills"]

    suggestion_map = {
        "aws": "Deploy the project to AWS and document the deployment architecture.",
        "rest apis": "Add or document REST API endpoints and include example requests.",
        "docker": "Containerize the project with Docker and add setup instructions.",
        "postgresql": "Add PostgreSQL persistence and document the database schema.",
        "sql": "Add SQL queries that demonstrate analytics or business insights.",
        "fastapi": "Expose the project through FastAPI endpoints.",
        "python": "Add Python-based backend or automation functionality.",
    }

    suggestions = []

    for skill in missing_skills:
        suggestion = suggestion_map.get(
            skill,
            f"Add a project feature that demonstrates {skill}.",
        )
        suggestions.append(suggestion)

    return suggestions

def calculate_projected_score(project_analysis: dict) -> float:
    """
    Calculate the projected match score if all missing skills
    were added to the project.
    """
    matched_skills = project_analysis["matched_skills"]
    missing_skills = project_analysis["missing_skills"]

    total_skills = len(matched_skills) + len(missing_skills)

    if total_skills == 0:
        return 0.0

    projected_score = round(
        (total_skills / total_skills) * 100,
        2,
    )

    return projected_score

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

    print("\nProject Recommendations:")

    for project in rankings:
        recommendation = generate_project_recommendation(project)
        print(recommendation)

    print("\nImprovement Suggestions:")

    for project in rankings:
        print(f"\n{project['name']}")

        suggestions = generate_improvement_suggestions(project)
        projected_score = calculate_projected_score(project)

        print(
            f"Current score: {project['match_score']}% "
            f"-> Projected score: {projected_score}%"
        )

        if not suggestions:
            print("- No major skill gaps detected.")
        else:
            for suggestion in suggestions:
                print(f"- {suggestion}")       

    print("\nProject Rankings:")

    for index, project in enumerate(rankings, start=1):
        print(
            f"{index}. {project['name']} "
            f"- {project['match_score']}%"
        )