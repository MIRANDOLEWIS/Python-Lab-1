user =  input("enter  palindrome  word :")

result = user[::-1]

if user == result:
    print("yes, the word is palindrome ")

else:
    print("no, the word is not palindrome   ")    