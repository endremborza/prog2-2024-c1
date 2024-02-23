import pandas as pd

pd.read_csv("input.csv").to_pickle("input.pickle")
pd.read_csv("query.csv").to_pickle("query.pickle")