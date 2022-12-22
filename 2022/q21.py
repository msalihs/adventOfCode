import copy


class Solution:
    def __init__(self):
        pass

    def solve(self, filepath):
        f = open(filepath, "r")
        result1, result2 = 0, 0
        ma = {}
        for r in f.read().split("\n"):
            monkey, action = r.split(': ')
            if action.isnumeric(): ma[monkey] = int(action)
            else: ma[monkey] = action.split(' ')

        original = copy.deepcopy(ma)
        while True:
            for m, a in ma.items():
                if isinstance(a, list):
                    for i in [0, 2]:
                        if isinstance(a[i], str) and isinstance(ma[a[i]], int):
                            ma[m][i] = ma[a[i]]
            
            for m, a in ma.items():
                if isinstance(a, list):
                    if isinstance(a[0], int) and isinstance(a[2], int):
                        if a[1] == '+':
                            ma[m] = a[0] + a[2]
                        elif a[1] == '-':
                            ma[m] = a[0] - a[2]
                        elif a[1] == '/':
                            ma[m] = a[0] // a[2]
                        elif a[1] == '*':
                            ma[m] = a[0] * a[2]
            if isinstance(ma['root'], int):
                break
            
        result1 = ma['root']

        ma = copy.deepcopy(original)
        ma['root'][1] = '='
        del ma['humn']
        while True:
            change = 0
            for m, a in ma.items():
                if isinstance(a, list):
                    for i in [0, 2]:
                        if isinstance(a[i], str) and isinstance(ma.get(a[i], None), int):
                            ma[m][i] = ma[a[i]]
                            change += 1
            
            for m, a in ma.items():
                if isinstance(a, list):
                    if isinstance(a[0], int) and isinstance(a[2], int):
                        if a[1] == '+':
                            ma[m] = a[0] + a[2]
                        elif a[1] == '-':
                            ma[m] = a[0] - a[2]
                        elif a[1] == '/':
                            ma[m] = a[0] // a[2]
                        elif a[1] == '*':
                            ma[m] = a[0] * a[2]
                        change += 1

            if change == 0:
                break
        print(ma)
        queue = [('root', 0)]
        while queue:
            print(queue)
            n, t = queue.pop(0)
            if ma[n][1] == '=':
                if isinstance(ma[n][0], int):
                    queue.append((ma[n][2], ma[n][0]))
                elif isinstance(ma[n][2], int):
                    queue.append((ma[n][0], ma[n][2]))
                else:
                    raise ValueError
            if ma[n][1] == '+':
                if isinstance(ma[n][0], int):
                    queue.append((ma[n][2], t - ma[n][0]))
                elif isinstance(ma[n][2], int):
                    queue.append((ma[n][0], t - ma[n][2]))
                else:
                    raise ValueError
            elif ma[n][1] == '-':
                if isinstance(ma[n][0], int):
                    queue.append((ma[n][2], ma[n][0] - t))
                elif isinstance(ma[n][2], int):
                    queue.append((ma[n][0], t + ma[n][2]))
                else:
                    raise ValueError
            elif ma[n][1] == '/':
                if isinstance(ma[n][0], int):
                    queue.append((ma[n][2], t * ma[n][0]))
                elif isinstance(ma[n][2], int):
                    queue.append((ma[n][0], t * ma[n][2]))
                else:
                    raise ValueError
            elif ma[n][1] == '*':
                if isinstance(ma[n][0], int):
                    queue.append((ma[n][2], t // ma[n][0]))
                elif isinstance(ma[n][2], int):
                    queue.append((ma[n][0], t // ma[n][2]))
                else:
                    raise ValueError
            if queue[-1][0] == 'humn':
                print(queue)
                result2 = queue[-1][1]
                break

        return result1, result2


solver = Solution()
print(solver.solve("2022/q21.txt"))
