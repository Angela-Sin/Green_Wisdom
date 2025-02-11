
---

<h1 align="center"><strong>Green Wisdom</strong>

---


# Project Overview

# Criteria

## content
* [Green Wisdom](#green-wisdom)
* [Project Overview](#project-overview)
* [Criteria](#criteria)
* [Goal & UX](#goal--ux)
* [Website Structure](#website-structure)
  * [Landing Page](#landing-page)
  * [Resources](#resources)
    * [Instructions](#instructions)
  * [Contact Page](#contact-page)
  * [Responsiveness](#responsiveness)
* [Wireframes](#wireframes)
* [Development Process](#development-process)
  * [Agile Methodology](#agile-methodology)
  * [Collaboration Tools](#collaboration-tools)
* [Features](#features)
  * [Technologies Used](#technologies-used)
   * [VsCode migration](#vscode-migration)
  * [Validation](#validation)
* [Future Adding](#future-adding)
* [Django Setup](#django-setup)
* [Prerequisites and Deployment](#prerequisites-and-deployment)
  * [Forking](#forking)
  * [Making a Local Clone](#making-a-local-clone)
  * [Obtaining EmailJS API](#obtaining-emailjs-api)
* [Acknowledgements](#acknowledgements)




# Project Milestones

| Milestone | Task | Status | Deadline |
|-----------|--------|-------------|------------|
| 1. Project Setup & Database Models | Project Setup & Database Models | ✅ Completed | Feb 14 |
| 2. Deployment | Deploy to Heroku with PostgreSQL | ✅ Completed | Feb 14 |
| 3. CRUD for Blog Posts | Implement Create, Read, Update, Delete for registered visitors | 🔄 In Progress | Feb 18 |
| 4. UI & Templates | Build HTML templates with Bootstrap/Tailwind | 🔄 In Progress | Feb 22 |
| 5. Permissions & User Roles | Ensure users can only edit/delete their posts | ⏳ Pending | Feb 26 |
| 6. Comments & Likes (Optional) | Allow users to comment/like posts | ⏳ Pending | Feb 29 |
| 7. Testing & Bug Fixes | Ensure authentication, permissions, and CRUD work properly |⏳ Pending | Mar 15 |
| 8. Documentation | Finalize README.md, API docs, and usage instructions |🔄 In Progress | Mar 10 |
| 9. Subbmition | Final Project subbmition | ⏳ Pending| Mar 10 |

# Goal & UX
# Website Structure
# Landing Page
# Resources
# Responsiveness
# Wireframes

![image](static/images/Example.png)

# Development Process
# Agile Methodology
# Collaboration Tools
# Features

# Technologies Used


| Source                                                                                                               | Location       | Notes                        |
| -------------------------------------------------------------------------------------------------------------------- | -------------- | ---------------------------- |
| [Git](https://git-scm.com) |Across website|used for version control.(`git add`, `git commit`, `git push`)
|[GitHub](https://github.com)|Across website|used for secure online code storage.
|[Gitpod](https://gitpod.io)|Across website|used as a cloud-based IDE for development.
|[VSCode](https://code.visualstudio.com)|Across website|used as a local IDE for development.
|[HTML](https://en.wikipedia.org/wiki/HTML)|Across website|used for the main site content.
|[CSS](https://en.wikipedia.org/wiki/CSS)|Across website|used for the main site design and layout.
| [YouTube](https://www.youtube.com/)                                                                                  | Across website  | Tutorial for troubleshouting |
| [Fonts Google](https://fonts.google.com/)                                                                            | Across website | Font selection               |
| [W3Schools](https://www.w3schools.com/)                                                                              | Across website | Various help pages           |
| [Bootstrap](https://getbootstrap.com/)                                         | Across website | used as the front-end CSS framework for modern responsiveness and pre-built components.   |
| [Flaticon](https://www.flaticon.com/free-icons/free)                                                                              | 
Social Media Icons | 
| [icons8](https://icons8.com/icons/set/food)                                                                              | Logo | 
| [Allauth](https://docs.allauth.org/en/dev/installation/quickstart.html#post-installation) | Allauth package | Across website |
| [stackoverflow](https://stackoverflow.com/questions/77012106/django-allauth-modulenotfounderror-no-module-named-allauth-account-middlewar) | Debbuging actions | |



# VS Code Migration

## Useful Links

1. **Setting up and activating .venv on VS Code**  
   [Read the guide](https://docs.google.com/document/d/e/2PACX-1vTrL4s5fkIY_SJXjazXiAd6LDKjS7uZMHwY9XW6REJ2T_DyCGRRjjmW-0p4NnkomUwAAru0vLYALohwY/pub)

2. **Migration Guide for Hello Django, Django Blog, PP4, and MS3 projects**  
   [Read the guide](https://docs.google.com/document/d/e/2PACX-1vRfWv2mSizbxD_QjmDlF-g87-WuKnaO6tAiJf6XrkgLZO6laULxBKPGgd9pB9v8q0TC_huVYJjSuwOp/pub)

3. **Converting an existing PA project from Gitpod to a Codespaces template**  
   [Read the guide](https://docs.google.com/document/d/e/2PACX-1vQeVAArk8HaowmShcEPYMQlK5D0hVt6XNVmr8YBmazARdk9Lj-8XA_xs3YmwTnxTCFNxCQJ_JQ9bbhw/pub)

4. **Migration guide for JavaScript Testing with Jest**  
   [Read the guide](https://docs.google.com/document/d/e/2PACX-1vQ7l-NroI9uGHmAq0yoi0H7CisuXsOOadYlDUJhRAZ0esg4omMnMfw63dAeKj-Tt1Yw1yXI3rXc4wVI/pub)

5. **Migration guide for the Taskmanager walkthrough with SQL**  
   [Read the guide](https://docs.google.com/document/d/e/2PACX-1vTb7E-raldOfsbrYvwCCH6szv0WEq9SStBE4MV62D4w6QD4ujKBlNgoQd_tlYUV4r1SxPw8g9sDJPdt/pub)

6. **Migration Guide for E-commerce walkthrough and projects**  
   [Read the guide](https://docs.google.com/document/d/e/2PACX-1vRSJVwU0rJ35m2w26Qr_D1algYpHwyvpnesk5vMx7ukrAYD2G1T6_8_0CNBQn2bPQQB8ov8ccKB_q1b/pub)

# Future Adding



# Django Setup


## Django Project Setup Guide

## 1. Install Django and Supporting Libraries
- Install Django and required dependencies:  
  - `django<4`
  - `gunicorn`
  - `dj_database_url`
  - `psycopg2`
  - `dj3-cloudinary-storage`
- After installing dependencies, create a `requirements.txt` file to track them using:  
  - `pip3 freeze --local > requirements.txt`

## 2. Create a Django Project and App
- Create a new Django project named **/**.  
- Create a new app (e.g., **app**).  
- Add the app name (**'/'**) to the `INSTALLED_APPS` list in `settings.py`.  

## 3. Create a Superuser
- Generate a superuser to access the Django admin panel.  
- Follow the prompts to enter a username, email, and password.  

## 4. Apply Database Migrations
- Run migrations to apply database changes.  

## 5. Set Up Environment Variables (`env.py`)
- Create an `env.py` file to store sensitive information such as:  
  - `DATABASE_URL`
  - `SECRET_KEY`
- Add the following code to `env.py`:  

  ```python
  import os
  os.environ["DATABASE_URL"] = "<copiedURLfromPostgresSQL>"
  os.environ["SECRET_KEY"] = "my_super^secret@key"
  ```

- Ensure `env.py` is added to `.gitignore` to prevent it from being uploaded to GitHub.  

### Update `settings.py`
- Modify `settings.py` to load environment variables:  

  ```python
  import os
  import dj_database_url

  if os.path.exists("env.py"):
      import env

  SECRET_KEY = os.environ.get("SECRET_KEY")  # Secret key stored in env.py
  ```

- Replace the `DATABASES` setting with:  

  ```python
  DATABASES = {
      'default': dj_database_url.parse(os.environ.get("DATABASE_URL"))
  }
  ```

## 6. Configure Templates Directory
- Define the templates directory in `settings.py`:  

  ```python
  TEMPLATES_DIR = os.path.join(BASE_DIR, "templates")
  ```

- Update the `TEMPLATES` configuration:  

  ```python
  TEMPLATES = [
      {
          ...,
          'DIRS': [
              os.path.join(BASE_DIR, "templates"),
              os.path.join(BASE_DIR, "templates", "allauth"),
          ],
          ...,
      }
  ]
  ```

## 7. Create Static, Media, and Templates Directories
- Inside the root project directory, create the following folders:  
  - **static**  
  - **media**  
  - **templates**  

## 8. Create a `Procfile` for Heroku Deployment
- In the project root, create a `Procfile` and add the following line:  

  ```
  web: gunicorn thescoop.wsgi
  ```

## 9. Apply Migrations Again
- Run the necessary migrations to finalize the setup.  

---

# PostgreSQL Setup

## 1. Create a New Database Instance  
- Set up a new database instance on **PostgreSQL** for your project.  

## 2. Retrieve Database URL  
- From your PostgreSQL user dashboard, locate and copy the [PostgreSQL](https://www.postgresql.org/) connection URL.  

## 3. Store the Database URL in `env.py`  
- Add the retrieved **DATABASE_URL** to your `env.py` file:  

  ```python
  import os
  os.environ["DATABASE_URL"] = "<your_postgres_connection_url>"
  ```

## 4. Add DATABASE_URL to Heroku Config Vars  
- In your **Heroku dashboard**, navigate to:  
  - **Settings** > **Reveal Config Vars**  
  - Add a new key-value pair:  
    - **Key:** `DATABASE_URL`  
    - **Value:** `<your_postgres_connection_url>`  



# Deployment

| Step | Location | Description |
|--------|----------|--------------------------------|
| Cloning the Repository	| GitHub & IDE |	Copy the repository link from GitHub and clone it in your IDE. |
| Creating a GitHub Repository	| GitHub |	Set up a new repository for version control. |
| Installing Django & Dependencies |	IDE |	Install Django, Gunicorn, and required packages. |
| Creating requirements.txt |	IDE |	Generate a list of dependencies using pip freeze > requirements.txt. |
| Initializing Django Project |	IDE	| Start the Django project and verify by running the local server. |
| Updating ALLOWED_HOSTS |	settings.py |	Add required domains for deployment compatibility. |
| Creating a Django App |	IDE |	Create and register a new Django app. |
| Creating a Heroku App |	Heroku |	Log in to Heroku and create a new app with a unique name. |
| Adding Config Vars	| Heroku |	Add DISABLE_COLLECTSTATIC=1, SECRET_KEY, and DATABASE_URL. |
| Installing Gunicorn	| IDE |	Install Gunicorn as the production WSGI server. |
| Creating a Procfile	| IDE |	Add web: gunicorn project_name.wsgi to configure deployment. |
| Connecting GitHub to Heroku |	Heroku |	Link Heroku with GitHub for automatic deployment. |
| Checking Heroku Resources	| Heroku |	Enable Eco Dynos and remove unnecessary PostgreSQL add-ons. |
| Creating a PostgreSQL Database |	CI Database Creator |	Generate a PostgreSQL database instance. |
| Installing Database Packages |	IDE |	Install dj-database-url and psycopg2-binary. |
| Creating env.py |	IDE |	Store DATABASE_URL and SECRET_KEY locally. |
| Adding Secret Keys to Config Vars |	Heroku |	Add environment variables for security. |
| Updating settings.py for DB |	IDE |	Configure database settings for PostgreSQL. |
| Running Migrations | IDE |	Apply database migrations with python manage.py migrate. |
| Creating a Superuser |	IDE |	Run python manage.py createsuperuser to set up an admin. |
| Setting  DEBUG = False |	settings.py	| Disable debug mode before deployment for security. |
| Deploying to Heroku |	GitHub & Heroku	Commit | changes, push to GitHub, and trigger deployment. |
| Restarting Heroku |	Heroku |	Use heroku restart to apply changes. |
# Forking
# Making a Local Clone
# Obtaining EmailJS API
# Acknowledgements

