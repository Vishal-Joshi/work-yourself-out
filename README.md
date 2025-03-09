# work-yourself-out
A basic workout planning service to help you log workouts, track progress and generate workout statistics.

## Technologies used
* Python: for development
* Docker: for containerisation
* Kubernetes: for container orchestration and deployments
* Poetry: for build management

## How can you build this project
Using poetry, you can run following command to create a sdist for this project
```bash
poetry build
```
which will create a local distribution for this project

## How to run a server locally?
```bash
poetry run uvicorn workoutplanner.main:app --reload 
```
uvicorn is an ASGI(Asynchronous Server Gateway Interface)