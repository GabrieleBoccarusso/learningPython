"""
Note: this is an implementation in python of the solution of
this problemin cpp: https://www.youtube.com/watch?v=XKu_SEDAykw,
copied here in javascript: https://replit.com/@aneagoie/containsCommonItem
"""
"""
Given 2 arrays, create a function that let's a user know (true/false) whether these two arrays contain any common items
For Example:
const array1 = ['a', 'b', 'c', 'x'];//const array2 = ['z', 'y', 'i'];
should return false.
-----------
const array1 = ['a', 'b', 'c', 'x'];//const array2 = ['z', 'y', 'x'];
should return true.
"""

# the first solution is to compare every element of the first array with the every element of the second one

arr1 = ['a', 'b', 'c', 'x']
arr2 = ['z', 'y', 'x']

# test case:
# arr1 = ['a', 'b', 'c', 'x', None]
# arr2 = ['z', 'y', None]

def checkCommonPairs(arr1, arr2):
  answer = False;
  i: int = 0 # first array iterator
  j : int = 0 # second array iterator

  for i in range(len(arr1)):
    for j in range(len(arr2)):
      if arr1[i] == arr2[j]:
        answer = True
        break # we put the break to make the code a bit efficient
              # despite making it being spaghetti code
  return answer

answer1: bool = checkCommonPairs(arr1, arr2)
print(f'using the first function: {answer1}')

# but this solution is not efficient, this because it has
# two nested arrays, making it a O(a * b) algorithm,
# which is O(n^2).
# a better way is touse hash tables

def checkCommonPairs2 (arr1, arr2):
  answer: bool = False
  hash_table = {}
  i: int = 0 # array iterator

  for i in range(len(arr1)):
    if arr1[i] not in hash_table:
      hash_table[arr1[i]] = True

  i = 0

  for i in range(len(arr2)):
    if arr2[i] in hash_table:
      answer = True
      break # spaghetti code
  
  return answer

answer2: bool = checkCommonPairs2(arr1, arr2)
print(f'using the first function: {answer2}')

# this is better than the first one because
# are two loop one after the other,
# making the algorithm O(a + b), then O(n)