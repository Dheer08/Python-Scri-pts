import random


words = ["Optmizer","Linear","Regression","Adam","Scalar","Vector","Matrix"]
ran_num = random.randint(1,len(words))
ran_word = words[ran_num]
print("random number : ",ran_num)
print("random Word : ",ran_word)
# ran_word = random.choice(words)
name = input("Enter your name : ")
print("Good Luck ",name)

print("Len of word : ",len(ran_word))
len_word = len(ran_word)

turns = 12
guess_word = ""

while turns > 0:
    fail = 0
    inp_char = str(input("Guess a character : "))
    if char in ran_word:
        if inp_char in guess_word:
            print(char,end="")
        else:
            print("_",end="")
            fail = fail + 1
    if fail == 0:
        print("You win")
        print(f"The Word is {ran_word}")
        break
    turns = turns -1
    print(f"You have {turns} left")


