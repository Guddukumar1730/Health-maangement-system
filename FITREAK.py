print("FITREAK")

print("enter the name of costumer")
name=input()

print("press 1 for  diet or press 0 for workout" )
N1=int(input())
n2=bool(N1)

if name=="guddu" and n2==True:
     with open("theguddudiet.txt","rt") as f:
        print(f.read())

elif name=="guddu" and n2==False:
     with open("thegudduworkout.txt","rt") as f:
         print(f.read())

elif name=="shreyansh" and n2==True:
     with open("shreyanshdiet.txt","rt") as f:
         print(f.read())

elif name=="shreyansh" and n2==False:
     with open("shreyanshworkout.txt","rt") as f:
         print(f.read())

elif name=="harry" and n2==True:
     with open("harrydiet.txt","rt") as f:
         print(f.read())
else:
    with open("harryworkout.txt","rt") as f:
        print(f.read())

