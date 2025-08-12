words = ["Donkey", "bad", "ugly"]

with open("fold.txt", "r") as f:
    content = f.read()
for word in words:
    content = content.replace(word, "#"*len(word))

with open("fold.txt", "w") as f:
    f.write(content)