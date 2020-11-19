print("Welcom to my first game!")

# Comments
'''sdasd'''

x = 5
print(x)

name = input("What is your name? ")
age = int(input("What is your age? "))
print("Hello", name, "you are", age, "years old.")

is_older = age >= 18
# print(is_older)

if age >= 18:
    print("You are old enough!")
    wants_to_play = input("Do you want to play? ")
    if wants_to_play == "yes":
        print("Let's play!")
elif age >= 14:
    print("You can play with supervision")
else:
    print("you are not old enough to play...")