# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Commands

```bash
# Run locally
streamlit run src/interface/app.py
make lrun

# Install for development
pip install -e ".[dev]"

# Tests
pytest

# Lint
ruff check .
ruff format .

# Docker
make build          # Build all images
make front          # Run Streamlit container
make run-jupyter    # Run Jupyter container
```

## Architecture

**Python/Streamlit app** with MongoDB-backed authentication.

### Key Files
- `src/interface/app.py` — Entry point: loads pages, handles auth, renders sidebar
- `src/interface/auth.py` — `streamlit-authenticator` setup
- `src/interface/auth_store.py` — MongoDB credential fetching
- `src/interface/settings.py` — Pydantic `BaseSettings` config (env vars with prefixes `MONGODB_`, `AUTH_`, `APP_`)
- `src/interface/pages/` — Page modules (auto-discovered)

### Page System
Pages are auto-discovered via `pkgutil.iter_modules()`. Each page module exposes:
- `name` — Display name in sidebar
- `order` — Sort order (default 10,000)
- `requires_auth` — Bool flag for protected pages
- `render()` — Page render function

### Environment Variables
```
MONGODB_HOST, MONGODB_USER, MONGODB_PASSWORD, MONGODB_DATABASE
AUTH_COOKIE_NAME, AUTH_COOKIE_KEY, AUTH_COOKIE_EXPIRY_DAYS
APP_NAME
```

### Deployment
Two Docker containers: `Dockerfile.frontend` (Streamlit, port 8501) and `Dockerfile.jupyter` (JupyterLab, port 8888).

## Instructions
- Save all memories in @CLAUDE.md
