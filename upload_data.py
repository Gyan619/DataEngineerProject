import pandas as pd

#read the parquet file
df = pd.read_parquet("C:/Users/gyane/OneDrive/yellow_tripdata_2025-01.parquet")

# Display the first few rows of the DataFrame
print(df.head())
