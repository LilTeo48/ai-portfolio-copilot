# AI Portfolio Copilot

AI Portfolio Copilot is a Python and Streamlit application that analyzes a job description against a developer's portfolio projects.

The app extracts relevant technical skills from the job description, compares them with the technologies used in each project, ranks the projects by match percentage, identifies missing skills, and recommends specific improvements that could strengthen each project for the target role.

# AI Portfolio Copilot

AI Portfolio Copilot is a Python and Streamlit application that analyzes job descriptions against a developer's portfolio projects.

## Links

- GitHub: https://github.com/LilTeo48
- AI Portfolio Copilot: https://github.com/LilTeo48/ai-portfolio-copilot
- Spotify Analytics Backend: https://github.com/LilTeo48/spotify-analytics-backend
- ETL / Data Warehouse Project: https://github.com/LilTeo48/pythonprojects
- LinkedIn: https://www.linkedin.com/in/tyler-chadwick-81b9a6275/
- Portfolio Website: [Add your portfolio URL here when ready]

## Features
...


## Features

- Paste and analyze a real job description
- Extract recognized technical skills automatically
- Compare job requirements against portfolio project skills
- Rank portfolio projects by match percentage
- Show matched and missing skills
- Generate project recommendation summaries
- Suggest specific improvements for missing skills
- Calculate projected match scores
- Estimate the impact of adding individual missing skills
- Interactive Streamlit web interface
- Automated test suite with Pytest

## Example Workflow

A backend engineering job description might include:

```text
Python
FastAPI
PostgreSQL
Docker
AWS
REST APIs

## Portfolio Projects

### Spotify Analytics Backend
Backend analytics API built with Python, FastAPI, PostgreSQL, and Docker.

**Skills demonstrated:**
- Python
- FastAPI
- PostgreSQL
- Docker
- REST API development
- Backend architecture

### E-Commerce Database System
Database-focused application designed around customers, products, orders, payments, and business analytics.

**Skills demonstrated:**
- Python
- PostgreSQL
- SQL
- Relational database design
- Data modeling
- Analytics queries

### IT Asset Tracker
Asset-management application that processes inventory data, stores it in SQLite, and presents results through a Streamlit dashboard.

**Skills demonstrated:**
- Python
- SQLite
- Streamlit
- Pandas
- Data cleaning
- Dashboard development

## Future Improvements

Planned enhancements include:

- Add support for more technical skills and skill aliases
- Improve job-description parsing for more complex role requirements
- Allow users to add and edit their own portfolio projects
- Analyze GitHub repositories automatically
- Compare resumes directly against job descriptions
- Generate more detailed project improvement recommendations
- Add LLM-powered job-description analysis
- Store portfolio data persistently
- Improve Streamlit UI and visualization
- Deploy the application publicly with Streamlit Community Cloud

## How It Works

AI Portfolio Copilot follows this workflow:

1. A user enters a job description.
2. The application extracts recognized technical skills.
3. Each portfolio project is compared against the job requirements.
4. Projects receive a match score based on overlapping skills.
5. Projects are ranked from strongest to weakest match.
6. Missing skills are identified.
7. Improvement recommendations are generated.
8. Projected scores show how specific upgrades could improve the match.

## Why I Built This

Software engineering and data job descriptions often contain long lists of technologies and requirements.

AI Portfolio Copilot helps turn those requirements into actionable portfolio decisions by showing:

- which projects best match a target role
- which skills are already demonstrated
- which skills are missing
- which project improvements could increase relevance to the role

The project demonstrates Python application design, skill extraction, recommendation logic, automated testing, data organization, and Streamlit development.
