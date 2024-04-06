from math import sqrt

numbersList = [16,24,64,96,86]

squareRoot = list(map(sqrt,numbersList))

print(squareRoot)


names1 = ["Santiago","Carla","Maria","Rosario","Diego"]
vowels = "aeiou"


def myFunction2(names):
    vowelsList = []
    for i in range(len(names)):
            if names[i]== vowels[0] or names[i]==vowels[1] or names[i]==vowels[2] or names[i]==vowels[3] or names[i]==vowels[4]:
                vowelsList.append(names[i])
    
    return vowelsList

myNewListVowels2 = list(map(myFunction2,names1))

print(myNewListVowels2)





