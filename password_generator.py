#Password Generator Project
import random
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the PyPassword Generator!")
total = int(input("How many letters would you like in your password?\n")) 
symbol = int(input(f"How many symbols would you like?\n"))
number = int(input(f"How many numbers would you like?\n"))


while(total!=0):
    x = random.randint(0,2)
    if(x==0 and symbol!=0):
        symbol = symbol - 1
        y = random.randint(0, len(symbols)-1)
        print(symbols[y], end="")
    elif(x==2 and number!=0):
        number = number - 1
        y = random.randint(0, len(numbers)-1)
        print(numbers[y], end="")
    else:
        y = random.randint(0, len(letters)-1)
        print(letters[y], end="")    
    total = total - 1         



