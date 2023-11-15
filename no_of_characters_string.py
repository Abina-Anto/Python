def count_characters(string):
    count=0
    for char in string:
        if char.isalpha():
            count+=1
    return count
string =input("Enter the string:")
result = count_characters(string)
print("Number of characters:", result)
