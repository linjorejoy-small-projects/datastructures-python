import re


class BigNumber:

    def __init__(self, number : str, size = 2):

        self.number = number
        self.size = size
        self.numData = []

        if re.search("^[\d]+e[\d]+$", self.number):
            mantissa, exponent = self.number.split("e")
            self.size = ((int(exponent)-1) // 308) + 1
            self.numData = [0] * self.size
            self.numData[self.size - 1] = int(mantissa) * 10**(((int(exponent)-1) % 308)+1)

        elif re.search("^[\d]+$", self.number):
            self.size = (len(number) // 308) + 1 
            self.numData = [0] * self.size
            for i in range(self.size):
                self.numData[self.size - i - 1] = self.number[i*308 : (i + 1)*308]

        else:
            raise ValueError("Invalid Number Format")

    


    def __str__(self):
        numberString = ""
        for i in range(self.size - 1, -1, -1):
            if(self.numData[i] == 0):
                numberString += "0"*308
            else:
                numberString += str(self.numData[i])
        
        return numberString


    def print(self):
        numberString = ""
        for i in range(self.size - 1, -1, -1):
            if(self.numData[i] == 0):
                print("0"*308, end="")
            else:
                print(str(self.numData[i]), end="")
        print()
        return numberString
    
    def __add__(self,otherBigNumber):#+
        
        return 5
    
    def __sub__(self,otherBigNumber):#-
        pass
    
    def __mul__(self,otherBigNumber):#-
        pass
    
    def __trudiv__(self,otherBigNumber):#/
        pass
    
    def __floordiv__(self,otherBigNumber):#//
        pass
    
    def __mod__(self,otherBigNumber):
        pass
    
    def __pow__(self,otherBigNumber):
        pass
    
    def __lt__(self,otherBigNumber):
        pass
    
    def __le__(self,otherBigNumber):
        pass
    
    def __gt__(self,otherBigNumber):
        return True
        
    
    def __ge__(self,otherBigNumber):
        pass
    
    def __eq__(self,otherBigNumber):
        pass
    
    def __ne__(self,otherBigNumber):
        pass

    def __isub__(self, otherBigNumber):
        pass
    
    def __iadd__(self,otherBigNumber):
        pass
    
    def __imul__(self,otherBigNumber):
        pass
    
    def __idiv__(self,otherBigNumber):
        pass
    
    def __ifloordiv__(self,otherBigNumber):
        pass
    
    def __imod__(self,otherBigNumber):
        pass
    
    def __ipow__(self,otherBigNumber):
        pass
    
    def __neg__(self,otherBigNumber):
        pass
    
    def __pos__(self,otherBigNumber):
        pass
    
    def __invert__(self,otherBigNumber):
        pass


num = BigNumber("5555e10")
num2 = BigNumber("555e666")
num3 = BigNumber("123456789" + "000000000000"*50)
num4 = BigNumber("466e500")

print(num + num2)
print(str(num))
print(len(str(num)))
num.print()
print(num3)
print(len(str(num3)))
print(num4)