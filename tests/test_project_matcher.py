from app.project_matcher import analyze_skill_match


def test_analyze_skill_match():
    project_skills = ["Python", "FastAPI", "PostgreSQL", "Docker"]
    job_skills = ["Python", "FastAPI", "AWS", "Docker"]

    result = analyze_skill_match(project_skills, job_skills)

    assert result["match_score"] == 75.0
    assert result["matched_skills"] == ["docker", "fastapi", "python"]
    assert result["missing_skills"] == ["aws"]


def test_case_insensitive():
    result = analyze_skill_match(
        ["python", "fastapi"],
        ["Python", "FastAPI"],
    )

    assert result["match_score"] == 100.0
    assert result["matched_skills"] == ["fastapi", "python"]
    assert result["missing_skills"] == []


def test_empty_job_skills():
    result = analyze_skill_match(["Python"], [])

    assert result == {
        "match_score": 0.0,
        "matched_skills": [],
        "missing_skills": [],
    }