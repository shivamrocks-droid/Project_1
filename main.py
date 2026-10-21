#we are making a quiz on capital of states of india
import random
from pathlib import Path
print("==========================QUIZ==========================")
with open('question.txt','r') as f:
    list=f.readlines()
    pair=[list[i:i+2] for i in range(0,len(list),2)]
    random.shuffle(pair)
    for qa in pair:
        print("_______________________________________________________________")
        for sep in qa:
            print(sep)
        ans=input("Enter your choice(the initials)=")
        with open("answers.txt","a") as fa:
            fa.write(ans)
            fa.write("\n")



