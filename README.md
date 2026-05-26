# Landing CMS (Minimal)

Minimal landing page with a tiny CMS. Backend: FastAPI (Python). Frontend: static HTML pages.

## Run (local)
1. Install Python 3.11+
2. From repo root:
   - Start backend:
     ```
     cd backend
     pip install fastapi uvicorn pydantic
     python -m uvicorn app:app --reload --port 8000
     ```
   - Open frontend files in a browser:
     - `frontend/index.html` (landing)
     - `frontend/admin.html` (admin)

API base: http://localhost:8000/api

## Notes
- Storage: `backend/data.json` (simple JSON). Replace with PostgreSQL/SQLAlchemy when ready.
- Contact send is mocked; integrate SMTP or provider in `app.py`.
- To dockerize later, add simple Dockerfiles.

## License
MIT
