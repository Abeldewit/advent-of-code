# read -p "Year: " YEAR
# read -p "Puzzle num : " NUM

# mkdir -p "advent_of_code/$YEAR/$NUM"

# cp "solution_template.py" "advent_of_code/$YEAR/$NUM/$NUM.py"
#!/bin/bash

# Get arguments or determine defaults
YEAR=$1
NUM=$2

# Define base directory
BASE_DIR="advent_of_code"

# If no YEAR provided, find the latest year folder
if [ -z "$YEAR" ]; then
  if [ -d "$BASE_DIR" ]; then
    YEAR=$(ls -d $BASE_DIR/*/ 2>/dev/null | awk -F'/' '{print $(NF-1)}' | sort -nr | head -n1)
  fi
  # Default to current year if no folders found
  YEAR=${YEAR:-$(date +%Y)}
fi

# If no NUM provided, find the latest NUM for the given YEAR
if [ -z "$NUM" ]; then
  if [ -d "$BASE_DIR/$YEAR" ]; then
    NUM=$(ls -d $BASE_DIR/$YEAR/*/ 2>/dev/null | awk -F'/' '{print $(NF-1)}' | sort -n | tail -n1)
    NUM=$((NUM + 1))
  else
    NUM=1
  fi
fi

# Create directory and copy template
TARGET_DIR="$BASE_DIR/$YEAR/$NUM"
mkdir -p "$TARGET_DIR"
sed \
  -e "s/{YEAR}/$YEAR/g" \
  -e "s/{DAY}/$NUM/g" \
  solution_template.py > "$TARGET_DIR/$NUM.py"

# Run the solution script
python "$TARGET_DIR/$NUM.py"
