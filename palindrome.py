import math

def palindrome(str):
    # str = input("Enter your cool palindrome string: ")

    isPal = True
    length = len(str)
    for i in range(0, math.floor((length)/2)):
        if str[i] != str[length - (i + 1)]:
            isPal = False

    # if isPal:
    #     print("The string is a palindrome!!!")
    # else:
    #     print("The string is not a palindrome :(")
    return(isPal)
