from datetime import datetime

def log(message):
    now = datetime.now()
    t = now.strftime("%Y-%m-%d %H:%M:%S")
    line = "[" + t + "] " + message + "\n"

    try:
        if message.strip() == "":
            raise ValueError("Message cannot be empty.")
        f = open("log.txt", "a")
        f.write(line)

    except ValueError as e:
        print("Bad input:", e)

    except IOError as e:
        print("Could not write to log.txt:", e)

    else:
        print("Logged:", message)

    finally:
        try:
            f.close()
        except:
            pass


log("app started")
log("loading data")
log("")           
log("data loaded")
log("app closed")


try:
    f = open("log.txt", "r")
    content = f.read()

except FileNotFoundError:
    print("log.txt not found. Nothing written yet.")

except IOError as e:
    print("Could not read log.txt:", e)

else:
    print(content)

finally:
    try:
        f.close()
    except:
        pass