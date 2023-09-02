import fastapi
import pandas as pd
from typing import List
from model import DelayModel
from pydantic import BaseModel
from fastapi import HTTPException

app = fastapi.FastAPI()

# Define una clase Pydantic para los datos de vuelo
class Flight(BaseModel):
    OPERA: str
    TIPOVUELO: str
    MES: int

class FlightData(BaseModel):
    flights: List[Flight]

@app.get("/health", status_code=200)
async def get_health() -> dict:
    return {
        "status": "OK"
    }

@app.post("/predict", status_code=200)
async def post_predict(codigo: FlightData) -> dict:
        predictions = []
        for flight in codigo.flights:
            error_text = ''
            if (flight.TIPOVUELO != 'N' and flight.TIPOVUELO != 'I') or (flight.MES < 1 or flight.MES > 12):
                error_text=f"TIPOVUELO o MES no válido para el vuelo con OPERA {flight.OPERA}"
                raise HTTPException(status_code=400, detail=error_text)
            else:
                df = pd.DataFrame([flight.dict()])
                features = model.preprocess(
                data=df
                )
                prediction = model.predict(features=features)
                # predictions.append({"OPERA": flight.OPERA, "prediction": prediction})
                predictions=prediction
                return {"predict":  predictions}

def initialize_model():
    data = pd.read_csv(filepath_or_buffer="../data/data.csv")
    model = DelayModel()
    features, target = model.preprocess(
        data=data,
        target_column="delay"
    )
    model.fit(features, target)
    return model

if "__main__" == "__main__":
    model = initialize_model()


