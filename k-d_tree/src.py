import pandas as pd
import numpy as np
from scipy import spatial


df = pd.read_csv("input.csv")
query_df = pd.read_csv("query.csv")

tree = spatial.KDTree(df[["x","y"]])
out = []
for idx, row in query_df.iterrows():
    out.append({"dist": tree.query(row)[0], "weapon": df.loc[tree.query(row)[1], "weapon"]})
pd.DataFrame(out).to_csv("out.csv", index=False)
