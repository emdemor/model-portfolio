# Streamlit App (Supersimple)

This is a minimal, professional Streamlit app packaged as a Python project.

## Quickstart

```bash
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
streamlit run src/streamlit_app/app.py
```

## Development

```bash
pip install -e ".[dev]"
pytest -q
ruff check .
```
