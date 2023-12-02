from collections import defaultdict


class Solution:
    def __init__(self):
        pass

    def solve(self, filepath):
        result1, result2 = 0, 0
        f = open(filepath, "r")
        input_ = [line.strip("\n") for line in f.readlines()]
        games = defaultdict(dict)

        for game in input_:
            k, v = game.split(":")
            k = int(k.split(" ")[1])
            for cubes in v.lstrip().split(";"):
                for cube in cubes.split(","):
                    n, color = cube.lstrip().split(" ")
                    games[k][color] = max(games[k].get(color, 0), int(n))

        target = {"blue": 14, "red": 12, "green": 13}
        for id, game in games.items():
            for k, v in target.items():
                if game[k] > v:
                    break
            else:
                result1 += id
            power = 1
            for k, v in game.items():
                power *= v
            result2 += power

        return result1, result2


solver = Solution()
print(solver.solve("2023/q2.txt"))
