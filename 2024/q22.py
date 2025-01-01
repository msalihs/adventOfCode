from collections import defaultdict
from functools import cache
import time


class Solution:
    def __init__(self):
        self.mod = 16777216

    def gen_next(self, secret):
        secret = (secret ^ (secret << 6)) % self.mod
        secret = (secret ^ (secret >> 5)) % self.mod
        secret = (secret ^ (secret << 11)) % self.mod
        return secret

    def solve(self, filepath):
        result1, result2 = 0, 0
        f = open(filepath, "r")
        nums = [int(line.strip("\n")) for line in f.readlines() if line.strip("\n")]

        it = 2000

        # PART 1
        for secret in nums:
            for _ in range(it):
                secret = self.gen_next(secret)
            result1 += secret

        # PART 2
        cache = defaultdict(dict)
        for idx, secret in enumerate(nums):
            prices = [secret % 10]
            for i in range(it):
                secret = self.gen_next(secret)
                prices.append(secret % 10)
                if i < 3:
                    continue
                seq = tuple([prices[j] - prices[j - 1] for j in range(-1, -5, -1)])
                if idx not in cache[seq]:
                    cache[seq][idx] = prices[-1]

        for prices in cache.values():
            result2 = max(result2, sum(prices.values()))

        return result1, result2


start = time.time()
solver = Solution()
print(solver.solve("2024/q22.txt"))
print(f"Time: {time.time() - start}")
