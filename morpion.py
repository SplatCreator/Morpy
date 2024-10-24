ligne1=[' ', ' ', ' ']
ligne2=[' ', ' ', ' ']
ligne3=[' ', ' ', ' ']
def position():
    ligne1[0]=7
    ligne1[1]=8
    ligne1[2]=9
    ligne2[0]=4
    ligne2[1]=5
    ligne2[2]=6
    ligne3[0]=1
    ligne3[1]=2
    ligne3[2]=3
if 1==2==3 or 4==5==6 or 7==8==9 or 1==4==7 or 2==5==8 or 9==6==3 or 1==5==9 or 7==5==3:
    print('Gagné')
else:
    print('match nul')
player1=input("Quel symbole veut tu jouer?")
player2='p'
if player1=='X':
    player2 == 'O'
else:
    player2=='X'
player1_2=int(input("Quel position veut tu jouer?"))
position()=print(player1)


