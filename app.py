def main_menu():
    print("\nWelcome to summercamp!\n")
    print("\nMENU\nMaximum number of children that can be registered: 8\n")
    print("1. Show registered children")
    print("2. Register new child")
    print("3. Search registered children")
    print("4. Register child for event")
    print("5. Finish")
    choice = input("Choose an alternative: ")
    if choice == "1":
        myfile = open(filename, "r+")
        filecontents = myfile.read()
        if len(filecontents) == 0:
            print("No children registered.")
        else:
            print(filecontents)
        myfile.close
        enter = input("Press enter to continue...")
        main_menu()
    elif choice == "2":
        file = open(filename, "r+")
        line_count = 0
        for line in file:
            if line != "\n":
                line_count += 1
        file.close()
        if line_count == 8:
            print("Sorry, can't register more than 8 children.")
        else:
            newchild()
        enter = input("Press enter to continue...")
        main_menu()
    elif choice == "3":
        searchkid()
        enter = input("Press enter to continue...")
        main_menu()
    elif choice == "4":
        event()
        enter = input("Press enter to continue...")
        main_menu()
    elif choice == "5":
        print("Have a nice day!")
    else:
        print("Choose a valid input!\n")
        enter = input("Press enter to continue...")
        main_menu()

# Definition of search-option to search a registered child
def searchkid():
    searchname = input("Enter the first name of the child for information: ")
    remname = searchname[1:]
    firstchar = searchname[0]
    searchname = firstchar.upper() + remname
    myfile = open(filename, "r+")
    filecontents = myfile.readlines()
    found = False
    for line in filecontents:
        if searchname in line:
            print("The asked child is:", end=" ")
            print(line)
            found = True
            break
    if found == False:
        print("The child does not exist.", searchname)

# First name
def input_firstname():
    first = input("First name: ")
    remfname = first[1:]
    firstchar = first[0]
    return firstchar.upper() + remfname


# Surname
def input_lastname():
    last = input("Surname: ")
    remlname = last[1:]
    firstchar = last[0]
    return firstchar.upper() + remlname


# List of children
def newchild():
    firstname = input_firstname()
    lastname = input_lastname()
    phoneNum = input("Phone number to parent: ")
    emailID = input("Email Adress to parent: ")
    swimID = input("Can your child swim? CAN SWIM/CANNOT SWIM: ")
    bedwetterID = input(
        "Does your child wet the bed? BEDWETTER/ NOT BEDWETTER: ")
    allergyID = input(
        "Does your child have any allergies? Enter which ones. If your child does not have any allergies enter NO ALLERGIES: ")
    kidDetails = ("[" + firstname + ", " + lastname + ", " + phoneNum + ", " +
                  emailID + ", " + swimID + ", " + bedwetterID + ", " +
                  allergyID + "]\n")
    myfile = open(filename, "a")
    myfile.write(kidDetails)
    print("Following child:\n " + kidDetails + "\nhas  been registrered!")

# Definition of hiking-event
def hike():
    firstname = input_firstname()
    lastname = input_lastname()
    phoneNum = input("Phone number to parent: ")
    emailID = input("Email Adress to parent: ")
    allergyID = input("Does your child have any allergies? Enter which ones. If your child does not have any allergies enter NO ALLERGIES: ")
    kidDetails = ("[" + firstname + ", " + lastname + ", " + phoneNum + ", " + emailID + ", " + allergyID + "]\n")
    myfile = open(x, "a")
    myfile.write(kidDetails)
    print("Following child:\n " + kidDetails +
          "\nhas  been registrered on Hiking!")

# Definition of movie-event
def movie():
    firstname = input_firstname()
    lastname = input_lastname()
    phoneNum = input("Phone number to parent: ")
    emailID = input("Email Adress to parent: ")
    allergyID = input("Does your child have any allergies? Enter which ones. If your child does not have any allergies enter NO ALLERGIES: ")
    kidDetails = ("[" + firstname + ", " + lastname + ", " + phoneNum + ", " + emailID + ", " + allergyID + " \n")
    myfile = open(y, "a")
    myfile.write(kidDetails)
    print("Following child:\n " + kidDetails +
          "\nhas  been registrered on movie!")

# Definition of baking
def baking():
    firstname = input_firstname()
    lastname = input_lastname()
    phoneNum = input("Phone number to parent: ")
    emailID = input("Email Adress to parent: ")
    allergyID = input("Does your child have any allergies? Enter which ones. If your child does not have any allergies enter NO ALLERGIES: ")
    kidDetails = ("[" + firstname + ", " + lastname + ", " + phoneNum + ", " + emailID + ", " + allergyID +  " \n")
    myfile = open(z, "a")
    myfile.write(kidDetails)
    print("Following child:\n " + kidDetails +
          "\nhas  been registrered in Baking!")

# Definiton of event-option
def event():
    print("1. Hiking 17/6")
    print("2. Movie Night 18/6")
    print("3. Baking 19/6")
    print("4. Show registered children in hiking")
    print("5. Show registered children in movie")
    print("6. Show registered children in baking")
    choice = input("Pick event: ")
    if choice == "1":
        xfile = open(x, "r+")
        x_count = 0
        for line in xfile:
            if line != "\n":
                x_count += 1
        xfile.close()
        if x_count == 8:
            print("Sorry, can't register more than 8 children in hiking.")
        else:
            hike()
    elif choice == "2":
        yfile = open(y, "r+")
        y_count = 0
        for line in yfile:
            if line != "\n":
                y_count += 1
        yfile.close()
        if y_count == 8:
            print("Sorry, can't register more than 8 children in movie.")
        else:
            movie()
    elif choice == "3":
        zfile = open(z, "r+")
        z_count = 0
        for line in zfile:
            if line != "\n":
                z_count += 1
        zfile.close()
        if z_count == 8:
            print("Sorry, can't register more than 8 children in baking.")
        else:
            baking()
    elif choice == "4":
        xfile = open(x, "r+")
        xfilecontents = xfile.read()
        if len(xfilecontents) == 0:
            print("No children registered.")
        else:
            print(xfilecontents)
        xfile.close
        enter = input("Press enter to continue...")
        main_menu()
    elif choice == "5":
        yfile = open(y, "r+")
        yfilecontents = yfile.read()
        if len(yfilecontents) == 0:
            print("No children registered.")
        else:
            print(yfilecontents)
        yfile.close
        enter = input("Press enter to continue...")
        main_menu()
    elif choice == "6":
        zfile = open(z, "r+")
        zfilecontents = zfile.read()
        if len(zfilecontents) == 0:
            print("No children registered.")
        else:
            print(zfilecontents)
        zfile.close
        enter = input("Press enter to continue...")
        main_menu()

    else:
        print("Enter a valid option!\n")
        enter = input("Press enter to continue ...")
        event()


# Creating .txt file to save registered kids
filename = "registeredkids.txt"
myfile = open(filename, "a+")
myfile.write('\n')

x = "registerhikings.txt"
xfile = open(x, "a+")
xfile.write('\n')

y = "registermovie.txt"
yfile = open(y, "a+")
yfile.write('\n')

z = "registerbaking.txt"
zfile = open(z, "a+")
zfile.write('\n')

main_menu()