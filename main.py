"""
Entry point for Simulado application.
Run with: uv run main.py
Or: uv run uvicorn app.main:app --reload --port 8000
"""

import uvicorn

if __name__ == "__main__":
    print("Starting Simulado Web App on http://127.0.0.1:8000 ...")
    uvicorn.run("app.main:app", host="127.0.0.1", port=8000, reload=True)
