from collections import defaultdict, deque


class Solution:
    def __init__(self):
        pass

    def solve(self, filepath):
        f = open(filepath, "r")
        result1, result2 = 10 ** 19 + 7, 10 ** 19 + 7
        readings = f.read().split("\n\n")

        seeds = [int(num) for num in readings[0].split(": ")[1].split(" ")]
        ranges = defaultdict(list)
        mappings = dict()
        for reading in readings[1:]:
            key = None
            for idx, line in enumerate(reading.split("\n")):
                if idx == 0:
                    line = line.rstrip(" map:").split("-")
                    key = (line[0], line[2])
                    mappings[line[0]] = line[2]
                else:
                    ranges[key].append(tuple(int(num) for num in line.split(" ")))

        for seed in seeds:
            current = "seed"
            desired = "location"
            val = seed
            while current != desired:
                next_ = mappings[current]
                for d, s, r in ranges[(current, next_)]:
                    if s <= val < (s + r):
                        val = d + val - s
                        break
                current = next_
            result1 = min(val, result1)

        queue = deque([])
        for i in range(0, len(seeds), 2):
            queue.append((seeds[i], seeds[i] + seeds[i + 1] - 1, "seed"))
        print(seeds)
        while queue:
            begin, end, state = queue.popleft()
            next_ = mappings[state]
            count = 0
            for d, s, r in ranges[(state, next_)]:
                if end >= s and begin <= (s + r - 1):
                    count += 1
                    if next_ == desired:
                        result2 = min(d + max(begin, s) - s, result2)
                    else:
                        queue.append(
                            (d + max(begin, s) - s, d + min(end, s + r - 1) - s, next_)
                        )
            if count == 0:
                if next_ == desired:
                    result2 = min(begin, result2)
                else:
                    queue.append((begin, end, next_))

        return result1, result2


solver = Solution()
print(solver.solve("2023/q5.txt"))
