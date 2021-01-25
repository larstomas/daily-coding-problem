names = ["Tomas", "Stina", "Marie", "Ralf"]

# index = 0
# for name in names:
#     print(index, name)
#     index += 1


# Altenative

for index, name in enumerate(names):
    print(index, name)

# extra
for index, name in enumerate(names, start=1):
    print(index, name)