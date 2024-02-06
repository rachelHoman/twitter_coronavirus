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
import glob
import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import matplotlib.dates as plt_dates
from matplotlib.ticker import MultipleLocator
from collections import Counter, defaultdict
from datetime import datetime

# initialize
# total_hashtags = defaultdict(lambda: Counter())
file_path = "/home/rmha2020/twitter_coronavirus/outputs/geoTwitter20*.lang"
files = glob.glob(file_path)
total = defaultdict(int)

# go through files
for file in files:
    with open(file) as f:
        date = os.path.basename(file)[10:18]
        tmp = json.load(f)
        for hashtag in args.hashtags:
            if hashtag in tmp:
                for language in tmp[hashtag]:
                    if (date, hashtag) not in total:
                        total[(date, hashtag)] = 0
                total[(date, hashtag)] += np.sum(list(tmp[hashtag].values()))

# plot the data
total = dict(sorted(total.items(), key=lambda key: key[0]))
fig, ax = plt.subplots()

for hashtag in args.hashtags:
    dates = []
    counts = []

    for k in total:
        if k[1] == hashtag:
            dates.append(k[0])
            counts.append(total[k])

    if dates:  # Check if the list is not empty
        dates_list = [datetime.strptime(date_str, "%y-%m-%d") for date_str in dates]
        ax.plot(dates_list, counts, label=hashtag)

ax.xaxis.set_major_locator(plt_dates.MonthLocator(interval=2))
ax.xaxis.set_major_formatter(plt_dates.DateFormatter("%y-%m-%d"))

# add labels
plt.xlabel('Date')
plt.ylabel('Number of Tweets')
plt.title('Number of Daily Tweets By Hashtags')
plt.legend()

#finalHashes = ""
#for hsh in args.hashtags:
#    finalHashes += hsh


# Save the plot to the specified output path
output_filename = f'{hashtag}_alt_reduce3.png'
output_p = os.path.join(args.output_path, output_filename)
plt.savefig(output_p)
