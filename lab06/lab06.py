class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
        self.child = None

    def add_child(self, child):
        self.child = child

    def print_family_line(self):
        print(f"{self.name} ({self.age})")
        if self.child:
            self.child.print_family_line()

    def count_large_age_gaps(self, gap_limit):
       if not self.child:
        return 0
       gap = self.age - self.child.age
       return (1 if gap > gap_limit else 0) + self.child.count_large_age_gaps(gap_limit)
       

def build_family_line():
    name = input("Enter person's name: ")
    age = int(input("Enter person's age: "))
    person = Person(name,age)
    has_child = input(f"Does {name} have a child? (yes/no) ")
    if has_child == "yes":
        child = build_family_line()
        person.add_child(child)
    return person

# --- Main Program Starts Here ---
print("Welcome to the Generational Gap Checker!\n")

# TODO: Build the family line from user input
root = build_family_line()

print("\nHere is your family line:\n")
root.print_family_line()

gap_limit = int(input("Enter the minimum age gap to check between generations: "))
large_gaps = root.count_large_age_gaps(gap_limit)
print(f"Number of generations with an age gap greater than {gap_limit}: {large_gaps}")