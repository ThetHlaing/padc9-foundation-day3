#request in input (n) from user
#create n+nn+nnn from the inputted value
#for eg. if the input is 1,  1+11+111 = 123

a = int(input('Input an integer : ')) # 5

doublea = int(f"{a}{a}") # 55
triplea = int(f"{a}{a}{a}") # 555

print( int(a) + int(doublea) + int(triplea))



