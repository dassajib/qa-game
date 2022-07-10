print("Welcome to my computer quiz!")

playing = input("Do you want to play? ")

if playing.lower() != "yes":
    quit()

print("Okay! Let's play :)")
score = 0

answer = input("Who is the best footballer? ")
if answer.lower() == "cristiano ronaldo":
    print('Correct!')
    score += 1
else:
    print("Incorrect!")

answer = input("Which team is the best football team? ")
if answer.lower() == "real madrid":
    print('Correct!')
    score += 1
else:
    print("Incorrect!")

answer = input("Which team was the champion in world cup 2018? ")
if answer.lower() == "france":
    print('Correct!')
    score += 1
else:
    print("Incorrect!")

answer = input("Which team is the current EURO champion? ")
if answer.lower() == "italy":
    print('Correct!')
    score += 1
else:
    print("Incorrect!")

print("You got " + str(score) + " questions correct!")
print("You got " + str((score / 4) * 100) + "%.")  