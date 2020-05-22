#### Please add your answers to the ***Analysis of  Algorithms*** exercises here.

## Exercise I

a)Line 1 and 3 are constants 
Line 2 while loop will run n^3 more times.Will get big very quick as n increases.
Quadratic Time complexity because of the O(n^3). 


b)O(n), because as n increases by 1 the loop will run n more times


c)bunnies = 3
4 + 2 
bunnies = 2  
2 + 2 
bunnies =1 
0 + 2 
bunnies =0 
0

As the input of "bunnies" increases the runtime increases by the same amount b/c each operation is the same, which makes it O(n) time complexity. 

## Exercise II

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


