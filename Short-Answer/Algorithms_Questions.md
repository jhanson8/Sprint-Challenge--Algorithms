# Analysis of Algorithms

## Exercise I

Give an analysis of the running time of each snippet of
pseudocode with respect to the input size n of each of the following:

```
python
a)  a = 0 #O(1)
    while (a < n * n * n): #O(n^3)
      a = a + n * n #O(1)
```
Line 1 and 3 are constants 
Line 2 while loop will run n^3 more times.Will get big very quick as n increases.
Quadratic Time complexity because of the O(n^3). 


```
b)  sum = 0 #O(1)
    for i in range(n): 
      j = 1 #O(1)
      while j < n: 
        j *= 2
        sum += 1

```
O(n), because as n increases by 1 the loop will run n more times

```
c)  def bunnyEars(bunnies): #O(n)
      if bunnies == 0:  #O(1)
        return 0        #O(1)

      return 2 + bunnyEars(bunnies-1) #O(n)
```

bunnies = 3
4 + 2 
bunnies = 2  
2 + 2 
bunnies =1 
0 + 2 
bunnies =0 
0

As the input of "bunnies" increases the runtime increases by the same amount b/c each operation is the same, which makes it O(n) time complexity. 

## Exercise II

Suppose that you have an n-story building and plenty of eggs. Suppose also that an egg gets broken if it is thrown off floor f or higher, and doesn't get broken if dropped off a floor less than floor f. Devise a strategy to determine the value of f such that the number of dropped + broken eggs is minimized.

Write out your proposed algorithm in plain English or pseudocode AND give the runtime complexity of your solution.

n story building 
x number of eggs 
for i in eggs:
  if thrown > f:
    x -= 1
  if thrown < f:
    return x 

Binary Search Strategy: 
  We can throw the first egg off at n/2
    if it breaks we can try (n/2)/2 
      keep cutting in half until it does not break 
      then go up by 1.5 the cur num until 

    if it does not break we can try (n/2) * 1.5 
      keep cutting in half up until the egg breaks 
      then go down until it does not 
  
  O(log n) b/c we are cutting the possible answers in half every time (binary tree) so it will flatten out.
