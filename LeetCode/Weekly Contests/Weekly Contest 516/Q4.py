import sys
import math
from collections import Counter, defaultdict, deque
from bisect import bisect_left, bisect_right
from heapq import heapify, heappop, heappush

class Solution:
    def validSubarrays(self, nums: list[int], k: int, queries: list[list[int]]) -> list[bool]:
        indexed_queries = []

        for i, (l, r) in enumerate(queries):
            indexed_queries.append((l, r, i))

        block = int(len(nums) ** 0.5) + 1

        indexed_queries.sort(
            key=lambda q: (
                q[0] // block,
                q[1] if (q[0] // block) % 2 == 0 else -q[1]
            )
        )
        ans = [False] * len(indexed_queries)

        L = 0
        R = -1
        distinct = 0
        odd = 0

        maxElement = max(nums)
        frequencies = [0] * (maxElement + 1)

        for x in indexed_queries:
            l = x[0]
            r = x[1]
            index = x[2]

            if L > l:
                while L > l:
                    L -= 1
                    frequencies[nums[L]] += 1

                    if frequencies[nums[L]] == 1:
                        distinct += 1

                    if frequencies[nums[L]] % 2 == 1:
                        odd += 1
                    else:
                        odd -= 1

            if R < r:
                while R < r:
                    R += 1
                    frequencies[nums[R]] += 1

                    if frequencies[nums[R]] == 1:
                        distinct += 1

                    if frequencies[nums[R]] % 2 == 1:
                        odd += 1
                    else:
                        odd -= 1

            if L < l:
                while L < l:
                    frequencies[nums[L]] -= 1

                    if frequencies[nums[L]] == 0:
                        distinct -= 1

                    if frequencies[nums[L]] % 2 == 0:
                        odd -= 1
                    else:
                        odd += 1

                    L += 1

            if R > r:
                while r < R:
                    frequencies[nums[R]] -= 1

                    if frequencies[nums[R]] % 2 == 1:
                        odd += 1
                    else:
                        odd -= 1

                    if frequencies[nums[R]] == 0:
                        distinct -= 1

                    R -= 1

            if distinct == k and odd == 0:
                ans[index] = True

        return ans




if __name__ == "__main__":
    sol = Solution()

    arr = [int(x) for x in input().split()]
    k = int(input().strip())
    rows = int(input())
    matrix = [list(map(int, input().split())) for _ in range(rows)]

    result = sol.validSubarrays(arr, k, matrix)
    print(result)
