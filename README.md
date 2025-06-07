# MyMicroservice

## Dominio
Este microservicio gestiona un catálogo de items (productos) permitiendo su registro y consulta. Está enfocado en un único dominio funcional siguiendo buenas prácticas de arquitectura.

## Estructura del proyecto
- **src/controllers**: Controladores (endpoints HTTP)
- **src/services**: Lógica de negocio
- **src/repositories**: Acceso a datos (repositorio en memoria)
- **src/models**: Modelos de datos (Pydantic)
- **src/interfaces**: Interfaces y clases abstractas
- **src/config**: Configuración externa (manejo de secretos)

## Cómo correr el microservicio

### Requisitos
- Docker y Docker Compose

### Pasos rápidos
```sh
docker-compose up --build
```
El microservicio estará disponible en `http://localhost:8000`.

## Endpoints principales
- `GET /items`: Lista todos los items
- `POST /items`: Crea un nuevo item
- `GET /health`: Health check para monitoreo

## Pruebas manuales
Puedes probar los endpoints usando [Swagger UI](http://localhost:8000/docs) o herramientas como Postman/curl.

## Inyección de dependencias
Se utiliza el sistema de dependencias de FastAPI (`Depends`) para inyectar el repositorio en el servicio y el servicio en los controladores.

## Manejo de configuración y secretos
La configuración (nombre y versión de la app, etc.) se encuentra en `src/config/config.py`. Puedes modificar este archivo para cambiar parámetros sin tocar el código principal.

## Despliegue con Docker
El proyecto incluye `Dockerfile` y `docker-compose.yml` para facilitar el despliegue y operación del microservicio de forma independiente.

## Observabilidad y resiliencia
- Se agregaron logs en controladores y servicios.
- Se maneja un endpoint `/health` para monitoreo.
- Se manejan excepciones y se retornan respuestas claras en caso de error.

---

Sigue las mejores prácticas de microservicios y es fácilmente extensible para bases de datos reales, métricas y más.
