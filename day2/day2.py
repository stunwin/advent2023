import sys

def main():
    total = 0  
    load = {
        "red": 12,
        "green": 13,
        "blue": 14
    }
    
    with open(sys.argv[1], "r") as input:
        list = input.read().splitlines()
    
    for idx, game in enumerate(list, start=1):
        valid = True
        game = game.split(": ", 1)[1]
        pulls = game.split("; ")
        for pdx, pull in enumerate(pulls):
            dice = pull.split(", ")
            for die in dice:
                if int(die.split(" ")[0]) > load[die.split(" ")[1]]:
                    valid = False
                    break
            else:
                continue
            break
        if valid:
            total += idx
            
    print(total) #3059
        
main()