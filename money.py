much= int(input('금액을 입력하세요:'))
ch = {"dollar":1167, "yen":1.096, "euro":1268, "yuan":171}

do = much/ch["dollar"]
print(f"{do}달러")
