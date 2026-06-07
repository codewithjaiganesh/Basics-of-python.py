#TO CHECK THE GIVEN STRING IS PALINDROME
input_user = input("enter the string to check palindrome: ").lower()
if(input_user[::-1] == input_user):
    print(f"The word {input_user} is a palindrome")
else:
    print("its not a palindrome!")
