import pandas as pd
from data_loading import load_data


# Load the data
def clean_data():
    df = load_data()  # Call the function from data_loading.py to fetch the data as a DataFrame.

    # 1. Check the structure of the data
    print("columns and data types:")
    print(
        df.info())  # Displays information about columns, data types, and non-null values to understand the dataset's structure.

    # 2. Check for missing values
    print("\nMissing Values:")
    print(df.isnull().sum())  # Identifies columns with missing values by summing up `NaN` occurrences.

    # 3. Handle Missing Values
    # Identify columns with missing values
    missing_columns = df.columns[df.isnull().sum() > 0]  # Filters out columns with missing values.
    print("\nColumns with missing values")
    print(missing_columns)  # Displays columns containing missing values.

    # Verify no missing values remain
    print("\nMissing values after handling")
    print(df.isnull().sum())  # Confirms if missing values were handled (in this case, there were none to handle).

    # 4. Handle duplicate rows
    # Check for duplicate rows
    duplicate_rows = df.duplicated().sum()  # Counts the number of duplicate rows in the dataset.
    print(f"\nNumber of duplicate rows : {duplicate_rows}")  # Prints the number of duplicates (0 in our case).

    # 5. Standardize column names
    # Rename columns for easier access (remove spaces, lowercase names, etc.)
    df.columns = df.columns.str.strip().str.replace(' ',
                                                    '_').str.lower()  # Strips extra spaces, replaces spaces with underscores, and converts names to lowercase.
    print("\nUpdated column names:")
    print(df.columns)  # Displays the updated column names to verify the changes.

    # 6. Convert numeric columns to appropriate types
    numeric_columns = ['sales', 'quantity', 'discount', 'profit']  # List of columns expected to contain numeric data.
    for col in numeric_columns:
        df[col] = pd.to_numeric(df[col],
                                errors='coerce')  # Converts columns to numeric, replacing invalid entries with `NaN`.

    # Verify conversion
    print("\nData types after numeric conversion ")
    print(df[numeric_columns].dtypes)  # Confirms that the specified columns have numeric data types.

    # 7. Convert columns to datetime format
    date_columns = ['order_date', 'ship_date']  # List of columns expected to contain date data.
    for col in date_columns:
        df[col] = pd.to_datetime(df[col],
                                 errors='coerce')  # Converts columns to datetime, replacing invalid entries with `NaN`.

    # Verify conversion
    print("\nData types after date conversion")
    print(df[date_columns].dtypes)  # Confirms that the specified columns have datetime data types.

    return df


# prevent execution during import
if __name__ == "__main__":
    df = clean_data()
    print("\nData Cleaning Complete")
