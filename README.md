# CampusConnect (CSIT327 – First Django)

- **Name:** Milbert Macarambon Jr.
- **Section:** G1
- **Course:** CSIT327

A Django app with sign-up, login, a dashboard, and a user profile page, styled with Bootstrap 5 (loaded from the CDN).

## Features

- Sign-up with a success message (Django messages framework, shown as a Bootstrap alert)
- Login / logout
- Profile page built with a class-based `UpdateView`; login required, and users can only view and edit their own profile
- Shared `base.html` with the Bootstrap 5 CDN links and a navbar; every page extends it
- CSRF protection on all forms

## How to run

1. Clone the repository and open the project folder:
   ```bash
   git clone https://github.com/TrebMcaf/CSIT327-G1-Macarambon-MilbertJr-FirstDjango
   cd CSIT327-G1-Macarambon-MilbertJr-FirstDjango
   ```
2. Create and activate a virtual environment:
   ```bash
   python -m venv .venv
   # Windows
   .venv\Scripts\activate
   # macOS / Linux
   source .venv/bin/activate
   ```
3. Install Django:
   ```bash
   pip install django
   ```
4. Apply migrations:
   ```bash
   python manage.py migrate
   ```
5. Start the server:
   ```bash
   python manage.py runserver
   ```
6. Open http://127.0.0.1:8000/ in your browser.

## Run the tests

```bash
python manage.py test
```

## Pages

| URL | Description |
| --- | --- |
| `/accounts/signup/` | Create an account |
| `/accounts/login/` | Log in |
| `/accounts/profile/` | View and edit your own profile (login required) |
| `/` | Dashboard (login required) |
