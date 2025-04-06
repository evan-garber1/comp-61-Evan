import random

class Person:
    def __init__(self,first_name, last_name, daily_salary):
        self.money = 0
        self.first_name = first_name
        self.last_name = last_name
        self.daily_salary = daily_salary
        self.yearly_salary_list = []

    def work(self, day):
        salary = self.daily_salary * day
        self.money = self.money + salary

    def work_a_month(self):
        salary = self.daily_salary * 30 * random.random()
        self.yearly_salary_list.append(salary)


person_list = []
shawn = Person("Shawn", "Lin", 10)
ben = Person("Ben", "Ben", 20)
evan = Person("Evan", "Garber", 30)
bob = Person("Bob", "Smith", 15)
person_list =[shawn, ben, evan, bob]
rich_person = None
most_daily_salary = 0 
for person in person_list:
    if person.daily_salary > most_daily_salary:
        rich_person = person
        most_daily_salary = rich_person.daily_salary
print(rich_person.first_name, rich_person.last_name)



shawn.work(30)
ben.work(15)




