import os
import random
import time

def conv(x,wx):
    if x%wx:
        j=x//wx
        i=x%wx-1
    else:
        j=x//wx-1
        i=wx-1
    return i,j

def jag(l,wx,wy):
    m=''
    for j in range(wy):
        m+='|---'+'----'*(wx-1)+'|'+'\n'
        for i in range(wx):
            if l[i][j]==0:
                m+='|   '
            elif l[i][j]=='\U0001F6A9':
                m+=f'| {l[i][j]}'
            elif l[i][j]=='\U0000274C' or l[i][j]=='\U0001F4A3' or l[i][j]=='\U0001F4A5':
               m+=f'|{l[i][j]} ' 
            else:
                m+=f'| {l[i][j]} '
        m+=f'|  ({j+1} \n'
    m+='|---'+'----'*(wx-1)+'|\n'
    for k in range(1,wx+1):
        if k//10==0:
            m+=f'  {k} '
        else:
            m+=f' {k} '
    return m

def sefr(x,y):
    global l,lis,wx,wy
    if x<wx-1:
        if lis[x+1][y]==' ':
            if l[x+1][y]==0:
                lis[x+1][y]='0'
                sefr(x+1,y)
            else:
                lis[x+1][y]=l[x+1][y]
    if x>0:
        if lis[x-1][y]==' ':
            if l[x-1][y]==0:
                lis[x-1][y]='0'
                sefr(x-1,y)
            else:
                lis[x-1][y]=l[x-1][y]
    if y<wy-1:    
        if lis[x][y+1]==' ':
            if l[x][y+1]==0:
                lis[x][y+1]='0'
                sefr(x,y+1)
            else:    
                lis[x][y+1]=l[x][y+1]
    if y>0:    
        if lis[x][y-1]==' ':
            if l[x][y-1]==0:
                lis[x][y-1]='0'
                sefr(x,y-1)
            else:
                lis[x][y-1]=l[x][y-1]

os.system('cls')

print('\n')
for g in range(40):
    time.sleep(1/15)
    print('\U00002588',end='')
os.system('cls')
if not os.path.isfile('database.txt'):
    f=open('database.txt','w')
    print('\U0001F600 Wellcome\U0001F600\nWhat is your name?')
    fname=input()
    f.write(f'{fname}\n')
    f.write('0\n0\n0\n0\n0\n0\n0\nMap=0')
    os.system('cls')
    f.close
