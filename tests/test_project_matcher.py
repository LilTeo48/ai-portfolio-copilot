from app.project_matcher import analyze_skill_match, rank_projects


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

def test_rank_projects():
    projects = [
        {
            "name": "Spotify Analytics Backend",
            "skills": ["Python", "FastAPI", "PostgreSQL", "Docker"],
        },
        {
            "name": "E-Commerce Database System",
            "skills": ["Python", "PostgreSQL", "SQL"],
        },
        {
            "name": "IT Asset Tracker",
            "skills": ["Python", "SQLite", "Streamlit", "Pandas"],
        },
    ]

    job_skills = [
        "Python",
        "FastAPI",
        "PostgreSQL",
        "Docker",
        "AWS",
    ]

    rankings = rank_projects(projects, job_skills)

    assert rankings[0]["name"] == "Spotify Analytics Backend"
    assert rankings[0]["match_score"] == 80.0

    assert rankings[1]["name"] == "E-Commerce Database System"
    assert rankings[1]["match_score"] == 40.0

    assert rankings[2]["name"] == "IT Asset Tracker"
    assert rankings[2]["match_score"] == 20.0    