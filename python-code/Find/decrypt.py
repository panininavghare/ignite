class dec:
    def call(self):
        code=input("\n************************************\nEnter the coded text:")
        distance=int(input("enter the distance value:"))
        plainText=''
        for ch in code:
            ordValue=ord(ch)
            cipherValue= ordValue - distance
            if cipherValue<ord('a'):
                cipherValue=ord('z')-\
                     (distance-(ord('a')-ordValue+1))
            plainText+=chr(cipherValue)
        print("Comp : "+plainText+"\n************************************\n")
        self.call()
ob=dec()
ob.call()
