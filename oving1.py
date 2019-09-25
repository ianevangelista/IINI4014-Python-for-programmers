# Øving 1
inputName = input('Type in your full name: ')
# Splits the different names which are typed in
name = inputName.split(" ")
# Creating an empty list for the initals
initals = []
# Creating a loop which goes through the amount of names
for n in range(len(name)):
    # Adding the first letter of the name in the initals-list
    initals.append(name[n][0])

# Joins all the initals from the list to create a word
yourInitals = ''.join(initals).upper()
# Printing
print('Welcome, {}, to Python for programmers'.format(yourInitals))
