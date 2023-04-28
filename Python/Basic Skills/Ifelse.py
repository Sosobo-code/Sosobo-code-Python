#Movie Score Gmae
import random
movie1 = ("Avengers & Guardians of The Galaxy")
movie2 = ("Toy Story 3 & Toy Story 4")
movie3 = ("Top Gun Maverick & Top Gun")
movie4 = ("Star Wars Revenge of The Sith, Star Wars Return of The Jedi")
list1 = [movie1, movie2]
list2 = [movie3, movie4]
introduction = input("""Hello, in this game you will be guessing which movies have a higher rating on rotten tomatoes. If you get 1 wrong, you lose
Are you ready to begin
>""")
                     
if introduction == "yes":
    print("good")

question1 = random.choice(list1)
question2 = random.choice(list2)

if question1 == movie1:
    answer1 = input("""Which has a higher score Avengers or Guardians of The Galaxy (type gotg)?
    
    >""")
    answer1 = answer1.lower()
    if answer1 == "avengers":
        print("GOOD JOB")

        if question2 == movie3:
            answer2 = input("Which movie has a higher score, Top Gun or Top Gun Maverick? (top gun m)")

            if answer2 == "top gun":
                print("""WRONG
                
                YOU LOSE""")
                exit()

            if answer2 == "top gun m":
                print("GOOD JOB!!!!!!")


        if question2 == movie4:
            answer2 = input("Which has a higher rating, Star wars revenge of the sith (rots), or star wars return of the jedi? (rotj)")
            if answer2 == "rots":





        elif answer1 == "gotg":
        print("""WRONG
        
        
        YOU LOSE""")
        exit()

if question1 == movie2:
    answer1 = input("""Which has a higher score, Toy Story 3, or Toy Story 4
    
    >""")
    answer1 = answer1.lower()

if answer1 == "toy story 3":
    print("GOOD JOB!!!!!")

elif answer1 == "toy story 4":
    print("""WRONG
    
   
    YOU LOSE""")
    exit()
    
