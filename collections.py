"""
Ricardo Cereceres
"""

"Excercise 1 - Lists"

"Creating a list"
myFruitList = ["apple", "banana", "cherry"]
print(myFruitList)
print(type(myFruitList))

"Accessing list values"
print(myFruitList[0])
print(myFruitList[1])
print(myFruitList[2])

"Changing values from a list"
myFruitList[2] = "orange"
print(myFruitList)

"Excercise 2 - Tuples"

"Creating a Tuple (cannot be changed/modified)"
myFinalAnswerTuple = ("apple", "banana", "pineapple")
print(myFinalAnswerTuple)
print(type(myFinalAnswerTuple))

"Accessing a tuple by position (same as lists)"
print(myFinalAnswerTuple[0])
print(myFinalAnswerTuple[1])
print(myFinalAnswerTuple[2])

"Excercise 3 - Dictionaries"

"Creating a Dictionary"
myFavoriteFruitDictionary = {
  "Akua" : "apple",
  "Saanvi" : "banana",
  "Paulo" : "pineapple"
}
print(myFavoriteFruitDictionary)
print(type(myFavoriteFruitDictionary))

"Accessing to Dictionary values"
print(myFavoriteFruitDictionary["Akua"])
print(myFavoriteFruitDictionary["Saanvi"])
print(myFavoriteFruitDictionary["Paulo"])