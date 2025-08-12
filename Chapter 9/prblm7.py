
with open("log.txt", "r") as f:
    lines = f.readlines()

lineno = 1    
for line in lines:
    if("python" in line):
        print(F"Python found in log file. Line no: {line}")
    lineno +=1

    
else:
    print("Python not found in any line of the log file.")        