#################################
# storage.py                    #
#                               #
# Animal Crossing: New Horizons #
# Home Storage Log              #
#                               #
# Version 0.5                   #
#################################
# Ralph McCracken, III          #
#################################

# Known issues - prior to release
# - Cannot load multiple-digit quantities from file.
# - Text of quantities not aligned with differing number of digits.

import os

def ClearScreen():
    # Clear the console of all ouput pervious input.

    if os.name == 'nt': 
        os.system('cls') 
    else: 
        os.system('clear')


def PrintTitle():
    # Print the title of the program to the console.

    ClearScreen()
    print("Animal Crossing: New Horizons")
    print("Home Storage Log\n")


def PrintStorage(storage):
    # Print the Storage to the console.

    for name, count in storage.items():
        print(f"{count} | {name}")


def GetStorage(storage):
    # Gather Storage data from log file, log.txt.
    # This also creates the log file, if it does not already exist.

    if storage is not None:
        return storage

    log = "log.txt"
    doesExist = os.path.exists(log)

    f = None

    if doesExist:
        f = open(log, "r")
    if not doesExist:
        f = open(log, "a+")
        f.write("0")
        f.close()
        input("Home Storage is empty... Creating log...\nPress any key to continue.")
        Run(storage)
    
    storage = {}
    n = int(f.readline())
    
    for i in range(n):
        count = int(f.readline(1))
        f.readline(1)
        name  = f.readline().strip()
        storage[name] = count

    f.close()

    return storage


def AddToStorage(storage):
    # Update the Storage, adding to the table or quantity already in table.

    PrintTitle()
    PrintStorage(storage)
    print("\nAdding to Storage...")
    item  = input("Item name: ").upper()
    count = int(input("Quantity: "))

    if item in storage.keys():
        storage[item] += count
    else:
        storage[item] = count
    
    Run(storage)


def RemoveFromStorage(storage):
    # Update the Storage, removing from the table or quantity already in table.

    PrintTitle()
    PrintStorage(storage)
    print("\nRemoving from Storage...")
    item  = input("Item name: ").upper()

    if item in storage.keys():
        count = int(input("Quantity: "))
    else:
        RemoveFromStorage(storage)

    if item in storage.keys():
        if storage[item] - count <= 0:
            del storage[item]
        else:
            storage[item] -= count
    
    Run(storage)


def SaveAndQuit(storage):
    # Converts table to text.
    # Saves text to log file.

    log = "log.txt"
    doesExist = os.path.exists(log)

    f = None

    if doesExist:
        f = open(log, "w")
    if not doesExist:
        f = open(log, "a+")
        f.write("0")
        f.close()
        input("Home Storage is empty... Creating log...\nPress any key to continue.")
        Run(storage)
    
    output = ""

    output += str(len(storage)) + '\n'
    for item, count in storage.items():
        output += str(count) + " " + item + '\n'
    
    f.write(output)
    f.close()
    exit()


def Menu(storage):
    # Print the menu for program operations to the console.

    PrintTitle()
    PrintStorage(storage)
    print("\n1) Add to Storage")
    print("2) Remove from Storage")
    print("3) Save and Quit\n")

    return storage


def Run(storage):
    # Runs a main loop, to facilitate program operations.

    option = None
    loop   = True

    while loop:
        storage = Menu(storage)
        option = input("Enter your selection [1-3]: ")

        if   option == '1':
            loop = False
            AddToStorage(storage)
        elif option == '2':
            loop = False
            RemoveFromStorage(storage)
        elif option == '3':
            loop = False
            SaveAndQuit(storage)
        else:
            loop = True



# Execution of operations

ClearScreen()
storage = None
storage = GetStorage(storage)
Run(storage)