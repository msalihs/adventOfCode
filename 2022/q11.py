
import copy
class Solution:
    def __init__(self):
        pass
    
    def get_monkey_business(self, monkeys, rounds, stress_manage_fcn):
        monkey_ops = dict()
        for _ in range(rounds):
            for i in sorted(monkeys.keys()):
                while monkeys[i]['items']:
                    monkey_ops[i] = monkey_ops.get(i, 0) + 1
                    old = monkeys[i]['items'].pop(0)
                    x = old if monkeys[i]['operation'][0] == 'old' else int(monkeys[i]['operation'][0])
                    y = old if monkeys[i]['operation'][2] == 'old' else int(monkeys[i]['operation'][2])
                    new = x*y if monkeys[i]['operation'][1] == '*' else x+y
                    if new % monkeys[i]['test'] == 0:
                        monkeys[monkeys[i]['true']]['items'].append(stress_manage_fcn(new))
                    else:
                        monkeys[monkeys[i]['false']]['items'].append(stress_manage_fcn(new))
        bussiest_monkey_ops = list(sorted(monkey_ops.values()))
        return bussiest_monkey_ops[-1] * bussiest_monkey_ops[-2]

    def solve(self, filepath):
        f = open(filepath, "r")
        readings = [x.split('\n') for x in f.read().split("Monkey")]
        monkeys, mod = dict(), 1
        for reading in readings[1:]:
            id = int(reading[0].strip(':'))
            monkeys[id] = dict()
            monkeys[id]['items'] = [int(x) for x in reading[1].strip('  Starting items: ').split(',')]
            monkeys[id]['operation'] = [x.strip(' ') for x in reading[2][19:].split(' ')]
            monkeys[id]['test'] = int(reading[3][21:])
            monkeys[id]['true'] = int(reading[4][29:])
            monkeys[id]['false'] = int(reading[5][30:])
            mod *= monkeys[id]['test']
        
        def divide_stress(stress):
            return stress // 3

        result1 = self.get_monkey_business(copy.deepcopy(monkeys), 20, divide_stress)
        
        def mod_stress(stress):
            return stress % mod
        result2 = self.get_monkey_business(copy.deepcopy(monkeys), 10000, mod_stress)

        return result1, result2


solver = Solution()
print(solver.solve("2022/q11.txt"))
