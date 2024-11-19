with open ("text.txt", "r", encoding="utf-8") as file:
    a = file.read()
    b = a.split()
print(len(b))
