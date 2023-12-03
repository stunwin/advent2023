import sys
import string




def main():
    total = 0
    numwords = ["oneight", "threeight", "fiveight", "nineight", "eightwo", "eighthree", "one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]
    replacements = ["18", "38", "58", "98", "82", "83", "1", "2", "3", "4", "5", "6", "7", "8", "9"]
    fixedlist = []
    with open(sys.argv[1], "r") as input:
        list = input.read().splitlines() 

    # print(list)
   
   #still coming up short with 53280  
    for i in list:
        for n in numwords:
            i = i.replace(n, replacements[numwords.index(n)])
        fixedlist.append(i)
        # print(i)
    
    #print(fixedlist)
    
    for i in fixedlist:
        numbers = ""
        for j in i:
            if j in string.digits:
                numbers = numbers + j
        value = numbers[0] + numbers[-1]
        total += int(value)
       
    print(total)
    
main()    

