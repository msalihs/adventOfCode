class Solution:
    def __init__(self):
        pass

    def solve(self, filepath):
        f = open(filepath, 'r')
        result1, result2 = 0, 0
        passes = list()
        allSeatNums = set()

        for line in f.readlines():
            passes.append(line.strip('\n'))

        for p in passes: 
            row = p[0:-3]
            col = p[-3:]
            row = row.replace('F', '0').replace('B', '1')
            col = col.replace('R', '1').replace('L', '0')
            allSeatNums.add(int(row,2) * 8 + int(col,2))
        result1 = max(allSeatNums)

        
        for seat in range(8, 8*126):
            if seat not in allSeatNums:
                if  seat+1 in allSeatNums and seat-1 in allSeatNums:
                    result2 = seat
                    break
    
        return result1, result2 

solver = Solution()
print(solver.solve('2020/q5.txt'))
