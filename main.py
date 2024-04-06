from math import sqrt

numbersList = [16,24,64,96,86]

squareRoot = list(map(sqrt,numbersList))

print(squareRoot)


names1 = ["Santiago","Carla","Maria","Rosario","Diego"]
vowels = "aeiou"
vowelsList=[];

def myFunction(names):
    vowelsList = []
    for i in range(len(names)):
        for j in range(len(names[i])):
            if names[i][j]== vowels[0] or names[i][j]==vowels[1] or names[i][j]==vowels[2] or names[i][j]==vowels[3] or names[i][j]==vowels[4]:
                vowelsList.append(names[i][j])
    
    return vowelsList


myNewListVowels = list(map(myFunction,names1))

print(myNewListVowels)


