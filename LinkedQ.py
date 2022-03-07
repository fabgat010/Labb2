
from linkedQFile import LinkedQ

#3.)
#Vad vi ska göra
#1. lägga in ordningen på "korten"
#2.Lägga in dem i en lista
#3. använda append, pop, deque gör att lägga ut rätt kort i taget
#4. använda "IsEmpty" för att kontrollera så att kortleken är slut

q=LinkedQ()
visakort=[]

#7 1 12 2 8 3 11 4 9 5 13 6 10
#sys.stdin.readline()

def main():
        svar=input("Vilka kort vill du använda?")
        svar_split=svar.split()
        for k in svar_split:
                q.enqueue(k)
        return q

def trolla():
    while not q.isEmpty():
        f_kort=q.dequeue()
        q.enqueue(f_kort)
        n_kort=q.dequeue()
        visakort.append(n_kort)

main()    
trolla()
print(*visakort, sep = ' ')
      