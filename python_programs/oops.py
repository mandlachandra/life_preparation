class Person:

    def __init__(self,name,age,salary):
        self.name = name
        self.age = age
        self.salary = salary

    # def __str__(self):
    #     return f"name:{self.name}, Age:{self.age},salary:{self.salary}"

    #creata a list of person objects
people = [
    Person("Alice",30,50000),
    Person("bob",28,49000),
    Person("charlie",27,45000),
    Person("max",25,30000)
    ]

#sort by age
people_sorted = sorted(people, key=lambda people: people.age)

#print the sorted list
print("Sorted by age:")
for people in people_sorted:
    print(people.age, people.name, people.salary)