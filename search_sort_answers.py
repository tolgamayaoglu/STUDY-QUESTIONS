import random

# Question 1
# Time complexity: O(n + k) where k is maximum possible element
def counting_sort(lst):
  sorted_lst = []
  aux = [0 for i in range(101)]
  for elt in lst:
    aux[elt] += 1
  for i, elt_count in enumerate(aux):
    for _ in range(elt_count):
      sorted_lst.append(i)
  return sorted_lst

# Question 2
# Time complexity: O(log(n))
def ternary_search(lst, target):
  return ternary_search_helper(0, len(lst) - 1, target, lst)

def ternary_search_helper(l, r, target, lst):
  if (r >= l):

    # Find the mid1 and mid2
    mid1 = l + (r - l) // 3
    mid2 = r - (r - l) // 3

    # Check if key is present at any mid
    if (lst[mid1] == target): 
      return mid1
      
    if (lst[mid2] == target): 
      return mid2
      
    # Since key is not present at mid,
    # check in which region it is present
    # then repeat the Search operation
    # in that region
    if (target < lst[mid1]): 

      # The key lies in between l and mid1
      return ternary_search_helper(l, mid1 - 1, target, lst)
      
    elif (target > lst[mid2]): 

      # The key lies in between mid2 and r
      return ternary_search_helper(mid2 + 1, r, target, lst)
      
    else: 

      # The key lies in between mid1 and mid2
      return ternary_search_helper(mid1 + 1, mid2 - 1, target, lst)
  # Key not found
  return -1
      

# Question 3
# Time complexity: O(n^2)
def insertion_sort(lst):
  for i in range(1, len(lst)):
    key = lst[i]
    j = i - 1
    while j >= 0 and key < lst[j]:
      lst[j+1] = lst[j]
      j -= 1
    lst[j+1] = key

# Question 4
# Time complexity: O(log(n+k))
def nary_search(lst, target, n):
  return nary_search_helper(0, len(lst) - 1, target, lst, n)

def nary_search_helper(l, r, target, lst, n):
  if (r >= l):

    # Find the mid1 and mid2
    mid_list = []
    for i in range(1, n):
      mid_list.append(l + (r - l) * i // n)

    # Check if key is present at any mid
    for ind in mid_list:
      if lst[ind] == target:
        return ind
      
    # Since key is not present at mid,
    # check in which region it is present
    # then repeat the Search operation
    # in that region
    if target < lst[mid_list[0]]:
      return nary_search_helper(l, mid_list[0] - 1, target, lst, n)
    if target > lst[mid_list[-1]]:
      return nary_search_helper(mid_list[-1] + 1, r, target, lst, n)
    for i in range(len(mid_list) - 1):
      if lst[mid_list[i]] < target and lst[mid_list[i+1]] > target:
        return nary_search_helper(mid_list[i] + 1, mid_list[i+1] - 1, target, lst, n)
  # Key not found
  return -1

# Question 5
# Time complexity: O(n/jump + log(jump))
def jumping_binary_search(sorted_lst, target, jump):
  index = -1
  prev = 0
  nxt = jump
  while sorted_lst[int(min(nxt, len(sorted_lst))-1)] < target:
    prev = nxt
    nxt += jump
    if prev >= len(sorted_lst):
      return -1
  
  # Using the code from question 4. You could also just implement binary search
  return prev + nary_search(sorted_lst[prev:nxt], target, 2)

# This function generates lists of random integers, you can use it to test your sorting code if you wish
def random_list(n=10):
  return [random.randint(0, 100) for i in range(n)]

# This function generates a sorted list of a given size (10 by default). You can use it to test your searching function if you wish
def sorted_list(n=10):
  return sorted(random_list(n))