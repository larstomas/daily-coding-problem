class Person:
    pass


person = Person()

# person.first = "Tomas"
# person.last = "Bäckman"

# print(person.first)
# print(person.last)

# first_key = "first"
# first_val = "Tomas"

# # setattr(person, "first", "Tomas")
# setattr(person, first_key, first_val)

# print(person.first)


# first = getattr(person, first_key)

# print(first)


person_info = {"first": "Tomas", "last": "Bäckamn"}

for key, val in person_info.items():
    setattr(person, key, val)


print(person.first)
print(person.last)

for key in person_info.keys():
    print(getattr(person, key))
