# Ask the user for a string and print out whether this string is a palindrome or not. 
# (A palindrome is a string that reads the same forwards and backwards.)




string = input("Enter a word to perform a palindrome check: ")
reverse_string = string[::-1]

if string == reverse_string:
    print("This word is palindrome")
else:
    print("This word is not a palindrome")