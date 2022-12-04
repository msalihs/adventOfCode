class Solution:
    def __init__(self):
        pass

    def solve(self, filepath):
        f = open(filepath, "r")
        result1, result2 = 0, 0
        rounds = []
        for line in f.readlines():
            line = line.strip("\n")
            rounds.append(tuple(line.split(" ")))
        hand_score = {"X": 1, "Y": 2, "Z": 3, "A": 1, "B": 2, "C": 3}
        beats = {"X": "C", "Y": "A", "Z": "B", "A": "Z", "B": "X", "C": "Y"}
        wins = {"A": "C", "B": "A", "C": "B"}
        loses = {"C": "A", "A": "B", "B": "C"}

        for opp, me in rounds:
            result1 += hand_score[me]
            if opp == beats[me]:
                result1 += 6
            elif me != beats[opp]:
                result1 += 3

        for opp, res in rounds:
            if res == "X":
                me = wins[opp]
            elif res == "Z":
                me = loses[opp]
                result2 += 6
            else:
                result2 += 3
                me = opp
            result2 += hand_score[me]

        return result1, result2


solver = Solution()
print(solver.solve("2022/q2.txt"))
