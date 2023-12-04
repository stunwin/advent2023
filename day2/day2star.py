import sys
import string



def main():
    total = 0
    

    
    with open(sys.argv[1], "r") as input:
        list = input.read().splitlines()
    
    for idx, game in enumerate(list, start=1):
        mins = {
            "red": 0,
            "green": 0,
            "blue": 0
        }
        game = game.split(": ", 1)[1]
        pulls = game.split("; ")
        for pdx, pull in enumerate(pulls):
            dice = pull.split(", ")
            mincalc(dice, mins)
        
        total += mins["blue"] * mins["green"] * mins["red"]

            
    
    print(total)


def mincalc(dice, mins):
    for die in dice:
        if int(die.split(" ")[0]) > mins[die.split(" ")[1]]:
            mins[die.split(" ")[1]] = int(die.split(" ")[0])


        
main()