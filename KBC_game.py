#kbc game 
# approach is to get 5 quesions with the options and their answers as well
print("Hello and welcome to our game of Kon Banega Crorepati!")
print("For each correct answer, you get prize amount and move to next question ")

q_list=["whats the colour of watermelon?",
        "there are how many 2 digit numbers?",
        "who gave laws of motion?",
        "how many continents in world?",
        "whats the name of actor playing caption america?",
        ]
a_list=["A.red \nB.green \nC.brown \nD.black",
        "A.100 \nB.84 \nC.89 \nD.90 ",
        "A.einstine \nB.newton \nC.feyman  \nD.edison",
        "A.5 \nB.9 \nC.2 \nD.7",
        "A.chris evans \nB.rock \nC.chris hemsworth \nD.daniel craig"]
answers=["B",
         "D",
         "B",
         "D",
         "A"]
print("starting with questions:\n")
for i in range(0,5):
        z = (i+1)*10000
        print(q_list[i])
        print(a_list[i])
        print("choose one option:")
        ans=input(str(""))
        
        if ans==answers[i]:
                 print("correct answer!! move to next question!")
                 print("your prize amount till now:",z)
        else:
                print("wrong answer!, journey stops")
                print("your prize amount till now:",z-10000)
                break
if z==50000:
        print("YOU ARE THE ULTIMATE WINNER OF THIS GAME \n keep it up!!")
else:
        print("close but well played!")

