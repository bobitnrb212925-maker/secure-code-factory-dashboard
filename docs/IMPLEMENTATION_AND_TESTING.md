# Implementation and Testing Summary

## Implemented modules

The Django application is organised into two main packages:

- `dashboard`: data models, admin registration, dashboard view, URL route, HTML template, database migration, and unit tests.
- `securefactory`: Django project settings and ASGI/WSGI entry points.

## Data model

- `SITFPillar` stores the five SITF areas: Endpoint/IDE, VCS, CI/CD, Registry, and Production.
- `SecurityFinding` stores the finding title, description, associated pillar, severity, status, and creation timestamp.
- A finding references its pillar using a protected foreign key so a pillar with findings cannot be deleted accidentally.

## Dashboard features

- Summary counts for all, open, resolved, and critical findings.
- Filtering by severity and SITF pillar.
- Matplotlib bar charts showing findings by severity and by pillar.
- A findings table ordered by creation date.
- Django admin registration for managing pillars and findings.

## Unit test cases

| Test ID | Test case | Expected result |
|---|---|---|
| UT-01 | Log in with a valid test account | Django test client login returns true |
| UT-02 | Create a security finding linked to a SITF pillar | One finding is stored and its severity is High |

The local test run reported by the contributor completed with **2 tests passing**. Run the suite again after cloning or changing the code with:

```bash
python manage.py test dashboard
```

## Security and deployment notes

- The SQLite database and virtual environment are intentionally excluded from source control.
- Django's secret key is read from the `DJANGO_SECRET_KEY` environment variable; the fallback in settings is for local development only.
- Set `DJANGO_DEBUG=False` and configure `DJANGO_ALLOWED_HOSTS` before deployment.
- CI/CD configuration and a deployment demonstration remain follow-up work and are not claimed as completed here.
