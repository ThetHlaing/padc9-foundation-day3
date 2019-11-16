#convert the given list into the string

given_list = [5,32,2,1,8,9,10]


string_list = ''

for item in given_list:
    #string_list = f"{string_list}{item}"
    string_list += str(item)

print(string_list)

