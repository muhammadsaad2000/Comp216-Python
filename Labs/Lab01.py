from random import randint

#the following variable will be used in the rest of the exercise
pm = 'justin pierre james trudeau'
instructor = 'narendra pershad'
harry = "You've gotta ask yourself a question: do I feel lucky? …well, do ya, punk?"
numbers = [randint(5, 10) for _ in range(20)]
new_set = "This is my lab 01 for python"

instructor_set = set(instructor)
print(instructor_set)

instructor_set.add('z')
print(instructor_set)

instructor_set.remove(' ')
print(instructor_set)

new_set = set('narendra')
print(instructor_set.intersection(new_set))

print(instructor_set.union(new_set))

print(instructor_set.pop())

instructor_set.update('xyz')
print(instructor_set)

print(len(instructor_set))

pm_tuple = tuple(pm)
print(pm_tuple)

print('There are {} e\'s in the tuple'.format(pm_tuple.count('e')))
print('You can find a at index {} of the tuple'.format(pm_tuple.index('a')))
print('There are {} elements in the tuple'.format(len(pm_tuple)))

a, b, *rest = pm_tuple
print(a)
print(b)
print(rest)

print(pm_tuple[2])
print(pm_tuple[4])

harry_list = harry.split()
print(harry_list)

harry_list.append('Eastwood')
harry_list.insert(0, 'Clint')
harry_list.remove('question:')
harry_list.extend(['Dirty', 'Harry'])
print(harry_list)

harry_list.sort()
print(harry_list)
harry_list.reverse()
print(harry_list)

print('There are {} do\'s in the list'.format(harry_list.count('do')))
print('You can find "ask" at index {} of the list'.format(harry_list.index('ask')))
print('There are {} elements in the list'.format(len(harry_list)))

d = {
    3462: 'Artificial Intelligence',
    3468: 'Software Engineering Technician',
    3469: 'Software Engineering Technology',
    3472: 'Artificial Intelligence (FT)',
    3478: 'Software Engineering Technician (FT)',
    3528: 'Health Informatics Technology (FT)',
    3609: 'Game - Programming',
    3668: 'Health Informatics Technology',
    3679: 'Game - Programming (FT)'}

print(d)

print(d.keys())
print(d.values())

print(d[3462])
print(d.get(3462))

set_from_tuple = set(pm_tuple)
set_from_list = set(harry_list)
set_from_dict = set(d.keys())

print(set_from_tuple)
print(set_from_list)
print(set_from_dict)

tuple_from_set = tuple(instructor_set)
tuple_from_list = tuple(harry_list)
tuple_from_dict = tuple(d.keys())

print(tuple_from_set)
print(tuple_from_list)
print(tuple_from_dict)

list_from_set = list(instructor_set)
list_from_tuple = list(pm_tuple)
list_from_dict = list(d.values())

print(list_from_set)
print(list_from_tuple)
print(list_from_dict)

for x in instructor_set:
    print(x)

for x in pm_tuple:
    print(x)

for x in harry_list:
    print(x)

for key in d:
    print(key, d[key])
    
for i, x in enumerate(instructor_set):
        print(i, x)
    
for i, x in enumerate(pm_tuple):
        print(i, x)
    
for i, x in enumerate(harry_list):
        print(i, x)
    
for i, (k,v) in enumerate(d.items()):
        print(i, k, v)
    
for i, (k,v) in enumerate(d.items()):
            print(i, k, v)
            