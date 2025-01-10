import great_expectations as gx
import pandas as pd

# carregar o dataset
df = pd.read_csv(
    "https://raw.githubusercontent.com/great-expectations/gx_tutorials/main/data/yellow_tripdata_sample_2019-01.csv"
)

# para checar se o dataset foi carregado corretamente
#print(df.head(5))

# criar um contexto do great_expectations
context = gx.get_context()

# adicionar um data source e um data asset
data_source = context.data_sources.add_pandas("pandas")
data_asset = data_source.add_dataframe_asset(name="pd dataframe asset")

# adicionar um batch definition e um batch
batch_definition = data_asset.add_batch_definition_whole_dataframe("batch definition")
batch = batch_definition.get_batch(batch_parameters={"dataframe": df})

# criar uma expectativa
expectation = gx.expectations.ExpectColumnValuesToBeBetween(
    column="passenger_count", min_value=1, max_value=6
)

# validar a expectativa
validation_result = batch.validate(expectation)

#printar os resultados
print(validation_result)
