class Person:
    def __init__(self, name, age):
        # Initialize name and age
        self.name = name
        self.age = age
        self.child = None  # Only one child (no list)

    def add_child(self, child):
        # Assign the given child to this person
        self.child = child

    def print_family_line(self):
        # Print this person's name and age
        print(f"{self.name} ({self.age})")
        # Then, if they have a child, call this same function on the child
        if self.child:
            self.child.print_family_line()

    def count_large_age_gaps(self, gap_limit):
        # Count how many parent-child pairs have an age gap > gap_limit
        if not self.child:
            return 0
        gap = self.age - self.child.age
        return (1 if gap > gap_limit else 0) + self.child.count_large_age_gaps(gap_limit)

def build_family_line():
    # Ask the user for the person's name
    name = input("Enter person's name: ")
    # Ask the user for the person's age
    age = int(input(f"Enter {name}'s age: "))
    # Create a Person object with that name and age
    person = Person(name, age)

    while True:
        # Ask the user if this person has a child (yes or no)
        has_child = input(f"Does {name} have a child? (yes/no): ").strip().lower()
        if has_child in ["yes", "no"]:
            break
        print("Invalid input. Please enter 'yes' or 'no'.")
    
    # If the user says "yes":
    if has_child == "yes":
        # Recursively call build_family_line() to create the child
        child = build_family_line()
        # Add the child to the current person using add_child()
        person.add_child(child)
    
    # Return the person object
    return person

# --- Main Program Starts Here ---
print("Welcome to the Generational Gap Checker!\n")

# Build the family line from user input
root = build_family_line()

print("\nHere is your family line:")
# Call the function to print the family line
root.print_family_line()

# Ask the user for an age gap value
while True:
    try:
        gap_limit = int(input("\nEnter the minimum age gap to check between generations: "))
        break
    except ValueError:
        print("Invalid input. Please enter a valid number.")

# Call the function to count large age gaps and print the result
large_gaps = root.count_large_age_gaps(gap_limit)
print(f"Number of generations with an age gap greater than {gap_limit}: {large_gaps}")



