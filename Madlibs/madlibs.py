import secrets

print("Title : Eat, Drink, And Be Sick")
noun = []
for i in range(4):
    n = input("Enter noun : ")
    noun.append(n)
plural = []
for i in range(6):
    pn = input("Enter plural noun : ")
    plural.append(pn)
adjective = []
for i in range(2):
    a = input("Enter adjective : ")
    adjective.append(a)
adverb = input("Enter adverb : ")
letter = input("Enter any letter : ")
body_part = input("Enter any body part : ")
print("An inspector from the Department of Health and ", secrets.choice(noun) , " Services paid a surprise visit to our " , secrets.choice(adjective) , " school cafeteria.")
print("The lunch special, prepared by our " , secrets.choice(adjective) , "dietician, was spaghetti and " , secrets.choice(noun) , " balls with a choice of either a " , secrets.choice(noun) , " salad or French " , secrets.choice(plural) , ".")
print("The inspector found the meat-" , secrets.choice(plural) , " to be overcooked and discovered a live " , secrets.choice(noun) , " in the fries,causing him to have a " + body_part + " ache.")
print("In response, he threw up all over his " , secrets.choice(plural) , ".")
print("In his report, the inspector " + adverb + " recommended that the school cafeteria serve only nutritious " , secrets.choice(plural) , " as well as low-calorie " , secrets.choice(plural) , " and that all of the saturated " , secrets.choice(plural) , " be eliminated.")
print("He rated the cafeteria a " + letter + "-minus.")
