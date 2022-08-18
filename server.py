from flask import Flask, request, abort
import json
import random
from data import me, catalog

app = Flask(__name__)



@app.get("/")
def home():
    return "Hello from flask"



@app.delete("/test")
def test():
    return "This is just another endpoint"


@app.get("/about")
def about():
    return "Hello Wesley"


###########################################################
############## API PRODUCTS################################



@app.get("/api/test")
def test_api():
    return json.dumps("OK")

# get  /api/ bbout return the me dictionary as json
@app.get("/api/about")
def about_api():
    return json.dumps(me)


@app.get("/api/catalog")
def get_catalog():
    return json.dumps(catalog)


@app.post("/api/catalog")
def save_product():
    product = request.get_json()
    if not "title" in product:
        return abort(400, "ERROR: Title is required")

    if len(product["title"]) < 5:
        return abort(400, "ERROR: You must enter at least 5 characters")

    if not "price" in product():
        return abort(400, "ERROR: Price is required")

    if product["price"] < 1:
        return abort(400, "ERROR: Price must be greater or equal to 1")


    product["_id"] = random.randint(100, 100000)

    catalog.append(product)

    return product 


@app.get('/api/product/<id>')
def get_product_by_id(id):
    for prod in catalog:
        if prod["_id"] == id:
            return json.dumps(prod)

    return json.dumps("Error: Invalid Id")


@app.get("/api/products/<category>")
def get_products_by_category(category):
   results = []
   for prod in catalog:
        if prod["category"].lower() == category.lower():
            results.append(prod)

   return json.dumps(prod)


@app.get("/api/count")
def catalog_count():
    count = len(catalog)
    return json.dumps(count)


@app.get("/api/catalog/total")
def catalog_total():
    total = 0
    for prod in catalog:
        total += prod["price"]

    return json.dumps(total)


@app.get("/api/catalog/cheapest")
def catalog_cheapest():
    cheapest = catalog[10.00]
    for prod in catalog:
       if prod["price"] < cheapest["price"]:
            cheapest = prod
    
    return json.dumps(cheapest)




@app.get("/api/game/<pick>")
def game(pick):
    

    num = random.randint(0,2)
    pc = ""
    if num == 0:
        pc = "paper"
    elif num == 1:
        pc = "rock"
    else:
        pc = "scissors"

    winner = ""
    if pick == "paper":
        if pc == "rock":
            winner = "you"
        elif pc == "scissors":
            winner = "pc" 
        else:
            winner = "draw"

    elif pick == "rock":
        if pc == "rock":
            winner = "draw"
        elif pc == "scissors":
            winner = "you" 
        else:
            winner = "pc"

    elif pick == "scissors":
        if pc == "rock":
            winner = "pc"
        elif pc == "scissors":
            winner = "draw" 
        else:
            winner = "you"

    results = {
        "you": pick,
        "pc": pc,
        "winner": winner
    }

    return json.dumps(results)










#app.run(debug=True)