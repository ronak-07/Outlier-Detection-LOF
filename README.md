
Outlier Detetction (LOF)
===========
The LOF algorithm is an unsupervised density based outlier detection method which computes the local density deviation of a given data point with respect to its neighbors. It considers as outlier samples that have a substantially lower density than their neighbors.

Steps Involved
----------------
- Step 1: Calculation of distance between every two data points
- Step 2: Calculation of the distance between each point and its kth nearest neighbour [distk(o)]
- Step 3: Calculation of k-distance neighbourhood of each point.
- Step 4: Calculation of local reachability density (LRD).
- Step 5: Calculation of LOFk(o).
- Step 6: Sort the LOFk(o) in descending order and pick the top n outliers.

Results
-------------

k=100

![For k=100](https://github.com/ronak-07/Outlier-Detection-LOF-/blob/master/100.png)

k=300

![For k=300](https://github.com/ronak-07/Outlier-Detection-LOF-/blob/master/300.png)

Contributors
-------------
[Ronak Sisodia](https://github.com/ronak-07)
