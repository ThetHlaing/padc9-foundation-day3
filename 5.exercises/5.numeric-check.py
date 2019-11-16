 #check if the inputted string is numeric.

def isNumberic(a):
    try:
        a =  float(a)
        return True
    except ValueError:
        return False
    except : 
        pass

print(isNumberic('123')) # true
print(isNumberic('123a')) # false
print(isNumberic('bcd')) # false
print(isNumberic('123.32')) # true