# 2024-03-03

## Inputs: 1000, Queries 20

| solution             |   setup_time |   preproc_time |   run_time |
|:---------------------|-------------:|---------------:|-----------:|
| barab-szabi-2        |     0.725503 |       0.356591 |   0.349379 |
| barab-szabi-1        |     0.725901 |       0.392618 |   0.358078 |
| k-d_tree_polars      |     0.725379 |       0.397059 |   0.359915 |
| solution-1           |     8.95698  |       1e-06    |   0.430759 |
| Bori_Aron_solution-1 |     0.715568 |       0.490238 |   0.490014 |
| k-d_tree_pandas      |     0.719925 |       0.376983 |   0.495846 |
| k-d_tree_sklearn     |    10.4139   |       1.10792  |   0.697323 |

## Inputs: 10000, Queries 50

| solution             |   setup_time |   preproc_time |   run_time |
|:---------------------|-------------:|---------------:|-----------:|
| barab-szabi-2        |     0.726336 |       0.361541 |   0.352301 |
| k-d_tree_polars      |     0.718596 |       0.401474 |   0.364149 |
| barab-szabi-1        |     0.750185 |       0.401497 |   0.366222 |
| Bori_Aron_solution-1 |     0.71293  |       0.512125 |   0.492134 |
| k-d_tree_pandas      |     0.72139  |       0.377737 |   0.500253 |
| k-d_tree_sklearn     |     0.730691 |       0.841023 |   0.666048 |

## Inputs: 50000, Queries 200

| solution             |   setup_time |   preproc_time |   run_time |
|:---------------------|-------------:|---------------:|-----------:|
| barab-szabi-2        |     0.722562 |       0.373446 |   0.366467 |
| k-d_tree_polars      |     0.727222 |       0.425296 |   0.388649 |
| barab-szabi-1        |     0.726553 |       0.424974 |   0.391922 |
| Bori_Aron_solution-1 |     0.728718 |       0.541415 |   0.495706 |
| k-d_tree_pandas      |     0.722599 |       0.396989 |   0.542909 |
| k-d_tree_sklearn     |     0.736298 |       0.888613 |   0.698282 |

## Inputs: 250000, Queries 500

| solution             |   setup_time |   preproc_time |   run_time |
|:---------------------|-------------:|---------------:|-----------:|
| barab-szabi-2        |     0.720291 |       0.439362 |   0.40335  |
| k-d_tree_polars      |     0.733747 |       0.534296 |   0.486704 |
| barab-szabi-1        |     0.72478  |       0.533094 |   0.497711 |
| Bori_Aron_solution-1 |     0.714865 |       0.724754 |   0.507908 |
| k-d_tree_pandas      |     0.722053 |       0.479503 |   0.680568 |
| k-d_tree_sklearn     |     0.725228 |       1.11355  |   0.749344 |

## Inputs: 1000000, Queries 1000

| solution             |   setup_time |   preproc_time |   run_time |
|:---------------------|-------------:|---------------:|-----------:|
| barab-szabi-2        |     0.72127  |       0.689599 |   0.437976 |
| Bori_Aron_solution-1 |     0.710631 |       1.36298  |   0.532238 |
| k-d_tree_polars      |     0.727968 |       0.866683 |   0.827734 |
| k-d_tree_sklearn     |     0.728652 |       1.92271  |   0.856856 |
| barab-szabi-1        |     0.724598 |       0.856598 |   0.867268 |
| k-d_tree_pandas      |     0.718657 |       0.756792 |   1.1027   |

## Inputs: 10000000, Queries 1000

| solution             |   setup_time |   preproc_time |   run_time |
|:---------------------|-------------:|---------------:|-----------:|
| Bori_Aron_solution-1 |     0.714528 |       10.8075  |   0.784503 |
| barab-szabi-2        |     0.720192 |        5.36258 |   0.805723 |
| k-d_tree_sklearn     |     0.731814 |       15.9433  |   1.04665  |
| k-d_tree_polars      |     0.724531 |        4.94875 |   6.56502  |
| barab-szabi-1        |     0.73448  |        4.94155 |   6.61817  |
| k-d_tree_pandas      |     0.729308 |        3.98365 |   6.87895  |

## Inputs: 100000000, Queries 10000

| solution             |   setup_time |   preproc_time |   run_time |
|:---------------------|-------------:|---------------:|-----------:|
| barab-szabi-2        |     0.972806 |        71.1518 |    4.11824 |
| k-d_tree_sklearn     |     0.729501 |       228.32   |    5.23459 |
| Bori_Aron_solution-1 |     0.851754 |       141.577  |   18.1865  |