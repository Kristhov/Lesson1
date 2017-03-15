# lst=[3,1,-7,-4,9,-2]
#
# def negative(lst):
#     print(lst)
#     for i in range(len(lst)):
#         if lst[i]<:0
#     print(lst)


# def cities3():
#     lst = []
#     while True:
#         city = input('Enter city: ')
#         if city == '':
#             break
#         lst.append(city)
#     print(lst)
#     return lst
# cities3()

# Dictionary
# employee = {
#     '864-20': ['Arm', 'Spartyan'],
#     '987-65': ['Vlad', 'Tundyan'],
#     '100-01': ['Kiazh', 'Damyan']}
# print(employee['100-01'])

# days = {'Mo': 1, 'Tu': 2, 'W': 3}
#
# days2 = {'Tu': 2, 'Fr': 5}
#
# print(days)
# print(days.pop('Tu'))
# print(days)
# days['Tu']=2
# print(days)
# days. update(days2)
# print(days)
# print(days.items())
# print(days.keys())
#
# for k, v in days.items():
#     print(k,v)

# itemList = [95, 96, 100, 85, 95, 90, 95, 100, 100]
# counters = {}
# for item in itemList:
#     if item in counters:  # increment item counter
#         counters[item] += 1
#     else:  # create item counter
#         counters[item] = 1
#
# print(counters)
#
# itemList = 'to be or not to be'.split()
# counters = {}
# for item in itemList:
#     if item in counters:  # increment item counter
#         counters[item] += 1
#     else:  # create item counter
#         counters[item] = 1
# print(counters)


# def word_count(text):
#     counters = {}
#
#     for item in text.split():
#         if item in counters:  # increment item counter
#             counters[item] += 1
#         else:  # create item counter
#             counters[item] = 1
#
#
#     print(counters)
#
# word_count('to be or not to be')


# phonebook = {
# 	'Arm':'56-78-90',
# 	'Vlad':'34-56-78',
# 	'Kiazh':'48-76-54'
# }
# while True:
#     print('Enter your name', end='')
#     name=input()
#     if name in phonebook:
#         print(phonebook[name])

# t = [('a', 10), ('c', 22), ('b', 1)]
# t.sort()
# print(t)
# sorted(t)
# print(t)

# lst = list()
# d = {'a': 10, 'b': 1, 'c': 22}
# for k, v in d.items():
#     lst.append((v, k))
#
# print(lst)
# sorted_lst=sorted(lst, reverse=True)
# print(sorted_lst)

f=open('romeo.txt', 'r+')
y=f.read()
f.close()
lst=y.split()
print(lst)

counters = {}
for item in lst:
    if item in counters:  # increment item counter
        counters[item] += 1
    else:  # create item counter
        counters[item] = 1

print(counters)

lst = list()
for k, v in counters.items():
   lst.append((v, k))

print(lst)
sorted_lst=sorted(lst, reverse=True)
print(sorted_lst)