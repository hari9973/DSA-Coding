import sys
import math
from collections import Counter, defaultdict, deque
from bisect import bisect_left, bisect_right
from heapq import heapify, heappop, heappush

class Solution:
    def findDisappearedNumbers(self, nums: list[int], lower: int, upper: int) -> list[list[int]]:
        arr_values = set(nums)
        ans = []
        first = None
        prev = None
        for x in range(lower, upper+1):
            if x in arr_values:
                if prev is not None:
                    ans.append([first, prev])
                    first = None
                    prev = None
            else:
                if first is None:
                    first = x
                    prev = x
                else:
                    prev = x
        if first is not None and prev is not None:
            ans.append([first, prev])
        return ans


if __name__ == "__main__":
    sol = Solution()

    arr = [int(x) for x in input().split()]
    lower = int(input().strip())
    upper = int(input().strip())
    
    result = sol.findDisappearedNumbers(arr, lower, upper)
    print(result)