Map=[]
while True:
    with open('database.txt','r+') as f:
        Name=f.readline()[:-1]
        cWins=int(f.readline()[:-1])
        cLosts=int(f.readline()[:-1])
        Last_Condition=f.readline()[:-1]
        wx=int(f.readline()[:-1])
        wy=int(f.readline()[:-1])
        tme=f.readline()[:-1]
        exec(f.readline())
    mP=[]
    if Last_Condition!='0':
        for io in range(wx):
            mP.append([])
            for jo in range(wy):
                mP[io].append(Map[io][jo])
    print('Hi',f'{Name}\U0001F605\n')
    time.sleep(1)
    print('Type the number of where you wanna go\U0001F607')
    print('1-Profile\n2-Change Name\n3-Play!\n4-History\n5-Exit')
    q=input()
    while (q!='1' and q!='2' and q!='3' and q!='4' and q!='5'):
        print('Unknown Command:)')
        q=input()
    os.system('cls')
    while (q=='1' or q=='2' or q=='4' or q=='5'):
        if q=='1':
            print('\nName:',Name)
            print('Wins:',cWins)
            print('Losts:',cLosts)
            print('\nType r to return\U0001F60A')
            x=input()
            while x!='r':
                print('Unknown Command:)')
                x=input()
            os.system('cls')
        elif q=='2':
            print('What do you want me to call you?\U0001F600')
            Name=input()
            with open('database.txt','w') as f:
                Mp=str(Map)
                f.write(f'{Name}\n{cWins}\n{cLosts}\n{Last_Condition}\n{wx}\n{wy}\n{tme}\nMap={Mp}')
            print('\nYour name has updated!\nType r to return\U0001F60A')
            x=input()
            while x!='r':
                print('Unknown Command:)')
                x=input()
            os.system('cls')
        elif q=='4':
            if Last_Condition=='0':
                print('You haven\'t played the game yet:)')
            else:
                print(f'{Last_Condition}\U0001F643 And your game-map ended like this:\n')
                for i in range(wx):
                    for j in range(wy):
                        if mP[i][j]=='b':
                            mP[i][j]='\U0001F4A3'
                        elif mP[i][j]=='f':
                            mP[i][j]='\U0001F6A9'
                        elif mP[i][j]=='z':
                            mP[i][j]='\U0000274C'
                        elif mP[i][j]=='e':
                            mP[i][j]='\U0001F4A5'
                Mins, Secs = divmod(int(tme), 60)
                tmer = '{:02d}:{:02d}'.format(Mins, Secs)
                print(f'Time Remained: | {tmer} |\n')
                print(jag(mP,wx,wy),end='\r')
            print('\n\nType r to return\U0001F60A')
            x=input()
            while x!='r':
                print('Unknown Command:)')
                x=input()
            os.system('cls')
        elif q=='5':
            print('Are you sure you wanna go?\U0001F61F')
            print('1-Yes! Exit\n2-No! Go back to menu')
            su=input()
            while su!='1' and su!='2':
                print('Unknown Command:)')
                su=input()
            os.system('cls')
            if su=='1':
                break
        print('Hi Again',f'{Name}\U0001F605\n')
        print('Type the number of where you wanna go\U0001F607')
        print('1-Profile\n2-Change Name\n3-Play!\n4-History\n5-Exit')
        q=input()
        while (q!='1' and q!='2' and q!='3' and q!='4' and q!='5'):
            print('Unknown Command:)')
            q=input()
        os.system('cls')
    if q=='5' and su=='1':
        break
    mc=1500
    while mc>=1500:
        mc=0
        print('Determine your map:\U0001F604')
        time.sleep(1)
        print('Width:',end=' ')
        wx=int(input())
        print('Height:',end=' ')
        wy=int(input())
        print('Bomb Amount:',end=' ')
        wb=int(input())
        xy=wx*wy
        if xy<wb:
            print('The amount of the bombs are unlogicly high! :)')
            continue
        bombs=[]
        l=[]
        lis=[]
        for i in range(wx):
            l.append([])
            lis.append([])
            for j in range(wy):
                l[i].append(0)
                lis[i].append(' ')
        cnty=4
        while cnty==4 and mc<1500:
            mc+=1
            bomb = random.sample(range(1,xy+1),wb)
            bombs=[]
            for i in bomb:
                bombs.append(conv(i,wx))
            for h in range(wx):
                cnty=0
                for p in bombs:
                    if p[0]==h:
                        cnty+=1
                    if cnty==4:
                        break
                if cnty==4:
                    break
        if mc==1500:
            print('The amount of the bombs are unlogicly high! :)')
    os.system('cls')
    #print(bombs)
    for i in bombs:
        l[i[0]][i[1]]='\U0001F4A3'
    for i in bombs:
        if i[0]+1<wx and l[i[0]+1][i[1]]!='\U0001F4A3':
            l[i[0]+1][i[1]]+=1
        if i[1]+1<wy and l[i[0]][i[1]+1]!='\U0001F4A3':
            l[i[0]][i[1]+1]+=1
        if i[0]-1>-1 and l[i[0]-1][i[1]]!='\U0001F4A3':
            l[i[0]-1][i[1]]+=1
        if i[1]-1>-1 and l[i[0]][i[1]-1]!='\U0001F4A3':
            l[i[0]][i[1]-1]+=1
        if i[0]+1<wx and i[1]+1<wy and l[i[0]+1][i[1]+1]!='\U0001F4A3':
            l[i[0]+1][i[1]+1]+=1
        if i[0]+1<wx and i[1]-1>-1 and l[i[0]+1][i[1]-1]!='\U0001F4A3':
            l[i[0]+1][i[1]-1]+=1
        if i[0]-1>-1 and i[1]+1<wy and l[i[0]-1][i[1]+1]!='\U0001F4A3':
            l[i[0]-1][i[1]+1]+=1
        if i[0]-1>-1 and i[1]-1>-1 and l[i[0]-1][i[1]-1]!='\U0001F4A3':
            l[i[0]-1][i[1]-1]+=1
    flag=wb
    flags=set({})
    Bombs=set(bombs)
    t=5*xy
    start = time.time()
    while flags!=Bombs and t-(time.time()-start)>0:
        #print(jag(l,wx,wy))
        mins, secs = divmod(int(t-(time.time()-start)), 60)
        timer = '{:02d}:{:02d}'.format(mins, secs)
        print(f'Time Left: | {timer} |')
        print(f'Flags Left: ( {flag} )\n')
        print(jag(lis,wx,wy),'\n')
        print('First type the x-Axis of the place and the press Enter for typing y-Axis and press Enter again to define Left\\Right-click by L\\R\n')
        while True:
            print('x-Axis:',end=' ')
            x=int(input())
            print('y-Axis:',end=' ')
            y=int(input())
            print('L or R:',end=' ')
            fl=input()
            x-=1
            y-=1
            ja=(x,y)
            if x>=wx or y>=wy:
                print('Out of order:)')
                continue
            if fl!='L' and fl!='R':
                print('Unknown Command:)')
                continue
            if (lis[x][y]=='0' or lis[x][y]==1 or lis[x][y]==2 or lis[x][y]==3 or
            lis[x][y]==4 or lis[x][y]==5 or lis[x][y]==6 or lis[x][y]==7 or lis[x][y]==8):
                print('This place in defined before and you can\'t change it:)')
                continue
            if (fl=='L' and lis[x][y]=='\U0001F6A9'):
                print('First you should remove the flag and then click on it:)')
                continue
            if (fl=='R' and flag==0 and lis[x][y]!='\U0001F6A9'):
                print('No flags left:)')
                continue
            break
        os.system('cls')
        if fl=='L':
            if l[x][y]=='\U0001F4A3':
                break
            else:
                if l[x][y]==0:
                    lis[x][y]='0'
                    sefr(x,y)
                else:
                    lis[x][y]=l[x][y]
        if fl=='R':
            if lis[x][y]=='\U0001F6A9':
                lis[x][y]=' '
                flag+=1
                flags.remove(ja)
            else:
                lis[x][y]='\U0001F6A9'
                flag-=1
                flags.add(ja)
    if t-(time.time()-start)<0:
        tme=0
        print('You ran out of time\U0001F614\U0001F614\n')
        cLosts+=1
        Last_Condition='You lost the last game'
        for i in bombs:
            if lis[i[0]][i[1]]==' ':
                lis[i[0]][i[1]]='\U0001F4A3'
        diff=flags.difference(Bombs)
        for k in diff:
            lis[k[0]][k[1]]='\U0000274C'
        print(jag(lis,wx,wy),'\n')
        Maap=lis.copy()
        for i in bombs:
            Maap[i[0]][i[1]]='b'
        for j in flags:
            Maap[j[0]][j[1]]='f'
        for k in diff:
            Maap[k[0]][k[1]]='z'
    elif flags!=Bombs :
        tme=int(t-(time.time()-start))
        Mins, Secs = divmod((tme), 60)
        tmer = '{:02d}:{:02d}'.format(Mins, Secs)
        print(f'You Lost\U0001F614\U0001F614\nTime Remained: | {tmer} |\n')
        cLosts+=1
        Last_Condition='You lost the last game'
        for i in bombs:
            if lis[i[0]][i[1]]==' ':
                lis[i[0]][i[1]]='\U0001F4A3'
        lis[x][y]='\U0001F4A5'
        diff=flags.difference(Bombs)
        for k in diff:
            lis[k[0]][k[1]]='\U0000274C'
        print(jag(lis,wx,wy),'\n')
        Maap=lis.copy()
        for i in bombs:
            Maap[i[0]][i[1]]='b'
        for j in flags:
            Maap[j[0]][j[1]]='f'
        for k in diff:
            Maap[k[0]][k[1]]='z'
        Maap[x][y]='e'
    else:
        tme=int(t-(time.time()-start))
        Mins, Secs = divmod(int(tme), 60)
        tmer = '{:02d}:{:02d}'.format(Mins, Secs)
        print(f'You Won\U0001F601\U0001F973\U0001F973\nTime Remained: | {tmer} |\n')
        cWins+=1
        Last_Condition='You won the last game'
        for i in bombs:
            lis[i[0]][i[1]]='\U0001F4A3'
        print(jag(lis,wx,wy),'\n')
        Maap=lis.copy()
        for i in bombs:
            Maap[i[0]][i[1]]='b'
    Map=str(Maap)
    with open('database.txt','w') as f:
        f.write(f'{Name}\n{cWins}\n{cLosts}\n{Last_Condition}\n{wx}\n{wy}\n{tme}\nMap={Map}')
    print('Do you want to go back to menu?\n1-Yes!\n2-No! Exit the game')
    d=input()
    while d!='1' and d!='2':
        print('Unknown Command:)')
        d=input()
    os.system('cls')
    if d=='2':
        print('Are you sure you wanna go?\U0001F61F')
        print('1-Yes! Exit\n2-No! Go back to menu')
        su=input()
        while su!='1' and su!='2':
            print('Unknown Command:)')
            su=input()
        os.system('cls')
        if su=='1':
            break
print('Hope you enjoyed the game\U0001F601 See you next time!\U0001F609')