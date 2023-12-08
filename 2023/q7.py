from collections import Counter
import math


class Solution:
    def __init__(self):
        self.strength = {str(i): i for i in range(2, 10)}
        self.strength["T"] = 10
        self.strength["J"] = 11
        self.strength["Q"] = 12
        self.strength["K"] = 13
        self.strength["A"] = 14

    def findStrongest(self, hand):
        if "J" not in hand:
            return hand
        strengths = list()
        for c in self.strength.keys():
            if c != "J":
                new_hand = hand.replace("J", c)
                strengths.append((-self.handStrength(new_hand), new_hand))
        return sorted(strengths)[0][1]

    def handStrength(self, hand):
        counts = Counter(hand)
        countOfCounts = Counter(counts.values())
        if len(set(list(hand))) == 5:  # High Card
            s = 5
        elif len(set(list(hand))) == 4:  # One pair
            s = 6
        elif countOfCounts[2] == 2:  # Two pair
            s = 7
        elif countOfCounts[3] == 1 and countOfCounts[1] == 2:  # Three of a kind
            s = 8
        elif countOfCounts[3] == 1 and countOfCounts[2] == 1:  # Full house
            s = 9
        elif countOfCounts[4] == 1:  # Four of a kind
            s = 10
        elif countOfCounts[5] == 1:  # Five of a kind
            s = 11
        return pow(15, s)

    def solve(self, filepath):
        f = open(filepath, "r")
        result1, result2 = 0, 0
        readings = f.read().split("\n")
        hands = list()

        for reading in readings:
            hand, bid = reading.split(" ")
            hands.append((hand, int(bid)))

        ranking = list()
        for hand, bid in hands:
            power = sum([self.strength[hand[i]] * pow(15, 4 - i) for i in range(5)])
            ranking.append((power * self.handStrength(hand), bid))
        for rank, (power, bid) in enumerate(sorted(ranking)):
            result1 += (rank + 1) * bid

        self.strength["J"] = 1
        ranking = list()
        for hand, bid in hands:
            power = sum([self.strength[hand[i]] * pow(15, 4 - i) for i in range(5)])
            ranking.append((power * self.handStrength(self.findStrongest(hand)), bid))
        for rank, (power, bid) in enumerate(sorted(ranking)):
            result2 += (rank + 1) * bid

        return result1, result2


solver = Solution()
print(solver.solve("2023/q7.txt"))
