# Testing Guide for Django Authentication Backend

## Prerequisites

Make sure your server is running:
```bash
python manage.py runserver
```

The server should be accessible at: **http://127.0.0.1:8000/**

---

## Test 1: User Signup (Registration)

### Steps:
1. Open your browser and go to: **http://127.0.0.1:8000/signup/**
2. Fill in the form:
   - **Full name:** John Doe
   - **Email:** john@example.com
   - **Password:** test1234
   - **Confirm Password:** test1234
3. Click **"Sign Up"** button

### Expected Result:
- ✅ Success message: "Account created successfully! Please login."
- ✅ Redirected to login page
- ✅ User account created in database

### Test Edge Cases:
- ❌ Try with password less than 6 characters (should show error)
- ❌ Try with mismatched passwords (should show error)
- ❌ Try with existing email (should show error)
- ❌ Try with empty fields (should show validation errors)

---

## Test 2: User Login

### Steps:
1. Go to: **http://127.0.0.1:8000/login/**
2. Enter credentials:
   - **Username/Email:** john@example.com (or the email you used in signup)
   - **Password:** test1234
3. Click **"Login"** button

### Expected Result:
- ✅ Success message: "Welcome back, [Full Name]!"
- ✅ Redirected to dashboard page
- ✅ User session created

### Test Edge Cases:
- ❌ Try with wrong password (should show error)
- ❌ Try with non-existent username (should show error)
- ❌ Try with empty fields (should show error)

---

## Test 3: Dashboard (Protected Route)

### Steps:
1. After successful login, you should be on: **http://127.0.0.1:8000/dashboard/**
2. Check the page displays:
   - Welcome message with your name
   - Username
   - Email
   - Full Name
   - Account creation date

### Expected Result:
- ✅ Dashboard page loads successfully
- ✅ Shows user information
- ✅ Logout button is visible

### Test Protection:
- ❌ Try accessing **http://127.0.0.1:8000/dashboard/** without logging in
- ✅ Should redirect to login page

---

## Test 4: Logout

### Steps:
1. From the dashboard, click **"Logout"** button
2. Or go to: **http://127.0.0.1:8000/logout/**

### Expected Result:
- ✅ Success message: "You have been logged out successfully."
- ✅ Redirected to login page
- ✅ Session ended

### Test After Logout:
- ❌ Try accessing dashboard again (should redirect to login)

---

## Test 5: Admin Panel

### Steps:
1. Go to: **http://127.0.0.1:8000/admin/**
2. Login with:
   - **Username:** admin
   - **Password:** admin123
3. Click on **"Custom Users"**

### Expected Result:
- ✅ Admin panel loads
- ✅ Can see list of all users (including the one you created)
- ✅ Can search, filter, and manage users

### Test Admin Features:
- ✅ **Create User:** Click "Add Custom User" and create a new user
- ✅ **Edit User:** Click on any username to edit details
- ✅ **Delete User:** Select users and delete them
- ✅ **Search:** Use search box to find users
- ✅ **Filter:** Use filters to narrow down user list

---

## Test 6: Database Verification

### Using Django Shell:
```bash
python manage.py shell
```

Then run:
```python
from django.contrib.auth import get_user_model
User = get_user_model()

# List all users
users = User.objects.all()
for user in users:
    print(f"Username: {user.username}, Email: {user.email}, Fullname: {user.fullname}")

# Count users
print(f"Total users: {User.objects.count()}")
```

### Using MySQL:
```bash
mysql -u root -p
```

Then:
```sql
USE login_db;
SELECT username, email, fullname, is_active, date_joined FROM authentication_customuser;
```

---

## Test 7: API Endpoints (Manual Testing)

### Test URLs:
1. **Home/Login:** http://127.0.0.1:8000/
2. **Login:** http://127.0.0.1:8000/login/
3. **Signup:** http://127.0.0.1:8000/signup/
4. **Dashboard:** http://127.0.0.1:8000/dashboard/
5. **Logout:** http://127.0.0.1:8000/logout/
6. **Admin:** http://127.0.0.1:8000/admin/

---

## Automated Testing Script

Run the automated test script:
```bash
python test_auth.py
```

This will test:
- User registration
- User login
- Protected routes
- User logout
- Database operations

---

## Common Issues & Solutions

### Issue: "No module named 'mysqlclient'"
**Solution:** Install mysqlclient or use mysql-connector-python

### Issue: "Can't connect to MySQL"
**Solution:** Check MySQL is running and credentials in settings.py

### Issue: "Template not found"
**Solution:** Ensure templates are in the `templates/` directory

### Issue: "CSRF verification failed"
**Solution:** Make sure `{% csrf_token %}` is in forms

### Issue: "Redirect loop"
**Solution:** Check LOGIN_URL and LOGIN_REDIRECT_URL in settings.py

---

## Performance Testing

### Test with Multiple Users:
1. Create 10-20 test users via signup
2. Test login/logout for each
3. Check admin panel performance with many users
4. Test search and filter with large dataset

---

## Security Testing

### Test Cases:
- ✅ Password is hashed (not stored in plain text)
- ✅ CSRF protection works
- ✅ Protected routes require authentication
- ✅ Session expires after logout
- ✅ SQL injection protection (Django ORM handles this)
- ✅ XSS protection (Django templates escape by default)

---

## Browser Testing

Test in different browsers:
- ✅ Chrome/Edge
- ✅ Firefox
- ✅ Safari (if on Mac)

Test responsive design:
- ✅ Desktop view
- ✅ Tablet view
- ✅ Mobile view

---

## Checklist

- [ ] User can signup successfully
- [ ] User can login with correct credentials
- [ ] User cannot login with wrong credentials
- [ ] Dashboard is protected (requires login)
- [ ] User can logout successfully
- [ ] Admin can view all users
- [ ] Admin can create users
- [ ] Admin can edit users
- [ ] Admin can delete users
- [ ] Search functionality works
- [ ] Filter functionality works
- [ ] Error messages display correctly
- [ ] Success messages display correctly
- [ ] Forms validate input correctly
- [ ] Database stores data correctly

