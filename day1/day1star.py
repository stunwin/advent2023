import sys
import string




def main():
    total = 0
    numwords = ["oneight", "twone", "threeight", "fiveight", "sevenine", "eightwo", "eighthree", "nineight", "one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]
    replacements = ["18", "21", "38", "58", "79", "82", "83", "98", "1", "2", "3", "4", "5", "6", "7", "8", "9"]
    fixedlist = []
    with open(sys.argv[1], "r") as input:
        list = input.read().splitlines() 

    for i in list:
        for n in numwords:
            i = i.replace(n, replacements[numwords.index(n)])
        fixedlist.append(i)
    
    for i in fixedlist:
        numbers = ""
        for j in i:
            if j in string.digits:
                numbers = numbers + j
        value = numbers[0] + numbers[-1]
        total += int(value)
       
    print(total)
    
main()    

