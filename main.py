# Online Python compiler (interpreter) to run Python online.
# Write Python 3 code in this online editor and run it.
print("Quiz Game")
game = input("would like to play the game? ")
if game.lower() == "no":
    print('ok play whenever you want ')
    quit()
print("let's go")
score = 0
question = 0
#question number one
answer = input("what is the stands for CPU ? ").lower()
question += 1
if answer == "centrol processing unit":
   print("your  first Question answer is correct")
   score += 1
else:
    print('incorrect')
#question number two
answer = input("what is the stands for RAM ? ").lower()
question += 1
if answer == "random acsess memory":
    print("your  second question answer is correct")
    score += 1
else:
    print('incorrect')
#question number three
answer = input("what is the stands for ROM ? ").lower()
question += 1
if answer == "read only memory":
    print("your answer is correct")
    score += 1
else:
    print('incorrect')
print("your got " +str(score)+" answer is correct")
print("your got " +str((score/question)*100)+" percentage on the above quiz!")