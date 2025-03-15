import time

minutes = 2
seconds = 30
while minutes >= 0:
    while seconds >= 0:
        print(minutes, ":", seconds)
        seconds -= 1 # second = second - 1
        time.sleep(1)
    minutes -= 1
    seconds = 59