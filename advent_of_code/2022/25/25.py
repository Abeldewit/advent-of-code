from pathlib import Path
import string

puzzle_input = Path(__file__).parent.joinpath('puzzle_input.txt')
with open(puzzle_input, 'r') as f:
    lines = [line.strip() for line in f.readlines()]
    

def snafu_to_decimal(snafu_line):
    line_parts = list(snafu_line)
    line_parts = [
        int(v) if v not in ('=', '-') else
        (-2 if v == '=' else -1)
        for v in line_parts
    ]
    number_places = [5**i for i in range(len(snafu_line))][::-1]
    part_calculation = [v[0] * v[1] for v in zip(line_parts, number_places)]
    return sum(part_calculation)

def decimal_to_snafu(decimal: int):
    digits = "=-012"
    base = len(digits)
    offset = digits.index("0")
    
    snafu = ""
    while decimal:
        shifted_index = (decimal + offset) % base
        snafu += digits[shifted_index]
        if shifted_index < offset:
            decimal += base
        decimal //= base
        
    return snafu[::-1]


input_decimals = []    
for line in lines:
    line_decimal = snafu_to_decimal(line)
    input_decimals.append(line_decimal)
    
    snafu_back = decimal_to_snafu(line_decimal)
    print(line == snafu_back, line_decimal)

total_fuel = sum(input_decimals)
total_fuel_snafu = decimal_to_snafu(total_fuel)

print(total_fuel_snafu)