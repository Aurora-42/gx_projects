import great_expectations as gx
from great_expectations.core.batch import BatchRequest
from great_expectations.validator.validator import Validator
import pandas as pd

url = "hf://datasets/mattrichmo/NetFlix-Imdb-Engagements-Films/cleanDataFilmFlat.csv"
df = pd.read_csv(url)
print(df)

context = gx.get_context()

data_source = context.data_sources.add_pandas("pandas")
data_asset = data_source.add_dataframe_asset(name="pd dataframe asset")

batch_definition = data_asset.add_batch_definition_whole_dataframe("batch definion")
batch = batch_definition.get_batch(batch_parameters={"dataframe": df})

expectation = gx.expectations.ExpectColumnValuesToBeBetween(
    column="imdbUserRating", min_value=0, max_value=10
)

validation_result = batch.validate(expectation)

if validation_result.success:
    print("Succes in expectations!")
else:
    print("Failure in expectations!")