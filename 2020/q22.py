class Solution:
    def __init__(self):
        pass

    def parse_file(self, filepath):
        f = open(filepath, "r")
        player1 = list()
        player2 = list()
        state = 0
        for line in f.readlines():
            line = line.strip("\n")
            if "Player" in line:
                state += 1
            elif state == 1 and line.isdigit():
                player1.append(int(line))
            elif state == 2 and line.isdigit():
                player2.append(int(line))

        return player1, player2

    def solve(self, filepath):
        result1, result2 = 0, 0

        def play(player1, player2, withRecursion=False):
            gameCache = set()
            while player1 and player2:
                if (tuple(player1), tuple(player2)) in gameCache:
                    return True
                else:
                    gameCache.add((tuple(player1), tuple(player2)))
                p1 = player1.pop(0)
                p2 = player2.pop(0)
                if withRecursion and len(player1) >= p1 and len(player2) >= p2:
                    if play(player1[:p1], player2[:p2], True):
                        player1 += [p1, p2]
                    else:
                        player2 += [p2, p1]
                elif p1 > p2:
                    player1 += [p1, p2]
                else:
                    player2 += [p2, p1]
            return player2 == []

        player1, player2 = self.parse_file(filepath)
        if play(player1, player2):
            result1 = sum([(i + 1) * x for i, x in enumerate(reversed(player1))])
        else:
            result1 = sum([(i + 1) * x for i, x in enumerate(reversed(player2))])

        player1, player2 = self.parse_file(filepath)
        if play(player1, player2, withRecursion=True):
            result2 = sum([(i + 1) * x for i, x in enumerate(reversed(player1))])
        else:
            result2 = sum([(i + 1) * x for i, x in enumerate(reversed(player2))])

        return result1, result2


solver = Solution()
print(solver.solve("2020/q22.txt"))
