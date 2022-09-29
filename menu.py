import read
import insertData
import update
import delete


def menuOptions():
    options = 0  # flag variable
    # check if options is in the list below
    while options not in ["1", "2", "3", "4", "5"]:
        print(
            "Songs Menu Options\nEnter \n1. Print.\n2. Add.\n3. Update.\n4. Delete.\n5. Exit"
        )
        # reassign a value to the options variable
        options = input("Enter one of the options listed above: ")
        if options not in ["1", "2", "3", "4", "5"]:
            print(f"{options} is not a valid choice")

    return options


# create a bolean flag variable
mainProgram = True  # assign variable mainProgram a boolean value of True

while mainProgram:
    mainMenu = (
        menuOptions()
    )  # we assigned the menuOptions() to the mainMenu variable and invoke/call it
    # if mainMenu = 1/2/3/4/5 we can then call the respective app and its subroutine
    if mainMenu == "1":
        read.readSongs()
    elif mainMenu == "2":
        insertData.addSongs()
    elif mainMenu == "3":
        update.updateSongs()
    elif mainMenu == "4":
        delete.deleteSongs()
    else:  # reassign the value of variable mainprogram to False
        mainProgram = False
input("press enter to exit")
