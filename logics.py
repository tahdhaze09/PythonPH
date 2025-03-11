choice = input("entr a number between 5 and 50: ")

while int(choice) < 5 or int(choice) > 50:
    print("please pick a number between 5 and 50")
    choice = input("entr a number between 5 and 50: ")
convertChoice = int(choice)
for i in range(1, convertChoice + 1):
    if i <= 30:
        print(i , "- #")
    else:
        print(i , "- *")