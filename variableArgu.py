def profile(name, age, *language):
    print("이름 : {0}\t나이 : {1}\t".format(name, age), end="")
    print(len(language))
    for i in range(len(language)):
        print(language[i])

profile("찰리", 20, "파이썬", "자바", "C", "C++", "C#", "자바스크립트")
print("-"*40) # 자바스크립트 추가
profile("루시", 25, "코틀린", "스위프트")
