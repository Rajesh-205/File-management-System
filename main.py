import os

def create_file(filename):
    try:
        with open("filename", "x") as f:
            print(f"File name {filename} : created successfully :)")
    except FileExistsError:
        print(f"File named {filename} already exists !!")
    except Exception as e:
        print("An error occurred !!")

def view_all_files():
    files = os.listdir()
    if not files:
        print("No file found!!")
    else:
        print("Files in directory :")
        for file in files:
            print(file)

def delete_file(filename):
    try:
        os.remove(filename)
        print(f"{filename} has been deleted successfully !!")
    except FileNotFoundError:
        print(f"{filename} not found !!")
    except Exception as e:
        print("An error occurred !!")

def read_file(filename):
    try:
        with open("sample.txt", "r") as f:
            content = f.read()
            print(f"Content of {filename} :\n {content}")
    except FileNotFoundError:
        print(f"File doesn't exists")
    except Exception as E:
        print("An error occured!!")
    
def edit_file(filename):
    try:
        with open("sample.txt","a") as f:
            content = input("Enter data to add = ")
            f.write(content + "\n")
            print(f"Content added to {filename} successfully...")
    except FileNotFoundError:
        print(f"{filename} not found!!")
    except Exception as E:
        print("An error occured!!")

def main():
    print("WELCOME TO FILE MANAGER")
    while True:
        print("1. Create file")
        print("2. View all files")
        print("3. Delete a file")
        print("4. Read file")
        print("5. Edit file")
        print("6. Exit")

        choice = int(input("Enter ur choice : "))

        if choice == 1:
            file = input("Enter the file name to create :")
            create_file(file)
        
        elif choice == 2:
            view_all_files()

        elif choice == 3:
            file = input("Enter the file name to delete :")
            delete_file(file)

        elif choice == 4:
            file = input("Enter the file name to read :")
            read_file(file)

        elif choice == 5:
            file = input("Enter the file name to edit :")
            edit_file(file)
        
        elif choice == 6:
            print("THANKS 4 USING ...")
            break

        else:
            print("Invalid choice :(")
            break

if __name__ == "__main__":
    main()
