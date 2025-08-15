# Django + React Dockerized Project

This is a simple full-stack application using:
- **Backend:** Django (Python 3.11)
- **Frontend:** React
- **Containerization:** Docker & Docker Compose

## 📦 Requirements
- Docker
- Docker Compose

## 🚀 How to Run

1. Clone the repository:
```bash
git clone https://github.com/your-username/your-repo-name.git
cd your-repo-name
```

2. Build and start containers:
```bash
docker-compose up --build
```

3. Access the services:
- **Backend (Django):** http://localhost:8000
- **Frontend (React):** http://localhost:3000

## 🛠 Development Notes
- Live code changes are reflected instantly because of volume mounting.
- Use `CTRL+C` to stop containers and `docker-compose down` to remove them.

## 📂 Project Structure
```
backend/      # Django application
frontend/     # React application
docker-compose.yml
```

---
**Author:** Esraa Antar
