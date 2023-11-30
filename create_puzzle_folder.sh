read -p "Year: " YEAR
read -p "Puzzle num : " NUM

echo "$YEAR $NUM"
mkdir -p "$YEAR/$NUM"

echo "from pathlib import Path\npuzzle_input = Path(__file__).parent.joinpath('puzzle_input.txt')\nwith open(puzzle_input, 'r') as f:\n    lines = [line.strip() for line in f.readlines()]" >> "$YEAR/$NUM/$NUM.py"

echo "Enter the puzzle input :"
while read -r domain
do

    echo "$domain" >> "$YEAR/$NUM/puzzle_input.txt"
done
