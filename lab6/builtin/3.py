text = input("Enter a string: ")

cleaned = text.replace(" ", "").lower()

if cleaned == ''.join(reversed(cleaned)):
    print("Palindrome")
else:
    print("Not a palindrome")
