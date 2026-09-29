# Aether Tester

A small FastAPI application with a greeting endpoint and a health check.

## Requirements

- Python 3
- `pip`

## Installation

1. Clone the repository and enter it:

   ```bash
   git clone <repository-url>
   cd <repository-directory>
   ```

2. Create and activate a virtual environment:

   ```bash
   python -m venv .venv
   source .venv/bin/activate
   ```

   On Windows PowerShell, activate it with:

   ```powershell
   .venv\Scripts\Activate.ps1
   ```

3. Install the dependencies:

   ```bash
   python -m pip install -r requirements.txt
   ```

## Run the API

Start the development server from the repository root:

```bash
uvicorn app.main:app --reload
```

The API is then available at `http://127.0.0.1:8000`. FastAPI's interactive
documentation is available at `http://127.0.0.1:8000/docs`.

## API reference

All endpoints return JSON.

### `GET /`

Returns the application's greeting.

**Response — `200 OK`**

```json
{
  "message": "Hello from Aether tester"
}
```

Example:

```bash
curl http://127.0.0.1:8000/
```

### `GET /health`

Returns the application's health status. This endpoint can be used by local
development tooling or service monitors to confirm that the API is responding.

**Response — `200 OK`**

```json
{
  "status": "ok"
}
```

Example:

```bash
curl http://127.0.0.1:8000/health
```

## Test

Run the test suite with:

```bash
pytest
```
