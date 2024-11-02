# python dictionaries - {key:value} pairs, ordered , changeable and contains no duplicates 

# methods :  .get() - get the values of the key 
            # .update ()
            # .pop("key") / popitem() - pops the latest updated pair 
            # .clear() - clears the dictionary 
            # .keys() - gives all keys existing /   .values() - gives all values existing

dict_captials = {"India":"New Delhi",
                 "USA": "Washington D.C",
                 "Russia": "Mascow"}

# print(dict_captials)

# get the values of keys 

print(dict_captials.get("India"))

for i in dict_captials:
    print(dict_captials[i])

dict_captials.update({"India": "Delhi"})
print(dict_captials)   # --> update the existing value

# insert a new value 
dict_captials.update({"Germany":"Berlin"})
print(dict_captials)

# delete a particular value 
dict_captials.pop("Russia")
print(dict_captials)

# popitem - deletes the last updated pair 
dict_captials.popitem()
print(dict_captials)

keys = dict_captials.keys()
print(keys)

valuesofDict = dict_captials.values()
print(valuesofDict)

for key in keys:
    print(key)

for value in valuesofDict:
    print(value)

items = dict_captials.items()  # ---> items = [(),()]
print(items)

for key, value in items:
    print(f"{key}:{value}")