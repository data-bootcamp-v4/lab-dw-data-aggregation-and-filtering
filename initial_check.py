'''This file perform and initial data check and output important details
from the data'''

import numpy as np
import pandas as pd

def initial_chk(data_frame):
    '''This function check for the number of columns and rows, 
        the data types, unique values, pisble categorial values
        and unique values count for categorical columns'''
       
    print(f"Number of columns: {data_frame.shape[1]} amd rows: {data_frame.shape[0]}")

    print("\nData types:")
    print(data_frame.dtypes)

    # Unique values count
    print("\nUnique values count:")
    unique_values_count = data_frame.nunique()
    print(unique_values_count)


    # Let's identify categorical columns 
    categorical_columns = unique_values_count[unique_values_count < 10].index
    print(f"\nThis columns apear to be categroical:\n {categorical_columns}")

    print("\nUnique value count for categorical columns:")
    for col_ in data_frame.columns:
        if col_ in categorical_columns:
            print(f"{data_frame[col_].value_counts()}\n")

def chech_null(data_frame):
    '''Check for NaN values in each column and print the total per column'''
    print("Count of null values:")
    print(data_frame.isnull().sum())

def chech_duplicated(data_frame):
    '''Check for duplicated values in the data frame and print the total'''
    print("\nCount of duplicated values:")
    print(data_frame.duplicated().sum())

def check(data_frame):
    '''A function to call all the function for the data cleaning'''
    initial_chk(data_frame)
    chech_null(data_frame)
    chech_duplicated(data_frame)

def snake_f(data_frame):
    data_frame.columns = ["state" if column == "ST" else column.lower().replace(" ", "_") for column in data_frame.columns]

def replace_col(data_frame, col_, old, new):
    data_frame[col_] = data_frame[col_].replace(old, new)

def filling_nan(data_frame, col_, method):
    if method == "mode":
        data_frame[col_] = data_frame[col_].fillna(data_frame[col_].mode()[0])

def drop(data_frame):
    data_frame.drop_duplicates(keep="first", inplace=True)

def in_col_replace(data_frame, col_, old, new, type_):
    if type_ == "float":
        data_frame[col_] = data_frame[col_].str.replace(old, new, regex=True).astype(float)

def drop_nan(data_frame):
    return data_frame.dropna()

def format_complain(data_frame, col_):
    data_frame[col_] = data_frame[col_].apply(lambda x: x.split('/')[1] if isinstance(x, str) and  '/' in x else x)
    data_frame[col_] = pd.to_numeric(data_frame[col_], errors = 'coerce')

def drop_col(data_frame, cols):
    data_frame = data_frame.drop(cols, axis = 1)
    return data_frame