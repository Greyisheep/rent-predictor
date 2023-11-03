from typing import List, Optional, Tuple

import numpy as np
import pandas as pd
from pydantic import BaseModel

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

class HouseDataInputSchema(BaseModel):
    Name:           Optional[str]
    StrtName:       Optional[str]
    Storeys:        Optional[int]
    Cheaperflrs:    Optional[str]
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
    RefDisposal:    Optional[bool]
    LodgeGen:       Optional[bool]
    SecPost:        Optional[bool]
    Solar:          Optional[bool]
    RunWater:       Optional[bool]
    Cleaners:       Optional[bool]
    Electricity:    Optional[bool]
    ElecLodgeGen:   Optional[bool]


class MultipleHouseDataInputs(BaseModel):
    inputs: List[HouseDataInputSchema]
