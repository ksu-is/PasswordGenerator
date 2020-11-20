import random
 
print('\nPassword Generator\n==================\n')
 
alphabets =['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P']
small = ['a','b','c','d','e','z','o','t','h','l','x','w']
numbers = ['1','2','3','4','5','6','7','8','9','0']
chars = ['!','@','#','$','*','|','%']

 
ran_1  = random.choice(small)  + str(random.choice(numbers)) + random.choice(chars) + random.choice(alphabets)
ran_2 = random.choice(small)  + str(random.choice(numbers)) + random.choice(chars) + random.choice(alphabets)
 
pass_length = int(input("Desired length of password (4 or 8 characters long): "))

if pass_length <= 4:
    for i in range(pass_length):
        password=ran_1
elif pass_length >= 5:
    for i in range(pass_length):
        password = ran_1+ran_2
 
print("your random password is:", password)
