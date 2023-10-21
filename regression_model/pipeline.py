from feature_engine.imputation import AddMissingIndicator
from sklearn.linear_model import Lasso
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import MinMaxScaler

from regression_model.config.core import config
from regression_model.processing import features as pp

price_pipe = Pipeline(
    [
        (
            "missing_indicator",
            AddMissingIndicator(variables=config.model_config.numerical_vars_with_na),
        ),
        (
            "mapper_some",
            pp.Mapper(
                variables=config.model_config.some_vars,
                mappings=config.model_config.some_mappings,
            ),
        ),
        (
            "mapper_location",
            pp.Mapper(
                variables=config.model_config.location_vars,
                mappings=config.model_config.location_mappings,
            ),
        ),
        (
            "mapper_finishing",
            pp.Mapper(
                variables=config.model_config.finishing_vars,
                mappings=config.model_config.finishing_mappings,
            ),
        ),
        ("scaler", MinMaxScaler()),
        (
            "Lasso",
            Lasso(
                alpha=config.model_config.alpha,
                random_state=config.model_config.random_state,
            ),
        ),
    ]
)
