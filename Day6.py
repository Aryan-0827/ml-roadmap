from datetime import datetime


# writing to a file
f = open("notes.txt", "w")
f.write("my name is aryan\n")
f.write("i am learning python\n")
f.write("files are easy\n")
f.close()

print("file created")
print()


# read the whole file
f = open("notes.txt", "r")
data = f.read()
f.close()
print("read():")
print(data)


# read one line at a time
f = open("notes.txt", "r")
line1 = f.readline()
line2 = f.readline()
line3 = f.readline()
f.close()

print("readline():")
print(line1)
print(line2)
print(line3)


# read all lines as a list
f = open("notes.txt", "r")
lines = f.readlines()
f.close()
print("readlines():")
print(lines)
print()


# add a new line without deleting the old ones
f = open("notes.txt", "a")
f.write("this line was added later\n")
f.close()

# check if it worked
f = open("notes.txt", "r")
print(f.read())
f.close()


# log function
def log(message):
    now = datetime.now()
    t = now.strftime("%Y-%m-%d %H:%M:%S")
    line = "[" + t + "] " + message + "\n"

    f = open("log.txt", "a")
    f.write(line)
    f.close()


log("app started")
log("loading data")
log("data loaded")
log("app closed")

f = open("log.txt", "r")
print(f.read())
f.close()