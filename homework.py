dictionary = {"멋사": "멋쟁이 사자처럼", "파이썬": "지금 배우는 언어"}


def create_word():
    cc = input("Enter word: ")
    ccc = input("Enter meaning: ")
    dictionary[cc] = ccc
    return print("The word has been successfully registered!")

def read_dictionary():
    print("Dictionary")
    print("---")
    for key, value in dictionary.items():
        print(key,':', value)

def update_word():
    uu = input("Enter word: ")
    if(uu in dictionary):
        uuu = input("Enter meaning: ")
        dictionary[uu] = uuu
        return print("The word has been successfully registered!")
    if(not uu in dictionary):
        return print("You don't have this word in your dictionary.")

def delete_word():
    dd = input("Enter word: ")
    if(dd in dictionary):
        del dictionary[dd]
        return print("The word has been successfully registered!")
    if(not dd in dictionary):
        return print("You don't have this word in your dictionary.")
    
def console_help():
    print("Command list")
    print("---")
    print("C for create")
    print("R for read")
    print("U for update")
    print("D for delete")
    print("Q for quit")


def receive_input():
    command = input("Input command: ")
    if command == 'c' or command == 'C':
        create_word()
        return True
    if command == 'r' or command == 'R':
        read_dictionary()
        return True
    if command == 'u' or command == 'U':
        update_word()
        return True
    if command == 'd' or command == 'D':
        delete_word()
        return True
    if command == 'q' or command == 'Q':
        return False
    else:
        print("Please enter one of the letters above.")
        return True


def main():
    console_help()
    while receive_input():
        pass



if __name__ == "__main__":
    main()