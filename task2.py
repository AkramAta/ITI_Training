

print("####################  Task1  ##################")

x = input("Enter a string: ")

count_vowels = 0
for char in x:
    if char.lower() in "aeiou":
        count_vowels += 1
print(f"Number of vowels in {x}: {count_vowels}")



print("####################  Task2  ##################")



find_char = "i"

if find_char in x:
    print(f"The character '{find_char}' is located in the string {x} in the position {x.index(find_char)}.")
else:
    print(f"The character '{find_char}' is not located in the string {x}.")



print("####################  Task3  ##################")




list_of_strings =  ["a","aba", "aa", "ad", "vcd", "aba"]

list_of_longest_strings = []

max_length = 0

for string in list_of_strings:
    if len(string) > max_length:
        max_length = len(string)
        list_of_longest_strings = [string]
    elif len(string) == max_length:
        list_of_longest_strings.append(string)

print(f"List of strings: {list_of_strings}")
print(f"Longest strings: {list_of_longest_strings}")




print("####################  Task4  ##################")





apple = [10, 20, 15]
capacity = [20, 35, 40, 50]


total_apples = sum(apple)


capacity.sort(reverse=True)

boxes = 0
current_capacity = 0

for cap in capacity:
    current_capacity += cap
    boxes += 1

    if current_capacity >= total_apples:
        break

print(boxes)