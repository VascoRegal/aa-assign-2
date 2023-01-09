import random
import math

class Solver:
    def __init__(self, problem):
        self.problem = problem
        self.solution = None

    def solve(self, k=3):
        pass


class ExhaustiveSolver(Solver):
    """
    Exhaustive Counter
    """
    def solve(self, k=3):
        self.solution = {}
        while True:
            char = self.problem.get_next()

            if not char:
                return dict(sorted(self.solution.items(), key=lambda e: e[1], reverse=True)[:k])

            if char not in self.solution:
                self.solution[char] = 1
            else:
                self.solution[char] += 1



class MistraGriesSolver(Solver):
    """
    Mistra & Gries implementation

    Finds most frequent letters
    """
    def solve(self, k=5):
        self.solution = {}
        while True:
            j = self.problem.get_next()
            if not j:
                return dict(sorted(self.solution.items(), key=lambda e: e[1], reverse=True))

            if j in self.solution:
                self.solution[j] += 1
            else:
                keys = [k for k in self.solution.keys()]
                if (len(keys) < (k - 1)):
                    self.solution[j] = 1
                else:
                    for t in keys:
                        self.solution[t] -= 1
                        if (self.solution[t] == 0):
                            del self.solution[t]


class ProbabilisticSolver(Solver):
    """
    Aproximate Counter with decreasing probability of:

                1 / sqrt(2)**k

    """
    def solve(self, k=3):
        self.solution = {}
        while True:
            j = self.problem.get_next()

            if not j:
                return dict(sorted(self.solution.items(), key=lambda e: e[1], reverse=True))
            else:
                if j not in self.solution:
                    self.solution[j] = 0
                cnt = self.solution[j]
                if random.uniform(0, 1) <  1 / math.sqrt(2)**k:
                    self.solution[j] += 1





