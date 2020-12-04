import random
 
print('\nPassword Generator\n==================\n')
 
alphabets =['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P']
small = ['a','b','c','d','e','z','o','t','h','l','x','w']
numbers = ['1','2','3','4','5','6','7','8','9','0']
chars = ['!','@','#','$','*','|','%']

#combined list and made it as one 
characters= small + numbers + chars + alphabets
 
#modified user input
pass_length = int(input("Desired length of password: "))

#adjusted output to meet specific length
password=""
for x in range(pass_length):
    password = password + random.choice(characters)
   
for x in password:
    break
 
print("your random password is:", password)
