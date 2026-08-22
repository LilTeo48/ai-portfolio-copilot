def calculate_skill_match(project_skills: list[str], job_skills: list[str]) -> float:
    """
    Calculate the percentage of job skills covered by a portfolio project.
    """
    if not job_skills:
        return 0.0

    project_set = {skill.lower().strip() for skill in project_skills}
    job_set = {skill.lower().strip() for skill in job_skills}

    matched_skills = project_set.intersection(job_set)

    return round((len(matched_skills) / len(job_set)) * 100, 2)