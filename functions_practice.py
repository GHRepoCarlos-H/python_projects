# A function named hello() that prints a greeting to the user. This function should accept no arguments and returns nothing.
def hello():
    print("Hello User")




# A function named pack() that accepts three arguments, and returns a single list with the three arguments inside as list elements.
def pack(nickname, firstname, lastname):
    return [nickname, firstname, lastname]



# A function called eat_lunch(). This function should accept a list of any length, and print out a series of strings that say "First I eat __" (the first element of the list), and "Next I eat ___" (for the following elements in the list). If the list is empty, print "My lunchbox is empty!". The function should not return anything.
def eat_lunch(food_items):
    if not food_items:
        print('My lunchbox is empty') #this will only run if the food_items variable is empty. 
    else:
        print("First I eat", food_items[0])
        for food in food_items[1:]:
            print('Next I eat', food)
    



# Test that your file works by running it in your terminal. Remember, you need to call your functions in order for them to run. Make sure that all three functions run (please print the output of pack()) before submitting the file.

hello()

boxer = pack('Iron', 'Mike', 'Tyson')
print('In the red corner:', boxer)

eat_lunch(['pizza', 'beer', 'wings'])
