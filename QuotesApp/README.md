# Quotes App

A full-stack web application for users to create, share, and rate quotes. The application allows users to log in using Google OAuth, create quotes, search and filter quotes, rate quotes from 1 to 5 stars, and save their favorite quotes. Additionally, users can choose to post quotes anonymously or publicly and can manage their own content.

## Table of Contents
- [Features](#features)
- [Technologies Used](#technologies-used)
- [Project Structure](#project-structure)
- [Getting Started](#getting-started)
- [Environment Variables](#environment-variables)
- [Running the Application](#running-the-application)
- [Deployment](#deployment)
- [API Endpoints](#api-endpoints)
- [Screenshots](#screenshots)
- [Contributing](#contributing)
- [License](#license)

---

## Features
- **User Authentication** using Google OAuth 2.0.
- **Create, view, and delete quotes**.
- **Rate quotes** from 1 to 5 stars.
- **Sort and filter quotes** by different criteria (highest rated, newest, rising, controversial).
- **Save quotes** to the user's profile for future reference.
- Users can choose to post quotes **publicly, anonymously, or privately**.
- **Admin dashboard** to review flagged content.
- **Responsive design** for mobile and desktop.

---

## Technologies Used
### Backend
- Python
- Flask
- Flask-SQLAlchemy
- Flask-Login
- Flask-OAuthlib
- Flask-Mail
- MySQL (Google Cloud SQL)
- Google Cloud Services (App Engine, Cloud SQL)

### Frontend
- React
- Axios
- React Router DOM
- React Google Login

---

## Project Structure
   ```css
quotes-app/
├── backend/
│   ├── app.py
│   ├── config.py
│   ├── models.py
│   ├── routes/
│   │   ├── auth.py
│   │   ├── quotes.py
│   │   ├── users.py
│   │   ├── ratings.py
│   │   └── admin.py
│   ├── utils/
│   │   ├── oauth.py
│   │   └── email.py
│   ├── templates/
│   ├── requirements.txt
│   └── .env
├── frontend/
│   ├── public/
│   │   ├── index.html
│   │   ├── manifest.json
│   │   └── icons/
│   ├── src/
│   │   ├── components/
│   │   ├── pages/
│   │   ├── styles.css
│   │   ├── App.js
│   │   ├── index.js
│   └── package.json
└── README.md
```

## Getting Started

### Prerequisites
- **Python** 3.8+
- **Node.js** and npm
- **MySQL**
- **Google Cloud account** (for deployment)

---

### Backend Setup

1. **Clone the repository:**
   ```bash
   git clone https://github.com/yourusername/quotes-app.git
   cd quotes-app/backend
   
2. **Create a virtual environment:**

   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows use `venv\Scripts\activate`
   
3. **Install dependencies:**
   ```bash
   pip install -r requirements.txt
   
4. **Set up the MySQL database:**

   - Create a MySQL database named quotes_db.
   - Update the .env file with your database credentials.
5. **Initialize the database:**

   ```bash
   flask db init
   flask db migrate
   flask db upgrade

### Frontend Setup
1. **Navigate to the frontend directory:**

   ```bash
   cd ../frontend
   
2. **Install dependencies:**

   ```bash
   npm install
   
3. **Create a .env file with the following content:**

   ```makefile
   REACT_APP_GOOGLE_CLIENT_ID=your_google_client_id
   
## Environment Variables

Create a .env file in the backend/ directory with the following content:

   ```makefile
   SECRET_KEY=your_secret_key
   DATABASE_URL=mysql+mysqlconnector://root:password@localhost/quotes_db
   GOOGLE_CLIENT_ID=your_google_client_id
   GOOGLE_CLIENT_SECRET=your_google_client_secret
   MAIL_USERNAME=your_email@gmail.com
   MAIL_PASSWORD=your_email_password
   FRONTEND_URL=http://localhost:3000
   RECAPTCHA_SITE_KEY=your_recaptcha_site_key
   RECAPTCHA_SECRET_KEY=your_recaptcha_secret_key
```

## Running the Application
### Backend
   ```bash
   cd backend
   flask run
```
### Frontend
   ```bash
   cd frontend
   npm start
```
## Deployment
### Deploying the Backend on Google App Engine
1. **Deploy the Flask backend:**
   ```bash
   gcloud app deploy

2.**Deploy the MySQL database on Google Cloud SQL.**
### Deploying the Frontend on Firebase
   ```bash
   cd frontend
   npm run build
   firebase deploy
```
## API Endpoints
### Authentication
   - POST /auth/login - User login with Google OAuth.
   - POST /auth/logout - User logout.
### Quotes
   - GET /api/quotes - Fetch all public quotes.
   - POST /api/quotes - Create a new quote (requires authentication).
   - DELETE /api/quotes/<id> - Delete a user's quote.
### Ratings
   - POST /api/ratings/rate/<quote_id> - Rate a quote.
   - GET /api/ratings/<quote_id> - Get all ratings for a quote.
### Users
   - GET /api/users/profile - Get user profile info.
   - GET /api/users/my-quotes - Get user's own quotes.
   - GET /api/users/saved - Get user's saved quotes.
### Admin
   - GET /api/admin/flagged - Get all flagged quotes (admin only).
   - DELETE /api/admin/delete_quote/<quote_id> - Delete a flagged quote (admin only).
## Screenshots
### Home Page

### Create Quote

### Profile Page

## Contributing
1. **Fork the repository.**
2. **Create a new branch** (git checkout -b feature-branch).
3. **Commit your changes** (git commit -m "Add new feature").
4. **Push to the branch** (git push origin feature-branch).
5. **Open a pull request.**

## License
This project is licensed under the MIT License.

## Acknowledgments
Google Cloud Platform
React and Flask communities
