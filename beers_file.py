import json

beers = {
    "hotequil": {
        "good": "ipa",
        "favorite": "double ipa"
    },
    "joao": {
        "good": "weiss",
        "favorite": "neipa"
    }
}

result = json.dumps(beers, indent=4)

print(f"beers: {beers}")
print(f"dumps: {result}")

file = open("./beers.json", "w", encoding="UTF-8")

file.write(result)
file.close()
