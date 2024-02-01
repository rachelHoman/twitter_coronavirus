#!/bin/bash

# Assuming your dataset files are in a directory named 'dataset'
# Adjust the path accordingly if your dataset is in a different location

for input_file in dataset/*.zip; do
    # Use the glob * to select only the tweets from 2020
    if [[ $input_file == *"2020"* ]]; then
        # Extract the base name of the file without extension
        base_name=$(basename -- "$input_file")
        base_name_no_ext="${base_name%.*}"

        # Run map.py in the background using nohup and &
        nohup python3 map.py --input_path "$input_file" --output_folder "outputs" > "$base_name_no_ext.log" 2>&1 &
    fi
done
