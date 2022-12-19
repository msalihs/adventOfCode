from collections import defaultdict, deque


class Solution:
    def __init__(self):
        self.queue = list()
        self.seen = dict()
        self.seen_hit = 0
    
    def get_geodes(self, blueprints, max_time):
        results = dict()
        for num in blueprints:
            bp = blueprints[num]
            results[num] = 0
            self.queue = deque([(1, 0, 0, 0, 0, 0, 0, 0, 1)])
            self.seen = dict()
            iter = dict()
            self.seen_hit = 0
            print(f'Processing blueprint {num}.')
            while self.queue:
                orer, clayr, obsidianr, geoder, ore, clay, obsidian, geode, time = self.queue.popleft()
                iter[time] = iter.get(time, 0) + 1
                if time > max_time:
                    if results[num] < geode:
                        results[num] = geode
                    continue
                
                clay += clayr
                ore += orer
                obsidian += obsidianr
                geode += geoder
                time += 1

                if (ore-orer) >= bp['geode'][0] and (obsidian-obsidianr) >= bp['geode'][1]:
                    self.queue.append((orer, clayr, obsidianr, geoder+1, ore-bp['geode'][0], clay, obsidian - bp['geode'][1], geode, time))
                elif (ore-orer) >= bp['obsidian'][0] and (clay-clayr) >= bp['obsidian'][1]:
                    self.queue.append((orer, clayr, obsidianr+1, geoder, ore-bp['obsidian'][0], clay - bp['obsidian'][1], obsidian, geode, time))
                else:
                    if (ore-orer) >= bp['clay']:
                        self.queue.append((orer, clayr+1, obsidianr, geoder, ore-bp['clay'], clay, obsidian, geode, time))
                    if (ore-orer) >= bp['ore']:
                        self.queue.append((orer+1, clayr, obsidianr, geoder, ore-bp['ore'], clay, obsidian, geode, time))
                    if (ore-orer) < 5:
                        self.queue.append((orer, clayr, obsidianr, geoder, ore, clay, obsidian, geode, time))
        return results

    def solve(self, filepath):
        f = open(filepath, "r")
        result1, result2 = 0, 1
        blueprints = defaultdict(dict)
        for reading in f.read().split("\n"):
            bpn, rem = reading.split(':')
            num = int(bpn.split(' ')[1])
            costs = rem.split('costs')
            blueprints[num]['ore'] = int(costs[1].split(' ')[1])
            blueprints[num]['clay'] = int(costs[2].split(' ')[1])
            blueprints[num]['obsidian'] = (int(costs[3].split(' ')[1]), int(costs[3].split(' ')[4]))
            blueprints[num]['geode'] = (int(costs[4].split(' ')[1]), int(costs[4].split(' ')[4]))

        results = self.get_geodes(blueprints=blueprints, max_time=24)
        result1 = sum([k*v for k,v in results.items()])

        results = self.get_geodes(blueprints={k:v for k,v in blueprints.items() if k < 4}, max_time=32)
        for _,v in results.items():
            result2 *= v

        return result1, result2


solver = Solution()
print(solver.solve("2022/q19.txt"))
