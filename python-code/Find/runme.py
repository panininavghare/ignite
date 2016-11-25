class run:

    def __init__(self):
        print("FIND_IT_First")
        print("\n\n\n\n\n\n\n\n***WARNING***\nDo not hit Enter key without entering any value !!"+"\nActually i was gonna add an exception for that but it was so boring.. :P\nSo please don't try that !!!")
        pc=input("\nEnter your Pc No. to continue: ")
    def check(self):
        self.lol=int(input("\nNow enter the answer of 6/2(2+1): "))
        if self.lol==9:
            print("I must say you do know Math.")
            self.next()
            
        else:
            print("Your basics of Math are simply weak. Try Again")
            self.lol= None
            self.check()

    def next(self):
        
        self.l=int(input("\nNow search for a file on Desktop with name * Solve me * \nThis file is availabe in Python and C++ formats.\n\nEnter the final result here: \n"))
        if self.l== 68:
            print("You are getting a hold of this.")
            print("\nGo to E:\Cat\code.(py/cpp)\nSolve it !!!")
            self.next1()
        else:
            print("Try Again !!!")
            self.l= None
            self.next()
        
    def next1(self):
        self.m=int(input("\nEnter the Result here: "))

        if self.m==5:
                print("Yeah ! you got it right.\n Now keep this in your mind !")
                print("\nSearch for a file with name * Crack me * on your desktop.\nYou know what to do !")
                self.next3()
        else:
                print("Try Again !!")
                self.m= None
                self.next1()

    def next3(self):
        self.o=int(input("\nTell me the last element of the output: "))
        if self.o==16:
            print("\nWell you are a Tough Cookie \nLets see if you can get pass through this")
            self.next4()
        else:
            print("\nNope that's not what i was asking for. Why don't you try again")
            self.o= None
            self.next3()

    def next4(self):

        self.p=int(input("\n\nEnter an Armstrong number of your choice: "))
        sum = 0
        temp = self.p
        while temp > 0:
            digit = temp % 10
            sum += digit ** 3
            temp //= 10
        if self.p == sum:
            print("\nCongrats you made it so far.\nNow comes the real test\nGo to  D:\Concat\code.py (py/cpp)")
            self.next5()
        else:
            print("Nah. Try Again")
            self.next4()
 

    def next5(self):
        self.q=int(input("\nEnter the last element here: "))
        if self.q== 4181:
            print("\n\nHow bout i help you.\nEnter the following text in the CMD(i.e. the decrypt.py) window without *\n*tsjtsjjnlmy* hit enter.\nNow comes the fun part.\n\nDo you remember something ? \nEnter that as next value in CMD")
            print("\nWhat are you waiting for ? Go find it !!!!")
            self.next6()

        else:
            print("Come on you can't give up now. Keep trying")
            self.next5()

    def next6(self): 
            self.n=int(input("\nDid You Find it ?\n1.Yes\t2.No\n"))
            if self.n==1:
                n1=int(input("\n\nEnter the number on it: "))

                if n1==17665:
                    print("Awesome !")
                    print("Now Call the one who's supervising this event.\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\nP.S. YOU WON :P")
                    x=input()
                else:
                    print("Are you trying to guess this ? You need to go and Find it First !")
                    self.next6()
            elif self.n==2:
                print("Come on Try Harder !!!")
                self.next6()
            else:
                print("All i can say is Try Again !!!")
                self.next6()

            
oo=run()
oo.check()
