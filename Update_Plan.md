# 📄 Resume-Ex API Update Development Plan

This document outlines the 10-step plan for upgrading the Resume-Ex project into a fully functional, secure, and lightweight resume analysis API using Python, Flask, and a small local language model.

---

## 1. Project Structure Setup

**Goal:** Prepare a modular Flask project environment.

**Substeps:**

* Create a virtual environment: `python -m venv venv`
* Install dependencies: `pip install Flask python-docx PyMuPDF`
* Directory layout:

  ```
  /app
    /routes
    /services
    /utils
    /models
  main.py
  requirements.txt
  .env
  ```

---

## 2. Flask API Boilerplate

**Goal:** Implement the main API route for file upload.

**Substeps:**

* Define a `/upload` POST route
* Accept `multipart/form-data`
* Save the file temporarily
* Return a dummy JSON response for now

---

## 3. File Parsing Logic

**Goal:** Extract resume text from PDF or DOCX.

**Substeps:**

* Use `fitz` for PDFs
* Use `python-docx` for Word documents
* Auto-detect file extension and use the appropriate parser
* Return cleaned text

---

## 4. Integrate Lightweight NLP Model

**Goal:** Process extracted text using a local model.

**Substeps:**

* Load a model from LM Studio, GPT4All, or Ollama
* Create a prompt template: "Extract Name, Email, Skills..."
* Parse model output into structured JSON

---

## 5. Implement Authentication

**Goal:** Allow only authorized users to access the API.

**Substeps:**

* Token-based authentication
* Store users and tokens in SQLite or JSON
* Middleware for token verification
* Return 401 Unauthorized for invalid tokens

---

## 6. Add Security & Rate Limiting

**Goal:** Ensure API reliability and safety.

**Substeps:**

* Use Flask-Limiter for rate control
* Enforce file size limits
* Validate file MIME types
* Sanitize filenames

---

## 7. Return Structured JSON

**Goal:** Deliver a clean, parseable JSON result.

**Sample format:**

```json
{
  "name": "John Doe",
  "email": "john@example.com",
  "skills": ["Python", "Flask"],
  "experience": [
    {"company": "ACME Corp", "role": "Developer", "years": 2}
  ]
}
```

---

## 8. Optional: Admin Dashboard

**Goal:** Monitor API usage and users.

**Substeps:**

* Flask + Jinja2 interface
* Admin login route
* View logs and registered users
* Manually issue API keys

---

## 9. Developer Documentation

**Goal:** Help developers consume the API.

**Substeps:**

* Write a `README.md` or full developer doc
* Include:

  * Overview
  * Authentication
  * Endpoints
  * Example requests (curl/Postman)
* Optional: Swagger UI or OpenAPI schema

---

## 10. Deployment & Monitoring

**Goal:** Make the API publicly accessible.

**Substeps:**

* Deploy to Railway, Render, or Heroku
* Add logging (e.g., to a file or log aggregator)
* Optionally: containerize with Docker
* Use Uptime Robot or Prometheus for uptime checks

---

## ✅ Notes

* Focus first on core functionality: upload → parse → model → JSON
* Keep model local and offline-friendly for now
* Use `.env` to keep tokens and config private
* Consider versioning your API (`/v1/upload`)

---

## 📌 Next Steps

* Finalize model choice for local inference
* Implement initial PDF parsing logic
* Create `/upload` endpoint
* Setup token authentication
