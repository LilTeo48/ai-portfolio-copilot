# AI Portfolio Copilot

AI Portfolio Copilot is a Python and Streamlit application that analyzes a job description against a developer's portfolio projects.

The app extracts relevant technical skills from a job description, compares them with the technologies used in each project, ranks the projects by match percentage, identifies missing skills, and recommends specific improvements that could strengthen each project for the target role.

## Links

- GitHub: https://github.com/LilTeo48
- AI Portfolio Copilot: https://github.com/LilTeo48/ai-portfolio-copilot
- Spotify Analytics Backend: https://github.com/LilTeo48/spotify-analytics-backend
- ETL / Data Warehouse Project: https://github.com/LilTeo48/pythonprojects
- LinkedIn: https://www.linkedin.com/in/tyler-chadwick-81b9a6275/
- Portfolio: https://ai-portfolio-copilot-gxrf4qde5mkzhv7amssxsp.streamlit.app/

## Features

- Paste and analyze a real job description
- Extract recognized technical skills automatically
- Normalize common skill aliases
- Compare job requirements against portfolio project skills
- Rank portfolio projects by match percentage
- Highlight the best project to feature
- Show matched and missing skills
- Generate project recommendation summaries
- Suggest specific improvements for missing skills
- Calculate projected match scores
- Estimate the impact of adding individual missing skills
- Add a custom portfolio project to the analysis
- Display polished technical skill names in the UI
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

Portfolio Projects
Spotify Analytics Backend

Backend analytics API built with Python, FastAPI, PostgreSQL, and Docker.

Skills demonstrated:

Python
FastAPI
PostgreSQL
Docker
REST API development
Backend architecture
E-Commerce Database System

Database-focused application designed around customers, products, orders, payments, and business analytics.

Skills demonstrated:

Python
PostgreSQL
SQL
Relational database design
Data modeling
Analytics queries
IT Asset Tracker

Asset-management application that processes inventory data, stores it in SQLite, and presents results through a Streamlit dashboard.

Skills demonstrated:

Python
SQLite
Streamlit
Pandas
Data cleaning
Dashboard development
How It Works

AI Portfolio Copilot follows this workflow:

- A user enters a job description.
- The application extracts recognized technical skills.
- Common aliases are normalized to consistent skill names.
- Each portfolio project is compared against the job requirements.
- Projects receive a match score based on overlapping skills.
- Projects are ranked from strongest to weakest match.
- The strongest project is highlighted as the best project to feature.
- Missing skills are identified for each project.
- Improvement recommendations are generated.
- Projected scores show how specific upgrades could improve the match.
- Users can optionally add a custom portfolio project to the analysis.
Why I Built This

Software engineering and data job descriptions often contain long lists of technologies and requirements.

AI Portfolio Copilot turns those requirements into actionable portfolio decisions by showing:

- which projects best match a target role
- which skills are already demonstrated
- which skills are missing
- which project improvements could increase relevance to the role
- how individual skill upgrades could improve a project's match score

The project demonstrates Python application design, skill extraction, recommendation logic, project-ranking logic, automated testing, structured data organization, and Streamlit development.

Future Improvements

Planned enhancements include:

- Expand support for additional programming languages, frameworks, cloud platforms, and data tools
- Improve job-description parsing for more complex and less explicitly formatted requirements
- Support adding and editing multiple custom portfolio projects in one session
- Automatically analyze GitHub repositories to detect technologies and project capabilities
- Compare resumes directly against job descriptions
- Generate richer and more context-aware project improvement recommendations
- Add LLM-powered job-description and portfolio analysis
- Store portfolio projects and analysis history persistently
- Add more advanced Streamlit visualizations and comparison views
- Export analysis results as a shareable report
Deploy the application publicly with Streamlit Community Cloud
