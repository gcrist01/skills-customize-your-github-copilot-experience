# 📘 Assignment: Building REST APIs with FastAPI

## 🎯 Objective

Learn how to build and test RESTful APIs using the FastAPI framework in Python. You will create endpoints, handle requests, and return JSON responses.

## 📝 Tasks

### 🛠️ API Setup

#### Description
Set up a FastAPI project and create a basic API endpoint that returns a welcome message.

#### Requirements
Completed program should:
- Install and import FastAPI
- Create an app instance
- Add a root endpoint (`/`) that returns a JSON welcome message

### 🛠️ CRUD Endpoints

#### Description
Implement CRUD (Create, Read, Update, Delete) endpoints for a simple resource, such as a list of books or users.

#### Requirements
Completed program should:
- Define a data model using Pydantic
- Implement endpoints for:
  - Creating a new resource (POST)
  - Reading all resources (GET)
  - Reading a single resource by ID (GET)
  - Updating a resource by ID (PUT)
  - Deleting a resource by ID (DELETE)
- Return appropriate JSON responses and status codes

#### Example
```python
# Example GET response
{
  "id": 1,
  "title": "FastAPI for Beginners",
  "author": "Jane Doe"
}
```

### 🛠️ API Testing

#### Description
Write tests for your API endpoints using pytest and httpx.

#### Requirements
Completed program should:
- Include test cases for each endpoint
- Use httpx to make requests to the FastAPI app
- Assert correct status codes and response data
