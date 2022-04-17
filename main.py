import random
alphabets = ["a","b","c","e","f","g","h","i","j","k","l"]
numbers= ["0","1","2","3","4","5","6","7","8","9"]
symbols =["!","#","$","%","&","(",")","*","+"]

no_char= int(input("How many Alphabets you want in your password: "))
#no_num= int(input("How many Alphabets you want in your password: "))
#no_symbol= int(input("How many Alphabets you want in your password: "))
total_alpha = [alphabets,numbers,symbols]
print(total_alpha)
password = ' '
for i in range(0,no_char):
  char_position =  random.randint(1,11)
  print(char_position)
  password = password + total_alpha[char_position]
  print(password)
