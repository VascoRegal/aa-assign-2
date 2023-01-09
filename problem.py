from data import DataStream
from solution import ExhaustiveSolver, MistraGriesSolver, ProbabilisticSolver

import time
import os
import json

class Problem:
    def __init__(self, data_dir : str, stopwords_path : str, k: int=5, solver: str='e'):
        self.data_stream = DataStream(data_dir, stopwords_path)
        self.solution = None
        self.execution_time = 0
        self.k = k
        self.solver = solver

    def solve(self):
        if self.solver == 'e':
            solver = ExhaustiveSolver(self)
        elif self.solver == 'm':
            solver = MistraGriesSolver(self)
        else:
            solver = ProbabilisticSolver(self)
        self.execution_time = time.time()
        self.solution = solver.solve(self.k)
        self.execution_time = time.time() - self.execution_time

    def get_next(self):
        return self.data_stream.next_token()

    def results(self):
        print(f"solver: {self.solver}, k={self.k}")
        for k, v in self.solution.items():
            print(f"{k} -> {v}")
        print(f"Computed in {self.execution_time}")
        print()

    def export(self, output_folder):
        if not os.path.exists(output_folder):
            os.makedirs(output_folder)

        file_name = f"{output_folder}/{str(time.time())}"
        file_name += f"-{self.solver}-{self.k}"

        with open(file_name, 'w') as f:
            json.dump({
                "solver": self.solver,
                "solution": self.solution,
                "time": self.execution_time,
                "k": self.k
            }, f)

