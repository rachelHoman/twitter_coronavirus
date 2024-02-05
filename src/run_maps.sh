#bin/sh

for file in /data/Twitter\ dataset/geoTwitter20*.zip; do
    # /home/rmha2020/twitter_coronavirus/src/map.py --input_path="$file" &
    nohup /home/rmha2020/twitter_coronavirus/src/map.py --input_path="$file" &
done

