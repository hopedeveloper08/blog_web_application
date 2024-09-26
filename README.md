# Django Blog Project

Welcome to my Django Blog project! This project is aimed at improving my Django skills by implementing various features commonly used in modern web applications. It is a full-stack blog application built with Django, including features such as post creation, tags, comments, pagination, and more.

## Features

Here is a list of features that have been added to the project through different commits:

- **Post Model**: A base model to represent blog posts.
- **Admin Panel**: Django Admin configuration for managing posts.
- **Model Manager for Published Posts**: To filter and manage published posts.
- **URLs for Post Views**: Basic URL routing for displaying blog posts.
- **Post Views (CBV)**: Class-based views for listing and viewing posts.
- **Base Template**: A foundational HTML template for reusing across pages.
- **Post List and Post Detail Templates**: Custom HTML pages for displaying post lists and details.
- **Pagination**: Added pagination for the post list.
- **Email Sharing**: Users can share blog posts via email.
- **Comments**: A commenting system for blog posts.
- **Tags**: Blog posts can be tagged for better categorization.
- **Similar Posts**: Display similar posts based on tags.
- **Custom Sidebar Tag**: Added a customizable sidebar for the frontend.
- **Markdown Support**: Blog posts can now support Markdown formatting.
- **Sitemap**: A sitemap has been added to help search engines index the site.

## Installation

Follow the steps below to install and run the project locally:

1. **Clone the repository:**

    ```bash
    git clone https://github.com/your-username/django-blog-project.git
    ```

2. **Navigate to the project directory:**

    ```bash
    cd django-blog-project
    ```

3. **Create a virtual environment:**

    ```bash
    python -m venv env
    ```

4. **Activate the virtual environment:**

    - On macOS/Linux:

        ```bash
        source env/bin/activate
        ```

    - On Windows:

        ```bash
        .\env\Scripts\activate
        ```

5. **Install the required dependencies:**

    ```bash
    pip install -r requirements.txt
    ```

6. **Set up the PostgreSQL database:**

    Ensure you have PostgreSQL installed and create a new database.

    Then update the `DATABASES` settings in your `settings.py` file with your PostgreSQL configuration:

    ```python
    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.postgresql',
            'NAME': 'your-database-name',
            'USER': 'your-database-user',
            'PASSWORD': 'your-database-password',
            'HOST': 'localhost',
            'PORT': '5432',
        }
    }
    ```

7. **Run the database migrations:**

    ```bash
    python manage.py migrate
    ```

8. **Create a superuser for accessing the Django admin:**

    ```bash
    python manage.py createsuperuser
    ```

9. **Run the development server:**

    ```bash
    python manage.py runserver
    ```

    The project will be available at `http://127.0.0.1:8000/`.

## How to Use

- You can access the admin panel at `/admin/` and manage the posts.
- Blog posts can be created, edited, and published through the admin interface.
- Users can view the list of posts, see post details, add comments, and share posts via email.
- Posts can be tagged and similar posts will be displayed based on the tags.
- You can explore the site with pagination and different views.

## Technologies Used

- **Django**: The main web framework used to build the application.
- **PostgreSQL**: The database for storing blog data.
- **HTML/Bootstrap**: For the frontend of the application.
- **Sitemap**: For improving the SEO of the site.

## Future Improvements

- **Search Functionality**: Adding search functionality to search for posts by keywords.
- **User Authentication**: Allow users to sign up and log in to manage their own posts and comments.
- **Rich Editor**: Implementing a rich text editor for creating and editing posts.
