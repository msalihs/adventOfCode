from math import gcd

class Solution:
    def __init__(self):
        pass
    
    def solve(self, filepath):
        f = open(filepath, 'r')
        result1, result2, mask = 0, 0, 0
        part1, part2 = dict(), dict()
        
        for line in f.readlines():
            if 'mask' in line:
                mask = line.strip('\n').split(' = ')[1]
                combinations = mask.count('X')
            else:
                address, value = line.split(' = ')
                address = int(address.strip(']')[4:])
                value = int(value)
                part1[address] = 0
                memLocs = [0]
                for x in range(len(mask)):
                    maskVal = mask[len(mask)-1-x]
                    bitValue = 0
                    if maskVal == '1': bitValue = 1
                    elif maskVal == '0': bitValue = 0
                    elif value & 2**x: bitValue = 1
                    part1[address] += (2**x * bitValue)

                    bitValue = 0
                    toProcess = len(memLocs)
                    for i in range(toProcess):
                        loc = memLocs.pop(0)
                        if maskVal == '1' or (maskVal == '0' and (address & 2**x) != 0):
                            memLocs.append(2**x + loc)
                        elif maskVal == 'X':
                            memLocs.append(2**x + loc)
                            memLocs.append(loc)
                        else:
                            memLocs.append(loc)
                
                for loc in memLocs:
                    part2[loc] = value

        result1 = sum(part1.values())
        result2 = sum(part2.values())
        
        return result1, result2

solver = Solution()
print(solver.solve('2020/q14.txt'))
