# Django Admin Panel Guide

## Access Admin Panel

1. Go to: **http://127.0.0.1:8000/admin/**
2. Login with:
   - **Username:** `admin`
   - **Password:** `admin123`

## User Management Features

### ✅ View All Users

- Click on **"Custom Users"** in the admin panel
- You'll see a list of all registered users with:
  - Username
  - Email
  - Full Name
  - Staff Status
  - Active Status
  - Date Joined
  - Last Login

### ✅ Search Users

- Use the **search box** at the top to search by:
  - Username
  - Email
  - Full Name
  - First Name
  - Last Name

### ✅ Filter Users

- Use the **filter sidebar** on the right to filter by:
  - Staff Status (is_staff)
  - Active Status (is_active)
  - Superuser Status
  - Date Joined

### ✅ Create New User

1. Click **"Add Custom User"** button (top right)
2. Fill in the form:
   - **Username** (required)
   - **Password** (required)
   - **Password confirmation** (required)
   - **Email** (required, must be unique)
   - **Full name** (optional)
   - **First name** (optional)
   - **Last name** (optional)
   - **Staff status** (checkbox - gives admin access)
   - **Active** (checkbox - user can login if checked)
   - **Superuser status** (checkbox - full admin access)
3. Click **"Save"**

### ✅ Edit User

1. Click on any **username** in the user list
2. Modify any fields:
   - Personal information (name, email)
   - Password (change password section)
   - Permissions (staff, active, superuser)
   - Groups and permissions
3. Click **"Save"** or **"Save and continue editing"**

### ✅ Delete User

**Single User:**
1. Click on the username you want to delete
2. Scroll to the bottom
3. Click **"Delete"** button
4. Confirm deletion

**Multiple Users:**
1. Check the boxes next to users you want to delete
2. Select **"Delete selected Custom Users"** from the action dropdown
3. Click **"Go"**
4. Confirm deletion

### ✅ Bulk Actions

- Select multiple users using checkboxes
- Choose an action from the dropdown:
  - **Mark selected users as active**
  - **Mark selected users as inactive**
  - **Delete selected Custom Users**

## User Fields Explained

- **Username:** Unique identifier for login
- **Email:** User's email address (must be unique)
- **Full Name:** Display name (custom field)
- **Staff Status:** Can access admin panel (if True)
- **Active:** User can login (if True)
- **Superuser:** Full admin privileges (if True)
- **Date Joined:** When account was created
- **Last Login:** Last successful login time

## Tips

1. **Always set a strong password** when creating users manually
2. **Use "Active" checkbox** to temporarily disable user access without deleting
3. **Staff status** allows users to access admin panel (but limited permissions)
4. **Superuser** has full access to everything
5. **Search and filters** help manage large user lists efficiently

## Security Notes

- Change the default admin password after first login
- Only grant staff/superuser status to trusted users
- Regularly review user accounts and remove inactive ones
- Use strong passwords for all admin accounts

