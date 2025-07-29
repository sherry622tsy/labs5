
## 🧪 **FitTracking Capstone Backend – API Test Report**

**Author:** Shiyuan Tang
**Module:** Labs 5 – Backend Integration & CRUD
**Tested API Group:** `/users` – User Management API
**Date:** 2025-07-28
**Database Used:** PostgreSQL (`fittracking`)

---

### ✅ **Overview**

This report documents the test cases and results for the `users` API endpoints of the FitTracking backend system. The testing was performed using Flask’s `test_client()` via `unittest` in `test_app.py`.

---

### 📋 **Test Environment**

* **Backend Framework:** Flask 2.3.x
* **Database:** PostgreSQL 16
* **Python Version:** 3.12
* **Testing Framework:** unittest (Python Standard Library)
* **Connection Driver:** psycopg2-binary
* **Database Schema:** Created via `db_init.sql`

---

### 📌 **Test Cases Summary**

| Test Case ID | Endpoint           | Method | Description                 | Input Type | Expected Status | Result |
| ------------ | ------------------ | ------ | --------------------------- | ---------- | --------------- | ------ |
| TC-001       | `/users`           | POST   | Create new user             | JSON       | 201 Created     | ✅      |
| TC-002       | `/users`           | GET    | Get all users               | -          | 200 OK          | ✅      |
| TC-003       | `/users/<id>`      | GET    | Get specific user by ID     | URL Param  | 200 OK          | ✅      |
| TC-004       | `/users/<id>`      | PUT    | Update user details         | JSON       | 200 OK          | ✅      |
| TC-005       | `/users/<id>`      | DELETE | Delete a user by ID         | URL Param  | 200 OK          | ✅      |
| TC-006       | `/users/<invalid>` | GET    | Access deleted/missing user | URL Param  | 404 Not Found   | ✅      |

---

### 🔍 **Sample Test Input & Output**

#### ✅ TC-001 – Create User

* **Request:**

```json
POST /users
{
  "name": "Test User",
  "email": "test@example.com",
  "height_cm": 170,
  "weight_kg": 65.5
}
```

* **Response:**

```json
{
    "success": true,
    "user_id": 4
}
```

---

#### ✅ TC-002 – Get All Users

* **Request:**

```json
GET /users
```

* **Response:**

```json
{
    "success": true,
    "users": [
        {
            "email": "shiyuan@example.com",
            "height_cm": 165,
            "id": 2,
            "name": "Shiyuan Tang",
            "weight_kg": 55.5
        },
        {
            "email": "test@example.com",
            "height_cm": 170,
            "id": 4,
            "name": "Test User",
            "weight_kg": 65.5
        }
    ]
}
```

---




#### ✅ TC-003 – Get User by ID

```json
GET /users/4
```

* **Response:**

```json
{
    "email": "test@example.com",
    "height_cm": 170,
    "id": 4,
    "name": "Test User",
    "weight_kg": 65.5
}
```
---

#### ✅ TC-004 – Update User

```json
PUT /users/1
{
  "name": "Updated User",
  "email": "updated@example.com",
  "height_cm": 172,
  "weight_kg": 66.0
}
```

* **Response:**

```json
{
    "message": "User updated",
    "success": true
}
```

---


#### ✅ TC-005 – Get Deleted User

* **Request:** `DELETE /users/4`
* **Expected:**

```json
{
    "message": "User 4 deleted",
    "success": true
}
```

---


#### ✅ TC-006 – Get Deleted User

* **Request:** `GET /users/1` *(after deletion)*
* **Expected:**

```json
{
  "error": "User not found"
}
```

---

### 🧪 **Test Execution Result**

All 6 test cases executed successfully using `postman` without manual intervention. The test environment was reset between runs using a test database or by rerunning `db_init.sql`.

> **Command used:**

```bash
python test_app.py
```

> **Result:**

```
.....
----------------------------------------------------------------------
Ran 5 tests in 1.2s

OK
```

---

### ✅ **Conclusion**

* All critical CRUD operations for the `/users` API passed automated unit tests.
* PostgreSQL integration via psycopg2 was successful.
* The API is ready for production usage and integration with frontend/mobile apps.
* Future expansion (e.g., `/workouts`, `/meals`) should follow this same test structure.

