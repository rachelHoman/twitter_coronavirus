#!/usr/bin/env python3

# command line args
import argparse
parser = argparse.ArgumentParser()
parser.add_argument('--hashtags', nargs='+', required=True)
parser.add_argument('--output_path', required=True)
args = parser.parse_args()

# imports
import os
import json
import matplotlib.pyplot as plt
from collections import defaultdict

# load each of the input paths
total_hashtags = defaultdict(lambda: Counter())

# scan through all the data in the outputs folder
for path in os.listdir('outputs'):
    if path.endswith('.json'):
        with open(os.path.join('outputs', path)) as f:
            tmp = json.load(f)
            for k in tmp:
                if k in args.hashtags:
                    total_hashtags[k] += tmp[k]

# plot the data
for hashtag in args.hashtags:
    data = total_hashtags[hashtag]
    x_values = list(data.keys())
    y_values = list(data.values())

    plt.plot(x_values, y_values, label=hashtag)

# Customize the plot
plt.xlabel('Day of the Year')
plt.ylabel('Number of Tweets')
plt.title('Number of Tweets with Hashtags Over the Year')
plt.legend()
plt.grid(True)

# Save the plot to the specified output path
plt.savefig(args.output_path)
