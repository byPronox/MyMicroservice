# 🚀 My Microservice

This is a fully modular microservice built with **FastAPI** and **Docker**, following best practices from Software Design and Architecture.

## ✅ Features

- Domain-based folder separation
- Interfaces and Dependency Injection
- External configuration with `config.py`
- Docker-ready
- Clean architecture and extendable logic
- Logging, error handling, and health check endpoint

## 📁 Project Structure

```
my_microservice/
│
├── docker-compose.yml
├── Dockerfile
├── README.md
├── requirements.txt
│
└── src/
    ├── config/
    │   └── config.py
    │
    ├── controllers/
    │   └── item_controller.py
    │
    ├── interfaces/
    │   ├── i_item_service.py
    │   └── i_item_repository.py
    │
    ├── main.py
    │
    ├── models/
    │   └── item_model.py
    │
    ├── repositories/
    │   └── item_repository.py
    │
    └── services/
        └── item_service.py
```

## 🐳 How to Run with Docker

```bash
docker-compose up --build
```
The app will be available at: [http://localhost:8000](http://localhost:8000)

## 🧪 Test the API

- **Swagger UI:** [http://localhost:8000/docs](http://localhost:8000/docs)
- **Health Check:** [http://localhost:8000/health](http://localhost:8000/health)

**With curl:**
```bash
curl http://localhost:8000/items

curl -X POST http://localhost:8000/items \
-H "Content-Type: application/json" \
-d '{"name": "Test Item", "price": 9.99}'
```

## 🛠️ Main Endpoints
- `GET /items` — List all items
- `POST /items` — Create a new item
- `GET /health` — Health check for monitoring

## 🧩 Architecture & Best Practices
- **Domain decomposition:** Each folder in `src/` represents a single responsibility.
- **Interfaces & Abstraction:** All business logic and data access are abstracted via interfaces for testability and extensibility.
- **Dependency Injection:** FastAPI's `Depends` is used for injecting dependencies.
- **External Configuration:** All secrets and config are managed in `src/config/config.py`.
- **Observability:** Logging and error handling are implemented in both controllers and services.
- **Resilience:** Global exception handler and clear error responses.

## 📚 How to Extend
- Add new domains by creating new folders and interfaces.
- Swap the in-memory repository for a real database by implementing the repository interface.
- Add more endpoints or business logic in the service layer.

---

> Made with ❤️ using FastAPI, following Clean Architecture principles.
