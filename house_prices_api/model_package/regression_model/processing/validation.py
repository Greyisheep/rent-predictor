from typing import List, Optional, Tuple

import numpy as np
import pandas as pd
from pydantic import BaseModel, ValidationError

from model_package.regression_model.config.core import config


def drop_na_inputs(*, input_data: pd.DataFrame) -> pd.DataFrame:
    """Check model inputs for na values and filter."""
    validated_data = input_data.copy()
    new_vars_with_na = [
        var
        for var in config.model_config.features
        if var
        not in config.model_config.numerical_vars_with_na
        and validated_data[var].isnull().sum() > 0
    ]
    validated_data.dropna(subset=new_vars_with_na, inplace=True)

    return validated_data


# def validate_inputs(*, input_data: pd.DataFrame) -> Tuple[pd.DataFrame, Optional[dict]]:
#     """Check model inputs for unprocessable values."""

#     # convert syntax error field names (beginning with numbers)
#     relevant_data = input_data[config.model_config.features].copy()
#     validated_data = drop_na_inputs(input_data=relevant_data)
#     errors = None

#     try:
#         # replace numpy nans so that pydantic can validate
#         MultipleHouseDataInputs(
#             inputs=validated_data.replace({np.nan: None}).to_dict(orient="records")
#         )
#     except ValidationError as error:
#         errors = error.json()

#     return validated_data, errors


class HouseDataInputSchema(BaseModel):
    Id:             Optional[int]
    Name:           Optional[str]
    Rent:           Optional[int]
    StrtName:       Optional[str]
    Storeys:        Optional[int]
    Cheaperflrs:    Optional[str]
    Electricity:    Optional[str]
    RefDisposal:    Optional[str]
    RunWater:       Optional[str]
    SecPost:        Optional[str]
    Cleaners:       Optional[str]
    LodgeGen:       Optional[str]
    Solar:          Optional[str]
    LgCond:         Optional[int]
    Age:            Optional[int]
    GenHouse:       Optional[str]
    Parking:        Optional[str]
    Distance:       Optional[int]
    Location:       Optional[str]
    RdCond:         Optional[int]
    SecurityLvl:    Optional[int]
    RmSize:         Optional[int]
    RmCond:         Optional[int]
    Wdrobe:         Optional[str]
    Finishing:      Optional[str]
    Balcony:        Optional[str]
    KitchenSize:    Optional[int]
    BathrmSize:     Optional[int]
    BalcnySize:     Optional[int]
    dtype:          Optional[str]


class MultipleHouseDataInputs(BaseModel):
    inputs: List[HouseDataInputSchema]
