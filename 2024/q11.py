from copy import deepcopy


class Solution:
    def __init__(self):
        pass

    def solve(self, filepath):
        result1, result2 = 0, 0
        f = open(filepath, "r")
        _input = [num for num in f.read().strip().split(" ")]

        def apply_rules(arr, it):
            nums = dict()

            for num in arr:
                nums[num] = nums.get(num, 0) + 1

            for i in range(it):
                numsp = dict()
                for k, v in nums.items():
                    if k == "0":
                        numsp["1"] = numsp.get("1", 0) + v
                    elif len(k) % 2 == 0:
                        n1, n2 = k[: len(k) // 2], str(int(k[len(k) // 2 :]))
                        numsp[n1] = numsp.get(n1, 0) + v
                        numsp[n2] = numsp.get(n2, 0) + v
                    else:
                        n = str(int(k) * 2024)
                        numsp[n] = numsp.get(n, 0) + v
                # print(i, numsp)
                nums = deepcopy(numsp)
            return sum(nums.values())

        # PART 1
        result1 = apply_rules(_input, 25)

        # PART 2
        result2 = apply_rules(_input, 75)

        return result1, result2


solver = Solution()
print(solver.solve("2024/q11.txt"))
