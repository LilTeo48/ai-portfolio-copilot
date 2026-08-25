

PROJECTS = [
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


KNOWN_SKILLS = [
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

SKILL_ALIASES = {
    "postgres": "postgresql",
    "postgresql": "postgresql",
    "amazon web services": "aws",
    "aws": "aws",
    "rest api": "rest apis",
    "rest APIs": "rest apis",
    "restful api": "rest apis",
    "restful apis": "rest apis",
    "javascript": "javascript",
    "js": "javascript",
    "typescript": "typescript",
    "ts": "typescript",
}


SAMPLE_JOB_DESCRIPTION = """
We are looking for a backend engineer with experience in
Python, FastAPI, PostgreSQL, Docker, AWS, and REST APIs.
"""



def test_projects_have_required_fields():
    assert PROJECTS

    for project in PROJECTS:
        assert "name" in project
        assert "skills" in project
        assert isinstance(project["skills"], list)
        assert project["name"]
        assert project["skills"]


def test_known_skills_not_empty():
    assert KNOWN_SKILLS
    assert "Python" in KNOWN_SKILLS


def test_sample_job_description_not_empty():
    assert SAMPLE_JOB_DESCRIPTION.strip()