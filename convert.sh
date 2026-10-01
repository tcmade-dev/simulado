#!/usr/bin/env bash
# Quick wrapper to run the PDF to DOCX converter using the local virtualenv

set -e

DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" >/dev/null 2>&1 && pwd)"
PYTHON_EXEC="$DIR/.venv/bin/python3"

if [ ! -f "$PYTHON_EXEC" ]; then
    echo "Virtual environment not found at $DIR/.venv"
    echo "Using system python3 instead..."
    PYTHON_EXEC="python3"
fi

export PYTHONWARNINGS="ignore"
exec "$PYTHON_EXEC" "$DIR/pdf_to_docx.py" "$@"
