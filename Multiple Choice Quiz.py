#Computers and Technology Quiz

#Time module.
import time
print("Welcome to the quiz about technology.")

#points

    #Questions tuple

questions = ("what is 2 + 2? \n (a) 5\n (b) 4\n (c) 9\n (d) 2\n", #0
             "What major new operating system was released in 2015? \n (a) Mac OS X\n (b) Windows 10\n (c) Windows 8\n (d) Ubuntu\n", #1
             "What was the first programming language ever created. \n (a) C\n (b) FORTRAN\n (c) python\n (d) MALBOLGE\n", #2
             "Who are the founders of valve corp?\n (a) Gabe Newell and Mike Harrington\n (b) Mike Harrington and Steve Wozniak\n (c) Steve Wozniak and Gabe Newell\n (d) Thomas Wayne and Gabe Newell?\n", #3
             "What does Valve specialize in?\n (a) Digital Editing Software and Photoediting software\n (b) Video Game Developers and Digital Publishing\n (c) Automotive Modifications\n (d) Search Engine Parent Corportation.\n",
             "What year was IBM founded?\n (a) 1967\n (b) 1971\n (c) 1932\n (d) 1911\n",
             "True or False:\n The United States is home to the fastest internet speed in the world\n (a) True\n (b) False",
             "Which Country has the fasted Internet Conection in the world?\n (a) Canada\n (b) South Korea\n (c) Japan\n (d) United Arab Emirates") 

answers = ("b", "b", "b", "a", "b", "d", "b", "c")

# Once the user has completed the quiz, they are asked whether or not they want to play again.
def playagain():
    play_again = input("would you like to play again y/n : ")
    if play_again == "y":
        return True
    else:
        print("Thanks for Playing")
        return False
    
    #

def askquestion():
    points = 0 #points start at 0 and get +1 after each correct answer.
    for i in range(len(questions)): #Gets length of questions.
        print(questions[i]) #The index is i. This means after each loop it will roll over to the next index. So it will start at 0, then go 1, 2, 3... so on
        guess = input("    :")
        guess = guess.lower() # Makes sure that the guesses aren't case sensitive.
        if guess == answers[i]:
            print("Correct")
            points += 1 #adds on a point.
            print(f"you have earned {points} points so far") #I print out the amount of points to make sure the code works.
            time.sleep(1) #adds a pause of 1 second between each question
            print("___________________________")
        else:
            print("Incorrect")
            time.sleep(1) #adds a pause of 1 second between each question
            print("___________________________")
    
    #Calculates percentage of score
    if points > 0:
        score = points / 15 * 100
        print(f"you got {score} %")


askquestion()

#If the user responed (y) to playagain, it runs the askquestion() function again, meaning the game is started

while playagain():
    askquestion()


###I have commented everything beyond this point because there was unncessessary repitition.
    


# #Where the questions are printed.
# q1 = input(questions[0])

# if q1 == answers[0]:
#     print("Good, you are elligible to do this quiz.!")
#     points += 1
# else:   #Exits script meaning you are not elligible to complete quiz.
#     print("May god help you...")
#     exit()

# q2 = input(questions[1])

# if q2 == answers[1]:
#     print("CORRECT!")
#     points += 1
# else:
#     print("WRONG :(.")

# q3 = input(questions[2])

# if q3 == answers[2]:
#     print("CORRECT!")
#     points += 1
# else:
#     print("WRONG :(.")
# q4 = input(questions[3])

# if q4 == answers[3]:
#     print("CORRECT!")
#     points += 1
# else:
#     print("WRONG :(.")
# q5 = input(questions[4])

# if q5 == answers[4]:
#     print("CORRECT!")
#     points += 1
# else:
#     print("WRONG :(.")
# q6 = input(questions[5])
# if q6 == answers[5]:
#     print("CORRECT, you may continue onto the next question.")
#     points += 1
# else:
#     print("...")
#     print("you got", points, "points")
#     exit()
