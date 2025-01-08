import great_expectations as gx
from great_expectations.core.batch import BatchRequest
from great_expectations.validator.validator import Validator
import pandas as pd

url = "https://github.com/hnawaz007/pythondataanalysis/blob/main/ETL%20Pipeline/Pytest/Session%20one/Product.xlsx?raw=true"
df=pd.read_excel(url)
print(df.head())

context = gx.get_context()

data_source = context.data_sources.add_pandas("pandas")
data_asset = data_source.add_dataframe_asset(name="pd dataframe asset")

batch_definition = data_asset.add_batch_definition_whole_dataframe("batch definion")
batch = batch_definition.get_batch(batch_parameters={"dataframe": df})

expectation = gx.expectations.ExpectColumnValuesToBeInSet(
    column="ProductKey",
    value_set=[0],
)

validation_result = batch.validate(expectation)
print(f"resultado Expectation: {validation_result.success}")