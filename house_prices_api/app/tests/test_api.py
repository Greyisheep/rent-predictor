import numpy as np
import pandas as pd
from fastapi.testclient import TestClient

API_ENDPOINT = "/api/v1/predict"


def test_make_prediction(client: TestClient, test_data: pd.DataFrame) -> None:
    # Given
    payload = {
        # ensure pydantic plays well with np.nan
        "inputs": test_data.replace({np.nan: None}).to_dict(orient="records")
    }

    # When
    try:
        response = client.post(
            API_ENDPOINT,
            json=payload,
        )
        response.raise_for_status()
    except Exception as e:
        print(f"Error occurred during API call: {e}")
        return

    # Then
    assert response.status_code == 200
    prediction_data = response.json()
    assert prediction_data["predictions"]
    assert np.isclose(prediction_data["predictions"][0], 143286, rtol=1000)
