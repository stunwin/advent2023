import sys
import string




def main():
    total = 0
    numwords = ["one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]
    replacements = ["1", "2", "3", "4", "5", "6", "7", "8", "9"]
    fixedlist = []
    with open(sys.argv[1], "r") as input:
        list = input.read().splitlines() 

    print(list[:10])
   
   #HAHAHA THIS DOESNT WORK because numbers can share a letter kill me  
    for i in list:
        for n in numwords:
            i = i.replace(n, replacements[numwords.index(n)])
        fixedlist.append(i)
    
    print(fixedlist[:10])
    
    for i in fixedlist[:10]:
        numbers = ""
        for j in i:
            if j in string.digits:
                numbers = numbers + j
        value = numbers[0] + numbers[-1]
        print(value)
        total += int(value)
       
    print(total)
    
main()    
