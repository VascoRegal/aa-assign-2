import pandas as pd
import matplotlib.pyplot as plt
import json
import os

def load_runs(output_dir):
    runs = []
    for f in os.listdir(output_dir):
        with open(f"{output_dir}/{f}", 'r') as run:
            runs.append(json.loads(next(run)))
    return runs


def dict_to_top_3(dic, limit=3):
    counter = 0
    res = ""
    print(dic)
    for term, cnt in dic.items():
        if counter == limit:
            res = res[:-1]
            return res
        res += f" {term}:{cnt} |"

def data_to_tex_table(data):
	print("\\begin{tabular}{|c c c|}")
	print("\\hline")
	print(" K & Most Frequent Letters & time(s)\\\\ [0.5ex] ")
	print("\\hline\\hline")
	for _, row in data.iterrows():
		print(f"{int(row['k'])} & {row['solution']} & {row['time']:.5f} \\\\")
		print("\\hline")
	print("\end{tabular}")

def absolute_error(actual, experimental):
	return (actual - experimental)

def aprox_error(computed, expected):
    cnt = 0
    abs_errors = []
    rel_errors = []
    print(expected)
    print(computed)
    for k, i in expected.items():
        if k not in computed:
            exp = 0
        else:
            exp = computed[k]
        act = i
        a = absolute_error(act, exp)
        abs_errors.append(a)
        rel_errors.append(a / act)

    print(sum(abs_errors) / len (abs_errors))
    print(sum(rel_errors) / len (rel_errors))




df = pd.DataFrame(load_runs("./runs"))
p_runs = df.loc[df['solver'] == 'p'].sort_values(by='k')
p_runs_pt = p_runs.loc[df['data'] == "data/1984_EN.txt"]
e_runs_pt = df.loc[df['solver'] == 'e'].sort_values(by='k').loc[df['data'] == "data/1984_EN.txt"]


EXACT_PT = e_runs_pt['solution'].to_dict()[17]
PROB_PT = p_runs_pt['solution'].to_dict()[11]

MGS_RUNS_PT = df.loc[df['solver'] == 'm'].sort_values(by='k').loc[df['data'] == "data/1984_PT.txt"]
MGS_RUNS_EN = df.loc[df['solver'] == 'm'].sort_values(by='k').loc[df['data'] == "data/1984_EN.txt"]
data_to_tex_table(MGS_RUNS_EN)
