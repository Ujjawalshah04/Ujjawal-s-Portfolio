import random

def gameWin(comp,you):
    if comp==you:
        return None
    elif comp == 's':
        if you=='w':
            return False
        elif you=='g':
            return True
    elif comp == 'w':
        if you=='g':
            return False
        elif you=='s':
            return True
    elif comp == 'g':
        if you=='s':
            return False
        elif you=='w':
            return True

print("Comp turn:snake(s) water(w) or gun(g)")
randNo = random.randint(1,3) 
if randNo==1:
    comp='s'
elif randNo==2:
    comp='w'
elif randNo==3:
    comp='g'
you=input("your's turn:snake(s) water(w) or gun(g)")
a=gameWin(comp,you)

print(f"computer choose {comp}")
print(f"you choose {you}")
print 
if a==None:
    print("the game is a tie!")
elif a:
    print("you win!")
else:
    print("you loose!")


