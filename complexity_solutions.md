## Free code

1. O(N + M), we do two separate for loops, it should be the maximum of them.
2. O(N^2), we do two nested for loops, it should be the multipcation of them.
3. O(N*logN), we are incrementing i by 1 and multiplying j by 2 in each respective for loop.
4. O(logN), we are multiplying i by 2 in each step.

## Searching

1. Best is O(1), first element is the element that we are looking for. Worst is O(N), element that we are looking for does not exist, we need to check every element in the list. It should be linear.
2. Use binary search. Then, it will be logarithmic. We can search one half of the array every time.
3. It is constant. Maximum element in a **sorted** list is the last element. 

## The Devil in the Permutations

For Sadra's solution below:

```
def get_permutations(sequence):
  if len(sequence) == 1:
    return [sequence]
  all_but_first = get_permutations(sequence[1:])
  all_permutations = []
  for permutation in all_but_first:
    for index in range(len(permutation) + 1):
      new_permutation = permutation[:index] + sequence[0] + permutation[index:]
      all_permutations.append(new_permutation)
  return all_permutations
```

> T(n) = T(n-1) + n!
>      = T(n-2) + (n-1)! + n!
>      = ...
>      = 1 + 2! + ... + (n-1)! + n!

where O(n*n!) is a clear upperbound.

## Math is fun!

1. O(N) because we are calling the function N times. (Doesn't this algorithm look like factorial code?)
2. O(logN) because every time we take square of the number, we reduce the total number of function calls by half.

## Duplicates

Check complexity_solutions.py file.

## Random Question

Check complexity_solutions.py file.