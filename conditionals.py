"""
Ricarod Cereceres
"""

"""
Exercise 1: Working with the if statement
In this exercise, you will edit a Python script to ship packages.

From the navigation pane of the IDE, choose the .py file that you created in the previous Creating your Python exercise file section.

Use the input() function to get information from the user:
"""

userReply = input("Do you need to ship a package? (Enter yes or no) ")

"""
Use the if statement to print a response.

The statements in an if statement are one tab indented from the if statement. In other programming languages, brackets are often used to indicate the start and end of a logic block, but Python uses spacing:
"""
if userReply == "yes":
    print("We can help you ship that package!")
else:
    print("Please come back when you need to ship a package. Thank you.")
    
"""
Exercise 2: Working with the else statement
To improve customer service, it would be nice to provide a reply even if the user doesn't want to ship a package. In this exercise, you will improve the Python script by using the else statement:

To handle the condition where the user doesn't want to ship a package, use the else statement:
"""

"""
Exercise 3: Working with the elif statement
In this exercise, you will improve the Python script by offering the user additional services. When you have multiple conditions, you can use the elif statement, which is short for else-if.

Note: The elif statement always comes after an if statement and before the else statement.

In the Python script, enter the following code
"""
userReply = input("Would you like to buy stamps, buy an envelope, or make a copy? (Enter stamps, envelope, or copy) ")
if userReply == "stamps":
    print("We have many stamp designs to choose from.")
elif userReply == "envelope":
    print("We have many envelope sizes to choose from.")
elif userReply == "copy":
    copies = input("How many copies would you like? (Enter a number) ")
    print("Here are {} copies.".format(copies))
else:
    print("Thank you, please come again.")