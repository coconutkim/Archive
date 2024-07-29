# dict_a = {}
# dict_a = {'name':'구름'}
# print(dict_a)

# dict_a = {'name':'구름'}
# dict_a = {}
# print(dict_a)

# ----------------------------------------

# numbers = [1,2,6,8,4,3,2,1,9,5,4,9,7,2,1,3,5,4,8,9,7,2,3]
# counter = {}

# for number in numbers:
#     a = numbers.count(number)
#     counter[number] = a
    
# print(counter)

# --------------------------------------------


# numbers = [1,2,6,8,4,3,2,1,9,5,4,9,7,2,1,3,5,4,8,9,7,2,3]
# counter = {}

# for number in numbers:
#     if number in counter:
#         counter[number] = counter[number]+1
#     else:
#         counter[number]=1

# print(counter)


# # -------------------------------------



# import collections

# numbers = ['apple','banana','cake','apple','cake']
# print(collections.Counter(numbers))



# # -------------------------------------------------------
character = {
    'name': '기사',
    'level':12,
    'items': {
        'sword':'불꽃의 검',
        'armor':'풀플레이트'
    },
    'skill':['베기','세게 베기','아주 세게 베기']
}

for key, value in character.items():
    print(type(value))


for key in character:
    if type(value) is str:
        print(f'{key}:{character[key]}')
    elif type(value) is int:
        print(f'{key}:{character[key]}')
    elif type(value) is dict:
        for k,v in value.items():
            print(f'{k}:{v}')
    # elif type(value) is list:
    #     for i in 

