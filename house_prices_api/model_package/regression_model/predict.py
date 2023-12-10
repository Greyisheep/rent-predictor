import os
import sys

# Add the project's root directory to sys.path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..')))

# print(sys.path)

import typing as t

import numpy as np
import pandas as pd

from model_package.regression_model.config.core import config
from model_package.regression_model.processing.data_manager import load_pipeline
from model_package.regression_model.processing.validation import drop_na_inputs

pipeline_file_name = f"{config.app_config.pipeline_save_file}.pkl"
_price_pipe = load_pipeline(file_name=pipeline_file_name)


# def make_prediction(
#     *,
#     input_data: t.Union[pd.DataFrame, dict],
# ) -> dict:
#     """Make a prediction using a saved model pipeline."""


# def make_prediction(
#     *,
#     input_data: t.Union[pd.DataFrame, dict],
# ) -> dict:
#     """Make a prediction using a saved model pipeline."""

#     data = pd.DataFrame(input_data)
#     validated_data = drop_na_inputs(input_data=data)
    
#     predictions = _price_pipe.predict(
#         X=data[config.model_config.features]
#     )
#     results = {
#         "predictions": [np.exp(pred) for pred in predictions],  # type: ignore
#     }

#     return results

def make_prediction(
    input_data: t.Union[pd.DataFrame, dict]
) -> dict:
    """Make a prediction using a saved model pipeline."""

    validated_data = drop_na_inputs(input_data=input_data)
    
    predictions = _price_pipe.predict(
        X=validated_data[config.model_config.features]
    )
    results = {
        "predictions": [np.exp(pred) for pred in predictions],  # type: ignore
    }

    return results
