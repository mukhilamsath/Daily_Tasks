# HTTP Status Code Cheatsheet

HTTP status codes are three-digit numbers returned by a server to indicate the result of a client's HTTP request. They are divided into different categories:

* **1xx** → Informational
* **2xx** → Successful
* **3xx** → Redirection
* **4xx** → Client Error
* **5xx** → Server Error

## 1. 200 OK

**Meaning:**
The request was successfully processed by the server.

**When to use:**
A backend developer commonly uses `200 OK` when a request successfully retrieves or processes data.

**Example:**

```http
GET /users/1
→ 200 OK
```

---

## 2. 201 Created

**Meaning:**
The request was successful and a new resource was created.

**When to use:**
Usually used after successfully creating a new resource with a `POST` request.

**Example:**

```http
POST /users
→ 201 Created
```

---

## 3. 204 No Content

**Meaning:**
The request was successfully processed, but there is no content to return in the response body.

**When to use:**
Commonly used when an operation succeeds but the client does not need any response data.

**Example:**

```http
DELETE /users/10
→ 204 No Content
```

---

## 4. 400 Bad Request

**Meaning:**
The server cannot process the request because the request is invalid or malformed.

**When to use:**
Used when the client sends invalid data or an incorrectly formatted request.

**Example:**

```http
POST /users

Invalid request data
→ 400 Bad Request
```

**Easy way to remember:**

> The client sent something wrong.

---

## 5. 401 Unauthorized

**Meaning:**
The request requires authentication, or the authentication provided by the client is invalid.

**When to use:**
Used when a user needs to log in or provide valid authentication credentials.

**Example:**

```http
GET /profile

No valid authentication
→ 401 Unauthorized
```

**Easy way to remember:**

> "Who are you?"

---

## 6. 403 Forbidden

**Meaning:**
The server understood the request, but the client does not have permission to access the requested resource.

**When to use:**
Used when the user is authenticated but does not have sufficient permission.

**Example:**

```text
Normal user
    ↓
Tries to access admin page
    ↓
403 Forbidden
```

**Easy way to remember:**

> "I know who you are, but you are not allowed to do this."

### 401 vs 403

| Status  | Meaning                                                     |
| ------- | ----------------------------------------------------------- |
| **401** | Authentication is missing or invalid                        |
| **403** | Authentication may be valid, but permission is insufficient |

---

## 7. 404 Not Found

**Meaning:**
The requested resource could not be found on the server.

**When to use:**
Used when the requested endpoint or resource does not exist.

**Example:**

```http
GET /users/9999
→ 404 Not Found
```

if user `9999` does not exist.

**Easy way to remember:**

> "I can't find what you're asking for."

---

## 8. 409 Conflict

**Meaning:**
The request conflicts with the current state of the resource.

**When to use:**
Useful when the request conflicts with existing data.

**Example:**

Suppose a user tries to register an email that already exists:

```http
POST /users
→ 409 Conflict
```

**Easy way to remember:**

> The request conflicts with existing data.

---

## 9. 422 Unprocessable Content

**Meaning:**
The server understands the request, but the submitted data does not satisfy the required validation rules.

**When to use:**
Commonly used by FastAPI when the request body does not satisfy a Pydantic model's validation requirements.

**Example:**

Suppose the API expects:

```python
class User(BaseModel):
    name: str
    age: int
```

but receives invalid data:

```json
{
    "name": "Mukhil",
    "age": "hello"
}
```

The request can result in:

```http
422 Unprocessable Content
```

**Easy way to remember:**

> The request reached the API, but the data failed validation.

---

## 10. 500 Internal Server Error

**Meaning:**
An unexpected error occurred on the server while processing the request.

**When to use:**
Used when a server-side problem prevents the request from being completed successfully.

For example:

```text
Client
   ↓
FastAPI
   ↓
Database error
   ↓
500 Internal Server Error
```

**Easy way to remember:**

> Something went wrong on the server.

---

# Quick Reference Table

| Status Code | Meaning               | Typical Backend Use                        |
| ----------- | --------------------- | ------------------------------------------ |
| **200**     | OK                    | Successful request                         |
| **201**     | Created               | Resource successfully created              |
| **204**     | No Content            | Successful operation with no response body |
| **400**     | Bad Request           | Invalid or malformed request               |
| **401**     | Unauthorized          | Authentication missing or invalid          |
| **403**     | Forbidden             | Insufficient permission                    |
| **404**     | Not Found             | Resource or endpoint doesn't exist         |
| **409**     | Conflict              | Conflict with existing resource/data       |
| **422**     | Unprocessable Content | Request data failed validation             |
| **500**     | Internal Server Error | Unexpected server-side error               |

# Easy Memory Trick

```text
200 → Success
201 → Created
204 → Success, no content

400 → Bad request
401 → Authentication problem
403 → Permission problem
404 → Not found
409 → Conflict
422 → Validation problem

500 → Server problem
```

## Important Backend Developer Rule

A backend developer should not simply return `200` for every situation.

The status code should communicate the actual result of the request to the client.

For example:

```text
Successfully retrieved data
        ↓
      200

Successfully created data
        ↓
      201

Resource doesn't exist
        ↓
      404

Authentication failed
        ↓
      401

Unexpected server failure
        ↓
      500
```

Using appropriate status codes makes an API easier for frontend developers, clients, and other services to understand and work with.
