import great_expectations as ge
from great_expectations.core.batch import BatchRequest
from great_expectations.data_context import DataContext
from great_expectations.validator.validator import Validator
import pandas as pd

url = "https://github.com/hnawaz007/pythondataanalysis/blob/main/ETL%20Pipeline/Pytest/Session%20one/Product.xlsx?raw=true"
df=pd.read_excel(url)
print(df.head())

context = DataContext()

data_source = context.data_source.add_pandas("pandas")
data_asset = data_source.add_dataframe_asset(name="pd dataframe asset")

batch_definition = data_asset.add_batch_definition_whole_dataframe("batch definion")
batch = batch_definition.get_batch(batch_parameters={"dataframe": df})

expectation = ge.dataset.expect_column_values_to_be_in_set(
    column="Product",
    value_set=["A", "B", "C", "D", "E"],
)