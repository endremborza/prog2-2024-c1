import polars as pl
from joblib import load
from sklearn.neighbors import KDTree

query_df = pl.read_csv("query.csv")
df = pl.read_parquet("input.parquet")
tree = load("sklearn_tree.joblib")
out = []
"""
for row in query_df.iter_rows():
    out.append({"dist": tree.query(row)[0], 
                "weapon": df[int(tree.query(row)[1])]["weapon"].item()})
    
"""
for row in query_df.iter_rows():
    out.append({"dist": tree.query([row])[0][0][0], 
                "weapon": df[int(tree.query([row])[1][0][0])]["weapon"].item()})
pl.DataFrame(out).write_csv("out.csv")
