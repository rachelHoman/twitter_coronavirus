#!/usr/bin/env python3

# command line args
import argparse
parser = argparse.ArgumentParser()
parser.add_argument('--input_path',required=True)
parser.add_argument('--key',required=True)
parser.add_argument('--percent',action='store_true')
args = parser.parse_args()

# imports
import os
import json
import argparse
import matplotlib
# Use Agg backend for non-interactive mode
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from collections import Counter,defaultdict

# Command line args
parser = argparse.ArgumentParser()
parser.add_argument('--input_path', required=True)
parser.add_argument('--key', required=True)
parser.add_argument('--percent', action='store_true')
args = parser.parse_args()

# open the input path
with open(args.input_path) as f:
    counts = json.load(f)

# Handle the case when the specified key is not present
try:
    data = counts[args.key]
except KeyError:
    print(f"The key '{args.key}' is not present in the loaded data.")
    exit(1)

# normalize the counts by the total values
if args.percent:
    for k in counts[args.key]:
        counts[args.key][k] /= counts['_all'][k]

# print the count values
items = sorted(counts[args.key].items(), key=lambda item: (item[1],item[0]), reverse=True)
#for k,v in items:
   # print(k,':',v)
top_items = items[-10:]

# Extract the keys and values for plotting
keys, values = zip(*top_items)

# Plot the bar graph
plt.barh(keys, values)
plt.xlabel('Values')
plt.ylabel(args.key)
plt.title(f'Top 10 {args.key} (Sorted from Low to High)')
plt.tight_layout()

# Determine whether it's lang or country data
data_type = "lang" if "lang" in args.input_path else "country"
# Save the png
output_path = os.path.splitext(args.input_path)[0] + f'_{args.key}_{data_type}_bar_graph.png'
plt.savefig(output_path)
