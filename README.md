
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
  * [Libraries](#libraries)
   * [VsCode migration](#vscode-migration)
  * [Validation](#validation)
* [Future Adding](#future-adding)
* [PostgreSQL Setup](#postgresql-setup)
* [Deployment](#deployment)
* [Bug/Issue](#bug-issue)
* [Acknowledgements](#acknowledgements)




# Project Milestones

| Milestone | Task | Status | Deadline |
|-----------|--------|-------------|------------|
| 1. Project Setup & Database Models | Project Setup & Database Models | ✅ Completed | Feb 14 |
| 2. Deployment | Deploy to Heroku with PostgreSQL | ✅ Completed | Feb 14 |
| 3. CRUD for Blog Posts | Implement Create, Read, Update, Delete for registered visitors | ✅ Completed | Feb 18 |
| 4. UI & Templates | Build HTML templates with Bootstrap | ✅ Completed | Feb 22 |
| 5. Permissions & User Roles | Ensure users can only edit/delete their posts | ✅ Completed | Feb 26 |
| 6. Comments & Likes (Optional) | Allow users to comment/like posts | ✅ Completed | Feb 28 |
| 7. Testing & Bug Fixes | Ensure authentication, permissions, and CRUD work properly |⏳ Pending | Mar 7  |
| 8. Documentation | Finalize README.md, API docs, and usage instructions |🔄 In Progress | Mar 10 |
| 9. Subbmition | Final Project subbmition | ⏳ Pending| Mar 10 |

# Goal & UX
### Pallete
![Image](static/images/README/pallete.png)
# Website Structure
# Landing Page and Blog
# Responsiveness
## Desctop
![Image](static/images/README/desctope2.png)
## Laptop
![Image](static/images/README/laptop.png)
## Tablet
![Image](static/images/README/tablet.png)
## Mobile
![Image](static/images/README/mobile1.png)
![Image](static/images/README/mobile2.png)
## User Authentication & Content Management Pages
 This project includes **Sign-Up**, **Sign-In**, **Log-Out**, **Comment**, **404**, **Add Post**, and **Update** pages, designed with classic Bootstrap templates for a sleek, clean, and user-friendly experience. Built with **Bootstrap**, ensuring full responsiveness and customization flexibility.

- **Sign-Up Page**: Simple and intuitive user registration form.

![Image](static/images/README/SignUp.png)

- **Sign-In Page**: Clean login interface for easy access.

![Image](static/images/README/SignIn.png)

- **Log-Out Page**: Smooth and hassle-free sign-out experience.

![Image](static/images/README/SignOut.png)

- **Comment Section**: User-friendly UI for discussions and interactions.

![Image](static/images/README/comment.png)

- **404 Page**: Minimalistic error page for better user navigation.

![Image](static/images/README/404.png)

- **Add Post Page**: Structured form to create new content.

![Image](static/images/README/AddPost.png)

- **Update Post Page**: Easy-to-use interface for modifying existing posts.

![Image](static/images/README/EditPost.png)


# Wireframes
## Home Page vs Blog Page Layout

The Home and Blog pages share a similar layout, with the following distinction:

- **Home Page**  
  - Displays a welcome message.  
  - Shows only the 4 latest posts.

- **Blog Page**  
  - Displays all available posts in a full archive, without any restrictions.
### Desctop
![image](static/images/Desctop.png)
### Ipad
![image](static/images/Ipad1.png)
![image](static/images/Ipad%20.png)
### Mobile
![image](static/images/Mobile.png)
![image](static/images/Mobilephone.png)
## Blog Post
### Desctop
![image](static/images/Post%20detail.png)
Ipad and mobile layout similar to Home page.
## Profile
![Image](static/images/README/Profile.png)

# Development Process
# Agile Methodology
# Collaboration Tools
# Features

# Technologies Used


| Source                                                                                                               | Location       | Notes                        |
| -------------------------------------------------------------------------------------------------------------------- | -------------- | ---------------------------- |
| [Git](https://git-scm.com) |Across website|used for version control.(`git add`, `git commit`, `git push`)
|[GitHub](https://github.com)|Across website|used for secure online code storage.
|[VSCode](https://code.visualstudio.com)|Across website|used as a local IDE for development.
|[HTML](https://en.wikipedia.org/wiki/HTML)|Across website|used for the main site content.
| [Readme](https://github.com/Angela-Sin/Green_Wisdom)                                                                   | Acros website  | As an example, created originally by me for hackathon |
|[CSS](https://en.wikipedia.org/wiki/CSS)|Across website|used for the main site design and layout.
| [YouTube](https://www.youtube.com/)                                                                                  | Across website  | Tutorial for troubleshouting |
| [Heroku](https://dashboard.heroku.com/apps)                                                                          | Acros website  | as the IDE for development.  |
|[Balsamiq](https://balsamiq.com/?gad_source=1&gclid=EAIaIQobChMIyraK9uzLiwMVIpdQBh306i98EAAYAiAAEgJ7JfD_BwE)| Across Website| Wireframes creation|
| [Fonts Google](https://fonts.google.com/)                                                                            | Across website | Font selection               |
| [W3Schools](https://www.w3schools.com/)                                                                              | Across website | Various help pages           |
| [Bootstrap](https://getbootstrap.com/)                                         | Across website | used as the front-end CSS framework for modern responsiveness and pre-built components.   |
| [Flaticon](https://www.flaticon.com/free-icons/free)|    Across Website |Social Media Icons |
| [icons8](https://icons8.com/icons/setfood) | Across website|| Logo|
| [Stackoverflow](https://stackoverflow.com/questions/77012106/django-allauth-modulenotfounderror-no-module-named-allauth-account-middlewar) | Across website|Debbuging actions | |
| [ChatGPT](https://chatgpt.com/)   | Across website |Content writing, debugging actions |
|[Svgrgrepo](https://www.svgrepo.com/svg/43426/profile)|Across website|Profile Icon Svg|
|[pep8ci](https://pep8ci.herokuapp.com/)||Python Validation|
|[colors.co](https://coolors.co/image-picker)||Pallete|

# Liabraries

## Libraries Used

## The following libraries and dependencies are used in this project:

- **Django** `v5.1.6` - A high-level Python web framework that encourages rapid development and clean, pragmatic design.
- **Cloudinary** `v1.42.2` - For managing media assets (images, videos) with cloud storage and delivery.
- **Crispy-Bootstrap5** `v2024.10` - Provides enhanced form styling for Django using Bootstrap 5.
- **Django-Allauth** `v65.4.1` - An integrated set of Django applications for handling authentication, registration, account management, and more.
- **Gunicorn** `v20.1.0` - A Python WSGI HTTP server for deploying Django applications.
- **OAuthLib** `v3.2.2` - A generic and standards-compliant library for implementing OAuth 1 and OAuth 2.
- **Pillow** `v11.1.0` - Python Imaging Library fork for image processing capabilities.
- **WhiteNoise** `v6.9.0` - Simplifies serving static files in production environments.

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

### Profile can be deleted by profile owner.
### Users can delete or update their comments.
### The number of likes is displayed next to the post.
### Social Sharing: Users will be able to share posts on social media platforms.
### Notifications: Users will receive notifications when their posts are commented on or liked.



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

# Forking the Repository

If you'd like to contribute to this project or make changes to your own version, you can **fork** the repository. This creates a copy of the repository under your own GitHub account, where you can make changes freely without affecting the original project.

## Steps to Fork the Repository

### 1. **Go to the GitHub Repository**
Navigate to the GitHub repository page you want to fork.

### 2. **Click on the Fork Button**
On the top right of the page, click the **Fork** button. GitHub will create a copy of the repository under your GitHub account.

### 3. **Clone Your Forked Repository**
Once the repository is forked, you can clone it to your local machine by following these steps:

- Go to your forked repository (it will be at `https://github.com/yourusername/your-repository-name`).
- Click the **Code** button and copy the repository's HTTPS URL.
  
    Example URL:
    ```
    https://github.com/yourusername/your-repository-name.git
    ```

- Open the terminal/command prompt on your local machine.
- Navigate to the directory where you want to clone the repository.
- Run the following command:

This will create a local copy of your forked repository.

## Making Changes in Your Fork

1. **Create a New Branch** (for feature work or fixes):
 - `git checkout -b your-feature-branch`

2. **Make Changes** to the files in the project.

3. **Stage the Changes** to Git:
 - `git add .`

4. **Commit the Changes**:
 - `git commit -m "Your commit message"`

5. **Push Your Changes** to GitHub:
 - `git push origin your-feature-branch`

## Submitting a Pull Request

Once you've made your changes and pushed them to your fork, you can submit a pull request to the original repository:

1. Go to the original repository (the one you forked from).
2. Click on the **Pull Requests** tab.
3. Click on the **New Pull Request** button.
4. Choose your forked repository and the branch you want to merge from.
5. Write a description of the changes you made and submit the pull request.

The repository owner will review your pull request and decide whether to merge it into the main project.

---

This section provides a clear guide on how users can fork the repository, make changes, and submit a pull request. You can add this to your README to help others contribute to your project. Let me know if you need more modifications!
# Making a Local Clone of the Repository

Follow these steps to make a local clone of the repository on your computer.

## Prerequisites

Make sure you have [Git](https://git-scm.com/) installed on your computer. If not, follow the installation instructions based on your operating system:

- **Windows**: [Download Git](https://git-scm.com/download/win) and follow the installation instructions.
- **macOS**: Install Git via [Homebrew](https://brew.sh/) by running:
  1. Open Terminal and run the command: `brew install git`
- **Linux**: Install Git using your package manager. For example, on Ubuntu:
  1. Open Terminal and run the command: `sudo apt install git`

## Cloning the Repository

### 1. Copy the Repository URL
- Go to the GitHub repository page you want to clone.
- Click the **Code** button (usually green) at the top right of the page.
- Copy the **HTTPS** URL of the repository. It will look something like this:
https://github.com/yourusername/your-repository-name.git

markdown
Copy
Edit

### 2. Open the Terminal/Command Prompt
- **Windows**: Open Command Prompt or PowerShell.
- **macOS/Linux**: Open the Terminal.

### 3. Navigate to the Desired Directory
Use the `cd` command to navigate to the folder where you want to clone the repository. For example:
- `cd /path/to/your/folder`

### 4. Clone the Repository
Run the following command, replacing `<repository-url>` with the URL you copied earlier:
- `git clone https://github.com/yourusername/your-repository-name.git`

This will create a new folder with the repository's name and download all the files from GitHub into that folder.

### 5. Enter the Cloned Directory
Once the clone is complete, navigate into the new directory:
- `cd your-repository-name`

### 6. Verify the Clone
To confirm that the repository has been cloned successfully, run the following command:
- `git status`

This should display the current status of the repository and indicate which branch you are on (e.g., "On branch main").

## Making Changes and Pushing Back to GitHub (Optional)

1. **Create a New Branch** (for feature work or fixes):
 - `git checkout -b your-feature-branch`

2. **Make Changes** to the files in the project.

3. **Stage the Changes** to Git:
 - `git add .`

4. **Commit the Changes**:
 - `git commit -m "Your commit message"`

5. **Push Your Changes** to GitHub:
 - `git push origin your-feature-branch`

6. **Create a Pull Request** on GitHub to merge your changes back into the main branch.
# Bug-Issue
## ISSUE #1 Deployment and Debugging Issues (Heroku, Cloudinary, and django-allauth)
### During the project setup and development, the following issues and resolutions were encountered:

Image Not Found (404 Error) in Admin Panel
After the initial setup, images were not loading in the admin panel, resulting in a 404 error. Updating the django-allauth and Django versions resolved this issue.

### 500 Error on Heroku After Modifying account.html

Locally, with DEBUG = True in settings.py, the application worked as expected.
However, deploying the changes to Heroku with DEBUG = False resulted in a 500 error. No error trace was visible in the terminal logs.
After updating django and django-allauth once again, the 500 error was resolved on Heroku.
Cloudinary Configuration Issue
A missing configuration in models.py related to Cloudinary was causing errors. Adding the correct command in models.py fixed the issue.
+from cloudinary_storage.storage import MediaCloudinaryStorage, +storage=MediaCloudinaryStorage(), =class BlogPost

## ISSUE #2
After upgrading texteditor reachtexteditor was changed to simple texteditor, so I lefted 4.14.0 with allert message.
![image](static/images/bug.png)
# Acknowledgements

- Special mention is also deserved by my mentor **Medale Oluwafemi** for helping me understand the requirements and guiding me through the realization of this project!
- My cohort facilitator, **Kay Welfare** for pointing out the important parts of fulfilling the project completion criteria I needed to focus on.
- **Vernell Clark** - past student from Code institute, He help me to fix the some of the repeating functions and syntaxes on the project by discussing them together.
- Mentor **Daisy Mc Girr's** tutorial on YouTube helped me build my project.
- As a tutoring team for help and support during the project.
- All **Slack** comunity members and espetially **Kasia Bogucka** who helped me to solve issue with VsCode migration.
- Code Institute's 'Django Blog' project.
- Stack Overflow.
