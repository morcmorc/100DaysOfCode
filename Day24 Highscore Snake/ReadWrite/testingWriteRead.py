# file = open("my_file.txt")
# contents = file.read()
# print(contents)
# file.close()

# with open ("my_file.txt") as file:
#     contents = file.read()
#     print(contents)

# with open ("my_file.txt", "a") as file:
#     contents = file.write("New Text.\n")
#     print(contents)

# with open ("C:\\Users\\marcs\\Desktop\\tes.txt") as file:
with open (r"C:\Users\marcs\Desktop\tes.txt") as file: # raw sting
    contents = file.read()
    print(contents)