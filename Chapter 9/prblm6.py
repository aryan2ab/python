with open("log.txt", "r") as f:
    log_content = f.read()

if("python" in log_content):
    print("Python found in log file.")
else:
    print("Python not found in log file.")    