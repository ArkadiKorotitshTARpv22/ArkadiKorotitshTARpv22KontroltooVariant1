#Ülesanne1
N = int(input())

print('    /V\    ' * N)
print('   / V \   ' * N)
print('  / V V \  ' * N)
print(' /VV V VV\ ' * N)

#Ülesanne2
R = int(input())

for i in range(2, R + 1, 2):
    print(i, end=' ')

#Ülesanne3
Q=0.0
while type(Q) !=int:
    try:
        Q=int(input("Sisestage number: "))
    except:
        TypeError
F=0
F1=1
while Q > 0:
    answer=Q %10
    F=F+answer
    F1=F1*answer
    Q=Q//10 
print("Numbrite summa sisestatud arvust: "+str(F))
print("Numbrite korrutis sisestatud arvust: "+str(F1))