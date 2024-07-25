# 2진수

# Help on class int in module builtins:
# class int(object)
#  |  int([x]) -> integer
#  |  int(x, base=10) -> integer

# 4가지 문제
# 1. 1-100까지 찍어라
# 2. 이진수 변환
# 3. 0이 하나만 포함된 숫자를 찾고
# 4. 누적합

output =  [i for i in range(1,101) if '{:b}'.format(i).count('0') == 1]
    
for i in output:
    print('{} : {}'.format(i,'{:b}'.format(i)))
print('합계:', sum(output))

# tot = 0
# for i in output:
#     tot+=i
# print(tot)

print('---------------------------------------')
# 숫자의 종류
li = [1,2,3,4,1,2,3,1,4,1,2,3]

ouput = {i:li.count(i) for i in li}
long = len(set(li))

# for i in li:
#     if i in ouput:
#         ouput[i] += 1
#     else:
#         ouput[i] = 1

print(long)
print(ouput)

print('------------------------------------')

# 염기의 개수
# 염기 서열을 입력했을 때
# 각각의 염기가 몇 개 포함되어 있는지
# 세는 프로그램을 구현해 보세요


# input('염기 서열을 입력해주세요:')
li = 'ctacaatgtcagtatacccattgcattagccgg'

# print(f'a의 개수: {li[0].count('a')}')
# print(f't의 개수: {li[0].count('t')}')
# print(f'g의 개수: {li[0].count('g')}')
# print(f'c의 개수: {li[0].count('c')}')

# ------------------------------------------------

# c, g, t, a = (0,0,0,0)

# for i in li:
#     if 'c' == i:
#         c  = c + 1
#     if 't' == i:
#         t += 1
#     if 'a' == i:
#         a += 1
#     if 'g' == i:
#         g += 1
        
# print(c, g, t, a)

# -----------------------------------------


di= {}

di['a'] = li.count('a')
di['t'] = li.count('t')
di['g'] = li.count('g')
di['c'] = li.count('c')

print(di)

print('------------------------------')

# 염기 코돈 개수
li = input('염기 서열을 입력해주세요:')
a = [li[i:i+3] for i in range(0,len(li),3)]
ouput = {}
for i in a:
    if len(i) == 3:
        ouput[i] = li.count(i)
        
print(ouput)

# --------------------------------


# 강사님 코드
dna=input('염기 서열을 입력해주세요:')
cnt = {}
for i in range(0,len(dna),3):
    codon = dna[i:i+3]
    if len(codon) ==3:
        if codon in cnt:
            cnt[codon] = cnt[codon] + 1
        else:
            cnt[codon] = 1
            
            
            

print('--------------------------')

# 2차원 리스트 평탄화
li2 = []
li = [1,2,[3,4],5,[6,7],[8,9]]
for i in li:
    if type(i) is list:
        li2.extend(i)
    else:
        li2.append(i)
print(f'{li}을 평탄화하면')
print(f'{li2}입니다')

