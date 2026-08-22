from app.project_matcher import calculate_skill_match


def test_calculate_skill_match():
    project_skills = ["Python", "FastAPI", "PostgreSQL", "Docker"]
    job_skills = ["Python", "FastAPI", "AWS", "Docker"]

    score = calculate_skill_match(project_skills, job_skills)

    assert score == 75.0


def test_case_insensitive():
    score = calculate_skill_match(
        ["python", "fastapi"],
        ["Python", "FastAPI"],
    )

    assert score == 100.0


def test_empty_job_skills():
    score = calculate_skill_match(["Python"], [])

    assert score == 0.0