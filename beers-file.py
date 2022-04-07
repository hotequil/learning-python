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

print(f"beers: {beers}")
print(f"dumps: {json.dumps(beers, indent=4)}")
