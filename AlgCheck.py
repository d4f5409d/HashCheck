quote = "\""
import os

print("What is the hash?")
hash = input()

hash

print("Which algo would you like to use?")

algo = input()

algo

file_path = input('Enter a file path: ')

if os.path.exists(file_path):
    filename = input()

    filename

    success = hash + " " + "*" + filename
    method = "shasum -a "
    add = quote + success + quote + " | " + method + algo + " --check"
    resolve = "" + add
    os.system(str(resolve))
else:
    print("This is not a valid location! Please try again.")
