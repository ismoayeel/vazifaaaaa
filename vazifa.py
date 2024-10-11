f=open("kitoblar.txt", "w+")

class Book:
    def __init__(self, id, name, author, count, price):
        self.ID=id
        self.name=name
        self.author=author
        self.count=count
        self.price=price

    def __str__(self):
        return f"{self.ID} {self.name} {self.author} {self.count} {self.price}\n"

k1=Book(1000, "O'tkan kunlar", "Abdulla Qodiriy", 10, 150000)
k2=Book(1001, "Qutlug' qon", "Chingiz aytmatov", 10, 200000)
k3=Book(1002, "Yodgor", "Hoshimjon", 10, 100000)
k4=Book(1003, "Sahro qizlari", "Zafar Qayumov", 10, 50000)
k5=Book(1004, "Ufq", "MuhammadAli", 10, 250000)


lst=[k1, k2, k3, k4, k5]
for i in lst:
    f.write(f"{i}")


lst=[]
for i in f.read().split("\n"):
    lst.append(i)

while True:
    print("1. ID boyicha bittaga kamaytirish")
    print("2. ID boyicha tanlab o'chirish")
    print("0. Tugatish")
    tanlov=int(input("tanla: "))
    if tanlov == 0:
        exit()
    elif tanlov == 1:
        kam_id=input("qaysi id ni kamaytiray: ")
        for i in lst:
            if i.split(" ")[0] == kam_id:
                m=int(i.split(" ")[-2])
                m-=1
                i.split(" ")[-2].remove(f"{m}").append(f"{m-1}")
                print(i)
                break
    elif tanlov == 2:
        ochir_id=input("qaysi id ni ochiray: ")
        for i in lst:
            if i.split(" ")[0]==ochir_id:
                lst.remove(i)
                print(i)
                break
    break

for i in lst:
    f.write(f"{i}")

f.close()
