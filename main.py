import random
alphabets = ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"]
numbers= ["0","1","2","3","4","5","6","7","8","9"]
symbols =["!","#","$","%","&","(",")","*","+"]

no_char= int(input("How many Alphabets you want in your password: "))
no_num= int(input("How many Numbers you want in your password: "))
no_symb= int(input("How many Symbols you want in your password: "))
total_alpha = []
password = ' '

for i in range(1,no_char + 1):
#  char_position =  random.randint(0,25)
#  print(total_alpha[0][char_position])
#  password = password + total_alpha[0][char_position]
  random_char = random.choice(alphabets) #it will choose random character from alphabet list randomly
  total_alpha += random_char
  

for i in range(1,no_num + 1):
  random_numb = random.choice(numbers) #it will choose random character from alphabet list randomly
  total_alpha += random_numb

for i in range(1,no_symb + 1):
  random_symb = random.choice(symbols) #it will choose random character from alphabet list randomly
  total_alpha += random_symb
  
print(total_alpha)
