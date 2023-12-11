from typing import List, Optional, Tuple

import numpy as np
import pandas as pd
from pydantic import BaseModel

from model_package.regression_model.config.core import config

def engineer_dataset() -> pd.DataFrame:
    # Load data from the specified URL
    url = config.model_config.url
    dataframe = pd.read_csv(url)
    
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
    
    transformed_data = dataframe.copy()

    return transformed_data


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
