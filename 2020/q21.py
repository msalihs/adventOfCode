class Solution:
    def __init__(self):
        pass

    def parse_file(self, filepath):
        f = open(filepath, "r")
        allFoods = list()
        allIngredients = set()
        allAlergens = set()
        for line in f.readlines():
            ings, allergens = line.strip(")\n").split(" (contains ")
            ings, allergens = ings.split(" "), allergens.split(", ")
            allFoods.append((ings, allergens))
            allAlergens |= set(allergens)
            allIngredients |= set(ings)
        return allFoods, allIngredients, allAlergens

    def solve(self, filepath):
        result1, result2 = 0, 0
        allFoods, allIngredients, allAlergens = self.parse_file(filepath)

        # PART 1
        potential = dict()
        counter = dict()
        for ii, aa in allFoods:
            for a in aa:
                if a in potential:
                    potential[a] &= set(ii)
                else:
                    potential[a] = set(ii)
            for i in ii:
                counter[i] = counter.get(i, 0) + 1

        potentialIngs = dict()
        for a, ii in potential.items():
            for i in ii:
                if i in potentialIngs:
                    potentialIngs[i].add(a)
                else:
                    potentialIngs[i] = {a}
        result1 = sum([counter[i] for i in allIngredients - set(potentialIngs.keys())])

        # PART 2
        finalAssignments = dict()
        while len(finalAssignments) != len(allAlergens):
            for i in potentialIngs:
                if len(potentialIngs[i]) == 1:
                    break
            a = potentialIngs[i].pop()
            finalAssignments[a] = i
            del potentialIngs[i]
            for j in potentialIngs:
                if a in potentialIngs[j]:
                    potentialIngs[j].remove(a)
        result2 = ",".join(
            [finalAssignments[i] for i in sorted(finalAssignments.keys())]
        )

        return result1, result2


solver = Solution()
print(solver.solve("2020/q21.txt"))
