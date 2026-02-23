# Dictionaries

# Stores data that are in key value pair

band = {
    'vocal': "plant",
    'guitar': 'Page',
}

band2 = dict(vocals='Plant', guitar='page')
band0 = dict(Alex=9, Adrian=6, Aaron=4, Sophie=13)

print(type(band0))
print(band0)
print(band2)
print(len(band0))

# Accessing the items

print(band['guitar'])

print(band0.get("Alex"))

# list all values
print(band0.values())
# list all keys
print(band0.keys())

print(band0.items())
print("Alex" in band0)


# add items
band0.update({"Munir": 42})
print(band0)
band0["Shahida"] = 40
print(band0)

# remove items

band0.pop('Munir')
print(band0)
band0.popitem()
print(band0)
band0.popitem()
print(band0)

band0.update({"Munir": 42})
print(band0)
band0["Shahida"] = 40
print(band0)

del band0['Shahida']
print(band0)

band.clear()
print(band)


# copy dictionaries

band3 = band2  # creats a reference. Wil change band2, if band 3 is
# altered. NOT a good idea

print(band2)
print(band3)

band3["drums"] = "Dave"

print(band2)

band4 = band2.copy()

band4.popitem()
print(band4)

# copy using the dictionary function
band5 = dict(band0)

print(band5)


# Nested Dictionary

member1 = {
    'name': 'Plant',
    'instrument': 'vocals'
}
member2 = {
    'name': 'Page',
    'instrument': 'guitar'
}
band99 = {
    'member1': member1,
    'member2': member2
}

print(band99)
print(band99['member1']['name'])
