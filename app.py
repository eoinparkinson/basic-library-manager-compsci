# importing libraries
import sys # using this to "END" the program, in theory it's not actually required.

print("Welcome to the coolboy library\nChoose one of three options:\n\n1. View all available books:\n2. Add a book:\n3. Search for a book:\nEND to end the program.\n\n") # opening spiel

# first choice, list all book names
def choiceOne(data):
    cleanData = "" # init variable

    for item in data: # each item in list, add it to new variable for nice visual list
        cleanData += item

    print("\n"+cleanData) # print them books
    chooseOption() # back to the start


# second choice, add a book
def choiceTwo():
    with open("data/books.txt","a") as f: # opening the file in append mode
        bookToAdd = input("Enter a book name: ") # getting the book name to add
        f.write(bookToAdd+"\n") # appending to the file with newline "\n"
        f.close() # closing the file

    chooseOption() # back to the start


# third choice, search for a book
def choiceThree(data):
    bookToSearch = input("\nEnter a book name: ") # input book name

    if bookToSearch+"\n" in data: # checking if book in list and adding "\n" to the item search as this is how .readlines() formats list items.
        print("\n'"+bookToSearch+"' exists.\n") # exists
    else:
        print("\nBook does not exist.\n") # doesn't exist
    chooseOption() # back to the start


# function to request choice input --------------------------------------------------
def chooseOption():
    with open("data/books.txt","r") as f: # opening & closing the file in this function allows the first option to hot reload
        allLines = f.readlines() # reading all lines
        f.close() # closing the file
    print("Please type either '1', '2' or '3' to continue, or 'END' to close the program.")
    option = input("Option: ") # asking user for option, 1,2,3,END
    if option == "1":
        choiceOne(allLines) # option 1 function
    elif option == "2":
        choiceTwo() # option 2 function
    elif option == "3":
        choiceThree(allLines) # option 3 function
    elif option == "END": # end the program
        sys.exit() # sys library to exit the app
    else:
        print("\nOption unavailable. Try again.")
        chooseOption() # option didn't exist, goes back to the beginning

# call main function ----------------------------------------------------------------
chooseOption()
