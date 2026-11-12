# Secure Code Factory – Part 2 Team Progress and Access Guide

This page brings together the current project links, the contribution prepared on the feature branch, and the remaining Part 2 work.

## 1. Main project links

- **GitHub repository:** https://github.com/bobitnrb212925-maker/secure-code-factory-dashboard
- **Contribution branch:** [feature/add-django-implementation](https://github.com/bobitnrb212925-maker/secure-code-factory-dashboard/tree/feature/add-django-implementation)
- **Pull Request #1 (review before merging):** https://github.com/bobitnrb212925-maker/secure-code-factory-dashboard/pull/1
- **CircleCI dashboard:** https://app.circleci.com/
- **CircleCI project page:** https://app.circleci.com/projects/github/bobitnrb212925-maker/secure-code-factory-dashboard

## 2. Work contributed on the feature branch

The branch contains the Django dashboard implementation and supporting project files, including:

- Dashboard application files (models, views, URLs, templates and admin configuration).
- Django project configuration and `manage.py`.
- Dependency list in `requirements.txt`.
- Dashboard unit tests.
- Implementation and testing notes in `docs/IMPLEMENTATION_AND_TESTING.md`.
- CircleCI pipeline configuration in `.circleci/config.yml`.

Two dashboard tests were run locally: the login test and the security-finding creation test. Both passed locally. The CircleCI configuration has been added, but the automated pipeline result must still be checked in CircleCI; do not treat it as passed until a successful run is visible.

## 3. How team members can review the work

1. Open the GitHub repository link above.
2. Open the feature branch link to view the contributed files.
3. Open Pull Request #1 to review the proposed changes and leave comments.
4. Do not merge the pull request until the group has reviewed and agreed.

To collaborate directly, the repository owner should add each member's GitHub username under **Repository → Settings → Collaborators** (or the equivalent access-management section) and the member must accept the invitation. A public repository can be viewed without collaborator access, but editing and other actions require appropriate permissions.

## 4. CircleCI review

Open the CircleCI project page and sign in using an authorized GitHub account. Check the pipeline for the `feature/add-django-implementation` branch. A green successful workflow is the evidence that the automated pipeline passed. If the project is not visible, check that CircleCI has been authorized for the repository and that the account has the required access.

## 5. Remaining Part 2 work for the group

- Complete the Software Requirements Specification (SRS).
- Prepare system modelling diagrams, including use-case, activity and architecture diagrams.
- Develop the Requirements Traceability Matrix (RTM).
- Complete the system design and justify the design choices.
- Expand the test plan and collect test execution evidence.
- Complete the Trello board with tasks, owners, deadlines and progress.
- Confirm and capture a successful CI/CD pipeline run.
- Prepare the final report within the assignment's seven-page limit, including references.

The group should allocate these remaining tasks among members and include the lecturer in the project team as required by the assignment brief. The stated submission deadline is 15 November 2026.

## 6. Important note

This page is a progress and access guide, not proof that every Part 2 requirement is complete. Team members should review the repository, verify the pipeline result, and agree on the remaining task allocation.
