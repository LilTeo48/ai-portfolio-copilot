from app.project_data import (
    PROJECTS,
    KNOWN_SKILLS,
    SAMPLE_JOB_DESCRIPTION,
)


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