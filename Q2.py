d=int( input('enter decimal number:'))
l=[]
while true:
    l.append(d%2)
    l=d//2
    if d==0:
        break
    l.reverse()
    for i in l:
        print (i,end='')
