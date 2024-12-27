import great_expectations as gx
import pandas as pd

df = pd.read_csv(
    "https://raw.githubusercontent.com/great-expectations/gx_tutorials/main/data/yellow_tripdata_sample_2019-01.csv"
)

print(df.head())