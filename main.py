# file = open("my_file.txt")
# content = file.read()
# print(content)
# file.close()
#
# file = open("my_file.txt",mode="w")
# file.write("Hello World")
# file.close()
#
# with open("my_file.txt", mode="w") as file:
#     file.write("\nHello World")
#
# with open("my_file.txt", mode="a") as file:
# file.write("\nHello World")
#
#
# with open("new_file.txt", mode="w") as file:
# file.write("\nHello World")
#
# with open("/Users/ashwi/OneDrive/Desktop/my_file.txt") as file:
#     content = file.read()
#     print(content)
#
# with open("../../../ashwi/OneDrive/Desktop/my_file.txt") as file:
#     content = file.read()
#     print(content)


# with open("/Users/ashwi/OneDrive/Desktop/my_file.txt") as file: absolute path
with open("../../../ashwi/OneDrive/Desktop/my_file.txt") as file:  # relative path
    content = file.read()
    print(content)
