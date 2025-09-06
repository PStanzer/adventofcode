#!/bin/bash

# Session Cookie valid until 22.12.2025 (?)
AOC_COOKIE="53616c7465645f5f4fab5f397f434b1cbc18c904814ec680bddf107331ce8c37b1dbf4ab03acc09e64352d62be6a4bbc26bb0513d3566bd7f1bc0dcd453dc45e"

# Check if parameter for old AoC puzzles is present
if [ $1 ]; then
    YEAR=$1
    DAY=$2
else
    YEAR=$(date +%Y)
    DAY=$(date +%-d)
fi

echo "Starting puzzle for $YEAR $DAY"

# Create folder and files
mkdir -p ./$YEAR/$DAY
echo "file = open('sample.txt', 'r')" >> ./$YEAR/$DAY/A.py
echo "" >> ./$YEAR/$DAY/A.py
echo "lines = file.read().split(\"\n\")" >> ./$YEAR/$DAY/A.py
echo "lines.pop()" >> ./$YEAR/$DAY/A.py
echo "print(lines)" >> ./$YEAR/$DAY/A.py
echo "file = open('sample.txt', 'r')" >> ./$YEAR/$DAY/B.py
echo "" >> ./$YEAR/$DAY/B.py
echo "lines = file.read().split(\"\n\").pop()" >> ./$YEAR/$DAY/B.py
echo "lines.pop()" >> ./$YEAR/$DAY/B.py
echo "print(lines)" >> ./$YEAR/$DAY/B.py

# Download puzzle input
echo "Getting input..."
curl --cookie "session=$AOC_COOKIE" https://adventofcode.com/$YEAR/day/$DAY/input > ./$YEAR/$DAY/input.txt

# Link to the puzzle text
echo "Link to Puzzle"
echo "https://adventofcode.com/$YEAR/day/$DAY"

# Option to paste sample input
echo "Past the sample input here. Press 'Ctrl+d' when done!"
echo "$(</dev/stdin)" > ./$YEAR/$DAY/sample.txt

# Opening the files in VSCode
echo "Opening files"
code -r ./$YEAR/$DAY/B.py
code -r ./$YEAR/$DAY/sample.txt
code -r ./$YEAR/$DAY/input.txt
code -r ./$YEAR/$DAY/A.py
