import random
import os

def wait():
    input()
    os.system('cls')
    

def print_lives(a,b):
    print("lives of player 1: ",a)
    print("lives of player 2: ",b,"\n\n")

def rand_ammo():
    ammo_sets=[1,2,3,4,5]
    Ch=random.choice(ammo_sets)
    L=0
    B=0
    match Ch:
        case 1:
            L=1
            B=1
        case 2:
            L=2
            B=3
        case 3:
            L=5
            B=3
        case 4:
            L=4
            B=4
        case 5:
            L=1
            B=5
    return L,B


def load_mag():
    mag=[]
    L,B=rand_ammo()
    while L>0 or B>0:
        if L>0 and B>0:
            ch=random.choice(['L','B'])
            if ch=='B':
                B-=1
            else:
                L-=1
            mag.append(ch)
            continue
        elif L==0 and B>0:
            for i in  range(0,B,1):
                mag.append('B')
            break
        elif B==0 and L>0:
            for i in  range(0,L,1):
                mag.append('L')
            break
    print("MAGIZINE INFORMATION \n\n LIVE AMMOS :" ,mag.count('L'), "\n","BLANK AMMOS :",mag.count('B'),"\n\n")
    wait()
    return mag

    
def start_game():
    print("WELCOME TO BUCKSHOT CLONE")
    L_P1=6
    L_P2=6
    print_lives(L_P1,L_P2)
    wait()
    Turn=random.choice([1,2])
    while L_P1>0  or L_P2>0:
        magzine=load_mag()
        while len(magzine)>0:
            print("Player ",Turn,"'s Turns",sep="")
            try:
                T=int(input("\n Choose target \n 1.Opponent \n 2.Yourself \n"))
            except TypeError:
                print("Enter either 1 or 2")
                continue
            if T!=1 and T!=2:
                print("Enter either 1 or 2")
                continue

            bullet=magzine.pop()

            if Turn==1:
                if T==2 and bullet=='L':
                    print("Player 1 is shot \n")
                    wait()
                    L_P1-=1
                    print_lives(L_P1,L_P2)
                    wait()
                    Turn=2
                elif T==1 and bullet=='B':
                    print("It  was blank bullet \n")
                    wait()
                    Turn=2
                elif T==2 and bullet=='B':
                    print("It  was blank bullet \n")
                    wait()
                    Turn=1
                else:
                    print("Player 2 is shot \n")
                    wait()
                    L_P2-=1
                    print_lives(L_P1,L_P2)
                    wait()
                    Turn=2
            else:
                if T==2 and bullet=='L':
                    print("Player 2 is shot \n")
                    wait()
                    L_P2-=1
                    print_lives(L_P1,L_P2)
                    wait()
                    Turn=1
                elif T==1 and bullet=='B':
                    print("It  was blank bullet \n")
                    wait()
                    Turn=1
                elif T==2 and bullet=='B':
                    print("It  was blank bullet \n")
                    wait()
                    Turn=2
                else:
                    print("Player 1 is shot \n")
                    wait()
                    L_P1-=1
                    print_lives(L_P1,L_P2)
                    wait()
                    Turn=1
            if L_P1==0:
                print("PLAYER 1 WON")
                return
            elif L_P2==0:
                print("PLAYER 2 WON")
                return