#Book attributes
class Book:

    #Book attributes passed by the user
    def __init__(self, title, author, yearPublished):
        self.title = title
        self.author = author
        self.yearPublished = yearPublished
        #Data about the next book in the list. 
        #Next book is None by default for the most recently added book.
        self.next = None

#Library
class BookManager:

    #First value is none by default
    def __init__(self):
        self.head = None
    
    #Add new book the library. all attributes of the book have to be passed.
    def addNewBook(self, inputTitle, inputAuthor, inputYearPublished ):

        #Create new book instance which was inputted by the user.
        newBook = Book(inputTitle, inputAuthor, inputYearPublished)
        
        #If the library is empty the new book becomes its first value.
        if self.head is None:
            self.head = newBook
            return
        
        #else iterate the whole library until we get to the last value.
        lastBook = self.head

        #We find the last value if a book has no data about the next book.
        while lastBook.next:
            lastBook = lastBook.next

        #pass the information to the last book about a new book.
        lastBook.next = newBook

    #show the entire library
    def displayBooksList(self):

        currentNode = self.head

        #Message if the library is empty
        if self.head == None:
            print("\nThe library is empty.\n")
            return

        #iterate the whole library and display all attributes of the book until we reach the last book.
        while currentNode:
            print(f"\nTitle: '{currentNode.title}'\nAuthor: {currentNode.author}\nYear of Publication: {currentNode.yearPublished}\n" )
            currentNode = currentNode.next

    #Check if the book is available in the library.
    def findBook(self, inputTitle):
        
        currentNode = self.head
        
        if self.head == None:
            print("\nThe library is empty.\n")
            return
        
        #Check if there is only one book
        if currentNode.title == inputTitle:
            print(f"\nBook '{currentNode.title}' is available in the library.\n")
            return

        #Else iterate the whole library
        while currentNode.next:
            if currentNode.title == inputTitle:
                print(f"\nBook '{currentNode.title}' is available in the library.\n")
                return
            currentNode = currentNode.next
            
        print(f"\nBook '{inputTitle}' is unavailable in the library.\n")
            

#Commands of the console
class Commands:

    #Users can interact with the library based on these commands.
    def __init__(self):
        self.libraryCommands = {1: 'Add a new book', 2: 'Show list of available books', 3: 'Find a specific book', 4: 'Shut the program'}
    
    #Return commands dictionary
    def getCommandsDict(self):
        return self.libraryCommands
    
    #Validate commands chosen by the user  
    def commandValidation(self, commandValue):
        #Validation Status
        IsDataValidated = False

        while not IsDataValidated:
            #Command chosen by the user
            commandValue = input("\nCommand: ")

            #Check if command value is an integer
            if not validation.checkDataTypeInt(commandValue):
                ValidationIndex = 0
                continue
                
            #Check if command value is available in the list of operations defined by the program.
            if not validation.checkAvailableCommandKeys(int(commandValue)):
                ValidationIndex = 0
                continue
            
            #Set data validation step to true
            IsDataValidated = not IsDataValidated

        return int(commandValue)


#Messages for invalid data
class InvalidData:

    def __init__(self): 
        pass
        
    #Message if data is not an integer
    def invalidIntMessage(self):
        print("\nPlease, input a numeric value.\n")

    #Message if command is unavailable
    def invalidCommandMessage(self):
        print("\nNo such command available. Please, try another one.\n")

#Actions for validating steps
class Validation():
    
    def __init__(self):
        pass

    #Check if input data is an integer
    def checkDataTypeInt(self, value):
        if not value.isdigit():
            inavlidDataType.invalidIntMessage()
        return value.isdigit()

    #Check if input data is available in the commands list
    def checkAvailableCommandKeys(self, commandValue):
        #get available commands
        AvaiableCommandsDict = commands.getCommandsDict()

        if not AvaiableCommandsDict.get(commandValue):
            inavlidDataType.invalidCommandMessage()
            return False
        return True
      
#
class UserInterface:
    def __init__(self):
        pass

    #Display avaialble commands options for the user
    def Introduction(self):
       #Message
       print("\nEnter a number to interact with the library:\n")
       #Get commands list
       libraryCommands = commands.getCommandsDict()
       #CommandsList
       for keys in libraryCommands:
            print(f"{keys}: {libraryCommands[keys]}")

    #User command: add new book.
    def userAddNewBook(self):
        inputTitle = input("\nEnter the title of the book: ")
        inputAuthor = input("\nEnter the author of the book: ")
        inputYear = input("\nEnter the year of publication: ")
        
        #Check if year is an integer.
        while not validation.checkDataTypeInt(inputYear):
            inputYear = input("\nEnter the year of publication: ") 

        inputYear= int(inputYear)

        #Add new book to the library.
        bookManager.addNewBook(inputTitle, inputAuthor, inputYear)

        #Display a validating message to the user.
        print("\nThe book has been successfully added to the library!")

    #User command: display the library.
    def userDisplayBooksList(self):
        bookManager.displayBooksList()

    #User command: find a book.
    def userFindBook(self):
        inputTitle = input("\nPlease, enter the title of the book: ")
        bookManager.findBook(inputTitle)

    
#Classes
commands = Commands()
validation = Validation()
inavlidDataType = InvalidData()
bookManager = BookManager()
userInterface = UserInterface()

#Is the console running
IsConsoleActive = True

#Run the console until the user shuts it down
while IsConsoleActive:
    #Run the console
    userInterface.Introduction()

    #Initialize the command chosen by the user
    commandValue = ''

    #Two-step validation of the command
    commandValue = commands.commandValidation(commandValue)

    #Add new book
    if commandValue == 1:

        userInterface.userAddNewBook()

    #Show the entire library
    elif commandValue == 2:

        userInterface.userDisplayBooksList()

    #Find the book
    elif commandValue == 3:

        userInterface.userFindBook()

    #Shut down the console
    elif commandValue == 4:

        IsConsoleActive = not IsConsoleActive
        
        print("\nSee you soon!\n")



        
        



