key_list = ['name','hp','mp','level']
value_list = ['기사',200,30,5]
character = {}

# for i in range(0,4):
#     v = value_list[i]
#     character[key_list[i]] = v

# print(character)

# for i, v in enumerate(key_list):
#     character[v] = value_list[i]
# print(character)

i = 0
for v in key_list:
    character[v] = value_list[i]
    i += 1
print(character)

# ----------------------------
limit = 10000
i = 1


# sum_value = 0
while sum_value <limit:
   
    sum_value              +=i
    i +=1  



print(f'{i}를 더할 때 {limit}을 넘으며 그때의 값은 {sum_value}입니다.')

------------------------------------------------------

max_value = 0
a = 0
b = 0

for i in range(1,100):
    j = 100-i


    if max_value<i*j:
        max_value = i*j
        a=i
        b=j

print('최대가 되는 경우 {} * {} = {}'.format(a,b,max_value))