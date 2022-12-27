#####################################
#      Exercice1                    #
#####################################

keys = ['Ten', 'Twenty', 'Thirty']
values = [10, 20, 30]
dictio = dict()
for a,b in zip(keys,values):
    dictio[a]=b
    
print(dictio)

#####################################
#      Exercice2                    #
#####################################

#Part 1

family = {"rick": 43, 'beth': 13, 'morty': 5, 'summer': 8}
price_TTC = 0
for j,i in family.items():
    
    if i <= 3:
        print(j,"must pay", 0)
        continue
    elif i <=12:
        price_TTC += 10
        print(j,"must pay", 10, "$")
    else:
        price_TTC +=15
        print(j,"must pay", 15, "$")
print("\n The total Price which family must pay is ", price_TTC,"$\n")


#Part 2 Bonus
family = {}
n = int(input("Enter the number of people wants a ticket "))
for i in range(0,n):
    a = input("Enter a name of person")
    b = int(input("Enter age of personne"))
    family[a] = b
price_TTC = 0
for j,i in family.items():
    
    if i <= 3:
        print(j,"must pay", 0)
        continue
    elif i <=12:
        price_TTC += 10
        print(j,"must pay", 10, "$")
    else:
        price_TTC +=15
        print(j,"must pay", 15, "$")
print("\n The total Price which family must pay is ", price_TTC,"$")




#####################################
#      Exercice3                    #
#####################################


brand = {
"name": "Zara",
"creation_date": 1975,
"creator_name": "Amancio Ortega Gaona ",
"type_of_clothes": ["men", "women", "children", "home" ],
"international_competitors": ["Gap", "H&M", "Benetton"], 
"number_stores": 7000,
"major_color":{
    "France": "blue",
    "Spain": "red",
    "US": ["pink", "green"]
    }
}