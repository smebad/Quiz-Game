print("Welcome to my Quiz Game")

play = input("Do you want to play? ")

if play.lower() != "yes":
  quit()

print("Okay! Let's play")
score = 0

# Question 1
reply = input("What does AI stand for? ")
if reply.lower() == "artificial intelligence":
  print("The answer is Correct!")
  score += 1
else:
  print("Wrong! The answer is Artificial Intelligence")

# Question 2
reply = input("What does CPU stand for? ")
if reply.lower() == "central processing unit":
  print("The answer is Correct!")
  score += 1
else:
  print("Wrong! The answer is Central Processing Unit")

# Question 3
reply = input("What does GPU stand for? ").lower()
if reply == "graphics processing unit":
  print("The answer is Correct!")
  score += 1
else:
  print("Wrong! The answer is Graphics Processing Unit")

# Question 4
reply = input("What does RAM stand for? ").lower()
if reply == "random access memory":
  print("The answer is Correct!")
  score += 1
else:
  print("Wrong! The answer is Random Access Memory")

# Question 5
reply = input("What does ROM stand for? ").lower()
if reply == "read only memory":
  print("The answer is Correct!")
  score += 1
else:
  print("Wrong! The answer is Read Only Memory")

print("You got " + str(score) + " questions correct!")
print("You got " + str((score / 5) * 100) + "%")