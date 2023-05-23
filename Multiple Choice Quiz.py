#Python General Knowledge quiz

print("Welcome to the quiz about technology.")

#points

points = 0
    #Questions tuple

questions = ("what is 2 + 2? \n (a) 5\n (b) 4\n (c) 9\n (d) 2\n     :",
             "What operating system was released in 2015?")

    #Options
options = (("A. 4", "B. 5", "C. 3", "2"))

answers = ("a", "b")

q1 = input(questions[0])

if q1  == answers[0]:
    print("correct")
