print("Welcome to the Game Good Luck")
print("Rules of the Game : ")
print("Winning Rules as follows:\nRock vs paper-> paper wins\nRock vs scissor-> Rock wins\npaper vs scissor-> scissor wins.")
replay_game = True
while replay_game:
    print("Enter your choice : \n1 - Rock \n2 - Paper\n - Scissors")
    choice = int(input("Enter your choice : "))
    if(choice == 1)