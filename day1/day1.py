import sys
import string




def main():
    total = 0
    
    with open(sys.argv[1], "r") as input:
        list = input.read().splitlines() 


    for i in list:
        numbers = ""
        for j in i:
            if j in string.digits:
                numbers = numbers + j
        value = numbers[0] + numbers[-1]
        total += int(value)
       
    print(total)
    
main()    
