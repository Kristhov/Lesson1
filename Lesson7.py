# from gpcharts import figure
#
# #simple line graph, as described in the readme.
# fig1 = figure()
# fig1.plot([8,7,6,5,4])
#
# #another line graph, but with two data types. Also adding title
# fig2 = figure(title='Two lines',xlabel='Days',ylabel='Count',height=600,width=600)
# xVals = ['Mon','Tues','Wed','Thurs','Fri']
# yVals = [[5,4],[8,7],[4,8],[10,10],[3,12]]
# fig2.plot(xVals,yVals)

# squares = []
# for x in range(10):
#     squares.append(x**2)
#
# print(squares)
#
# squares = [x**2 for x in range(10) if x>4]
# print(squares)
#
# fruits = ['  banana', '  raspberry ', ' grapefruit  ']
# fruits=[fruit.strip().upper() for fruit in fruits]
# print(fruits)

# nums=[(x, x**2, x**4) for x in range(6)]
# print(nums)

# y=sum([x for x in range (1, 101) if x%2==0])
# print(y)

# start=(1329)
# end=(1423)
# for i in range(start, end + 1):
#     print(format(i, 'X'), end=' ')  #hex
#     print(i, end=' ')               #dec
#     print(chr(i))

import requests

start=(1329)
end=(1423)

res=requests.get('http://www.news.am/arm/')
text=res.text

for symbol in text:
    print(symbol, ord(symbol))