f = open("poem.txt")

c = f.read()

if("twinkle" in c):
    print("Yes, the word 'twinkle' is present in the file.")
else:
    print("No, the word 'twinkle' is not present in the file.")
f.close()    
        