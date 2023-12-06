read -p "Year: " YEAR
read -p "Puzzle num : " NUM

mkdir -p "advent_of_code/$YEAR/$NUM"

cp "solution_template.py" "advent_of_code/$YEAR/$NUM/$NUM.py"