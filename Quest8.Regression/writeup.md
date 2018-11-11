# Quest 8. Regression Transpose

# Hypothesis

Here are the function implementations for individual transpose method

**Matrix Definition**
```python
given an n x m matrix

matrix = [ [1,2,3], 
           [4,5,6], 
           [7,8,9] ]

Where n = number of rows
      m = number of elements in a row = number of columns

```


**Simple**
```python
[[matrix[j][i] for j in range(len(matrix))] for i in range(len(matrix[0]))]
```
This is using list comprehension. Inner list containing for j, will create a list element with length equal to number of the rows in the matrix. Outer list repeats this for as many times as the number of columns, or the number of elements in the initial matrix's rows. 

Time Complexity of this is $O(nm) = O(n^2) | n = m$

**Zip**
```python
zip(*matrix)
```
This is a cool way of using advnaced python function zip. Since the implementation shows no implementation, I cannot guess its time complexity.

**Numpy**
```python
import numpy as np
np.transpose(marix)
```
This is standard numpy implementation. It shows no implementation so I cannot guess its time complexity, but knowing the optimizations being done in other numpy functions I can assume that it will have faster than list comprehension.

# Results


# Graphs



# Conclusion