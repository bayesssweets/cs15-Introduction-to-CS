print("Привет! Я твой помощник по здоровью.")
name = input("Как тебя зовут? ")
print("Приятно познакомиться, " + name + "!")
height = input("Введи свой рост в сантиметрах: ")
height = int(height)
weight = input("Введи свой вес в килограммах: ")
weight = float(weight)
age = input("Сколько тебе лет? ")
age = int(age)
gender = input("Какой у тебя пол (мужской/женский)? ")
if gender == "мужской":
    bmr = 10 * weight + 6.25 * height - 5 * age + 5
elif gender == "женский":
    bmr = 10 * weight + 6.25 * height - 5 * age - 161
else:
    print("Я не понял твой пол, посчитаю по формуле для женщин.")
    bmr = 10 * weight + 6.25 * height - 5 * age - 161
print()
print("Вот что я узнал о тебе:")
print("Имя: " + name)
print("Рост: " + str(height) + " см")
print("Вес: " + str(weight) + " кг")
print("Возраст: " + str(age) + " лет")
print("Пол: " + gender)
print()
print("Тебе нужно примерно " + str(round(bmr, 2)) + " калорий в день.")
print("Если хочешь похудеть или набрать вес, скорректируй это число!")



