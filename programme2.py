print("entrer le premier nombre")
a= input()
try:
    a = int(a)
except ValueError:
    print("Vous avez fait une erreur")
else:
    print("entrer le deuxieme nombre")
    b = input()
    try:
        b = int(b)
    except:
        print("Vous avez fait une erreur")
    else:
        if a > b :
            print(str(a) + " > " + str(b))
        elif a < b:
            print(str(a) + " < " + str(b))
        else:
            print(str(a) + " = " + str(b))