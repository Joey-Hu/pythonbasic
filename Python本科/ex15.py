from sys import argv

script,filename = argv

txt = open(filename,encoding='UTF-8')

print(f"Here is your file {filename}:")
print(txt.read())

print("Type the filename again:")
file_again = input("> ")

txt_again=open(file_again,encoding='UTF-8')

print(txt_again.read())