from data import me

#get data from dicitionary
print(me["first_name"] + "" +me["last_name"])

#modify
me["color"] = "blue"

#add new keys
me["age"] = 27


# read non existing key
#     print(me["title"])#<--- will crash code

# check if a key exists inside a dictionary
if "title" in me:
    print(me["title"])



# print the full address
# street num, city

address = me["address"]
print(address["street"] + " " + str(address["number"]) + "," + address["city"])



