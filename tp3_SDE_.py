#exo1
var1 = 12
var2 = 17.9
var3 = "SdE2"
print("var1 = " , var1, "of type ", type(var1))
print("var2 = " , var2, "of type ", type(var2))
print("var3 = " , var3, "of type ", type(var3))

#exo2
def premierNombres(n):
    for i in range(1, n + 1):
        if i > 1:
            ok = True
            for j in range(2, i):
                if(i % j == 0):
                    ok = False
                    break
            if(ok):
                print(i)    

print("Les premiers nombres premiers inférieurs à 15 sont : ")
premierNombres(15)   

#exo3 :

fruitsList = ["Pomme", "orange", "frasie", "raisin", "cerises"]
fruitsList.sort()

for fruit in fruitsList:
    print(fruit, len(fruit))

fruitsList.append("bleu")
fruitsList.append("vert")
fruitsList.append("jaune")

fruitsList.reverse()
print(fruitsList)

#exo 4 :

libraryDictionary = dict({
    "Victor Hugo": ["Les misérables ", "Le Dernier Jour d'un condamné ", "L'Homme qui rit"],
    "Émile Zola": ["Nana", "La bête ", "La curée "],
    "Nizar Kabbani": "arabian love poems",
    "William Shakespeare": "Hamlet"
})

command = ""

while(command != "sortir"):
    command = input("Entre un auteur  ")
    livres = libraryDictionary.get(command.lower())
    if livres != None:
        print(livres)
    else: 
        print("auteur non trouvé")




