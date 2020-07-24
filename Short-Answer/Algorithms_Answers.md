#### Please add your answers to the **_Analysis of Algorithms_** exercises here.

## Exercise I

a) n - cancel n's with n's then your left with one n in the while loop. While loop is like a for loop and its based off an input so therefore its O(n)

b) n log(n) - for loop outside takes in a input so its automatically n. Meanwhile, the nested while loop is not iterating + 1, its skipping \* 2 so its log n.

c) n - recursive is similar to a for loop so and we wont return until it hits 0.

## Exercise II

I might not be understanding this problem correctly but....

First of all, assuming f was either giving or there was some sort of formula to calculate it.

I would take in an array of the number of stories of the building, assuming its already sorted, do a binary search to see when the eggs break in order to minimize the number of eggs dropped and eggs broken as opposed to a linear approach.

Solution would be log n
