score_file = open("score.txt", "r", encoding="utf8") # score.txt 파일을 읽기 모드로 열기
print(score_file.read()) # 파일 전체 읽어 오기
score_file.close()

score_file = open("score.txt", "r", encoding="utf8")
while True:
    line = score_file.readline()
    if not line: # 더 이상 읽어 올 내용이 없을 때
        break # 반복문 탈출
    print(line, end="") # 읽어 온 내용 출력

score_file.close()
