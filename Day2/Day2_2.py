string = input("Enter the string : ")
alpha = 'abcdefghijklmnopqrstuvwxyz'
if len(set(alpha) - set(string.lower()))==0:
    print("It's a pangram.")
else:
    print("It's not a pangram.")
