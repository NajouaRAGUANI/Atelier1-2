'''Atelier1-Exercice1'''

nombre=int(input("Entrer le nombre des termes:"))
sum = 0
def factorielle(n):
    if n == 0 :
        return 1
    else :
        return n * factorielle(n - 1)
for i in range( 1 ,nombre + 1):
    sum = sum + factorielle(i) / i

print("la somme de" , nombre , "termes de la serie est:" , sum)
