class Solution:
    def __init__(self):
        pass

    def parse_file(self, filepath):
        fields, allRanges, myTicket, nearByTickets = dict(), set(), list(), dict()
        state, index = 0, 0
        f = open(filepath, "r")
        for line in f.readlines():
            if "your" in line:
                state = 1
            elif "nearby" in line:
                state = 2
            elif state == 0 and len(line.strip("\n").split(": ")) == 2:
                k, ranges = line.strip("\n").split(": ")
                r1, r2 = ranges.split(" or ")
                r1start, r1end = r1.split("-")
                r2start, r2end = r2.split("-")
                fields[k] = set(range(int(r1start), int(r1end) + 1)) | set(
                    range(int(r2start), int(r2end) + 1)
                )
                allRanges |= set(range(int(r1start), int(r1end) + 1)) | set(
                    range(int(r2start), int(r2end) + 1)
                )
            elif state == 1:
                myTicket += [int(x) for x in line.strip("\n").split(",") if x.isdigit()]
            elif state == 2:
                nearByTickets[index] = [
                    int(x) for x in line.strip("\n").split(",") if x.isdigit()
                ]
                index += 1
        return fields, allRanges, myTicket, nearByTickets

    def solve(self, filepath):
        result1, result2 = 0, 0
        fields, allRanges, myTicket, nearByTickets = self.parse_file(filepath)

        # PART 1
        for i in range(len(nearByTickets)):
            for number in nearByTickets[i]:
                if number not in allRanges:
                    result1 += number
                    del nearByTickets[i]
                    break

        # PART 2
        assignments = dict()
        for i in range(len(fields)):
            allNums = set()
            assignments[i] = list()
            for j in nearByTickets:
                allNums.add(nearByTickets[j][i])
            for k in fields:
                if allNums.issubset(fields[k]):
                    assignments[i].append(k)

        finalAssignments = dict()
        while len(finalAssignments) != len(fields):
            for i in assignments:
                if len(assignments[i]) == 1:
                    break
            field = assignments[i][0]
            finalAssignments[field] = i
            del assignments[i]
            for j in assignments:
                if field in assignments[j]:
                    assignments[j].remove(field)

        result2 = 1
        for field in finalAssignments:
            if "departure" in field:
                result2 *= myTicket[finalAssignments[field]]

        return result1, result2


solver = Solution()
print(solver.solve("2020/q16.txt"))
