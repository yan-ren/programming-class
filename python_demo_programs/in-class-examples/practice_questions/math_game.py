import random
import time
good=0
bad=0
answered=0
questions=int(input("how many questions:"))
set_timer=int(input('how much time (in seconds):'))
start = current = time.time()
while current - start < set_timer:
    numbera=random.randint(1,10)
    numberb=random.randint(1,10)
    answer=numbera+numberb
    youranswer=int(input(str(numbera)+"+"+str(numberb)))
    if youranswer==answer:
        good+=1
        answered+=1
    else:
        bad+=1
        answered+=1
    print("..........")
    current = time.time()


print("good:"+str(good))
print("bad:"+str(bad))
print("number of question answered:"+str(answered))
