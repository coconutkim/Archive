class telAddr :
    def __init__(self, name, age, tel):
        self.name = name
        self. age = age
        self.tel = tel
    def setName(self, name):
        self.name = name
    def setAge(self, age):
        self.age = age
    def setTel(self, tel):
        self.tel = tel

telBook = []

te = telAddr('sunhee', 24, '010-625-9928')
telBook.append(te)
te = telAddr('chulsu', 36, '010-536-9019')
telBook.append(te)
te = telAddr('malhee', 40, '010-893-0092')
telBook.append(te)
te = telAddr('sunshin', 26, '010-772-9920')
telBook.append(te)


for i in telBook:
        print(f'name: {i.name}   age: {i.age}   tel: {i.tel}')