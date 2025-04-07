# Dev Sync

Dev Sync is an AI-powered SDLC Optimization Tool that bridges the gap between expectations and delivery. It streamlines the requirement-to-ticket-to-code process, making software development more efficient and intelligent.

## Features

- **AI-Powered User Story Generation** - Automatically generates user stories from requirement documents.
- **Developer Ticket Generation** - Converts user stories into actionable developer tickets.
- **Ticket Test Case Generation** - AI-driven test case creation for tickets.
- **AI-Powered Code Review** - Automates code reviews for better code quality and adherence to best practices.

## Documentation

Refer the notion board for documentation: [Docs](https://www.notion.so/yesweeyes/Dev-Sync-Documentation-1ce12c3598cd80b6a68ac447989bf648?pvs=4)

## Tech Stack

- **Backend**: [FastAPI](https://fastapi.tiangolo.com/)
- **Frontend**: [React Native](https://reactnative.dev/)
- **UI Library**: [Gluestack](https://gluestack.io/)
- **Database**: [PostgreSQL](https://www.postgresql.org/download/)

## Installation & Setup

### Prerequisites

Ensure you have the following installed:

- **Python 3.12**
- **Node.js 18**
- **PostgreSQL**: Follow the [official PostgreSQL setup guide](https://www.postgresql.org/download/)

### Clone the repository

```bash
https://github.com/yesweeyes/dev-sync.git
```

### Setup .env files

IMPORTANT: Copy the .env files to their respective directories

### PostgreSQL Setup

Ensure that PostgreSQL is installed and running. Create a new database:

```sql
CREATE DATABASE devsync;
```

### Backend Setup (FastAPI)

```bash
cd api  # Navigate to backend folder
python -m venv venv  # Create a virtual environment
source venv/bin/activate  # Activate virtual environment (Linux/macOS)
venv\Scripts\activate  # Activate virtual environment (Windows)
pip install -r requirements.txt  # Install dependencies
uvicorn main:app --reload  # Start FastAPI server
```

### Database Migration Setup (Alembic)

```bash
cd api  # Navigate to backend folder
alembic init migrations  # Initialize Alembic (only run once)
```

Update `alembic.ini` file to include your database connection URL:

```
sqlalchemy.url = postgresql://postgres:password@localhost:5432/devsync
```

Run the migrations:

```bash
alembic revision --autogenerate -m "Initial migration"  # Generate migration
alembic upgrade head  # Apply migration
```

### Frontend Setup (React Native)

```bash
cd client  # Navigate to frontend folder
npm install  # Install dependencies
npm start  # Start the React Native app
```
