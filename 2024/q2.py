class Solution:
    def __init__(self):
        pass

    def solve(self, filepath):
        result1, result2 = 0, 0
        f = open(filepath, "r")

        maps = []
        for line in [line.strip("\n") for line in f.readlines()]:
            maps.append([int(x) for x in line.split(" ")])

        def checkmap(map):
            if len(map) < 2:
                return True

            curr = map[0]
            increasing = map[1] > map[0]
            for x in map[1:]:
                if (increasing and x > curr and x <= (curr + 3)) or (
                    not increasing and x < curr and x >= (curr - 3)
                ):
                    curr = x
                else:
                    return False

            return True

        # Part 1
        for map in maps:
            if checkmap(map):
                result1 += 1

        # Part 2
        for map in maps:
            if checkmap(map):
                result2 += 1
            else:
                for i in range(len(map)):
                    submap = map[:i] + map[i + 1 :]
                    if checkmap(submap):
                        result2 += 1
                        break

        return result1, result2


solver = Solution()
print(solver.solve("2024/q2.txt"))
