info = {
    "name" : "nasim",
    "age" : 20,
    "department" : "computer",
    "shift" : "1st",
    21 : 21,
    "tup" : True
    }

print(info.keys())
print()
print(list(info.keys()))
print()
print(info.values())
print()
print(tuple(info.values()))
print()
print(info.items())
print()
print(info.get("name"))
print()
info.update({"full_name" : "Nasim Uddin","new_name" : "rasel khan"})
print(info)

