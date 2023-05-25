#Computers and Technology Quiz

print("Welcome to the quiz about technology.")

#points

points = 0
j = 0
    #Questions tuple

questions = ("what is 2 + 2? \n (a) 5\n (b) 4\n (c) 9\n (d) 2\n     :", #0
             "What major new operating system was released in 2015? \n (a) Mac OS X\n (b) Windows 10\n (c) Windows 8\n (d) Ubuntu\n     : ", #1
             "What was the first programming language ever created. \n (a) C\n (b) FORTRAN\n (c) python\n (d) MALBOLGE\n    :", #2
             "Who are the founders of valve corp?\n (a) Gabe Newell and Mike Harrington\n (b) Mike Harrington and Steve Wozniak\n (c) Steve Wozniak and Gabe Newell\n (d) Thomas Wayne and Gabe Newell?\n   :", #3
             "What does Valve specialize in?\n (a) Digital Editing Software and Photoediting software\n (b) Video Game Developers and Digital Publishing\n (c) Automotive Modifications\n (d) Search Engine Parent Corportation.\n     :") #4

answers = ("b", "b", "b", "a", "b")

guess = []


#Where the questions are printed.
q1 = input(questions[0])

if q1 == answers[0]:
    print("Good, you are elligible to do this quiz.!")
    points += 1
else:   #Exits script meaning you are not elligible to complete quiz.
    print("May god help you...")
    exit()

q2 = input(questions[1])

if q2 == answers[1]:
    print("CORRECT!")
    points += 1
else:
    print("WRONG :(.")

q3 = input(questions[2])

if q3 == answers[2]:
    print("CORRECT!")
    points += 1
else:
    print("WRONG :(.")
q4 = input(questions[3])

if q4 == answers[3]:
    print("CORRECT!")
    points += 1
else:
    print("WRONG :(.")
q5 = input(questions[4])

if q5 == answers[4]:
    print("CORRECT!")
    points += 1
else:
    print("WRONG :(.")



