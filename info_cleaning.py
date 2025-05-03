import pandas as pd

def quick_info_dfs (df: pd.DataFrame):
    print("\nDataFrame shape:", df.shape)
    print("\nData types:\n", df.dtypes)
    print("\nMissing values:\n", df.isnull().sum())
    print("\nDescriptive statistics:\n", df.describe())
    print("\nDuplicated values\n", df.duplicated())

def standartize_columns(df):
    df.columns = df.columns.str.lower().str.strip().str.replace(' ', '_')

    return df

def fill_customer_lifetime_value(df):
    median_clv = df['customer_lifetime_value'].median()
    df['customer_lifetime_value'] = df['customer_lifetime_value'].fillna(median_clv)
    return df

def datetime_effective(df):
    df['effective_to_date'] = pd.to_datetime(df['effective_to_date'], errors='coerce')
    return df