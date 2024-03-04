import pandas as pd
import numpy as np

if __name__ == "__main__":

    df = pd.read_csv("input.csv")
    query_df = pd.read_csv("query.csv")

    # `numpy` tömbökké konvertálás
    coords = df[["x", "y"]].values
    query_coords = query_df[["x", "y"]].values
    weapons = df["weapon"].values

    # Távolságok és minimális indexek kiszámítása
    distances = np.sqrt(((coords[:, np.newaxis, :] - query_coords)**2).sum(axis=2))
    min_indices = distances.argmin(axis=0)

    # Eredmények összegyűjtése
    out = [{"dist": np.min(distances[:, i]), "weapon": weapons[min_indices[i]]} for i in range(min_indices.size)]

    # Eredmények exportálása CSV-be
    pd.DataFrame(out).to_csv("out.csv", index=False)
