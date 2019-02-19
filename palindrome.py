# ask the user to enter words to be run through the program:

potential_palindrome = input("Enter text to see if it will be a palindrome: ")

# what the program does: outputs text telling you if the user input string is a palindrome.


def reverse(potential_palindrome):
    revpotential_palindrome = ''
    index = len(potential_palindrome)
    #print(index) is not needed for end user, it's  a good check for step by step, it would be uncommented during development
    print(index)
    while index > 0:
        revpotential_palindrome += potential_palindrome[index - 1]
        index = index - 1

    #print(revpotential_palindrome) is not needed for end user, it's  a good check for step by step
    if potential_palindrome == revpotential_palindrome:
        return print(potential_palindrome + " is a palindrome!")      
    else: 
        return print(potential_palindrome + " is not a palindrome!")

reverse(potential_palindrome)

###### make it recognize upper and lower case palindromes! - figure it out


