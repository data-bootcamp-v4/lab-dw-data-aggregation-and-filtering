# Standardize the column names
def lower_snake(df):

    df.columns = df.columns.str.lower()  # Convert all column names to lowercase
    df.columns = df.columns.str.replace(" ", "_")  # Replace spaces with underscores

    return df
