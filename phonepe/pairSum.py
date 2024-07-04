""" 
Problem statement
You are given an integer array 'ARR' of size 'N' and an integer 'S'. Your task is to return the list of all pairs of elements such that each sum of elements of each pair equals 'S'.

Note:

Each pair should be sorted i.e the first value should be less than or equals to the second value. 

Return the list of pairs sorted in non-decreasing order of their first value. In case if two pairs have the same first value, the pair with a smaller second value should come first.
Detailed explanation ( Input/output format, Notes, Images )
Constraints:
1 <= N <= 10^3
-10^5 <= ARR[i] <= 10^5
-2 * 10^5 <= S <= 2 * 10^5

Time Limit: 1 sec
Sample Input 1:
5 5
1 2 3 4 5
Sample Output 1:
1 4
2 3
Explaination For Sample Output 1:
Here, 1 + 4 = 5
      2 + 3 = 5
Hence the output will be, (1,4) , (2,3).
Sample Input 2:
5 0
2 -3 3 3 -2
Sample Output 2:
-3 3
-3 3
-2 2
"""


from os import *
from sys import *
from collections import *
from math import *

def pairSum(arr, s):
    # make a result array
    res = []
    # for i in range len of original arr
    for i in range(len(arr)):
        # for j in range of i+1 and len of original array
        for j in range(i+1, len(arr)):
            # if i + j == s
            if arr[i] + arr[j] == s:
                # get the min and get the max as it want the res pair in sorted order, and append it to the array
                res.append([ min(arr[i], arr[j]), max(arr[i], arr[j]) ])
    
    # sort the resultant array
    res.sort()
    return res