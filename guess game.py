print("GUESS GAME OR DABHI")


print("COUNT TIME 6")


print(" ")

print("jo tame ane computre same number typs karso to tame win:\n [guess is 1 to 2]")

print("   ")

import random

def guess( ):
    computer = random.choice([1, 2])
    you = int(input("guess you number: ")) 
    print(f"you guess: {you} \ncomput guess: {computer}")
    if( computer == you ):
             print("Guess Game win") 
             return True      
    else:
        print("Gueee Game loss")
        return False            
win_count = 0
for i in range(6):
    if guess( ): # AGAR function true retrun kare tab jite
        win_count += 1
print("   ") 
print("  ")                  
print(f"you win {win_count}, out of 6 time!")
print("(Try Again)") 
print ("   ")
guess( )
win_count = 0
for i in range(6):
    if guess( ): # AGAR function true retrun kare tab jite
        win_count += 1
print("   ") 
print("  ")                  
print(f"you win {win_count}, out of 6 time!")
print("(Try Again)")  
print(" ")
guess( )  
win_count = 0
for i in range(6):
    if guess( ): # AGAR function true retrun kare tab jite
        win_count += 1
print("   ") 
print("  ")                  
print(f"you win {win_count}, out of 6 time!")
print("(Try Again)")   