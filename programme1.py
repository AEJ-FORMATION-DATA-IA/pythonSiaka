print("entrer le premier nombre A")
a=input()
try:
       a = int(a)
except ValueError:
    print("Vous avez fait une erreur")
else:
    print("entrer le deuxieme nombre B")
    b=input()
    try:
        b = int(b)
    except:
        print("Vous avez fait une erreur")
    else:
        print("la somme de A=" +str(a) +  " et de B= " + str(b) + " est " + str(a + b))