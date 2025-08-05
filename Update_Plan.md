# 📄 Resume-Ex API Update Development Plan

This document outlines the 10-step plan for upgrading the Resume-Ex project into a fully functional, secure, and lightweight resume analysis API using Python, Flask, and a small local language model.

---

## 1. Project Structure Setup - DONE
 
**Goal:** Prepare a modular Flask project environment.

**Substeps:**

- [x] Create a virtual environment: `python -m venv venv`
- [x] Install dependencies: `pip install Flask python-docx PyMuPDF`
- [x] Directory layout:

  ```
  /app
    /model
    /prompts
    /routes
    /services
    /template
    /utils
  /extensions
  /instance
  main.py
  requirements.txt
  .env
  ```

---

## 2. Flask API Boilerplate - DONE

**Goal:** Implement the main API route for file upload.

**Substeps:**

- [x] Define a `/upload` POST route
- [x] Accept `multipart/form-data`
- [x] Save the file temporarily
- [x] Return a dummy JSON response for now

---

## 3. File Parsing Logic - DONE

**Goal:** Extract resume text from PDF or DOCX.

**Substeps:**

- [x] Use `fitz` for PDFs
- [x] Use `python-docx` for Word documents
- [x] Auto-detect file extension and use the appropriate parser
- [x] Return cleaned text

---

## 4. Integrate Lightweight NLP Model - DONE

**Goal:** Process extracted text using a local model.

**Substeps:**

- [x] Load a model from LM Studio, GPT4All, or Ollama
- [x] Create a prompt template: "Extract Name, Email, Skills..."
- [x] Parse model output into structured JSON

---

## 5. Implement Authentication - DONE

**Goal:** Allow only authorized users to access the API.

**Substeps:**

- [x] Token-based authentication
- [x] Store users and tokens in SQLite or JSON
- [x] Middleware for token verification
- [x] Return 401 Unauthorized for invalid tokens

---

## 6. Add Security & Rate Limiting - DONE

**Goal:** Ensure API reliability and safety.

**Substeps:**

- [X] Use Flask-Limiter for rate control
- [X] Enforce file size limits
- [x] Validate file MIME types
- [x] Sanitize filenames

---

## 7. Return Structured JSON - DONE

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

- [ ] Flask + Jinja2 interface
- [ ] Admin login route
- [ ] View logs and registered users
- [ ] Manually issue API keys

---

## 9. Developer Documentation

**Goal:** Help developers consume the API.

**Substeps:**

* Write a `README.md` or full developer doc
* Include:

- [X] Overview
- [X] Authentication
- [X] Endpoints
- [ ] Example requests (curl/Postman)

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
