ingreds_per_cake = {"sukker" : 2,
                    "mel" : 3,
                    "melk" : 3,
                    "egg" : 1}

ingred = {"sukker" : 0,
          "mel" : 0,
          "melk" : 0,
          "egg" : 0}

with open("../data/leveringsliste.txt") as infile:
    for line in infile:
        pairs = line.split(",")
        for pair in pairs:
            ingredient, num = pair.split(":")
            ingredient = ingredient.strip()
            num = int(num.strip())
            ingred[ingredient] += num

possible_num_cakes = []
for ingredient in ingred:
    possible_num_cakes.append(ingred[ingredient]//ingreds_per_cake[ingredient])

print(min(possible_num_cakes))