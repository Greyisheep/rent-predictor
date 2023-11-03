import json
from typing import Any

# import numpy as np
import pandas as pd
from fastapi import APIRouter, HTTPException
from fastapi.encoders import jsonable_encoder
from loguru import logger
# from regression_model import __version__ as model_version
from model_package.regression_model.predict import make_prediction

# from app import __version__, schemas
from app import schemas
from app.config import settings

api_router = APIRouter()


@api_router.get("/health", response_model=schemas.Health, status_code=200)
def health() -> dict:
    """
    Root Get
    """
    health = schemas.Health(
        # name=settings.PROJECT_NAME, api_version=__version__, model_version=model_version
        name=settings.PROJECT_NAME
    )

    return health.dict()


@api_router.post("/predict", response_model=schemas.PredictionResults, status_code=200)
async def predict(input_data: schemas.MultipleHouseDataInputs) -> Any:
    """
    Make house price predictions with the regression model
    """

    input_df = pd.DataFrame(jsonable_encoder(input_data.inputs))

    # Advanced: You can improve performance of your API by rewriting the
    # `make prediction` function to be async and using await here.
    # logger.info(f"Making prediction on inputs: {input_data.inputs}")
    # results = make_prediction(input_data=input_df.replace({np.nan: None}))

    logger.info(f"Making prediction on inputs: {input_data.inputs}")
    results = make_prediction(input_data=input_df)

    # if results["errors"] is not None:
    #     logger.warning(f"Prediction validation error: {results.get('errors')}")
    #     raise HTTPException(status_code=400, detail=json.loads(results["errors"]))

    logger.info(f"Prediction results: {results.get('predictions')}")

    return results


# @api_router.post("/predict", response_model=schemas.PredictionResults, status_code=200)
# async def predict(input_data: schemas.MultipleHouseDataInputs) -> Any:
#     """
#     Make house price predictions with the regression model
#     """

#     input_dicts = jsonable_encoder(input_data.inputs)
    
#     cleaned_input_dicts = []
#     for input_dict in input_dicts:
#         cleaned_input_dict = {k: v for k, v in input_dict.items() if v is not None}
#         cleaned_input_dict = {k: v for k, v in cleaned_input_dict.items() if v is not None}
#         if cleaned_input_dict:
#             cleaned_input_dicts.append(cleaned_input_dict)

#     if not cleaned_input_dicts:
#         raise HTTPException(status_code=400, detail={"error": "No valid input data provided"})

#     input_df = pd.DataFrame(cleaned_input_dicts)

#     logger.info(f"Making prediction on inputs: {cleaned_input_dicts}")
#     results = make_prediction(input_data=input_df)

#     logger.info(f"Prediction results: {results.get('predictions')}")

#     return results


