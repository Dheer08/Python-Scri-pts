import random

print("Enter the range of numbers : ")
range_a = int(input("Enter a staring range integer number : "))
range_b = int(input("Enter a ending range integer number : "))
ran_num = random.randint(range_a,range_b)
print("A value has been picked by computer : ",ran_num)
num = int(input("Guess  the number : "))
count = 1

while ran_num != num : 
    count = count + 1
    if num > ran_num: 
        print("THe Guess is wrong, you Guessed too high") 
    elif num < ran_num: 
        print("The Guess is wrong, you Guessed too low")
    else :
        continue
    num = int(input("Guess the number : "))

print(f"Congratualtion! you Finally guessed the Number in {count} guesses")