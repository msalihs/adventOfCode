from collections import defaultdict


class Solution:
    def __init__(self):
        pass

    def solve(self, filepath):
        result1, result2 = 0, 0
        f = open(filepath, "r")
        memory = f.read().strip()
        mem_layout = list()
        empty_blocks = list()
        file_locations = list()

        for i, c in enumerate(memory):
            if i % 2 == 0:
                file_locations.append((len(mem_layout), int(c)))
                mem_layout += [str(i // 2)] * int(c)
            elif int(c) > 0:
                empty_blocks.append((int(c), len(mem_layout)))
                mem_layout += ["."] * int(c)

        # print(''.join(mem_layout))

        # PART 1
        fixed_memory = mem_layout.copy()
        l, r = 0, len(fixed_memory) - 1
        while l < r:
            while l < r and fixed_memory[l] != ".":
                l += 1
            while l < r and fixed_memory[r] == ".":
                r -= 1
            if l < r:
                fixed_memory[l], fixed_memory[r] = fixed_memory[r], fixed_memory[l]
                l += 1
                r -= 1

        result1 = sum([idx * int(c) for idx, c in enumerate(fixed_memory) if c != "."])

        # PART 2
        fixed_memory = mem_layout.copy()
        while file_locations:
            source_idx, c = file_locations.pop()

            for idx, (size, destination_idx) in enumerate(empty_blocks):
                if size >= c and destination_idx < source_idx:
                    for i in range(c):
                        fixed_memory[destination_idx + i] = fixed_memory[source_idx + i]
                        fixed_memory[source_idx + i] = "."
                    if size > c:
                        empty_blocks[idx] = (size - c, destination_idx + c)
                    else:
                        empty_blocks.pop(idx)
                    break

        result2 = sum([idx * int(c) for idx, c in enumerate(fixed_memory) if c != "."])

        return result1, result2


solver = Solution()
print(solver.solve("2024/q9.txt"))
