# Social Media API

This project is a Social Media API built using Django and Django REST Framework. It provides user authentication, including registration and login functionality, with a custom user model.

---

## Setup Process

Follow these steps to set up and run the project locally:

### Prerequisites
- Python 3.8 or later
- Pip (Python package manager)
- Virtual environment tool (optional but recommended)

### Installation Steps

1. **Clone the Repository:**
   ```bash
   git clone https://github.com/your-username/Alx_DjangoLearnLab.git
   cd Alx_DjangoLearnLab/social_media_api


Register a User
URL: /accounts/register/
Method: POST
Request Body:
{
    "username": "testuser",
    "password": "password123",
    "email": "test@example.com",
    "bio": "Hello, world!"
}

Response:
{
    "id": 1,
    "username": "testuser",
    "email": "test@example.com",
    "bio": "Hello, world!",
    "profile_picture": null
}

Login a User
URL: /accounts/login/

Method: POST

Request Body:
{
    "username": "testuser",
    "password": "password123"
}

Response:
{
    "token": "abc123def456gh789ijk"
}


Usage: Include the token in the Authorization header for authenticated requests:
Authorization: Token abc123def456gh789ijk


Overview of the User Model
The user model is a custom implementation of Django’s AbstractUser and includes additional fields:

Username: Unique identifier for the user.
Password: Secured using Django’s built-in hashing mechanism.
Email: User's email address.
Bio: A short description or biography of the user.
Profile Picture: Optional image upload for the user's profile picture.
Followers: A many-to-many relationship allowing users to follow others.
This model is extensible and suitable for building a robust social media platform.

Author
Created by Your Name.

---

### Instructions:
1. Save this content as `README.md` in the root directory of your project.
2. Replace the placeholders:
   - `your-username` with your GitHub username.
   - `[Your Name]` with your actual name.
3. Modify or expand on sections if needed to match your specific project setup.




Posts

GET /api/posts/: List all posts (paginated).
POST /api/posts/: Create a new post.
Request Body:
json

{
    "title": "Sample Post",
    "content": "This is a sample post."
}
GET /api/posts/{id}/: Retrieve a specific post.
PUT /api/posts/{id}/: Update a post (only the author can update).
DELETE /api/posts/{id}/: Delete a post (only the author can delete).
Comments

GET /api/comments/: List all comments.
POST /api/comments/: Create a new comment.
Request Body:
json

{
    "post": 1,
    "content": "This is a sample comment."
}
GET /api/comments/{id}/: Retrieve a specific comment.
PUT /api/comments/{id}/: Update a comment (only the author can update).
DELETE /api/comments/{id}/: Delete a comment (only the author can delete).



Follow/Unfollow
POST /accounts/follow/<user_id>/: Follow a user.
POST /accounts/unfollow/<user_id>/: Unfollow a user.
Feed
GET /posts/feed/: Retrieve an aggregated feed of posts from followed users.



# Test Likes and Notifications Features
Like a post:

Request: POST /posts/<int:pk>/like/
Response: {"detail": "Post liked successfully!"}
Unlike a post:

Request: POST /posts/<int:pk>/unlike/
Response: {"detail": "Post unliked successfully!"}
View unread notifications:

Request: GET /notifications/
Response: List of unread notifications.



# Deployment Guide
This section outlines how to deploy the social_media_api Django REST API to a production environment.

Step 1: Prepare for Deployment
Update settings.py for Production:

Set DEBUG to False:
python
Copy code
DEBUG = False
Configure ALLOWED_HOSTS: Add the domain or IP address of your hosting service:
python
Copy code
ALLOWED_HOSTS = ['your-domain.com', 'your-server-ip']
Security Settings: Enable production-level security:
python
Copy code
SECURE_BROWSER_XSS_FILTER = True
SECURE_CONTENT_TYPE_NOSNIFF = True
SECURE_SSL_REDIRECT = True
X_FRAME_OPTIONS = 'DENY'
Add an environment variable for the secret key:
python
Copy code
SECRET_KEY = os.environ.get('DJANGO_SECRET_KEY', 'your-secret-key')
Install Required Packages: Install the necessary libraries for production:

bash
Copy code
pip install gunicorn psycopg2-binary whitenoise
Static Files Configuration: Add Whitenoise to serve static files:

python
Copy code
MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'whitenoise.middleware.WhiteNoiseMiddleware',
    # other middleware
]

STATIC_ROOT = BASE_DIR / 'staticfiles'
STATICFILES_STORAGE = 'whitenoise.storage.CompressedManifestStaticFilesStorage'
Step 2: Choose a Hosting Service
Recommended Hosting Options:
Heroku: Easiest for beginners. Free tier available.
AWS Elastic Beanstalk: Scalable and flexible.
DigitalOcean: Offers VPS for direct control over deployment.
Render: Simple hosting solution with free plans.
Step 3: Deployment with Heroku (Example)
Install the Heroku CLI: Follow the Heroku CLI Installation Guide.

Create a Heroku App:

bash
Copy code
heroku create your-app-name
Configure Heroku for Django:

Add a Procfile to the project root:
makefile
Copy code
web: gunicorn social_media_api.wsgi
Push Your Code to Heroku:

bash
Copy code
git add .
git commit -m "Prepare for deployment"
git push heroku main
Set Environment Variables:

bash
Copy code
heroku config:set DJANGO_SECRET_KEY=your-secret-key
heroku config:set ALLOWED_HOSTS=your-app-name.herokuapp.com
Migrate the Database:

bash
Copy code
heroku run python manage.py migrate
Step 4: Test the Live Application
Visit the live application URL provided by the hosting service (e.g., https://your-app-name.herokuapp.com).
Use Postman or a web browser to interact with the API endpoints.
Step 5: Ongoing Monitoring and Maintenance
Enable Logging: Use services like Sentry for error tracking or monitor logs in the hosting provider's dashboard.

Regular Updates: Keep dependencies updated by running:

bash
Copy code
pip install --upgrade -r requirements.txt
Database Backups: Use managed services like Heroku Postgres or AWS RDS for automated backups.

Live Application URL
Once deployed, access the live API at:
https://your-app-name.herokuapp.com

