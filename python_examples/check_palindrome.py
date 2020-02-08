
import time
import os


def palindrome_check():

    my_string = input("Submit a word or phrase to be checked if it is a Palindrome:")
    my_rev_string = ""
    
    my_length = len(my_string)


    count = 1
    while count <= my_length:
        x = my_string[-count]
        count = count + 1
        my_rev_string = my_rev_string + x


    if my_string.lower().replace(" ", "") == my_rev_string.lower().replace(" ", ""):
        print("\n")
        time.sleep(1)
        print("A Palindrome has been submitted!" + "\n")
    
    
    else:
        print("\n")
        time.sleep(1)
        print("A Palindrome has NOT bee submitted!" + "\n")


def main():
    os.system('clear')
    palindrome_check()

    
if __name__ == "__main__":
    main()