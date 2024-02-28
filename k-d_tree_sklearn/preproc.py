import polars as pl
from scipy import spatial
import pandas as pd

df = pd.read_csv("input.csv")
print(df.columns)
tree = spatial.KDTree(df[["x","y"]])
df.to_parquet("input.parquet")