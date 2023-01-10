from problem import Problem


if __name__ == '__main__':
    EXPORT = "runs/"
    K_VALS = [3, 5, 10]
    SOLVERS = ['e', 'm', 'p']

    sets = {"PT": {
                "data": "data/1984_PT.txt",
                "stopwords": "stopwords/portuguese.txt"
            },
            "EN": {
                "data": "data/1984_EN.txt",
                "stopwords": "stopwords/english.txt"
            }
    }


    for lang, params in sets.items():
        for s in SOLVERS:
            for k in K_VALS:
                p = Problem(params["data"], params["stopwords"], k, s)
                p.solve()
                p.export(EXPORT)
