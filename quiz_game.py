print("Welcome to my computer quiz!")

playing = input("Do you want to play? ").lower()

if playing != 'yes':
    quit()

print("Okay! Let's play :)")
score = 0

question1 = input("What does CPU stands for? ").lower()
if question1 == "central processing unit":
    print("Great That's Correct!")
    score += 1
else:
    print("Oops Incorrect!")


question2 = input("What does RAM stands for? ").lower()
if question2 == "random access memory":
    print("Great That's Correct!")
    score += 1
else:
    print("Oops Incorrect!")


question3 = input("What does GPU stands for? ").lower()
if question3 == "graphics processing unit":
    print("Great That's Correct!")
    score += 1
else:
    print("Oops Incorrect!")


question4 = input("What does ROM stands for? ").lower()
if question4 == "read only memory":
    print("Great That's Correct!")
    score += 1
else:
    print("Oops Incorrect!")


question5 = input("What does GUI stands for? ").lower()
if question5 == "graphical user interface":
    print("Great That's Correct!")
    score += 1
else:
    print("Oops Incorrect!")

print("You answered", score ,"questions correctly!")
print("You got", ((score/5)) * 100 ,"%")
