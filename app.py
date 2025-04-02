import numpy as np
from fastapi import FastAPI
from fastapi.exceptions import HTTPException
from pydantic import BaseModel
from sklearn.datasets import load_digits
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split


app = FastAPI()

digits = load_digits()
X, y = digits.data, digits.target
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
model = LogisticRegression(max_iter=2000)
model.fit(X_train, y_train)


class InputData(BaseModel):
    features: list


@app.get("/")
def read_root():
    return {"message": "Witaj w FastAPI z modelem ML!"}


@app.post("/predict")
def predict(data: InputData):
    try:
        expected_features = X.shape[1]
        if len(data.features) != expected_features:
            raise ValueError(f"Oczekiwano {expected_features} cech, otrzymano {len(data.features)}.")

        input_array = np.array(data.features).reshape(1, -1)
        predicted_class = model.predict(input_array)[0]

        return {"predicted_class": int(predicted_class)}

    except ValueError as ve:
        raise HTTPException(status_code=400, detail=str(ve))
    except Exception as e:
        raise HTTPException(status_code=500, detail="Wystąpił błąd serwera.")
    

@app.get("/info")
def model_info():
    """Zwraca podstawowe informacje o modelu."""
    return {
        "model_type": "LogisticRegression",
        "num_features": X.shape[1],
        "num_classes": len(np.unique(y)),
        "max_iter": model.max_iter
    }


@app.get("/health")
def health_check():
    """Zwraca status działania serwera."""
    return {"status": "ok"}


@app.get("/docs")
def get_docs():
    """Przekierowuje do dokumentacji Swagger UI."""
    return {"docs_url": "/docs"}
