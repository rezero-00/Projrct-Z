name = input("Как тебя зовут? ")
age = int(input("Сколько тебе лет? "))

print("Привет!", name)

if age >= 18:
    print("Доступ разрешён")
else:
    print("Доступ запрещён")    
