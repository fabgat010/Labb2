from array import array
#Vad vi ska göra:
#1.Skapa en class för arrayq
#2. Skapa en tom array
#3. Lägga till saker i arrayen genom en funktion enqueue, genom append
#4. Använda kommandot Pop för att plocka ut ett elemet och spara den i en variabel, göra en funktion dequeue
#5. Skapa en funktion för att kolla ifall listan är tom, retunera true/false


class ArrayQ:
    def __init__(self):
        self.__array = array("i") # Skapar en tom array som vill ha integers

    def enqueue(self, x): # Metod för att lägga till värden
        self.__array.append(int(x)) #Lägger x sist i arrayen

    def __str__(self):
        return str(self.__array)

    def dequeue(self): # Metod för att ta bort värden
        popv = self.__array.pop(0) #poppar första elementet i arrayen och sparar det i en variabel som vi senare returnerar
        return popv

    def isEmpty(self): # Metod för att kolla om arrayen är tom eller inte.
        if self.__array:
            return False
        elif not self.__array:
            return True

            