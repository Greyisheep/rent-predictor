import typing as t
from pathlib import Path

import joblib
import pandas as pd
from sklearn.pipeline import Pipeline

from model_package.regression_model.config.core import TRAINED_MODEL_DIR, config

def engineer_dataset() -> pd.DataFrame:
    # Load data from the specified URL
    dataframe = pd.read_csv("https://docs.google.com/spreadsheets/d/1l4Ea9PXEXv_GwcIWTORX_oK6TgZds7yTrek-fGLbJq8/gviz/tq?tqx=out:csv&sheet=Housing_in_Eziobodo")
    
    # Extract all unique utilities
    all_utilities = set()
    for row in dataframe['What utilities are available?']:
        if isinstance(row, str):
            utilities = [utility.strip() for utility in row.split(',')]
            all_utilities.update(utilities)

    # Create columns for each utility and initialize with False
    for utility in all_utilities:
        dataframe[utility] = False

    # Update the columns based on the 'What utilities are available?' column
    for index, row in dataframe.iterrows():
        if pd.notna(row['What utilities are available?']):
            utilities = [utility.strip() for utility in row['What utilities are available?'].split(',')]
            for utility in utilities:
                dataframe.at[index, utility] = True

    # Drop the 'What utilities are available?' column
    dataframe.drop('What utilities are available?', axis=1, inplace=True)

    # Drop the 'Timestamp' column
    dataframe = dataframe.drop('Timestamp', axis=1)
    
    dataframe.columns = ['Name', 'Rent', 'StrtName', 'Storeys', 'Cheaperflrs', 'LgCond', 'Age', 'GenHouse', 'Parking', 'Distance',
       'Location', 'RdCond', 'SecurityLvl', 'RmSize', 'RmCond', 'Wdrobe',
       'Finishing', 'Balcony', 'KitchenSize', 'BathrmSize', 'BalcnySize', 
       'RefDisposal', 'LodgeGen', 'SecPost', 'Solar', 'RunWater', 'Cleaners',
       'Electricity', 'ElecLodgeGen']

    # Convert the "Rent" column to numeric (ignore errors for non-numeric values)
    dataframe['Rent'] = pd.to_numeric(dataframe['Rent'], errors='coerce')

    # Apply the condition to the "Rent" column using a mask
    mask = (dataframe['Rent'].notna()) & (dataframe['Rent'] < 1000)

    # Multiply the values that meet the condition by 1000
    dataframe.loc[mask, 'Rent'] *= 1000

    # Create a new 'ID' column with row IDs
    dataframe['ID'] = range(1, len(dataframe) + 1)

    # Reorder the columns so that 'ID' is the first column
    dataframe = dataframe[['ID'] + [col for col in dataframe if col != 'ID']]

    # Iterate through each column to handle NaN values
    for col in dataframe.columns:
        if dataframe[col].dtype in [int, float]:
            # Replace NaN with the column's average
            dataframe[col].fillna(dataframe[col].mean(), inplace=True)
        elif dataframe[col].dtype == 'object':
            # Replace NaN with the most common string value in the same column
            most_common = dataframe[col].mode()[0]
            dataframe[col].fillna(most_common, inplace=True)
        elif dataframe[col].dtype == 'bool':
            # Replace NaN with the most frequent boolean value
            most_frequent = dataframe[col].mode()[0]
            dataframe[col].fillna(most_frequent, inplace=True)
    
    transformed = dataframe.copy()

    return transformed


def save_pipeline(*, pipeline_to_persist: Pipeline) -> None:
    """Persist the pipeline.
    Saves the versioned model, and overwrites any previous
    saved models. This ensures that when the package is
    published, there is only one trained model that can be
    called, and we know exactly how it was built.
    """

    # Prepare versioned save file name
    save_file_name = f"{config.app_config.pipeline_save_file}.pkl"
    save_path = TRAINED_MODEL_DIR / save_file_name

    remove_old_pipelines(files_to_keep=[save_file_name])
    joblib.dump(pipeline_to_persist, save_path)


def load_pipeline(*, file_name: str) -> Pipeline:
    """Load a persisted pipeline."""

    file_path = TRAINED_MODEL_DIR / file_name
    trained_model = joblib.load(filename=file_path)
    return trained_model


def remove_old_pipelines(*, files_to_keep: t.List[str]) -> None:
    """
    Remove old model pipelines.
    This is to ensure there is a simple one-to-one
    mapping between the package version and the model
    version to be imported and used by other applications.
    """
    do_not_delete = files_to_keep + ["__init__.py"]
    for model_file in TRAINED_MODEL_DIR.iterdir():
        if model_file.name not in do_not_delete:
            model_file.unlink()
