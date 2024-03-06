# 2024-03-06

## Inputs: 1000, Queries 20

| solution             |   setup_time |   preproc_time |   run_time |
|:---------------------|-------------:|---------------:|-----------:|
| barab-szabi-2        |     0.727449 |       0.360282 |   0.353365 |
| barab-szabi-1        |     0.729203 |       0.395155 |   0.366473 |
| Bori_Aron_solution-1 |     0.718143 |       0.497771 |   0.496669 |
| k-d_tree_pandas      |     0.727434 |       0.377938 |   0.502575 |
| k-d_tree_sklearn     |     4.0649   |       1.14613  |   0.66986  |
| solution-1           |     8.90803  |       1e-06    |   0.694031 |
| k-d_tree_polars      |     9.00735  |       0.543559 |   0.832467 |

## Inputs: 10000, Queries 50

| solution             |   setup_time |   preproc_time |   run_time |
|:---------------------|-------------:|---------------:|-----------:|
| barab-szabi-2        |     0.726449 |       0.363091 |   0.358222 |
| k-d_tree_polars      |     0.729734 |       0.40662  |   0.365029 |
| barab-szabi-1        |     0.725669 |       0.409882 |   0.367419 |
| Bori_Aron_solution-1 |     0.718149 |       0.50576  |   0.497725 |
| k-d_tree_pandas      |     0.72837  |       0.390404 |   0.508516 |
| k-d_tree_sklearn     |     0.730524 |       0.872835 |   0.677816 |

## Inputs: 50000, Queries 200

| solution             |   setup_time |   preproc_time |   run_time |
|:---------------------|-------------:|---------------:|-----------:|
| barab-szabi-2        |     0.728499 |       0.381619 |   0.371398 |
| k-d_tree_polars      |     0.73034  |       0.441577 |   0.391673 |
| barab-szabi-1        |     0.742166 |       0.43266  |   0.395047 |
| Bori_Aron_solution-1 |     0.715381 |       0.544981 |   0.501285 |
| k-d_tree_pandas      |     0.726312 |       0.405    |   0.553783 |
| k-d_tree_sklearn     |     0.734881 |       0.909293 |   0.697464 |

## Inputs: 250000, Queries 500

| solution             |   setup_time |   preproc_time |   run_time |
|:---------------------|-------------:|---------------:|-----------:|
| barab-szabi-2        |     0.731758 |       0.446287 |   0.403378 |
| k-d_tree_polars      |     0.725749 |       0.541105 |   0.49188  |
| barab-szabi-1        |     0.725921 |       0.538401 |   0.505598 |
| Bori_Aron_solution-1 |     0.721257 |       0.735657 |   0.51187  |
| k-d_tree_pandas      |     0.729789 |       0.487627 |   0.691942 |
| k-d_tree_sklearn     |     0.73741  |       1.13632  |   0.765813 |

## Inputs: 1000000, Queries 1000

| solution             |   setup_time |   preproc_time |   run_time |
|:---------------------|-------------:|---------------:|-----------:|
| barab-szabi-2        |     0.732679 |       0.690819 |   0.448302 |
| Bori_Aron_solution-1 |     0.715057 |       1.36591  |   0.537469 |
| k-d_tree_polars      |     0.733279 |       0.868714 |   0.84001  |
| k-d_tree_sklearn     |     0.788556 |       1.93943  |   0.858075 |
| barab-szabi-1        |     0.726966 |       0.86356  |   0.880173 |
| k-d_tree_pandas      |     0.727688 |       0.761734 |   1.13243  |

## Inputs: 10000000, Queries 1000

| solution             |   setup_time |   preproc_time |   run_time |
|:---------------------|-------------:|---------------:|-----------:|
| Bori_Aron_solution-1 |     0.720403 |       10.8018  |   0.799615 |
| barab-szabi-2        |     0.725954 |        5.47597 |   0.818976 |
| k-d_tree_sklearn     |     0.73414  |       16.3376  |   1.0642   |
| barab-szabi-1        |     0.731269 |        5.04162 |   6.61982  |
| k-d_tree_polars      |     0.736632 |        4.93741 |   6.67116  |
| k-d_tree_pandas      |     0.728878 |        4.01032 |   6.97421  |

## Inputs: 100000000, Queries 10000

| solution             |   setup_time |   preproc_time |   run_time |
|:---------------------|-------------:|---------------:|-----------:|
| barab-szabi-2        |     0.857744 |        77.0342 |    4.05544 |
| k-d_tree_sklearn     |     0.740434 |       243.26   |    5.21861 |
| Bori_Aron_solution-1 |     0.820652 |       146.05   |   17.0494  |