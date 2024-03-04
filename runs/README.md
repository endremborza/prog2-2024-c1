# 2024-03-04

## Inputs: 1000, Queries 20

| solution             |   setup_time |   preproc_time |   run_time |
|:---------------------|-------------:|---------------:|-----------:|
| barab-szabi-1        |     1.66944  |       0.397949 |   0.359134 |
| k-d_tree_polars      |     1.66126  |       0.419673 |   0.37002  |
| barab-szabi-2        |     0.754725 |       0.37781  |   0.378997 |
| k-d_tree_pandas      |     1.64573  |       0.377946 |   0.500866 |
| Bori_Aron_solution-1 |     1.60072  |       0.510279 |   0.518994 |
| solution-1           |     9.39791  |       1e-06    |   0.884658 |
| k-d_tree_sklearn     |    12.0442   |       2.03962  |   0.991146 |

## Inputs: 10000, Queries 50

| solution             |   setup_time |   preproc_time |   run_time |
|:---------------------|-------------:|---------------:|-----------:|
| barab-szabi-2        |     0.745601 |       0.377281 |   0.373215 |
| barab-szabi-1        |     0.768847 |       0.428301 |   0.37877  |
| k-d_tree_polars      |     0.763937 |       0.441732 |   0.390865 |
| k-d_tree_pandas      |     0.745406 |       0.407011 |   0.53588  |
| Bori_Aron_solution-1 |     0.752749 |       0.544674 |   0.536099 |
| k-d_tree_sklearn     |     0.765851 |       0.906324 |   0.687021 |

## Inputs: 50000, Queries 200

| solution             |   setup_time |   preproc_time |   run_time |
|:---------------------|-------------:|---------------:|-----------:|
| barab-szabi-2        |     0.72152  |       0.375639 |   0.366912 |
| k-d_tree_polars      |     0.722589 |       0.429258 |   0.395504 |
| barab-szabi-1        |     0.728214 |       0.431485 |   0.398747 |
| Bori_Aron_solution-1 |     0.713237 |       0.544902 |   0.496584 |
| k-d_tree_pandas      |     0.729226 |       0.401058 |   0.557453 |
| k-d_tree_sklearn     |     0.756294 |       0.902709 |   0.708484 |

## Inputs: 250000, Queries 500

| solution             |   setup_time |   preproc_time |   run_time |
|:---------------------|-------------:|---------------:|-----------:|
| barab-szabi-2        |     0.724307 |       0.441487 |   0.401793 |
| k-d_tree_polars      |     0.730844 |       0.540216 |   0.488752 |
| barab-szabi-1        |     0.728697 |       0.540722 |   0.499792 |
| Bori_Aron_solution-1 |     0.71348  |       0.726567 |   0.511432 |
| k-d_tree_pandas      |     0.732778 |       0.484509 |   0.682765 |
| k-d_tree_sklearn     |     0.735751 |       1.11147  |   0.753321 |

## Inputs: 1000000, Queries 1000

| solution             |   setup_time |   preproc_time |   run_time |
|:---------------------|-------------:|---------------:|-----------:|
| barab-szabi-2        |     0.724678 |       0.693135 |   0.449254 |
| Bori_Aron_solution-1 |     0.716556 |       1.36176  |   0.53543  |
| k-d_tree_polars      |     0.726615 |       0.863387 |   0.836423 |
| k-d_tree_sklearn     |     0.733879 |       1.98134  |   0.851004 |
| barab-szabi-1        |     0.731792 |       0.869941 |   0.869672 |
| k-d_tree_pandas      |     0.725352 |       0.752942 |   1.11554  |

## Inputs: 10000000, Queries 1000

| solution             |   setup_time |   preproc_time |   run_time |
|:---------------------|-------------:|---------------:|-----------:|
| Bori_Aron_solution-1 |     0.711364 |       10.6776  |   0.792928 |
| barab-szabi-2        |     0.737486 |        5.24676 |   0.811052 |
| k-d_tree_sklearn     |     0.730068 |       15.5671  |   1.05783  |
| k-d_tree_polars      |     0.725028 |        4.96668 |   6.37854  |
| barab-szabi-1        |     0.731367 |        4.96653 |   6.40311  |
| k-d_tree_pandas      |     0.728621 |        3.87797 |   6.72988  |

## Inputs: 100000000, Queries 10000

| solution             |   setup_time |   preproc_time |   run_time |
|:---------------------|-------------:|---------------:|-----------:|
| barab-szabi-2        |     0.907966 |        69.5021 |    4.09509 |
| k-d_tree_sklearn     |     0.732691 |       225.724  |    5.17388 |
| Bori_Aron_solution-1 |     0.823364 |       139.524  |   18.3568  |