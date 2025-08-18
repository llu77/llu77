# Chatbot Full-Stack Example

This repository contains a simple full-stack AI chatbot application using FastAPI for the backend, React (via Vite) for the frontend, and SQLite for data persistence.

## Backend
- FastAPI REST API with SQLite and SQLAlchemy.
- Small rule-based chatbot that replies to common greetings and stores the
  conversation in a database.
- Run locally:
  ```bash
  cd backend
  uvicorn app.main:app --reload
  ```
- Tests:
  ```bash
  pytest
  ```

## Frontend
- React application built with Vite.
- Fetches existing chat history on load and communicates with backend via
  `/api` proxy.
- Development:
  ```bash
  cd frontend
  npm install
  npm run dev
  ```
- Tests:
  ```bash
  npm test -- --run
  ```
- Build for production:
  ```bash
  npm run build
  ```
