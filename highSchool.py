#형설고등학교 3학년 기말고사 수학, 영어, 국어의 성적을 딕셔너리로 구축하고
# 각 개인의 평균과 총점을 구하세요.

# 1. 키로 학번을 사용하는데 1번부터 9번까지
# 2. 수학, 영어, 국어 순으로 점수값만 딕셔너리로 구성하세요
# 3. 평균은 소수점 1자리에서 반올림해서 정수로 출력하세요.
# 4. 총점은 표시하시고 실행하면 1번부터 9번까지 성적목록을 출력하세요
# 5. 학번, 국어, 영어, 수학, 총점, 평균 순으로 목록을 출력해주세요

num = input("학번:")

dic = {"수학":91, "영어":88, "국어":57}

kor = str(dic["국어"])
print(f"국어:{kor}")

eng = str(dic["영어"])
print(f"영어:{eng}")

mth = str(dic["수학"])
print(f"수학:{mth}")

total = str(dic["국어"]+dic['수학']+dic['영어'])
print(f"총점: {total}")

total = int(total)
totel = total/3
totel = str(totel)
print(f"평균: {totel}")