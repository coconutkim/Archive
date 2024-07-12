score = {"1":[80, 67, 98],
       "2":[80, 67, 98],
       "3":[80, 67, 98],
       "4":[80, 67, 98],
       "5":[80, 67, 98],
       "6":[80, 67, 98],
       "7":[80, 67, 98],
       "8":[80, 67, 98],
       "9":[80, 67, 98]}

print('  <형설고등학교 3학년 기말고사 결과>')
print('='*40)
print('학번  국어  영어  수학   총점  평균')
print('-'*40)

hakbun = 

def scor(hakbun):
       for i in range(1,hakbun+1):
              slist = score[str(i)]
              tot = slist[0]+slist[1]+slist[2];
              ave = int(round(tot / 3, 0))
              print(f'{i}    {slist[0]}    {slist[1]}    {slist[2]}    {tot}    {ave}')
 