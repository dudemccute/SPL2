#Zahlenreihe.py

#n = input("Bitte n eingeben")
#n = int(n)
n = 1000
for i in range (1,n+1):
    if(i < n):
     print(i, end= " < ")
    else:
        print(i)

#Alle geraden Zahlen von 1..n ausgebe
for i in range (1,n+1):
    if (i % 2 == 0):
        print(i , end = " ; ")


#Alle ungeraden
for i in range (1,n+1):
    if (i % 2 != 0):
        print(i , end = " ; ")
