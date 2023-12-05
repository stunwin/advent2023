import sys
import string
import pathlib

def main():
    p = pathlib.Path("C:/Users/stunwin/Code/advent2023/day3/input.txt")
    
    with open(p, "r") as input:
        grid = input.read().splitlines()
    
    valid_parts = []
    total = 0
    found = False
    for x, line in enumerate(grid):
        if found:
            num_end = y
            found = False
            charscan(grid, x - 1, num_start, num_end, valid_parts)
        for y, char in enumerate(line):
            if (char not in string.digits and not found) or (char in string.digits and found):
                continue
            elif (char in string.digits and not found):
                num_start = y
                found = True
            elif ((char not in string.digits or y > len(line) - 1) and found):
                num_end = y
                found = False
                charscan(grid, x, num_start, num_end, valid_parts)
                
    for part in valid_parts:
        total += part
    print(valid_parts)
    print(total)
                
def charscan(grid, line, start, end, valid_parts):
    for i in range(start,end):
        for x in range(-1,2):
            for y in range(-1,2):
                if (line + x < 0 or line + x > len(grid) - 1) or (i + y < 0 or i + y > len(grid[0]) - 1):
                    continue
                elif grid[line+x][i+y] not in string.digits and grid[line+x][i+y] != ".":
                     valid_parts.append(int(grid[line][start:end]))
                     return

main()