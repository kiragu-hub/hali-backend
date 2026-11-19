# HALI Backend

Backend development workspace for the HALI Wellness Platform.

## Project Overview

HALI is an anonymous wellness support platform designed to help university students and communities access wellness support while protecting their privacy.

This repository contains the backend development work.

## Technology Stack

- Python
- FastAPI
- PostgreSQL
- SQLAlchemy
- Alembic
- Psycopg 3

## Current Backend Structure

- `app/main.py` - FastAPI application entry point
- `app/core/` - Application configuration
- `app/db/` - Database connections and sessions
- `app/models/` - SQLAlchemy models
- `app/schemas/` - API schemas
- `app/services/` - Business logic
- `app/api/` - API routes
- `alembic/` - Database migration configuration

## Local Development Setup

### 1. Create a virtual environment

```bash
python3 -m venv .venv
source .venv/bin/activate
```

### 2. Install dependencies

```bash
pip install -r requirements.txt
```

### 3. Configure environment variables

```bash
cp .env.example .env
```

Edit `.env` and enter your local PostgreSQL credentials.

### 4. Start the API

```bash
uvicorn app.main:app --reload
```

API documentation: `http://127.0.0.1:8000/docs`

## Security

- Never commit `.env` or real credentials.
- Keep `.env.example` limited to placeholders.
- Do not commit virtual environments or generated files.
- Security and privacy controls require testing before production use.

## Project Status

Initial FastAPI application structure, PostgreSQL connectivity, SQLAlchemy sessions, and Alembic configuration are in place. Models, migrations, authentication, and API functionality remain under development.
