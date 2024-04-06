from math import sqrt

numbersList = [16,24,64,96,86]

squareRoot = list(map(sqrt,numbersList))

print(squareRoot)


names1 = ["Santiago","Carla","Maria","Rosario","Diego"]

name = 'Santiago'
vowels = "aeiou"
otherName = [];
vowelsList=[];

print(name[0])


for i in range(len(name)):
    if name[i]== vowels[0] or name[i]==vowels[1] or name[i]==vowels[2] or name[i]==vowels[3] or name[i]==vowels[4]:
        otherName.append(name[i]);

print(otherName)


def myFunction(names):
    vowelsList = []
    for i in range(len(names)):
        for j in range(len(names[i])):
            if names[i][j]== vowels[0] or names[i][j]==vowels[1] or names[i][j]==vowels[2] or names[i][j]==vowels[3] or names[i][j]==vowels[4]:
                vowelsList.append(names[i][j])
    
    return vowelsList


myNewListVowels = list(map(myFunction,names1))

print(myNewListVowels)








myList = ["Santiago","Cristina"]

myList.append(["Rosario"])

myList.insert(3,["k","F"])


print(myList)


