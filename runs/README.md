# 2024-03-02

## Inputs: 1000, Queries 20

| solution             |   setup_time |   preproc_time |   run_time |
|:---------------------|-------------:|---------------:|-----------:|
| barab-szabi-2        |     0.763725 |       0.376371 |   0.365789 |
| k-d_tree_polars      |     0.777605 |       0.420375 |   0.385994 |
| barab-szabi-1        |     0.786449 |       0.433473 |   0.397121 |
| solution-1           |     9.08496  |       1e-06    |   0.40012  |
| Bori_Aron_solution-1 |     0.733842 |       0.52228  |   0.512802 |
| k-d_tree_pandas      |     0.787365 |       0.408247 |   0.535272 |
| k-d_tree_sklearn     |    11.3474   |       1.02198  |   0.736955 |

## Inputs: 10000, Queries 50

| solution             |   setup_time |   preproc_time |   run_time |
|:---------------------|-------------:|---------------:|-----------:|
| k-d_tree_polars      |     0.734681 |       0.419302 |   0.37014  |
| barab-szabi-1        |     0.75724  |       0.421669 |   0.375349 |
| barab-szabi-2        |     0.742947 |       0.375273 |   0.38599  |
| Bori_Aron_solution-1 |     0.737583 |       0.526048 |   0.510459 |
| k-d_tree_pandas      |     0.747759 |       0.390709 |   0.526149 |
| k-d_tree_sklearn     |     0.768901 |       0.893975 |   0.682858 |

## Inputs: 50000, Queries 200

| solution             |   setup_time |   preproc_time |   run_time |
|:---------------------|-------------:|---------------:|-----------:|
| barab-szabi-2        |     0.75357  |       0.404608 |   0.396356 |
| k-d_tree_polars      |     0.766771 |       0.451476 |   0.400921 |
| barab-szabi-1        |     0.74885  |       0.447679 |   0.404044 |
| Bori_Aron_solution-1 |     0.762914 |       0.571592 |   0.525005 |
| k-d_tree_pandas      |     0.750719 |       0.413422 |   0.608787 |
| k-d_tree_sklearn     |     0.751426 |       0.92679  |   0.722719 |

## Inputs: 250000, Queries 500

| solution             |   setup_time |   preproc_time |   run_time |
|:---------------------|-------------:|---------------:|-----------:|
| barab-szabi-2        |     0.75446  |       0.44614  |   0.408017 |
| k-d_tree_polars      |     0.752134 |       0.556636 |   0.498363 |
| barab-szabi-1        |     0.744292 |       0.559335 |   0.523563 |
| Bori_Aron_solution-1 |     0.743188 |       0.754026 |   0.549375 |
| k-d_tree_pandas      |     0.752389 |       0.510159 |   0.719022 |
| k-d_tree_sklearn     |     0.776496 |       1.16362  |   0.794872 |

## Inputs: 1000000, Queries 1000

| solution             |   setup_time |   preproc_time |   run_time |
|:---------------------|-------------:|---------------:|-----------:|
| barab-szabi-2        |     0.73366  |       0.699719 |   0.457073 |
| Bori_Aron_solution-1 |     0.74094  |       1.40209  |   0.545297 |
| k-d_tree_polars      |     0.755019 |       0.89473  |   0.858626 |
| k-d_tree_sklearn     |     0.752421 |       2.02559  |   0.900082 |
| barab-szabi-1        |     0.763366 |       0.886887 |   0.904611 |
| k-d_tree_pandas      |     0.75677  |       0.785685 |   1.17277  |

## Inputs: 10000000, Queries 1000

| solution             |   setup_time |   preproc_time |   run_time |
|:---------------------|-------------:|---------------:|-----------:|
| Bori_Aron_solution-1 |     0.7216   |       11.1774  |   0.83941  |
| barab-szabi-2        |     0.774897 |        5.90557 |   0.905877 |
| k-d_tree_sklearn     |     0.737616 |       17.48    |   1.08317  |
| k-d_tree_polars      |     0.737932 |        5.08293 |   6.67422  |
| k-d_tree_pandas      |     0.783246 |        4.00459 |   6.87773  |
| barab-szabi-1        |     0.737288 |        5.2512  |   7.22239  |

## Inputs: 100000000, Queries 10000

| solution             |   setup_time |   preproc_time |   run_time |
|:---------------------|-------------:|---------------:|-----------:|
| barab-szabi-2        |     0.975066 |        78.1161 |    4.03563 |
| k-d_tree_sklearn     |     0.800445 |       245.458  |    5.39528 |
| Bori_Aron_solution-1 |     0.828803 |       149.62   |   16.5194  |