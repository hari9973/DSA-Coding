import sys
import math
from collections import Counter, defaultdict, deque
from bisect import bisect_left, bisect_right
from heapq import heapify, heappop, heappush

class Solution:
    def get_prime_factors(self, n):
        factors = []

        while n % 2 == 0:
            factors.append(2)
            n //= 2
        
        factor = 3
        while factor * factor <= n:
            while n % factor == 0:
                factors.append(factor)
                n //= factor
            factor += 2
        
        if n > 1:
            factors.append(n)
        return factors

    def longestSubarray(self, nums: list[int], k: int) -> int:
        left = 0
        right = 0
        cache_prime_factors = {}
        distinct_prime_factors = {}
        max_subarray = 0
        for x in nums:
            prime_factors = None
            if x in cache_prime_factors:
                prime_factors = cache_prime_factors.get(x)
            else:
                prime_factors = list(set(self.get_prime_factors(x)))
                cache_prime_factors[x] = prime_factors
            for y in prime_factors:
                if y in distinct_prime_factors:
                    distinct_prime_factors[y] += 1
                else:
                    distinct_prime_factors[y] = 1
            if len(distinct_prime_factors) <= k:
                t = right - left + 1
                if t > max_subarray:
                    max_subarray = t
            else:
                remove_left = nums[left]
                remove_left_factors = cache_prime_factors[remove_left]
                for y in remove_left_factors:
                    if y in distinct_prime_factors:
                        if distinct_prime_factors[y] == 1:
                            del distinct_prime_factors[y]
                        else:
                            distinct_prime_factors[y] -= 1
                left += 1
                if len(distinct_prime_factors) <= k:
                    t = right - left + 1
                    if t > max_subarray:
                        max_subarray = t
            right += 1
        return max_subarray


if __name__ == "__main__":
    sol = Solution()

    arr = [int(x) for x in input().split()]
    k = int(input().strip())
    
    result = sol.longestSubarray(arr, k)
    print(result)
