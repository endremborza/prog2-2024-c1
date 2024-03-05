# 2024-03-05

## Inputs: 1000, Queries 20

| solution             |   setup_time |   preproc_time |   run_time |
|:---------------------|-------------:|---------------:|-----------:|
| barab-szabi-2        |     0.73607  |       0.361671 |   0.357657 |
| barab-szabi-1        |     0.736069 |       0.404472 |   0.361464 |
| k-d_tree_polars      |     0.736386 |       0.400414 |   0.363228 |
| solution-1           |     8.15469  |       1e-06    |   0.364615 |
| Bori_Aron_solution-1 |     0.718318 |       0.50616  |   0.500941 |
| k-d_tree_pandas      |     0.737482 |       0.394615 |   0.511511 |
| k-d_tree_sklearn     |    10.3273   |       1.16925  |   0.684405 |

## Inputs: 10000, Queries 50

| solution             |   setup_time |   preproc_time |   run_time |
|:---------------------|-------------:|---------------:|-----------:|
| barab-szabi-2        |     0.734416 |       0.36822  |   0.356683 |
| barab-szabi-1        |     0.737464 |       0.408217 |   0.368788 |
| k-d_tree_polars      |     0.732768 |       0.408633 |   0.373109 |
| k-d_tree_pandas      |     0.732684 |       0.388802 |   0.519123 |
| Bori_Aron_solution-1 |     0.719145 |       0.503752 |   0.520593 |
| k-d_tree_sklearn     |     0.747683 |       0.863084 |   0.674507 |

## Inputs: 50000, Queries 200

| solution             |   setup_time |   preproc_time |   run_time |
|:---------------------|-------------:|---------------:|-----------:|
| barab-szabi-2        |     0.734248 |       0.395289 |   0.376271 |
| barab-szabi-1        |     0.732571 |       0.443093 |   0.399509 |
| k-d_tree_polars      |     0.748438 |       0.455584 |   0.404044 |
| Bori_Aron_solution-1 |     0.766588 |       0.562116 |   0.509268 |
| k-d_tree_pandas      |     0.741173 |       0.408436 |   0.567743 |
| k-d_tree_sklearn     |     0.74382  |       0.92446  |   0.710267 |

## Inputs: 250000, Queries 500

| solution             |   setup_time |   preproc_time |   run_time |
|:---------------------|-------------:|---------------:|-----------:|
| barab-szabi-2        |     0.734305 |       0.448723 |   0.406828 |
| k-d_tree_polars      |     0.740059 |       0.546302 |   0.497658 |
| barab-szabi-1        |     0.7406   |       0.567647 |   0.507528 |
| Bori_Aron_solution-1 |     0.725195 |       0.732432 |   0.527051 |
| k-d_tree_pandas      |     0.739673 |       0.484276 |   0.687342 |
| k-d_tree_sklearn     |     0.747341 |       1.13321  |   0.762598 |

## Inputs: 1000000, Queries 1000

| solution             |   setup_time |   preproc_time |   run_time |
|:---------------------|-------------:|---------------:|-----------:|
| barab-szabi-2        |     0.733493 |       0.697952 |   0.464922 |
| Bori_Aron_solution-1 |     0.714768 |       1.39469  |   0.557016 |
| k-d_tree_polars      |     0.734968 |       0.86238  |   0.849638 |
| k-d_tree_sklearn     |     0.739243 |       1.98762  |   0.874015 |
| barab-szabi-1        |     0.74215  |       0.871846 |   0.888248 |
| k-d_tree_pandas      |     0.735907 |       0.765349 |   1.11427  |

## Inputs: 10000000, Queries 1000

| solution             |   setup_time |   preproc_time |   run_time |
|:---------------------|-------------:|---------------:|-----------:|
| Bori_Aron_solution-1 |     0.727573 |       10.6757  |   0.800302 |
| barab-szabi-2        |     0.739616 |        5.28375 |   0.813586 |
| k-d_tree_sklearn     |     0.737772 |       15.9102  |   1.07226  |
| k-d_tree_polars      |     0.734552 |        5.05418 |   6.51431  |
| barab-szabi-1        |     0.736747 |        4.91693 |   6.55497  |
| k-d_tree_pandas      |     0.732639 |        3.98861 |   6.87984  |

## Inputs: 100000000, Queries 10000

| solution             |   setup_time |   preproc_time |   run_time |
|:---------------------|-------------:|---------------:|-----------:|
| barab-szabi-2        |     0.923427 |         71.521 |    4.16082 |
| k-d_tree_sklearn     |     0.735948 |        229.929 |    5.01536 |
| Bori_Aron_solution-1 |     0.800256 |        143.253 |   16.7799  |