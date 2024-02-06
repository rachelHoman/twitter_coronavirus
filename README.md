# Coronavirus twitter analysis

In this project I scanned all geotagged tweets sent in 2020 to monitor for the spread of the coronavirus on social media. In order to complete this I used large scale data sets, worked with multilingual text, and used the MapReduce divide-and-conquer paradigm to create parallel code.

For this project I used geotagged Tweets. Approximately 500 million tweets are sent everyday. Of those tweets, about 2% are geotagged. In total, there are about 1.1 billion tweets in this dataset. The tweets were stored by days in `.zip` files in the format: `geoTwitterYY-MM-DD.zip`. Inside each zip file there are 24 text files, one for each hour of the day. Each text file contains a single tweet per line in `JSON` format.

I followed these steps in order to visualize the coronavirus data on Twitter:

1. Created a mapper. This is the `map.py` file that is located in the src/ folder. This file tracks the usage of the hashtags on both a language and country level. It outputs two files: one that ends in `.lang` and one that ends in `.country`.

2. Ran the mapper. To run `map.py` I created a shell script `run_maps.sh` that loops over each file in the dataset and runs the `map.py` command on that file.

3. Reduce. The files outputed from the `run_maps.sh` file are stored in the `outputs/` folder. Using the `reduce.py` file found in the `src/` folder, `reduce.py` combines all the `.lang` files into a single file and all of the `.country` files into a different file.

4. Visualize. The `visualize.py` file, found in the `src/` folder, generates a bar graph of the results and stores the bar graph as a `.png` file. The final results are sorted from low to high, and only include the top 10 keys. I created 4 different pngs: two with the `--key` set to `#coronavirus` (one based on the languages and the other based on the countries) and two with the `--key` set to `#코로나바이러스` (again a language and then a country png).

<img src=src.png />

5. Alternative reduce. Lastly, I created a new reduce file that take as input on the command line a list of hashtags, and output a line plot where there is one line per input hashtag, the x-axis is the day of the year, and the y-axis is the number of tweets that use that hashtag during the year.



