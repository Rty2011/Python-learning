cabinet={3:"me",50:"you"}
print(cabinet[50])
print(cabinet[3])
print(3 in cabinet)
print(49 in cabinet)
print(cabinet)
cabinet["3"]="boy"
cabinet["4"]="girl"
print(cabinet)
del cabinet[50]
print(cabinet)
print(cabinet.values())
print(cabinet.keys())
print(cabinet.items())
cabinet.clear()
print(cabinet)