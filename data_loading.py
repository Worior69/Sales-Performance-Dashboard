import pandas as pd  # Import the pandas library for data manipulation and analysis
import pyodbc  # Import the pyodbc library to connect to SQL Server

def load_data():
    # Establish connection using Windows Authentication
    # Specify the SQL Server driver, server name, database name, and use Trusted_Connection for authentication.
    conn = pyodbc.connect(
        'DRIVER={SQL Server};'  # The driver to connect to SQL Server
        r'SERVER=HUMAN\SQLEXPRESS;'  # Replace 'HUMAN\SQLEXPRESS' with your server name
        'DATABASE=SuperStoreDB;'  # Replace 'SuperStoreDB' with your database name
        'Trusted_Connection=yes;'  # Use Windows Authentication to connect
    )

    # Query to fetch data (replace with your actual table/query)
    query = "SELECT * FROM [Sample - Superstore]"
    # This query selects all data from the specified table in the database.

    # Load data into a pandas DataFrame
    df = pd.read_sql(query, conn)
    # Executes the SQL query and stores the results in a DataFrame for further manipulation.

    # Close the connection
    conn.close()  # Always close the database connection after use to free up resources.

    return df  # Return the DataFrame containing the data fetched from the database
