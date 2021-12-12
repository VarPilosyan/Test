import random
my_score = 0
comp_score = 0

l = ["qar", "tuxt", "mkrat"]
lucky = [("mkrat", "tuxt"), ("tuxt", "qar"), ("qar", "mkrat")]

while my_score != 3 or comp_score != 3 :
    me = input("CHING-A-CHUNG  ")
    comp = random.choice(l)
    if (me, comp) in lucky :
        my_score += 1
        print("+1 to ME")
    elif (comp, me) in lucky :
        comp_score += 1
        print("+1 to COMPUTER")
if my_score == 3 :
    print("հաղթեցիր դու ☻")
else :
    print("հաղթեց համակարգիչը ☹")
