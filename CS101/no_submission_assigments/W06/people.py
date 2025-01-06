people = [
    "Stephanie 36",
    "John 29",
    "Emily 24",
    "Gretchen 54",
    "Noah 12",
    "Penelope 32",
    "Michael 2",
    "Jacob 10"
]

youngest_person = ''
youngest_age = 1000

for person in people:

    person = person.split()
    name = person[0]
    age = int(person[1])

    if age < youngest_age:
        youngest_person = name
        youngest_age = age


    # print(f"name: {person[0]}, age: {person[1]}")    

print(f'The youngest is {youngest_person}, with {youngest_age} years old')
