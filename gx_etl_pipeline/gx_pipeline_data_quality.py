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

batch_definition = data_asset.add_batch_definition_whole_dataframe("batch definition")
batch = batch_definition.get_batch(batch_parameters={"dataframe": df})

# Define expectations
expectations = [
    gx.expectations.ExpectColumnValuesToBeBetween(
        column="imdbUserRating", min_value=0, max_value=10
    ),
    gx.expectations.ExpectColumnValuesToNotBeNull(column="title"),
    gx.expectations.ExpectColumnValuesToBeUnique(column="title"),
    gx.expectations.ExpectColumnValuesToMatchRegex(
        column="releaseYear", regex=r"^\d{4}$"
    )
]

# Validate expectations
for expectation in expectations:
    validation_result = batch.validate(expectation)
    if validation_result.success:
        print(f"Success in expectation: {expectation.expectation_type}")
    else:
        print(f"Failure in expectation: {expectation.expectation_type}")