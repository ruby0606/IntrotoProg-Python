# ------------------------------------------------------------------------ #
# Title: Assignment 05
# Description: Working with Dictionaries and Files
#              When the program starts, load each "row" of data
#              in "ToDoToDoList.txt" into a python Dictionary.
#              Add the each dictionary "row" to a python list "table"
# ChangeLog (Who,When,What):
# RRoot,1.1.2030,Created started script
# Rabiya Abdul,08-10-2020,Added code to complete assignment 5
# ------------------------------------------------------------------------ #
# -- Data -- #
# Declare variables and constants
objFile = "ToDoList.txt"   # An object that represents a file
strData = ""  # A row of text data from the file
dicRow = {}    # A row of data separated into elements of a dictionary {Task,Priority}
lstTable = []  # A list that acts as a 'table' of rows
strMenu = ""   # A menu of user options
strChoice = "" # A Capture the user option selection
strTask = "" # Adding a new task
strPriority = "" # The priority of the task
strRmvTask = "" # Removing a task

# -- Processing -- #
# Step 1 - When the program starts, load the any data you have
# in a text file called ToDoList.txt into a python list of dictionaries rows (like Lab 5-2)
objFile=open("ToDoList.txt", 'r')
for row in objFile:
    strData=row.split(",")
    dicRow={"Task": strData[0], "Priority": strData[1].strip()}
    lstTable.append(dicRow)
    print(lstTable, "List with Dictionary Objects")
objFile.close()
# -- Input/Output -- #
# Step 2 - Display a menu of choices to the user
while (True):
    print("""
    Menu of Options
    1) Show current data
    2) Add a new item.
    3) Remove an existing item.
    4) Save Data to File
    5) Exit Program
    """)
    strChoice = str(input("Which option would you like to perform? [1 to 5] - "))
    print()  # adding a new line for looks
    # Step 3 - Show the current items in the table
    if (strChoice.strip() == '1'):
        for dicRow in lstTable:
            print(dicRow)
        continue
    # Step 4 - Add a new item to the list/Table
    elif (strChoice.strip() == '2'):
        strTask= str(input("Enter a new task: "))
        strPriority= str(input("Add the priority for the task. You can add High/Medium/Low: "))
        dicRow= {"Task": strTask, "Priority": strPriority}
        lstTable.append(dicRow)
        print("New task and priority added")
        continue
    # Step 5 - Remove a new item from the list/Table
    elif (strChoice.strip() == '3'):
        strRmvTask= str(input("Which task would you like to remove? "))
        for dicRow in lstTable:
            if dicRow["Task"] == strRmvTask:
                lstTable.remove(dicRow)
                print("Selected task is now removed from the table")
                break
        else:
            print("Did not find a matching task.")
    # Step 6 - Save tasks to the ToDoList.txt file
    elif (strChoice.strip() == '4'):
        objFile=open("ToDoList.txt", 'w')
        for dicRow in lstTable:
            objFile.write(dicRow["Task"] + "," + dicRow["Priority"] + "\n")
        objFile.close()
        print("Saved to the file")
        continue
    # Step 7 - Exit program
    elif (strChoice.strip() == '5'):
        print(dicRow)
        print("Exiting the Program")
        break  # and Exit the program
