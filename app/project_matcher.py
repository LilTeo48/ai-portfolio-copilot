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


if __name__ == "__main__":
    project_skills = ["Python", "FastAPI", "PostgreSQL", "Docker"]
    job_skills = ["Python", "FastAPI", "AWS", "Docker"]

    result = analyze_skill_match(project_skills, job_skills)

    print(result)