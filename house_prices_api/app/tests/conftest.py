from typing import Generator

import pandas as pd
import pytest
from fastapi.testclient import TestClient
from house_prices_api.model_package.regression_model.processing.data_manager import engineer_dataset

from app.main import app


@pytest.fixture(scope="module")
def test_data() -> pd.DataFrame:
    return engineer_dataset()


@pytest.fixture()
def client() -> Generator:
    with TestClient(app) as _client:
        yield _client
        app.dependency_overrides = {}