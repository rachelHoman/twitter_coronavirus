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
# To handle the Korean font
import matplotlib.font_manager
path = '/home/rmha2020/twitter_coronavirus/Noto_Serif_KR/NotoSerifKR-Regular.otf'
fp = matplotlib.font_manager.FontProperties(fname=path)

# Use Agg backend for non-interactive mode
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from collections import Counter,defaultdict

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
#    print(k,':',v)

# top ten items
top_items = items[:10]

# Extract the keys and values for plotting
keys = [item[0] for item in top_items]
values = [item[1] for item in top_items]
keys = keys[::-1]
values = values[::-1]

# Plot the bar graph
plt.bar(range(len(keys)), values)
plt.xticks(range(len(keys)), keys)
xLabel = "Language"
if args.input_path == "reduced.country":
    xLabel = 'Country'
    plt.title(f'Number of Tweets by Country')
else:
    xLabel = 'Language'
    plt.title(f'Number of Tweets by Language')
plt.xlabel(xLabel, fontproperties=fp)
plt.ylabel("Number of Tweets", fontproperties=fp)
lang = "English"
if args.key != "#coronavirus":
    lang = "Korean"
plt.title(f'Top 10 countires with ' + args.key + ' tweets by ' + xLabel, fontproperties=fp)
# plt.tight_layout()


# Determine whether it's lang or country data
data_type = "lang" if "lang" in args.input_path else "country"
# Save the png
if (data_type == "lang" and lang == "English"):
    output_path = os.path.splitext(args.input_path)[0] + f'English_lang_graph.png'
elif (data_type == "lang" and lang == "Korean"):
    output_path = os.path.splitext(args.input_path)[0] + f'Korean_lang_graph.png'
elif (data_type == "country" and lang == "English"):
    output_path = os.path.splitext(args.input_path)[0] + f'English_country_graph.png'
else:
    output_path = os.path.splitext(args.input_path)[0] + f'Korean_country_graph.png'

plt.savefig(output_path)


