import time
class run:
    def __init__(self):                                             #initialization statement
        print("FIND IT FIRST 2.0....Bought to you by. Technical Team\n\nExclusively for IGNITE")
        print("*\n*\nUnderstand clues in every level, using your logic and knowledge to win the game")
        while True:
            self.name=input("Enter your uid : ")
            if 100000 <= int(self.name) <= 999999:
                self.level11()
            else:
                 print("Enter a valid id")
    def level11(self):                                              #Level-1 Sublevel-1
        print("Lets start with a warmup")
        print("*\n*\nAnswer this simple Math question")
        print("*\n*\n*\n*\n*\n*\n*\n*\n")
        time.sleep(1)
        try:                                                        #Exception/Error Handling Start
            a=int(input("What is the answer of {[(6+2)x3x5]/2}-10 : "))
            if a==50:
                print("*\n*\n*\nNow lets test your Logic \n Read the question and answer carefully")
                fo=open(self.name+".txt","a")
                fo.write("10\n")
                fo.close()
                self.level12()
            else:
                print("Sorry your Math is weak")
                fo=open(self.name+".txt","a")
                fo.write("-1\n")
                fo.close()
                time.sleep(1)
                self.level11()
        except:                                                     #Exception/Error Handling End
            print("SORRY\nTry Again")
            time.sleep(1)
            self.level11()
    def level12(self):                                              #level-1 Sublevel-2
        print("*\n*\n*\n")
        print("Mr. & Mrs. Mustard have 4 Daughters,\nEach Daughter has 1 Brother")
        time.sleep(1)
        try:                                                        #Exception/Error Handling Start
            b=int(input("How many People in Mustard Family? : "))
            if b==7:
                print("Good, But it's Gonna Get Tough Ahead")
                fo=open(self.name+".txt","a")
                fo.write("10\n")
                fo.close()
                time.sleep(1)
                self.level13()
            else:
                print("Sorry your Logic is weak")
                fo=open(self.name+".txt","a")
                fo.write("-1\n")
                fo.close()
                time.sleep(1)
                self.level12()
        except:                                                     #Exception/Error Handling End
            print("SORRY\nTry Again")
            time.sleep(1)
            self.level12()
    def level13(self):                                              #Level-1 Sublevel-3 Factorial program 9!=362880
        print("*\n*\nGo to the E drive of this computer,\n& locate a folder names uses,\nthere is program named solveme in python and c++ language")
        time.sleep(1)
        try:                                                        #Exception/Error Handling Start
            c=int(input("So whats the Answer? : "))
            if c==362880:
                print("Good\nNow to test your Skills")
                fo=open(self.name+".txt","a")
                fo.write("10\n")
                fo.close()
                time.sleep(1)
                self.level21()
            else:
                print("Sorry that is not what i want")
                fo=open(self.name+".txt","a")
                fo.write("-1\n")
                fo.close()
                self.level13()
        except:                                                     #Exception/Error Handling End
            print("SORRY\nTry Again")
            self.level13()
        
    def level21(self):                                              #Level-2 Sublevel-1
        print("\n\n\nThis is the test of your Technical Knowledge")
        print("*\n*\n*\n")
        print("I am a Computer,\nI only inderstand 1's and 0's")
        time.sleep(1)
        try:                                                    #Exception/Error Handling Start
            d=int(input("What is 0101x0011 : "))
            if d==1111:
                print(":) AWW! You really understand me\n Lets go ahead")
                fo=open(self.name+".txt","a")
                fo.write("10\n")
                fo.close()
                time.sleep(1)
                self.level22()
            else:
                print(":( You dont Understand me")
                fo=open(self.name+".txt","a")
                fo.write("-1\n")
                fo.close()
                time.sleep(1)
                self.level21()
        except:                                                 #Exception/Error Handling End
            print("SORRY\nTry Again")
            time.sleep(1)
            self.level21()
    def level22(self):                                              #Level-2 Sublevel-2 Html page containig logic circuit diagram the answer is 010
        print("*\n*\nNow go to D drive of this computer,\n& locate a folder name counterstrike1.6,\n there is a HTML page there named justcause.html,\n open it and give me the answer")
        time.sleep(1)
        try:                                                    #Exception/Error Handling Start
            e=input("What is the answer : ")
            if e=="":
                print("Sorry tryagain111")
                time.sleep(1)
                self.level22()
            elif e=='010':
                print("Your Logic is good\nLet's proceed")
                fo=open(self.name+".txt","a")
                fo.write("10\n")
                fo.close()
                time.sleep(1)
                self.level23()
            else:
                print("Sorry\nYour logic is weak\nTry Again")
                fo=open(self.name+".txt","a")
                fo.write("-1\n")
                fo.close()
                time.sleep(1)
                self.level22()
        except Exception:                                       #Exception/Error Handling End
            print("SORRY\nTry Again")
            time.sleep(1)
            self.level23()
    def level23(self):                                              #Level-2 Sublevel-3 Html page The partcipant needs to see source code
        print("*\n*\nI am very weak at games will you give me a HINT?")
        print("Don't worry,\n I have one for you")
        print("Go to Desktop of this computer,\n& locate a folder named NeW FoLDeRr,\n there is a Html page ther named gogogo.html,\nopen it and give me my HINT")
        f=input("So what's my HINT : ")
        if f=="":                                                   #Exception/Error Handling Start
            print("Try Again")
            self.level23()                                          #Exception/Error Handling End
        elif f=="anything":
            print("Thank you, You are a Life Saver")
            fo=open(self.name+".txt","a")
            fo.write("10\n")
            fo.close()
            time.sleep(1)
            self.level23()
        else:
            print("Are you guessing?\nDo it seriously")
            fo=open(self.name+".txt","a")
            fo.write("-1\n")
            fo.close()
            time.sleep(1)
            self.level23()
q=run()
#The code uploaded is incomplete because the level 3 is under progress
#The 3rd Level will be uploaded soon
