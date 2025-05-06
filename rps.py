import random

rock = ''' 
                                  88         
                                  88         
                                  88         
8b,dPPYba,  ,adPPYba,   ,adPPYba, 88   ,d8   
88P'   "Y8 a8"     "8a a8"     "" 88 ,a8"    
88         8b       d8 8b         8888[      
88         "8a,   ,a8" "8a,   ,aa 88`"Yba,   
88          `"YbbdP"'   `"Ybbd8"' 88   `Y8a  
'''

paper = '''
 _ __   __ _ _ __   ___ _ __ 
| '_ \ / _` | '_ \ / _ \ '__|
| |_) | (_| | |_) |  __/ |   
| .__/ \__,_| .__/ \___|_|   
| |         | |              
|_|         |_|    
'''

scissor = '''
   ____
  / __ \
 ( (__) |___ ___
  \________,'   """""----....____
   _______<  () dd       ____----'
  / __   __`.___-----""""
 ( (__) |
  \____/
  '''


game_images = [rock, paper, scissor]

user_choice = int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissor. \n"))
if user_choice >=0 and user_choice <= 2:
    print("Your Choice: ", game_images[user_choice])

comp_choice = random.randint(0, 2)
print("Computer Choice: ", game_images[comp_choice])

if user_choice >2 or comp_choice < 0:
    print("You entered an invalid number. You lose!")
elif user_choice == 0 and comp_choice == 2:
    print("You Winn!")
elif comp_choice == 0 and user_choice == 2:
    print("You loose!")
elif comp_choice > user_choice:
    print("You lose!")
elif user_choice > comp_choice:
    print("You win!")
elif user_choice == comp_choice:
    print("It's Draw!")
