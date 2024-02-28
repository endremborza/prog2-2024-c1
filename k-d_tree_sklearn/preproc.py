from sklearn.neighbors import KDTree
import pandas as pd
from joblib import dump

df = pd.read_csv("input.csv")
# Use sklearn because it can be imported faster
tree = KDTree(df[["x","y"]],leaf_size=10)
dump(tree,"sklearn_tree.joblib")
df.to_parquet("input.parquet")
