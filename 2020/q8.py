class Solution:
    def __init__(self):
        pass

    def solve(self, filepath):
        f = open(filepath, 'r')
        result1, result2 = 0, 0
        inFile = list()
        operations = list()

        for line in f.readlines():
            inFile.append(line.strip('\n'))
        
        for line in inFile:
            cmd, val = line.split(' ')
            operations.append((cmd, int(val)))

        index, seen = 0, set()
        while index not in seen:
            seen.add(index)
            cmd, val = operations[index]
            index += 1
            if cmd == 'jmp':
                index += val - 1
            elif cmd == 'acc':
                result1 += val

        for i in range(len(operations)):
            if operations[i][0] == 'acc': continue
            cmd1, val1 = operations[i]
            if cmd1 == 'nop': operations[i] = ('jmp', val1)
            elif cmd1 == 'jmp': operations[i] = ('nop', val1)
            
            result2 = 0
            index = 0
            seen = set()

            while index not in seen:
                seen.add(index)

                if index == len(operations):
                    return result1, result2

                cmd, val = operations[index]
                if cmd == 'nop':
                    index += 1
                elif cmd == 'acc':
                    result2 += val
                    index += 1
                elif cmd == 'jmp':
                    index += val

            operations[i] = (cmd1, val1)

        return result1, -1

solver = Solution()
print(solver.solve('2020/q8.txt'))
