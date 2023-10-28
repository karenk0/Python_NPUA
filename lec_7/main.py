while True:
    try:
        fileName = input("Input text file's name to be opened:\n  ")
        fileNumber = int(fileName)  # This might cause ValueError

        f = open(f"{fileNumber}.txt","r")
        text = f.readlines()
        print(text)
        f.close()
        break

    except ValueError:
        print("Enter a valid file name.")
    except FileNotFoundError:
        print("File doesn't exists!")

while True:
    print("Do you want to make some changes in the following file, or create new file?")
    choice = input("Input 1 for first option or 2 for the second:")

    try:
        if(choice == "2"):
            fileName = input("Input New file name:  ")
            fileNumber = int(fileName)
            f = open(f"{fileNumber}.txt","wt")
            content = input("Input file's content:  ")
            f.write(content)
            break

        elif(choice == "1"):
            content = input("Input file's content:  ")
            f = open(f"{fileNumber}.txt","at")
            f.write(content)
            break

        else:
            print("No valid option! Try again\n")

    except FileNotFoundError:
        print("File doesn't exists!")
    except ValueError:
        print("Enter a valid file name.") 
        
    else:
        print("Choice successfully done!")
    finally:
        f.close()
        print("The file has been closed.")

