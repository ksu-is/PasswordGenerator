import random
 
print('\nPassword Generator\n==================\n')
 
alphabets =['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P']
small = ['a','b','c','d','e','z','o','t','h','l','x','w']
numbers = ['1','2','3','4','5','6','7','8','9','0']
chars = ['!','@','#','$','*','|','%']

combined = alphabets + small + numbers + chars
 
ran_1  = random.choice(small)  + str(random.choice(numbers)) + random.choice(chars) + random.choice(alphabets)
 
ran_2 = random.choice(small)  + str(random.choice(numbers)) + random.choice(chars) + random.choice(alphabets)
 
random_password = ran_1 + ran_2
 
print("your random password is:", random_password)
