#made new imports
import random
import array

#7. created title for the passsword generator
print('\nJacobs Password Generator:\n')

#1. Changed the default values for the function and created arrays for all the elements of the password for me to better understand.
id_length = 12
CAPITAL_alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z'] 
LOWER_alphabet = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'M', 'N', 'O', 'p', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'] 
DIGITS = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
SYMBOLS = ['@', '#', '$', '%', '=', ':', '?', '.', '/', '|', '~', '>', '*', '(', ')'] 

#2.combined all my arrays
COMBINED_ELEMENTS = DIGITS + CAPITAL_alphabet + LOWER_alphabet + SYMBOLS 
  

#3.created an easier way to generate a special character in the random password generator as well as the other random elements. 
random_digit = random.choice(DIGITS) 
random_upper = random.choice(CAPITAL_alphabet) 
random_lower = random.choice(LOWER_alphabet) 
random_symbol = random.choice(SYMBOLS) 

#4.combined the random elements selected above to create a temporary 4 element long password.
temporary_pass = random_digit + random_upper + random_lower + random_symbol 

#5.extended that 4 element passsword above to 12 for the complete password by pulling from the combined arrays above."combined elements"
for x in range(id_length - 4): 
    temporary_pass = temporary_pass + random.choice(COMBINED_ELEMENTS) 

#6.created a loop to enter the additional 8 elements 
password = "" 
for x in temporary_pass: 
        password = password + x 
          
print(password) 
  



