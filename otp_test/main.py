#!/usr/bin/env python

import argparse
import numpy as np
from src.utils import *

def parsing():
    # Initiating parser
    parser = argparse.ArgumentParser(description=
    "A tool to fetch the association score data from the Open Targets REST API for a given disease id or target.")

    # Setting optional arguments inside a mutually exclusive group
    group = parser.add_mutually_exclusive_group(required=True)
    group.add_argument("-t", dest="target", type=str, help="The ID of the target for which you want to do the analysis.")
    group.add_argument("-d", dest="disease", type=str, help="The ID of the disease for which you want to do the analysis.")
    parser.add_argument("-e", dest="export", type=str, default="output.json", nargs="?", help="JSON filename from the exported query result. If not indicated, default name is: output.json.")
    parser.add_argument("-m", dest="minimum", type=float, help="Minimum score value to filter associations with lower quality data points.")

    args = parser.parse_args()
    
    return args

def main():
    args = parsing()

    data = query(args.disease, scorevalue_min=args.minimum)

    # stdout prints for every association
    for record in data.values():
        print(record)
    
    # overall metrics
    scores = [record["association_score.overall"] for record in data.values()]
    mean = np.mean(scores)
    highest = np.max(scores)
    lowest = np.min(scores)
    stdev = np.std(scores)
    print("-------------------------------------")
    print(f"""Association score values:
    Average score: {mean}
    Maximum score: {highest}
    Minimum score: {lowest}
    Standard Deviation: {stdev}""")
    print("-------------------------------------")

    if args.export:
        export(data, args.export)


    return mean, highest, lowest, stdev


if __name__ == "__main__":
    main()