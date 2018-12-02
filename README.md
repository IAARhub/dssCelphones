# Decision-Support System to select best celphone.
This is a simple example of prescriptive analytics. In this case we implemented AHP and TOPSIS in python to help a human selecting a phone within an array of 10k celphone options based on a given budget.

## Autor

* Patricio J. Gerpe

## Tech stack

* Python 2.7

## Libraries:

* Numpy

## Running...
`python celphones.py`

## How it works?
We have a random-made dataset made of 10,000 of celphones with different features such as : Price, Camera MP and Use life.
The program simply takes user input on the preferences over these criteria by applying a Saaty-scale[1] survey.
Weight is calculated via the algorithm AHP (Analytic Hierachical Process)[1].

**AHP** works the following way:
1. Subjective judgments data collected from the survey is computed in a nxn matrix, where n is the number of criterias.
2. We compute the sum of each column needed to calculate the normalised criteria matrix.
3. Once we calculated the normalised criteria matrix, we compute the aritmethic mean of each row, which will give us the eighen vector. (This vector indicates us the weighting of each criteria)

Once we have the weights of each criteria we implement **TOPSIS**[3] algorithm.

That algorithm works the following way:

1. A decision matrix is defined representing alternatives (rows) and criterias (columns).
2. We compute the norm of each column, which we will use to normalise the matrix.
3. Once we computed the normalised decision matrix, we multiply that matrix with the eighen vector. That returns us the weighted normalised decision matrix.
4. We calculate the ideal solution. (By selecting values of the set of alternatives that are maximising benefitial criteria and minimising cost criteria).
5. We calculate the anti-ideal solution. (By selecting values of the set of alternatives that are minimising benefitial criteria and maximising cost criteria).
6. For each alternative we compute the euclidean distance from the ideal and anti-ideal solution.
![](https://i.stack.imgur.com/tQdee.png)
7. For each alternative we compute the performance score. (It is the distance from anti-ideal solution divided by the sum of the distance to ideal and anti-ideal solution)
![](https://i.stack.imgur.com/DRdj6.png)
8. We rank the options in descending order according to performance score.

Once we have the rank we checked if the alternative is within the range of our user. If not we iterate until finding the best affordable solution.

## Resources
* Numpy documentation. Retrieved from https://docs.scipy.org/doc/numpy-1.15.0

## References
* [1] Saaty, T. L. (1986). Axiomatic Foundation of the Analytic Hierarchy Process. Management Science, 32(7), 841. doi:10.1287/mnsc.32.7.841
* [2] Saaty, R. W. (1987). The analytic hierarchy process—what it is and how it is used. Mathematical Modelling, 9(3-5), 167. doi:10.1016/0270-0255(87)90473-8
* [3] Hwang, C.L.; Yoon, K. (1981). Multiple Attribute Decision Making: Methods and Applications. New York: Springer-Verlag.
