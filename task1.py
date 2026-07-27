
print("####################  Task1  ##################")


input1 = "aabaa"
input2 = "abac"
input3 = "a"

ifPalindrome = False

if input1 == input1[::-1]:
    ifPalindrome = True
    print(f"{input1} is a palindrome.")
else:
    print(f"{input1} is not a palindrome.")    

if input2 == input2[::-1]:
    ifPalindrome = True
    print(f"{input2} is a palindrome.")
else:
    print(f"{input2} is not a palindrome.")

if input3 == input3[::-1]:
    ifPalindrome = True
    print(f"{input3} is a palindrome.")
else:
    print(f"{input3} is not a palindrome.")    





print("####################  Task2  ##################")


list1 = [1, 2, 3, 4, 5]

list2 = [6, 7, 8, 9, 10]

list3 = list1 + list2

print(f"List1: {list1}")
print(f"List2: {list2}")    



print(f"List3: {list3}")



print("####################  Task3  ##################")


list_of_names = ["Ali", "Akram", "Bob", "CR7", "Ashraf","Nada" ,"Alex" ,  "John", "Mohammed"]

dict_of_names = {}


for name in list_of_names:
    first_letter = name[0].upper()
    if first_letter not in dict_of_names:
        dict_of_names[first_letter] = []
    dict_of_names[first_letter].append(name)

print(f"List of names: {list_of_names}")
print(f"Dictionary of alphabets by their names: {dict_of_names}")



print("####################  Task4  ##################")


while True:
    x = input("Enter your Name: ")



    if not x.isalpha():
        print("Invalid name. Only letters are allowed.")

        continue

    email = input("Enter your Email: ")

    if email.count("@") == 1 and "." in email.split("@")[1]:


        break

    print("Invalid email.")

print(f"Your Name is: {x}")

print(f"Your Email is: {email}")