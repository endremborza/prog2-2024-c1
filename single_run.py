import csv
import random
import subprocess
import time
from pathlib import Path

import typer

WEAPONS = ["bomb", "rifle", "arrow"]
SMAX = 100
RUNDIR = "runs"


def write_csv(path, cols, n, generator_fun):
    with path.open("wt") as fp:
        csv_handle = csv.DictWriter(fp, fieldnames=cols)
        csv_handle.writeheader()
        for _ in range(n):
            csv_handle.writerow(dict(zip(cols, generator_fun())))


def maybe_float(v):
    try:
        return round(float(v), 3)
    except ValueError:
        return v


def round_l(l: list):
    return [maybe_float(v) for v in l]


def main(
    solution: str, in_n: int = 10_000, q_n: int = 50, comparison: str = "", seed=742
):
    """no spaces or tabs in commands!"""
    s_path = Path(solution)
    assert s_path.exists()

    rng = random.Random(seed)

    in_p, q_p, o_p = map(s_path.joinpath, ["input.csv", "query.csv", "out.csv"])

    def c():
        return SMAX * rng.random()

    def call(comm):
        p = s_path.joinpath(comm)
        if p.exists():
            args = p.read_text().split()
            start_time = time.time()
            subprocess.call(args, cwd=solution)
        else:
            return time.time()
        return start_time

    def dump_input():
        write_csv(
            in_p,
            ["weapon", "x", "y"],
            in_n,
            lambda: [rng.choice(WEAPONS), c(), c()],
        )

    def dump_query():
        write_csv(q_p, ["x", "y"], q_n, lambda: [c(), c()])

    out = [in_n, q_n]
    for comm, prep in [
        ("setup", lambda: None),
        ("preproc", dump_input),
        ("compute", dump_query),
    ]:
        prep()
        stime = call(comm)
        out.append("{:.6f}".format(time.time() - stime))
    assert o_p.exists()
    in_p.unlink()
    q_p.unlink()
    call("cleanup")

    if comparison:
        with o_p.open() as b_fp, Path(comparison).joinpath("out.csv").open() as c_fp:
            for (base_l, comp_l) in zip(*map(csv.reader, [b_fp, c_fp])):
                assert round_l(base_l) == round_l(comp_l), f"{base_l}, {comp_l}"
    Path(f"{RUNDIR}/{time.time()}-{solution}").write_text(",".join(map(str, out)))
    print("\n\nsuccess!", f"solution: {solution}")
    print(f"validated with {comparison}" if comparison else "non-validated")
    print("inputs: %d queries: %d\nsetup: %ss\nprep: %ss\nrun: %ss\n\n" % tuple(out))
    return out


if __name__ == "__main__":
    typer.run(main)
