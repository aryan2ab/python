word = "Donkey"

with open("fold.txt", "r") as f:
    content = f.read()

contentNew = content.replace(word, "#####")

with open("fold.txt", "w") as f:
    f.write(contentNew)