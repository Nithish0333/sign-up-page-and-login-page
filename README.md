# Django Authentication Backend

A Django backend application for user authentication (login and signup) using MySQL database.

## Features

- User registration (signup) with email, fullname, and password
- User login with username/email and password
- Password validation (minimum 6 characters)
- Email uniqueness validation
- Session-based authentication
- Protected dashboard page
- Bootstrap-based UI

## Prerequisites

- Python 3.8 or higher
- MySQL Server installed and running
- pip (Python package manager)

## Installation Steps

### 1. Install Python Dependencies

```bash
pip install -r requirements.txt
```

**Note for Windows users:** If you encounter issues installing `mysqlclient`, you can use `pip install mysqlclient` or install MySQL Connector/Python instead:

```bash
pip install mysql-connector-python
```

Then update `settings.py` to use:
```python
'ENGINE': 'django.db.backends.mysql',
# ... rest of config
```

### 2. Create MySQL Database

Login to MySQL and create a database:

```sql
CREATE DATABASE auth_db CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci;
```

### 3. Configure Database Settings

Edit `auth_project/settings.py` and update the database configuration:

```python
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'auth_db',           # Your database name
        'USER': 'root',               # Your MySQL username
        'PASSWORD': '',               # Your MySQL password
        'HOST': 'localhost',          # Your MySQL host
        'PORT': '3306',               # Your MySQL port
        'OPTIONS': {
            'init_command': "SET sql_mode='STRICT_TRANS_TABLES'",
        },
    }
}
```

### 4. Run Migrations

Create the database tables:

```bash
python manage.py makemigrations
python manage.py migrate
```

### 5. Create Superuser (Optional)

Create an admin user to access Django admin panel:

```bash
python manage.py createsuperuser
```

### 6. Run the Development Server

```bash
python manage.py runserver
```

The application will be available at `http://127.0.0.1:8000/`

## URLs

- `/` or `/login/` - Login page
- `/signup/` - Signup page
- `/dashboard/` - Dashboard (requires login)
- `/logout/` - Logout
- `/admin/` - Django admin panel

## Project Structure

```
.
├── auth_project/          # Main project directory
│   ├── settings.py       # Django settings
│   ├── urls.py           # Main URL configuration
│   └── ...
├── authentication/       # Authentication app
│   ├── models.py        # Custom User model
│   ├── views.py         # Login/Signup views
│   ├── urls.py          # App URL configuration
│   └── ...
├── templates/            # HTML templates
│   ├── login.html
│   ├── signup.html
│   └── dashboard.html
├── manage.py
├── requirements.txt
└── README.md
```

## Usage

1. **Sign Up**: Visit `/signup/` and fill in the form with:
   - Full Name
   - Email (used as username)
   - Password (minimum 6 characters)
   - Confirm Password

2. **Login**: Visit `/login/` and enter your email and password.

3. **Dashboard**: After successful login, you'll be redirected to the dashboard.

4. **Logout**: Click the logout button to end your session.

## Custom User Model

The project uses a custom user model (`CustomUser`) that extends Django's `AbstractUser` with:
- `fullname` field
- `email` field (unique)

## Troubleshooting

### MySQL Connection Issues

If you get MySQL connection errors:
1. Ensure MySQL server is running
2. Verify database credentials in `settings.py`
3. Check if the database exists
4. For Windows, you might need to install MySQL Connector/Python instead of mysqlclient

### Migration Issues

If migrations fail:
```bash
python manage.py makemigrations authentication
python manage.py migrate
```

## Security Notes

- Change `SECRET_KEY` in `settings.py` for production
- Set `DEBUG = False` in production
- Use environment variables for sensitive data
- Implement proper password hashing (already handled by Django)
- Add HTTPS in production

## License

This project is open source and available for use.


