
---

<h1 align="center"><strong>Green Wisdom</strong>

---

![Image](static/images/README/UI%20(2).png)


## Welcome to the **Green Wisdom** Blog – A Gardening Community!

Developed for Project Milestone 4 of the Code Institute Full-Stack Development Program, this blog is a full-stack Django project hosted on Heroku.

The **Green Wisdom** Blog is designed specifically for gardening enthusiasts. Whether you're a seasoned gardener or just starting out, this platform allows you to read, create, and share your own blog posts about gardening. Share your experiences, tips, and plant care advice with a like-minded community. Engage with other gardeners by commenting on posts, discussing new techniques, and finding inspiration for your next green-thumb project!

Happy Gardening! 🌱🌿🌼

## [LIVE SITE](https://green-wisdom-99e0528945fb.herokuapp.com/)

## [GITHUB RESPOSITORY](https://github.com/Angela-Sin/Green_Wisdom)




# Content
* [Green Wisdom](#green-wisdom)
* [Project Overview](#project-overview)
* [Project Milestones](#project-milestones)
* [Goal & UX](#goal--ux)
  * [Website Structure](#website-structure)
  * [Responsiveness](#responsiveness)
* [Wireframes](#wireframes)
* [Development Process](#development-process)
* [Future Adding](#future-adding)
* [Agile Methodology](#agile-methodology)
* [Testing](#testing)
* [Features](#features)
  * [Technologies Used](#technologies-used)
  * [Libraries](#libraries)
  * [VsCode migration](#vs-code-migration)
  * [PostgreSQL Setup](#postgresql-setup)
  * [Deployment](#deployment)
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
| 7. Testing & Bug Fixes | Ensure authentication, permissions, and CRUD work properly |✅ Completed | Mar 7  |
| 8. Documentation | Finalize README.md, API docs, and usage instructions |✅ Completed | Mar 10 |
| 9. Subbmition | Final Project subbmition | ✅ Completed| Mar 10 |

# Goal & UX

## 🌱 Project Overview  

The **Green Wisdom Blog** is designed to provide an engaging and interactive space for gardeners to share their insights and learn from one another. Users can explore gardening content, submit their own blog posts, and participate in discussions through comments.  

##  Project Goals  

- **Engaging User Experience:** Create an inviting and interactive platform where users can explore and contribute gardening posts.  
- **Seamless Navigation:** Offer an intuitive layout that makes it easy to browse articles, submit posts, and engage with the community.  
- **User Participation:** Enable users to share their gardening stories, tips, and experiences by posting articles.  
- **Community Interaction:** Allow users to read and comment on posts, fostering discussions and knowledge-sharing. Note: Comments cannot be edited or updated after submission.  
- **Responsive Design:** Ensure a smooth and user-friendly experience across all devices, including smartphones, tablets, and desktops.  

##  First-Time Visitors’ Experience  

- **Explore Gardening Content:** Discover a variety of posts filled with gardening tips, techniques, and inspiration.  
- **Search for Topics:** Easily find specific posts about plant care, gardening methods, or seasonal tips.  
- **Read Community Discussions:** Gain insights and advice from fellow gardeners by exploring comment sections.  
- **Leave a Comment:** Share thoughts and feedback on blog posts to contribute to the conversation.  
- **Learn About the Blog:** Access social media links and additional resources to stay connected with the community.  

##  Returning Visitors’ Experience  

- **Access Previous Posts:** View and manage blog posts they have contributed.  
- **Submit New Content:** Share fresh gardening insights by adding new posts.  
- **Engage with the Community:** Continue participating by reading and commenting on new content.  

##  Frequent Visitors’ Experience  

- **Discover the Latest Posts:** Stay updated with newly added gardening articles from the community.  
- **Contribute More Content:** Regularly share gardening knowledge, ideas, and personal experiences.  
- **Stay Inspired:** Connect with like-minded individuals and continue expanding gardening wisdom.  


# Website Structure

## Page Structure Overview

| Feature              | Home Page (`index.html`) | Blog Page (`posts.html`) | Single Post Page (`post_detail.html`) | Profile Page (`profile.html`) |
|----------------------|----------------------|-----------------------|-----------------------------|----------------------------|
| **Main Purpose**     | Highlights the latest blog posts | Lists all blog posts | Displays the full content of a single blog post | Displays user profile details and their posts |
| **Post Limit**       | Only the last 4 posts | All posts displayed | Only one specific post | User's latest posts |
| **Content Structure** | Includes a welcome message | No welcome message, just a list of posts | Full post content, title, category, and featured image | User avatar, name, join date, posts list, edit button |
| **Sorting**         | Shows only the newest posts | Displays posts in descending order (newest first) | Not applicable (displays a single post) | Shows the user's latest posts in descending order |
| **User Navigation** | Designed to attract attention | Designed to browse all content | Provides easy navigation back to the blog or home page | Allows user to manage their profile and view their posts |
| **Buttons/Actions** | None | None | **Edit, Delete, Like, Add Comment** | **Edit Profile** |
| **Additional Features** | Featured post images, categories | Search bar, category filters | Comments section, related posts suggestion | Edit profile button, profile picture, social media links |

## Page Details
### Home Page (`index.html`)
- Displays a **welcome message** and highlights the latest **4 blog posts**.
- Includes featured post images and categories.
- Focuses on attracting user attention.

![Image](static/images/README/index.png)


### Blog Page (`posts.html`)

- Lists **all blog posts** in **descending order** (newest first).
- Includes a **search bar** and **category filters** for easy navigation.

![Image](static/images/README/posts.png)

### Single Post Page (`post_detail.html`)
- Displays **full blog post content** along with the **title, category, and featured image**.
- Includes user interaction options:
  - **Edit Button** - Allows the author to modify the post.
  - **Delete Button** - Removes the post.
  - **Like Button** - Users can like the post. ![Image](static/images/README/Screenshot%202025-03-04%20093035.png)
  - **Add Comment Section** - Users can engage by adding comments.

![Image](static/images/README/post-detail.png)
![Image](static/images/README/post-detail1.png)

### Profile Page (`profile.html`)
- Displays **user profile information**, including:
  - **Profile picture**
  - **Username**
  - **Join date**
  - **List of user's latest posts**
- Includes an **"Edit Profile" button** for user customization.

![Image](static/images/README/profile3.png)


### Common Elements on All Pages
- **Navigation Bar**  
  The navigation bar provides easy and seamless access to different pages and stays fixed at the top of the page as you scroll.  
  The following links are included:
  - **Home** (Currently Active)
  - **Blog**
  - **New** (Create Post)
  - **Profile**
  - **Logout**
  - **Search Bar** (For quick search functionality)
      - User can search for posts by entering a keyword in the search bar. The search function looks for matches in the title, summary, content, and category of posts.

         - If a match is found, the relevant posts will be displayed.
         - If no keyword is entered, all posts will be shown.

![Image](static/images/README/Navbar.png)
- ## Responsive Navigation for Smaller Devices
  On tablets and smaller devices, the website uses a hamburger menu (☰) to improve navigation.

   - The menu is hidden by default and appears when the hamburger icon is clicked.
   - It includes links to Home, Blog, New, Register, and Login for easy access.
   - A search bar is placed below the menu, allowing users to quickly find content.

![Image](static/images/README/header.t.png)
![Image](static/images/README/header.m.png)

- **Sticky Footer**  
  The footer is fixed at the bottom of all pages and contains social media icons:
  - Facebook
  - GitHub
  - Instagram
  - YouTube

![Image](static/images/README/footer.png)

### Pallete

![Image](static/images/README/pallete.png)

# Responsiveness

## Desktop
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

![Image](static/images/README/singout.png)

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
### Desktop
![image](static/images/Desctop.png)
### Ipad
![image](static/images/Ipad1.png)
![image](static/images/Ipad%20.png)
### Mobile
![image](static/images/Mobile.png)
![image](static/images/Mobilephone.png)
## Blog Post
### Desktop
![image](static/images/Post%20detail.png)
Ipad and mobile layout similar to Home page.
## Profile
![Image](static/images/README/Profile.png)

# Future Adding

### Profile can be deleted by profile owner.
### Users can delete or update their comments.
### The number of likes is displayed next to the post.
### Social Sharing: Users will be able to share posts on social media platforms.
### Notifications: Users will receive notifications when their posts are commented on or liked.
### 500 error custom page

# Agile Methodology

This project was developed using the [Project Camban Board](https://github.com/users/Angela-Sin/projects/10/views/1), enabling an iterative and incremental approach to building my app while maintaining the flexibility to adapt the design throughout the development process.

To manage development effectively, I utilized GitHub Issues and Projects. The app's features were organized into Epics, which were further broken down into User Stories and Tasks. An Epic represents a significant piece of functionality, while User Stories define specific user needs. I used the Project feature’s board view as a Kanban board to track progress. User stories were initially placed in the To Do column for prioritization, then moved to In Progress once development began, and finally transitioned to Done upon successful implementation and fulfillment of acceptance criteria.
Also by creation a project milestones which You can find at [Project Milestones](#project-milestones)

![Image](static/images/README/agile.png)

![Image](static/images/README/agile1.png)

## **Testing**
- **Manual Testing:** Validated all user stories through structured tests.
- **Google Lighthouse Performance:** Performance scores captured for mobile and desktop.
- **Browser Compatibility:** Verified across Chrome, Firefox, Edge, Opera.
- **Code Validation:** W3C Code Validator and PEP8 formatting were used.  CI Python Linter, CSS Validation.

- **Bug** **ISSUE**

  For detailed testing results and see Bug/ISSUE, refer to the [Testing Documentation](TESTING.md).

# Technologies Used


| Source                                                                                                               | Location       | Notes                        |
| -------------------------------------------------------------------------------------------------------------------- | -------------- | ---------------------------- |
| [Git](https://git-scm.com) |Across website|used for version control.(`git add`, `git commit`, `git push`)
|[GitHub](https://github.com)|Across website|used for secure online code storage.
|[VSCode](https://code.visualstudio.com)|Across website|used as a local IDE for development.
|[Django](https://www.djangoproject.com/)|Across website|Used as a backend framework for building web applications.|
|[JavaScript](https://www.w3schools.com/js/)|Across Website|Used for client-side scripting and dynamic web development.|
|[HTML](https://en.wikipedia.org/wiki/HTML)|Across website|used for the main site content.
| [Readme](https://github.com/Angela-Sin/Green_Wisdom)                                                                   | Acros website  | Project Documentation |
|[CSS](https://en.wikipedia.org/wiki/CSS)|Across website|used for the main site design and layout.
| [YouTube](https://www.youtube.com/)                                                                                  | Across website  | Tutorial for troubleshouting |
| [Heroku](https://dashboard.heroku.com/apps)                                                                          | Acros website  | as the IDE for development.  |
|[Balsamiq](https://balsamiq.com/?gad_source=1&gclid=EAIaIQobChMIyraK9uzLiwMVIpdQBh306i98EAAYAiAAEgJ7JfD_BwE)| Across Website| Wireframes creation|
| [Fonts Google](https://fonts.google.com/)                                                                            | Across website | Font selection               |
| [W3Schools](https://www.w3schools.com/)                                                                              | Across website | Various help pages           |
| [Bootstrap](https://getbootstrap.com/)                                         | Across website | used as the front-end CSS framework for modern responsiveness and pre-built components.   |
| [Flaticon](https://www.flaticon.com/free-icons/free)|    Across Website |Social Media Icons |
| [icons8](https://icons8.com/icons/setfood) | Across website| Logo|
| [Stackoverflow](https://stackoverflow.com/questions/77012106/django-allauth-modulenotfounderror-no-module-named-allauth-account-middlewar) | Across website|Debbuging actions | |
| [ChatGPT](https://chatgpt.com/)   | Across website |Content writing, debugging actions |
|[Svgrepo](https://www.svgrepo.com/svg/43426/profile)|Across website|Profile Icon Svg|
|[pep8ci](https://pep8ci.herokuapp.com/)| Across website|Python Validation|
|[CSS-Valitador](#https://jigsaw.w3.org/css-validator/)| Across website|CSS Validation|
|[W3C](https://validator.w3.org/)| Across website|HTML Validation|
|[colors.co](https://coolors.co/image-picker)| Across website|Color palette selection.|
|[techsini](https://techsini.com/multi-mockup/)| Across website|Responsiveness tool|

# Libraries



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

## Forking the Repository

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
- Copy the **HTTPS** URL of the repository.
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

# Acknowledgements

- Special mention is also deserved by my mentor **Medale Oluwafemi** for helping me understand the requirements and guiding me through the realization of this project!
- My cohort facilitator, **Kay Welfare** for pointing out the important parts of fulfilling the project completion criteria I needed to focus on.
- **Vernell Clark** - past student from Code institute, He help me to fix the some of the repeating functions and syntaxes on the project by discussing them together.
- Mentor **Daisy Mc Girr's** tutorial on [YouTube](https://www.youtube.com/watch?v=sBjbty691eI&list=PLXuTq6OsqZjbCSfiLNb2f1FOs8viArjWy) helped me build my project.
- As a **Tutoring team** for help and support during the project.
- All **Slack** comunity members and espetially **Kasia Bogucka** who helped me to solve issue with VsCode migration.
- Code Institute's 'Django Blog' project.
- Stack Overflow.
- Slack **#peer-code-review** channel memebers for they opinion and suggestions
