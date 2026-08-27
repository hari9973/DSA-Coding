import sys
import math
from collections import Counter, defaultdict, deque
from bisect import bisect_left, bisect_right
from heapq import heapify, heappop, heappush

class Solution:
    def isPalindromic(self, s: str) -> bool:
        binary_output = "".join(f"{ord(char):08b}" for char in s)
        return binary_output == binary_output[::-1]

if __name__ == "__main__":
    sol = Solution()

    user_input = input().strip()
    
    result = sol.isPalindromic(user_input)
    print(result)
