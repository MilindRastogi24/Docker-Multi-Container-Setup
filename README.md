# Flask-Postgres-Redis Docker Setup

This repository contains a **Flask application** connected to a **Postgres database** and a **Redis server**. All services run inside Docker containers on the same network.

## Features
- **Flask App**: Handles API requests.
- **Postgres Database**: Stores data.
- **Redis Server**: Used for caching or other in-memory operations.

---

## Setup Instructions

### Prerequisites
- Install [Docker](https://www.docker.com/).

---

### Step 1: Clone the Repository 
```bash
git clone https://github.com/MilindRastogi24/Docker-Multi-Container-Setup.git
cd DockerAssignment
```

### Step 2: Start and build the containsers
```bash
docker compose up
```

After running this command flask app will start at http://127.0.0.1:8000

### Add and view data in the database
To add a data in the database you can use
Post request for http://127.0.0.1:8000/data
with body as

{
    "name": "test",
    "email": "test@gmail.com"
}

Data will be saved

To view the latest saved data use
Get request for  http://127.0.0.1:8000/data

### Stop and remove containers
```bash
docker compose down
```
