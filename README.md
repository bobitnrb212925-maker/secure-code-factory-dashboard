# Secure Code Factory Monitoring Dashboard

A Django-based dashboard for monitoring security findings across the five pillars of the Secure Integrated Toolchain Framework (SITF): Endpoint/IDE, Version Control System (VCS), CI/CD, Registry, and Production.

## Implemented functionality

- Stores SITF pillars and security findings in Django models.
- Tracks finding title, description, severity, status, pillar, and creation date.
- Displays total, open, resolved, and critical finding counts.
- Filters findings by severity and SITF pillar.
- Generates Matplotlib charts for findings by severity and pillar.
- Provides Django administration pages for managing pillars and findings.
- Includes automated tests for user login and security finding creation.

## Technology stack

- Python
- Django
- SQLite for local development
- Matplotlib for dashboard charts
- HTML and CSS for the dashboard interface

## Run locally

1. Create and activate a Python virtual environment.
2. Install dependencies:

   ```bash
   pip install -r requirements.txt
   ```

3. Apply database migrations:

   ```bash
   python manage.py migrate
   ```

4. Create an administrator account if needed:

   ```bash
   python manage.py createsuperuser
   ```

5. Start the development server:

   ```bash
   python manage.py runserver
   ```

6. Open http://127.0.0.1:8000/ for the dashboard and http://127.0.0.1:8000/admin/ for administration.

## Run tests

```bash
python manage.py test dashboard
```

The current automated test suite contains two tests: user login and security finding creation. Both passed in the local test run recorded by the project contributor.

## Repository notes

- Do not commit the local SQLite database, virtual environment, Python cache files, or real secret keys.
- Configure `DJANGO_SECRET_KEY`, `DJANGO_DEBUG`, and `DJANGO_ALLOWED_HOSTS` as environment variables when deploying.
- This repository contains the current development implementation. CI/CD pipeline configuration and deployment evidence are separate follow-up tasks.
