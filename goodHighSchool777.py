# class_list = [cl for cl in range(1, 9+1)]
# print(class_list)
# print(round(94.77, 0))
import random
import numpy
# ran_list = [random.sample(range(60, 100), 3) for ran in range(27)]
gimal = {i : random.sample(range(60, 100), 3) for i in range(1,9+1)}
print(gimal)
#for index, item in enumerate(gimal.items(), start=1) :
print('학번', '국어', '영어', '수학', '총점', '평균')
for item in gimal.items() :
    
    #print(item[0], item[1][0], item[1][1], item[1][2], numpy.sum(item[1]), int(round(numpy.average(item[1]),0)) )
    #print(item)
    #space = 4
    print(f'{item[0]:4} {item[1][0]:3} {item[1][1]:4} {item[1][2]:3} {numpy.sum(item[1]):4} {int(round(numpy.average(item[1]),0)):3} ')
