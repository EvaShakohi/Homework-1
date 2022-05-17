infile= open('t.txt','r')
Q=[for x in infile]
Q=[x.strip()]
c=0
for i in Q:
    print(i)
a=input('enter answer')
if a ==i:
    c=c+1
nam = input('enter name')
print(nam,c)