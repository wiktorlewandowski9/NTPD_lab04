# NTPD Lab04

## Features

- **Machine Learning Model**: Logistic Regression model trained on the `digits` dataset from `scikit-learn`.
- **REST API**: Built with FastAPI, providing endpoints for predictions, model information, and health checks.
- **Dockerized**: Includes a `Dockerfile` and `docker-compose.yml` for containerized deployment.
- **PostgreSQL Integration**: Configured to work with a PostgreSQL database via Docker Compose.

## Endpoints

- `GET /`: Welcome message.
- `POST /predict`: Predict the class of input features.
- `GET /info`: Retrieve model details (type, number of features, etc.).
- `GET /health`: Check the server's health status.
- `GET /docs`: Access the Swagger UI documentation.

## Prerequisites

- Docker and Docker Compose installed on your system.
- Python 3.9+ (if running locally).

## Setup Instructions

### 1. Clone the Repository

```bash
git clone <repository-url>
cd NTPD_lab04
```

### 2. Build and Run with Docker Compose

```bash
docker-compose up --build
```

This will start the application on `http://localhost:8000`.

### 3. Test the API

You can test the API using tools like `curl`, Postman, or directly via the Swagger UI at `http://localhost:8000/docs`.

Example `curl` command for the `/predict` endpoint:

```bash
curl -X POST "http://localhost:8000/predict" -H "Content-Type: application/json" -d '{"features": [0, 0, 5, 13, 9, 1, 0, 0, 0, 0, 13, 15, 10, 15, 5, 0, 0, 3, 15, 2, 0, 11, 8, 0, 0, 4, 12, 0, 0, 8, 8, 0, 0, 5, 8, 0, 0, 9, 8, 0, 0, 4, 11, 0, 1, 12, 7, 0, 0, 2, 14, 5, 10, 12, 0, 0, 0, 0, 6, 13, 10, 0, 0, 0]}'
```

### 4. Run Locally (Optional)

If you prefer to run the application locally without Docker:

1. Create a virtual environment and activate it:
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv/Scripts/activate
   ```

2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

3. Start the application:
   ```bash
   uvicorn app:app --host 0.0.0.0 --port 8000
   ```

## Project Structure

```
NTPD_lab04/
├── app.py                # FastAPI application
├── Dockerfile            # Dockerfile for containerizing the app
├── docker-compose.yml    # Docker Compose configuration
├── requirements.txt      # Python dependencies
├── README.md             # Project documentation
└── NTPD_lab03.ipynb      # Jupyter Notebook with project notes
```
