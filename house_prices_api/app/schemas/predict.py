from typing import List, Optional

from pydantic import BaseModel

from model_package.regression_model.processing.validation import \
    HouseDataInputSchema


class PredictionResults(BaseModel):
    # errors: Optional[Any]
    # version: str
    predictions: Optional[List[float]]


class MultipleHouseDataInputs(BaseModel):
    inputs: List[HouseDataInputSchema]

    class Config:
        schema_extra = {
            "example": {
                "inputs": [
                    {
                        "Storeys": 3,
                        "Cheaperflrs": "Yes",
                        "LgCond": 3,
                        "Age": 4,
                        "GenHouse": "Yes",
                        "Parking": "No",
                        "Distance": 1,
                        "Location": "Near Eziobodo Gate",
                        "RdCond": 2,
                        "SecurityLvl": 4,
                        "RmSize": 4,
                        "RmCond": 4,
                        "Wdrobe": "Yes",
                        "Finishing": "Tiles",
                        "Balcony": "Yes",
                        "KitchenSize": 3,
                        "BathrmSize": 3,
                        "BalcnySize": 3,
                        "RefDisposal": True,
                        "LodgeGen": False,
                        "SecPost": False,
                        "Solar": False,
                        "RunWater": True,
                        "Cleaners": False,
                        "Electricity": False,
                        "ElecLodgeGen": False,
                    }
                ]
            }
        }
