# Secure Code Factory Monitoring Dashboard

A Django-based monitoring dashboard project for tracking security findings.

## Project structure
- `dashboard/` – dashboard application, models, views, routes, templates, migrations, and unit tests.
- `securefactory/` – Django project configuration and URL routing.
- `manage.py` – Django management command-line utility.

## Run locally
1. Create and activate a Python virtual environment.
2. Install Django: `pip install django`
3. Run migrations: `python manage.py migrate`
4. Run tests: `python manage.py test dashboard`
5. Start the server: `python manage.py runserver`

Do not commit local databases, virtual environments, secrets, or Python cache files.
