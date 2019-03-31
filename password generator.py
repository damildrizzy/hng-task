import random
import string
characters = list(string.printable)
strength = str(input("Do you want a weak, medium or strong password? "))
length = int(input("How long do you want your password "))
def password(strength, length):
    if strength == "strong":
        new = list(random.sample(characters,length))
        return new
        
print(password(strength,length))
    
                     
