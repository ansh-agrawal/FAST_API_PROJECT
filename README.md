# Simple FastAPI Application

This is a minimal FastAPI app with four endpoints:

- `GET /` → welcome message
- `GET /health` → health status
- `GET /items` → list all created in-memory items
- `POST /items` → create an item with request validation

## Setup

1. Create and activate a virtual environment (recommended):

   ```powershell
   python -m venv .venv
   .\.venv\Scripts\Activate.ps1
   ```

2. Install dependencies:

   ```powershell
   pip install -r requirements.txt
   ```

3. Run the server:

   ```powershell
   uvicorn main:app --reload
   ```

4. Open in browser:

- App: <http://127.0.0.1:8000>
- Swagger UI: <http://127.0.0.1:8000/docs>
- ReDoc: <http://127.0.0.1:8000/redoc>

## Quick test for POST endpoint

```powershell
Invoke-RestMethod -Uri http://127.0.0.1:8000/items -Method Post -ContentType "application/json" -Body '{"name":"Notebook","price":199.99}'
```

## Quick test for GET items

```powershell
Invoke-RestMethod -Uri http://127.0.0.1:8000/items -Method Get
```
