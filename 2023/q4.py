class Solution:
    def __init__(self):
        pass

    def solve(self, filepath):
        f = open(filepath, "r")
        result1, result2 = 0, 0
        readings = f.read().split("\n")
        cards = {}

        for reading in readings:
            card, numbers = reading.split(": ")
            idx = int(card.split(" ")[-1])
            winning, mine = numbers.split(" | ")
            cards[idx] = [
                {int(x) for x in winning.split(" ") if x.isnumeric()},
                {int(x) for x in mine.split(" ") if x.isnumeric()},
            ]

        weights = {k: 1 for k in cards}

        for card, (w, m) in cards.items():
            common = w & m
            if len(common) > 0:
                result1 += pow(2, len(common) - 1)
                for i in range(len(common)):
                    weights[card + i + 1] += weights[card]

        result2 = sum(weights.values())
        return result1, result2


solver = Solution()
print(solver.solve("2023/q4.txt"))
