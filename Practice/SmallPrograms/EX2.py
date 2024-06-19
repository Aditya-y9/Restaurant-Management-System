# exercise
# user does not need to enter an input to this
# the program automatically gets the time from your computer.
import time
timestamp = time.strftime("%H, %M, %S")
print(timestamp)
timestamp = int(time.strftime("%H"))
if timestamp < 5:
    print("Good Night")
elif timestamp > 5 and timestamp < 12:
    print("Good Morning")
elif timestamp >= 12 and timestamp < 15:
    print("Good Afternoon")
else:
    print("Good Evening")

