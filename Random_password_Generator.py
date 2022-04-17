import random
alphabets = ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"]
numbers= ["0","1","2","3","4","5","6","7","8","9"]
symbols =["!","#","$","%","&","(",")","*","+"]

no_char= int(input("How many Alphabets you want in your password: "))
no_num= int(input("How many Numbers you want in your password: "))
no_symb= int(input("How many Symbols you want in your password: "))
total_alpha = [alphabets,numbers,symbols]
print(total_alpha)
password = ' '

for i in range(1,no_char + 1):
  char_position =  random.randint(0,25)
  print(char_position)
  print(total_alpha[0][char_position])
  password = password + total_alpha[0][char_position]

for i in range(1,no_num + 1):
  num_position =  random.randint(0,9)
  print(num_position)
  print(total_alpha[1][num_position])
  password = password + total_alpha[1][num_position]

for i in range(1,no_symb + 1):
  symb_position =  random.randint(0,9)
  print(symb_position)
  print(total_alpha[2][symb_position])
  password = password + total_alpha[2][symb_position]

print(password)
