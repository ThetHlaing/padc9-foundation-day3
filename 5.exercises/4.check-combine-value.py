#Check if the given integer numbers are the same or 
# their difference or sum is greater than 20

def test_number20(a,b):
    if(a==b or abs(a-b) >= 20 or a+b >= 20):
        return True
    else:
        return False


print(test_number20(21, 1))
print(test_number20(5, 15))
print(test_number20(1, 5))        
print(test_number20(8, 8))        

