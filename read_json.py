from json import loads

file = open("./beers.json", "r", encoding="UTF-8")
content = file.read()
beers = loads(content)

print(f"content: {content}")
print(f"content type: {type(content)}")
print(f"beers: {beers}")
print(f"beers type: {type(beers)}")
