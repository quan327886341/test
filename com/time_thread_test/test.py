import time
import datetime


# def calcProd():
#     product = 1
#     for i in range(1, 100000):
#         product = product * i
#     return product
#
# startTime = time.time()
# prod = calcProd()
# endTime = time.time()
# print('The result is %s digits long.' % len(str(prod)))
# print('Took %s seconds to calculate.' % (endTime - startTime))


print(datetime.datetime.now())
dt = datetime.datetime(2018, 12, 24, 16, 37, 36)
print(datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S'))
print(dt.year, dt.month, dt.day)
print(dt.hour, dt.minute, dt.second)
thousandDay = datetime.timedelta(days=1000)
print(dt + thousandDay)