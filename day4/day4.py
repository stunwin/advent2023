import string
import pathlib

def main():
    p = pathlib.Path("C:/Users/stunwin/Code/advent2023/day4/input.txt")
    winners = []
    picks = []
    total = 0
    
    with open(p, "r") as input:
        input = input.read().splitlines()

    for line in input:
        winners.append([int(i) for i in line.split(" | ")[0].split(": ")[1].split()])
        picks.append([int(i) for i in line.split(" | ")[1].split()])

    for i, pick in enumerate(picks):
        wincount = 0
        for num in picks[i]:
            if num in winners[i]:
                wincount += 1
        if wincount > 0:        
            total += 2 ** (wincount - 1)
    
    print(total)
    
main()
