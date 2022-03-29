import random
from emoji import emojize

def same_diff(ch):
    same = emojize(":raised_back_of_hand: :raised_back_of_hand: :raised_hand: :raised_hand:")
    different = emojize(":raised_back_of_hand: :raised_hand:",)
    if ch == "same":
        return print(same)
    elif ch == "different":
        return print(different)
    else:
        print("input a valid one")

print("So you guys are in trouble and want to decide whether what! \n")
user_choice=input("It's okay then! choose one from same or different this same \n as you played in your childhood: ")
print("you have choosen: ",user_choice)
same_diff(user_choice)

options=["same", "different"]
computer_choise = random.choice(options)

if user_choice =="same" or user_choice == "different":
    print("\nOkay now if I WIN your gonna listen to your friend...")

    print("I have choosed too: ",computer_choise)

    same_diff(computer_choise)

if user_choice == computer_choise:
    print(emojize(":smirking_face:")+" You Won")
elif computer_choise == "different" and user_choice == "same" or computer_choise =='same' and user_choice == 'different':
    print(emojize(":smiling_face_with_sunglasses:")+" I Won")
else:
    print('something went wrong')    

