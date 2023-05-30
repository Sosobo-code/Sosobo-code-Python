#Computers and Technology Quiz

#Time module.
import time
print("Welcome to the quiz about technology. There are 15 questions. Each question gets harder as it goes.")

#points

    #Questions tuple

questions = ("1. what is 2 + 2? \n (a) 5\n (b) 4\n (c) 9\n (d) 2\n", #0
             "2. What major new operating system was released in 2015? \n (a) Mac OS X\n (b) Windows 10\n (c) Windows 8\n (d) Ubuntu\n", #1
             "3. What was the firnguagst programming lae ever created. \n (a) C\n (b) FORTRAN\n (c) python\n (d) MALBOLGE\n", #2
             "4. Who are the founders of valve corp?\n (a) Gabe Newell and Mike Harrington\n (b) Mike Harrington and Steve Wozniak\n (c) Steve Wozniak and Gabe Newell\n (d) Thomas Wayne and Gabe Newell?\n", #3
             "5. What does Valve specialize in?\n (a) Digital Editing Software and Photoediting software\n (b) Video Game Developers and Digital Publishing\n (c) Automotive Modifications\n (d) Search Engine Parent Corportation.\n", #4
             "6. What year was IBM founded?\n (a) 1967\n (b) 1971\n (c) 1932\n (d) 1911\n", #5
             "7. True or False:\n The United States is home to the fastest internet speed in the world\n (a) True\n (b) False", #6
             "8. Which Country has the fasted Internet Conection in the world?\n (a) Canada\n (b) South Korea\n (c) Japan\n (d) United Arab Emirates", #7
             "9. what does GPU stand for?\n (a) Graphical Processing Uploader\n (b) Graphing Processing Unit\n (c) Graphics Processing Unit\n (d) Graphics Processor Unit", #8
             "10. What does CPU stand for?\n (a) Central Process Unit\n (b)Centralized Proccesser Units\n (c) Central Processing Unit\n (d) Cententrally Processed Utility", #9
             "11. How many Mb is 4Gb?\n (a) 4000mb\n (b) 4096mb\n (c)4028mb\n (d)4128mb", #10
             "12. What is larger than a Petabyte, but smaller than a Zettabyte?\n (a) Picobyte\n (b) Ultrabyte\n (c) Exabyte\n (d) Yottabyte", #11
             "13. Which Duo were the first Aviators?\n (a) Alex Wright & Wilbur Reed\n (b) Wilbur Wright & Orville Wright\n (c) Alex Reed & Orville Reed\n (d) Wilbur Wright & Orville Reed", #12
             "14. What is the best selling GPU as of 2023?\n (a) Nvidia Geforce RTX 3060\n (b) Nvidia Geforce GTX 1080\n (c)Nvidia Geforce 1650Ti\n (d)AMD RX 580\n", #13
             "15. Which of these is not a real operating system?\n (a)Unix\n (b) Ux2-DOS\n (c) MS-DOS\n (d) DR-DOS") #14

#Answers
answers = ("b", "b", "b", "a", "b", "d", "b", "c", "c", "c", "b", "c", "b", "a", "b")


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
            time.sleep(1)#adds a pause of 1 second between each question
            points += 1 #adds on a point
            print("___________________________")
        else:
            print("Incorrect")
            time.sleep(1)#adds a pause of 1 second between each question
            print("___________________________") #Is a line breaker, makes it cleaner.
    
    #Calculates percentage of score:
    if points >= 0:
        score = points / len(questions) * 100
        round(score, 2)
        print(f"you got {score} %\n")
        print("The correct answers were...\n 1: (b) - 4\n 2: (b) - Windows 10\n 3: (b) - FORTRAN\n 4: (a) - Gabe Newell and Mike Harrington\n 5: (b) - Video Game Developers and Digital Publishing\n 6: (d) - 1911\n 7: (b) - False\n 8: (c) - Japan\n 9: (c) Graphics Proccessing Unit\n 10: (c) - Central Processing Unit\n 11: (b) - 4096Mb\n 12: (c) - Exabyte\n 13: (b) - Wilblur Wright & Orville Wright\n 14: (a) - Nvidia Geforce RTX 3060\n 15: (b) Ux2-DOS")

askquestion()

#If the user responed (y) to playagain, it runs the askquestion() function again, meaning the game is started

while playagain():
    askquestion()
