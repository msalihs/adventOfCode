class Solution:
    def __init__(self):
        self.nums = list()

    def mix(self, numbers, order, n_iter=1):
        for i in range(1, n_iter + 1):
            for n, j in order:
                idx = numbers.index((n, i**2 * j))
                del numbers[idx]
                new_idx = (idx + n) % len(numbers)
                numbers.insert(new_idx, (n, (i + 1) ** 2 * j))
        return numbers

    def get_groove_coords(self, numbers):
        idx = numbers.index((0, 0))
        return sum(
            [numbers[(idx + target) % len(numbers)][0] for target in [1000, 2000, 3000]]
        )

    def solve(self, filepath):
        f = open(filepath, "r")
        result1, result2 = 0, 1
        nums = [int(r) for r in f.read().split("\n")]
        idx = nums.index(0)
        self.nums = [(n, i - idx) for i, n in enumerate(nums)]

        nums1 = self.mix(self.nums.copy(), self.nums)
        result1 = self.get_groove_coords(nums1)

        dkey = 811589153
        nums2 = [(n[0] * dkey, n[1]) for n in self.nums]
        nums2 = self.mix(nums2.copy(), nums2.copy(), n_iter=10)
        result2 = self.get_groove_coords(nums2)
        return result1, result2


solver = Solution()
print(solver.solve("2022/q20.txt"))
