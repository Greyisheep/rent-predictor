from typing import Any

import pandas as pd
from fastapi import APIRouter
from fastapi.encoders import jsonable_encoder
from loguru import logger

from app import schemas
from model_package.regression_model.predict import make_prediction

api_router = APIRouter()


@api_router.post("/predict", response_model=schemas.PredictionResults, status_code=200)
async def predict(input_data: schemas.MultipleHouseDataInputs) -> Any:
    """
    Make house price predictions with the regression model
    """

    input_df = pd.DataFrame(jsonable_encoder(input_data.inputs))

    logger.info(f"Making prediction on inputs: {input_data.inputs}")
    results = make_prediction(input_data=input_df)

    logger.info(f"Prediction results: {results.get('predictions')}")

    return results
