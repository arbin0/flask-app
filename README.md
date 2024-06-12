# Flask App

This repository contains the source code for a Flask application, including both backend and frontend components.

## File Structure

flask-app/
├── backend/
│ ├── Dockerfile.backend     # Dockerfile for building the backend image
│ ├── app.py                 # Main entry point for the backend application
│ └── backend.yaml           # Configuration for backend services , deployments, etc.
├── frontend/
│ ├── templates/             # Directory for HTML templates used in the frontend
│ ├── Dockerfile.frontend    # Dockerfile for building the frontend image
│ ├── frontend.py            # Main entry point for the frontend application
│ └── frontend.yaml          # Configuration for frontend services, deployments, etc.
├── .gitignore               # Specifies files and directories to be ignored by Git
└── README.md                # Main documentation file for the project
