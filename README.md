# Dev Sync

Dev Sync is an AI-powered SDLC Optimization Tool that bridges the gap between expectations and delivery. It streamlines the requirement-to-ticket-to-code process, making software development more efficient and intelligent.

## Features
- **AI-Powered User Story Generation** - Automatically generates user stories from requirement documents.
- **Developer Ticket Generation** - Converts user stories into actionable developer tickets.
- **Ticket Test Case Generation** - AI-driven test case creation for tickets.
- **AI-Powered Code Review** - Automates code reviews for better code quality and adherence to best practices.

## Tech Stack
- **Backend**: FastAPI (Python 3.12)
- **Frontend**: React Native
- **UI Library**: Gluestack

## Installation & Setup

### Prerequisites
Ensure you have the following installed:
- **Python 3.12**
- **Node.js 18**

### Clone the repository
```bash
git clone https://github.com/yesweeyes/DevSync.git
```

### Setup .env files
IMPORTANT: Copy the .env files to their respective directories

### Backend Setup (FastAPI)
```bash
cd api  # Navigate to backend folder
python -m venv venv  # Create a virtual environment
source venv/bin/activate  # Activate virtual environment (Linux/macOS)
venv\Scripts\activate  # Activate virtual environment (Windows)
pip install -r requirements.txt  # Install dependencies
uvicorn main:app --reload  # Start FastAPI server
```

### Frontend Setup (React Native)
```bash
cd client  # Navigate to frontend folder
npm install  # Install dependencies
npm start  # Start the React Native app
```
