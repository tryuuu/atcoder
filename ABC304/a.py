def get_person_order(names, ages):
    n = len(names)
    min_age = min(ages)
    min_age_index = ages.index(min_age)

    person_order = []
    for i in range(n):
        index = (min_age_index + i) % n
        person_order.append(names[index])

    return person_order

n = int(input())  
names = []
ages = []
for _ in range(n):
    name, age = input().split() 
    names.append(name)
    ages.append(int(age))

result = get_person_order(names, ages)
for name in result:
    print(name)
