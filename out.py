# reference

string = input("enter str: ")

new_str = ""

for character in string:
    if character not in ["a", "e", "i", "o", "u"]:
        new_str += character

print(new_str)