from problem import Problem
import argparse

SOLVERS=['e', 'm', 'p']

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description = "Run letter occurence problems in text files")

    parser.add_argument('data_path',
                        type=str,
                        help='Path to the text file')

    parser.add_argument('stopwords',
                        type=str,
                        help='Path to stopwords file')

    parser.add_argument('-e', '--export',
                        help='Export run to file')

    parser.add_argument('-s', '--solver',
                        help='Shoose solver - (E)xhaustive Counter | (P)robabilistic Counter | (M)istra & Gries most frequent')

    parser.add_argument('-k',
                        default=5,
                        type=int,
                        help='Value of k to use in algorithms')

    args = parser.parse_args()

    s = args.solver
    s = s.lower() if s and s in SOLVERS else 'e'

    p = Problem(args.data_path, args.stopwords, args.k, s)
    p.solve()

    if args.export:
        p.export(args.export)

    p.results()
