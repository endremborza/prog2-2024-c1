# 2024-03-01

## Inputs: 1000, Queries 20

| solution             |   setup_time |   preproc_time |   run_time |
|:---------------------|-------------:|---------------:|-----------:|
| k-d_tree_polars      |     0.779459 |       0.412243 |   0.372474 |
| barab-szabi-1        |     0.746216 |       0.420666 |   0.376634 |
| barab-szabi-2        |     0.750343 |       0.690002 |   0.380755 |
| Bori_Aron_solution-1 |     0.742081 |       0.536285 |   0.51906  |
| k-d_tree_pandas      |     0.753624 |       0.408869 |   0.539212 |
| solution-1           |     9.76992  |       1e-06    |   0.700719 |
| k-d_tree_sklearn     |    15.7304   |       1.4299   |   0.800582 |

## Inputs: 10000, Queries 50

| solution             |   setup_time |   preproc_time |   run_time |
|:---------------------|-------------:|---------------:|-----------:|
| barab-szabi-2        |     0.761172 |       0.377934 |   0.37096  |
| k-d_tree_polars      |     0.760826 |       0.430971 |   0.382627 |
| barab-szabi-1        |     0.753989 |       0.42532  |   0.386647 |
| Bori_Aron_solution-1 |     0.738528 |       0.533941 |   0.531445 |
| k-d_tree_pandas      |     0.764176 |       0.407558 |   0.544888 |
| k-d_tree_sklearn     |     0.773538 |       0.919856 |   0.715688 |

## Inputs: 50000, Queries 200

| solution             |   setup_time |   preproc_time |   run_time |
|:---------------------|-------------:|---------------:|-----------:|
| barab-szabi-2        |     0.749421 |       0.387151 |   0.379839 |
| k-d_tree_polars      |     0.755088 |       0.445439 |   0.397617 |
| barab-szabi-1        |     0.744662 |       0.44583  |   0.406131 |
| Bori_Aron_solution-1 |     0.72907  |       0.560898 |   0.519479 |
| k-d_tree_pandas      |     0.744463 |       0.411385 |   0.575994 |
| k-d_tree_sklearn     |     0.750471 |       0.938659 |   0.733724 |

## Inputs: 250000, Queries 500

| solution             |   setup_time |   preproc_time |   run_time |
|:---------------------|-------------:|---------------:|-----------:|
| barab-szabi-2        |     0.74803  |       0.449866 |   0.458002 |
| k-d_tree_polars      |     0.743336 |       0.549561 |   0.497633 |
| barab-szabi-1        |     0.757621 |       0.561295 |   0.515261 |
| Bori_Aron_solution-1 |     0.736222 |       0.742616 |   0.524845 |
| k-d_tree_pandas      |     0.743819 |       0.495678 |   0.704806 |
| k-d_tree_sklearn     |     0.751595 |       1.16182  |   0.784055 |

## Inputs: 1000000, Queries 1000

| solution             |   setup_time |   preproc_time |   run_time |
|:---------------------|-------------:|---------------:|-----------:|
| barab-szabi-2        |     0.744435 |       0.72654  |   0.48205  |
| Bori_Aron_solution-1 |     0.735431 |       1.39647  |   0.55681  |
| k-d_tree_sklearn     |     0.75111  |       2.00865  |   0.871579 |
| k-d_tree_polars      |     0.740917 |       0.862934 |   0.882463 |
| barab-szabi-1        |     0.746464 |       0.88075  |   0.921904 |
| k-d_tree_pandas      |     0.755725 |       0.758395 |   1.13897  |

## Inputs: 10000000, Queries 1000

| solution             |   setup_time |   preproc_time |   run_time |
|:---------------------|-------------:|---------------:|-----------:|
| Bori_Aron_solution-1 |     0.738673 |       10.9038  |   0.800371 |
| barab-szabi-2        |     0.749084 |        5.61908 |   0.817069 |
| k-d_tree_sklearn     |     0.750899 |       16.4861  |   1.06181  |
| barab-szabi-1        |     0.731839 |        4.92076 |   6.63852  |
| k-d_tree_polars      |     0.7298   |        5.04121 |   6.91537  |
| k-d_tree_pandas      |     0.759095 |        3.99651 |   6.95114  |

## Inputs: 100000000, Queries 10000

| solution             |   setup_time |   preproc_time |   run_time |
|:---------------------|-------------:|---------------:|-----------:|
| barab-szabi-2        |     0.915136 |        71.2394 |    4.05425 |
| k-d_tree_sklearn     |     0.761434 |       231.472  |    5.18483 |
| Bori_Aron_solution-1 |     0.846219 |       146.653  |   15.2745  |