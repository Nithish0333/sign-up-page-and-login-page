"""
Quick setup script to help configure MySQL database.
Run this script to test your MySQL connection.
"""
import mysql.connector
from mysql.connector import Error

def test_mysql_connection():
    print("=" * 50)
    print("MySQL Database Connection Test")
    print("=" * 50)
    
    # Get database credentials
    db_name = input("Enter database name (or press Enter for 'auth_db'): ").strip() or 'auth_db'
    db_user = input("Enter MySQL username (or press Enter for 'root'): ").strip() or 'root'
    db_password = input("Enter MySQL password (or press Enter if no password): ").strip() or ''
    db_host = input("Enter MySQL host (or press Enter for 'localhost'): ").strip() or 'localhost'
    db_port = input("Enter MySQL port (or press Enter for '3306'): ").strip() or '3306'
    
    try:
        # Test connection
        print("\nTesting connection...")
        connection = mysql.connector.connect(
            host=db_host,
            port=int(db_port),
            user=db_user,
            password=db_password
        )
        
        if connection.is_connected():
            print("✓ Successfully connected to MySQL server!")
            
            # Check if database exists
            cursor = connection.cursor()
            cursor.execute("SHOW DATABASES")
            databases = [db[0] for db in cursor.fetchall()]
            
            if db_name in databases:
                print(f"✓ Database '{db_name}' already exists!")
            else:
                create = input(f"\nDatabase '{db_name}' doesn't exist. Create it? (y/n): ").strip().lower()
                if create == 'y':
                    cursor.execute(f"CREATE DATABASE {db_name} CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci")
                    print(f"✓ Database '{db_name}' created successfully!")
                else:
                    print("Database not created. Please create it manually.")
            
            cursor.close()
            connection.close()
            
            # Generate settings.py snippet
            print("\n" + "=" * 50)
            print("Add this to your auth_project/settings.py:")
            print("=" * 50)
            print(f"""
DATABASES = {{
    'default': {{
        'ENGINE': 'django.db.backends.mysql',
        'NAME': '{db_name}',
        'USER': '{db_user}',
        'PASSWORD': '{db_password}',
        'HOST': '{db_host}',
        'PORT': '{db_port}',
        'OPTIONS': {{
            'init_command': "SET sql_mode='STRICT_TRANS_TABLES'",
        }},
    }}
}}
""")
            
    except Error as e:
        print(f"\n✗ Error connecting to MySQL: {e}")
        print("\nTroubleshooting:")
        print("1. Make sure MySQL server is running")
        print("2. Check your username and password")
        print("3. Verify MySQL is accessible on the specified host/port")

if __name__ == "__main__":
    try:
        test_mysql_connection()
    except KeyboardInterrupt:
        print("\n\nSetup cancelled.")
    except Exception as e:
        print(f"\nError: {e}")

