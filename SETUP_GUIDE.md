# MySQL Database Setup Guide

## Step 1: Update Database Configuration

Edit `auth_project/settings.py` and update the `DATABASES` section with your MySQL credentials:

```python
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'login_db',      # Change this to your database name
        'USER': 'root',      # Usually 'root'
        'PASSWORD': '',  # Your MySQL password (leave empty '' if no password)
        'HOST': 'localhost',
        'PORT': '3306',
        'OPTIONS': {
            'init_command': "SET sql_mode='STRICT_TRANS_TABLES'",
        },
    }
}
```

## Step 2: Create Database (if not exists)

Login to MySQL and create the database:

```bash
mysql -u root -p
```

Then run:
```sql
CREATE DATABASE your_database_name CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci;
EXIT;
```

## Step 3: Install MySQL Client

For Windows, install one of these:

**Option 1: mysqlclient (Recommended)**
```bash
pip install mysqlclient
```

**Option 2: mysql-connector-python (If mysqlclient fails)**
```bash
pip install mysql-connector-python
```

If using Option 2, update `settings.py`:
```python
'ENGINE': 'django.db.backends.mysql',
```

## Step 4: Run Migrations

```bash
python manage.py makemigrations
python manage.py migrate
```

## Step 5: Create Superuser (Optional)

```bash
python manage.py createsuperuser
```

## Step 6: Run Server

```bash
python manage.py runserver
```

Visit: http://127.0.0.1:8000/

