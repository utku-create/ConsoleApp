def Menu():
    print("****************\n1)Factorial\n2)Exponential\n3)ArrayLoc\n****************")

    choice = int(input(">>:")) #giriş inputu

    if(choice == 1):
        Factorial()
    if(choice == 2):
        Exponential()
    if(choice == 3):
        print(ArrayLoc())
    else:
        print("Please select only the options in the menu!")
        Menu()

def Factorial():

    stop = False
    while stop == False:
        factorialNum = int(input("Calculate for factorial:"))

        if(factorialNum != -1):
            value = 1
            for i in range(factorialNum):
                value = value * (i + 1)

            print("Factorial : ", value)
        else:
            Menu()

def Exponential():

    stop = False
    while stop == False:
        taban = int(input("exponential radix:"))
        us = int(input("exponential:"))

        if(taban != -1 or us != -1):
            expoRes = taban ** us
            print(expoRes)
        else:
            Menu()

def ArrayLoc():

    array = []  #Array'e ekleme
    resArray = []
    i = 0

    while (i < 5):
        nums = input("Enter 5 numbers to add to Array:")
        array.append(nums)
        i += 1
    print(array)

    target = int(input("Target?:"))
    for x in array:
        for y in array:
            test = int(x) + int(y)
            if(test == target):
                resArray.append(array.index(x))
                resArray.append(array.index(y))
                return resArray



Menu()