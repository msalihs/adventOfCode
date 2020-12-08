class Solution:
    def __init__(self):
        pass

    def solve(self, filepath):
        f = open(filepath, 'r')
        result1, result2 = 0, 0
        inFile = list()
        allConditions = dict()

        for line in f.readlines():
            inFile.append(line.strip('\n'))

        for line in inFile:
            k, v = line.split('contain')
            k = k.replace(' bags ', '')

            if k not in allConditions:
                allConditions[k] = list()

            if 'other' not in v:
                v = v.replace(' bag', '').replace(' bags', '').rstrip('.').split(',')
                for pair in v:
                    allConditions[k].append((int(pair[:3]), pair[3:].strip(' ').rstrip('s')))
        
        contained = dict()

        for k, v in allConditions.items():
            for n, c in v:
                if c in contained: contained[c].add(k)
                else: contained[c] = {k}
        
        # Part 1
        queue = ['shiny gold']
        seen = set()
        while queue:
            c = queue.pop()
            seen.add(c)
            if c in contained: 
                queue += [n for n in contained[c] if n not in seen]

        result1 = len(seen) - 1
        
        # Part 2
        queue = [(1, 'shiny gold')]
        seen = set()
        while queue:
            n, c = queue.pop(0)
            seen.add(c)
            result2 += n
            for number ,color in allConditions[c]:
                #if color not in seen:
                queue.append((n*number, color))

        result2 = result2 - 1
        
        return result1, result2 

solver = Solution()
print(solver.solve('2020/q7.txt'))
