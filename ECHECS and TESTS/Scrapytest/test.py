import json
selected = []

exclure = ["Tablette", "NOUVEAU FUSIBLE", "Webcam", "NOUVEAUFUSIBLE"]
inclure  = []

def exclu(titre) :
    for i in exclure : 
        if i in titre : 
            return True
    return False 

def inclu(titre) : 
    for i in inclure : 
        if i in titre : 
            return True
    return True

for i in json.load(open("ecrans3.json")) :
    if (i.get("price") is not None) and (i.get("price").replace(",", "").isnumeric()) and (not exclu(i["title"])) and inclu(i["title"]) :
        price = float(i["price"].replace(",", "."))
        if True:
            i["price"] = price
            selected.append(i)

selected2 = []
for i in json.load(open("ecrans3.json")) :
    if (i.get("price") is None) : 
        selected2.append(i)


with open("selected.json", "w") as f :
    #json.dump(selected2, f)
    json.dump(sorted(selected, key = lambda x  : x["price"]), f, indent=4)

print("177.8".replace(".", "").isnumeric())
