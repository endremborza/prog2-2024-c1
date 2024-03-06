import flask
import pandas as pd
from sklearn.neighbors import KDTree

app = flask.Flask(__name__)

df = pd.read_csv("input.csv")
weps = df["weapon"].values
tree = KDTree(df[["x", "y"]])


@app.route("/ping")
def ping():
    qdf = pd.read_csv("query.csv")
    dists, inds = tree.query(qdf)
    df = pd.DataFrame({"dist": dists.reshape(-1), "weapon": weps[inds.reshape(-1)]})
    df.to_csv("out.csv", index=False)
    return "OK"


@app.route("/")
def ok():
    return "OK"


if __name__ == "__main__":
    app.run(port=5678)
