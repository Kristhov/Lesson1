# def f():
#     pass
#
# def append(str_list):
#     pass
#
# f()
# g()

# lst = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h']
# print(lst[0:4])
# print(lst[3:6])
# print(lst[3:4])

# link = 'http://www.main.com/smith/index.html'
# x = link[:4].upper()
# x = link.find('com')
# print(x)

# link = 'http://www.main.com/smith/index.html'
# x=link.replace('smith','ferreira')
# print(x)

# link = 'http://www.main.com/smith/index.html'
# x=link.count('/')
# print(x)

# link = 'http://www.main.com/smith/index.html'
# x=link.split('/')
# print(x)

# events = '9/13 2:30 PM\n9/14\n9/14 11:15 AM\n9/14 1:00 PM\n9/15 9:00 AM'
# # print(events)
#
# x=events.count('9/14')
# print(x)
#
# x=events.find('9/14')
# print(x)
#
# x=events.find('9/15')
# print(x)

# f=open('data.txt', 'r+')
# y=f.readlines()
# print(y)
# f.close()
#
# f=open('test.txt','w')
# f.write('This is a new file')
# f.close()
#
# f=open('test.txt','r')
# y=f.read()
# print(y)
# f.close()


f=open('hist.txt','w')
def histrograme(number_list):
    for i in number_list:
        f.write('*'*i+'\n')
    f.close()

histrograme([4,9,7])
