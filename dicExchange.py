much= int(input('환전하실 금액을 입력하세요:'))
ch = {"dollar":1167, "yen":1.096, "euro":1268, "yuan":171}

do = much/ch["dollar"]
do = round(do, 2)
print(f"{do}달러")

ye = much/ch["yen"]
ye = round(ye, 2)
print(f'{ye}엔')

eu = much/ch["euro"]
eu = round(eu, 2)
print(f'{eu}유로')

yu = much/ch["yuan"]
yu = round(yu, 2)
print(f'{yu}위안')