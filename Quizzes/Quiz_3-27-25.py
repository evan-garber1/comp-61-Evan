class Person:
    def __init__(self,first_name, last_name, daily_salary):
        self.money = 0
        self.first_name = first_name
        self.last_name = last_name
        self.daily_salary = daily_salary

    def work(self, day):
        salary = self.daily_salary * day
        self.money = self.money + salary


shawn = Person("Shawn", "Lin", 10)
ben = Person("Ben", "Ben", 20)

shawn.work(30)
ben.work(15)

if shawn.money > ben.money:
    print("Shawn has more money.")
else:
    print("Ben has more money.")

