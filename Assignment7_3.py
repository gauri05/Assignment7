print("Arithmetic.......")
class Arithmetic:
    def __init__(self,val):
        self.value=val
    def ChkPrime(self):
        flag = False
        for i in range(2, self.value):
            if self.value % i == 0:
                flag = True
                break  # not prime
        return flag
    def ChkPerfect(self):
        ans = 0
        flag = False
        #print(int(self.value/2))
        for i in range(1, self.value):
            #print(i)
            if self.value % i == 0:
                #print (i)
                ans = ans + i
               # print (ans)

        if self.value==ans:
            flag=True
        return flag
    def Factors(self):
        arrlist= list()

        for i in range(1, self.value):
            # print(i)
            if self.value % i == 0:
                arrlist.append(i)
        return arrlist

    def SumFactors(self):
        ans = 0
        for i in range(1, self.value):
            # print(i)
            if self.value % i == 0:
                ans = ans + i
        return ans

def main():
    val=int(input("Enter value::"))
    obj1=Arithmetic(val)
    ans = obj1.ChkPrime()
    #print(ans)
    if ans:
        print("Number is not prime.....")
    else:
        print("Number is prime....")

    chkperfect=obj1.ChkPerfect()
    if chkperfect:
        print ("Number is perfect")
    else:
        print ("Number is not perfect")

    factors=obj1.Factors()
    print ("Factors===",factors)

    sumfactors=obj1.SumFactors()
    print ("SumFactors===",sumfactors)
if __name__ == "__main__":
    main()
