from math import sqrt

numbersList = [16,24,64,96,86]

squareRoot = list(map(sqrt,numbersList))

print(squareRoot)


names = ["Santiago","Carla","Maria","Rosario","Diego"]
vowels = "aeiou"


def myFunction2(elements):
    vowelList = []
    for i in range(len(elements)):
            if elements[i]== vowels[0] or elements[i]==vowels[1] or elements[i]==vowels[2] or elements[i]==vowels[3] or elements[i]==vowels[4]:
                vowelList.append(elements[i])
    
    return vowelList

myNewListVowels2 = list(map(myFunction2,names))

print(myNewListVowels2)





