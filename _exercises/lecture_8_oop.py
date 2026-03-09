"""
============================================================
  CS50P LECTURE 8 — OBJECT-ORIENTED PROGRAMMING
  Post-Lecture Coding Exercises
============================================================
  RULES:
  1. Do NOT look at the lecture while solving these.
  2. If you can't solve it in 10 minutes, mark it ❌ and move on.
  3. Come back to ❌ problems after 24 hours.
  4. You pass this lecture when ALL 13 are ✅.
============================================================
"""

# ─── EXERCISE 1: Your First Class ─────────────────────────
# Create a class `Dog` with:
#   __init__(self, name, breed, age)
#   bark(self) → returns "Woof! My name is [name]!"
#   __str__(self) → returns "[name] the [breed], age [age]"
# Create 3 Dog objects and print each.

# YOUR CODE:


# ─── EXERCISE 2: Instance vs Class Variables ──────────────
# Create a class `Student` with:
#   Class variable: school = "BMSCE" (shared by all students)
#   Instance variables: name, semester, gpa (unique to each)
#   __str__ method
# Create 3 students. Print each, then print Student.school.
# Change school for ONE student. What happens to the others? Add comment.

# YOUR CODE:


# ─── EXERCISE 3: Methods ─────────────────────────────────
# Create a class `BankAccount` with:
#   __init__(self, owner, balance=0)
#   deposit(self, amount) → adds to balance, returns new balance
#   withdraw(self, amount) → subtracts (if enough funds), returns new balance
#                           → raise ValueError if insufficient funds
#   __str__(self) → "Account of [owner]: $[balance]"
# Test with deposits, withdrawals, and an attempted overdraft.

# YOUR CODE:


# ─── EXERCISE 4: Properties ──────────────────────────────
# Create a class `Temperature` with:
#   Store temperature internally as Celsius
#   Property `celsius` → get/set in Celsius
#   Property `fahrenheit` → get/set in Fahrenheit (converts automatically)
#   Setting fahrenheit should update the internal Celsius value
#   Use @property decorator
# Test:
#   t = Temperature(100)
#   print(t.fahrenheit)  → 212.0
#   t.fahrenheit = 32
#   print(t.celsius)     → 0.0

# YOUR CODE:


# ─── EXERCISE 5: Inheritance ─────────────────────────────
# Create a class hierarchy:
#   Shape (base class):
#     __init__(self, color)
#     area(self) → raise NotImplementedError
#     __str__ → "[color] [class_name] with area [area]"
#
#   Rectangle(Shape):
#     __init__(self, color, width, height)
#     area() → width * height
#
#   Circle(Shape):
#     __init__(self, color, radius)
#     area() → π * radius²
#
#   Square(Rectangle):  # inherits from Rectangle!
#     __init__(self, color, side) → calls super().__init__(color, side, side)
#
# Create one of each and print them.

# YOUR CODE:


# ─── EXERCISE 6: super() ─────────────────────────────────
# Create a class hierarchy for vehicles:
#   Vehicle(make, model, year) → __str__, start(), stop()
#   Car(Vehicle + num_doors) → overrides __str__ to include doors
#   ElectricCar(Car + battery_kwh) → overrides start() to say "Silent start..."
#                                  → new method range() → returns battery_kwh * 5 km
# Each __init__ should call super().__init__()
# Create an ElectricCar and test all methods.

# YOUR CODE:


# ─── EXERCISE 7: Polymorphism ────────────────────────────
# Create a list of different shapes (from Exercise 5).
# Loop through them and call .area() on each.
# The correct area method runs based on the actual object type.
# Print: "[shape] → area = [area]"
# This IS polymorphism — same method name, different behavior.

# YOUR CODE:


# ─── EXERCISE 8: Operator Overloading ────────────────────
# Create a class `Vector` with x and y coordinates.
# Implement:
#   __add__ → Vector(1,2) + Vector(3,4) = Vector(4,6)
#   __sub__ → Vector(5,3) - Vector(1,1) = Vector(4,2)
#   __mul__ → Vector(2,3) * 3 = Vector(6,9) (scalar multiplication)
#   __eq__  → Vector(1,2) == Vector(1,2) → True
#   __str__ → "Vector(x, y)"
#   magnitude(self) → returns √(x² + y²)

# YOUR CODE:


# ─── EXERCISE 9: Composition ─────────────────────────────
# Build a Library system with composition (objects containing objects):
#   Book(title, author, isbn, available=True)
#   Member(name, member_id, borrowed_books=[])
#   Library(name, books=[], members=[])
#     - add_book(book)
#     - register_member(member)
#     - borrow_book(member_id, isbn) → marks book unavailable, adds to member's list
#     - return_book(member_id, isbn) → reverse of borrow
#     - search(query) → returns books matching title or author
# Test the full flow: create library, add books, register member, borrow, return.

# YOUR CODE:


# ─── EXERCISE 10: classmethod and staticmethod ───────────
# Create a class `Employee`:
#   __init__(self, name, salary)
#   Class variable: employee_count = 0 (increments in __init__)
#   
#   @classmethod
#   from_string(cls, emp_str) → creates Employee from "name-salary" string
#     Employee.from_string("Tejas-50000") → Employee("Tejas", 50000)
#
#   @staticmethod
#   is_valid_salary(salary) → returns True if salary > 0

# YOUR CODE:


# ─── EXERCISE 11: __repr__ vs __str__ ────────────────────
# Create a class `Point` with x and y.
# __str__  → "Point at (x, y)" — human readable
# __repr__ → "Point(x, y)"     — developer readable (can recreate the object)
#
# Show the difference:
#   p = Point(3, 4)
#   print(p)          → uses __str__
#   print(repr(p))    → uses __repr__
#   print([p])        → uses __repr__ (lists use repr for their items!)

# YOUR CODE:


# ─── EXERCISE 12: Exception Classes ──────────────────────
# Create custom exception classes for a banking app:
#   BankError(Exception) — base exception
#   InsufficientFundsError(BankError) — not enough money
#   InvalidAmountError(BankError) — negative or zero amount
#   AccountNotFoundError(BankError) — account doesn't exist
#
# Update your BankAccount class to raise these custom exceptions
# instead of generic ValueError.

# YOUR CODE:


# ─── EXERCISE 13: The "Can You Build Something?" Test ────
# Build a CLI Task Manager (OOP version):
# Classes:
#   Task(title, description, priority="medium", completed=False)
#     - complete() → marks as done
#     - __str__ → "[✅/⬜] [priority] title"
#   TaskManager(tasks=[])
#     - add_task(task)
#     - complete_task(index)
#     - delete_task(index)
#     - list_tasks(filter=None) → show all, or filter by priority/status
#     - save(filename) → save to JSON
#     - load(filename) → load from JSON
#
# Features:
#   - Menu-driven CLI
#   - Persistent storage (JSON)
#   - Filter by: all, completed, pending, high/medium/low priority
#   - Should be impossible to crash with bad input.

# YOUR CODE:


"""
============================================================
  SCOREBOARD
  Mark each exercise: ✅ (solved) or ❌ (couldn't solve)

  Ex 1:  |  Ex 2:  |  Ex 3:  |  Ex 4:  |  Ex 5:
  Ex 6:  |  Ex 7:  |  Ex 8:  |  Ex 9:  |  Ex 10:
  Ex 11: |  Ex 12: |  Ex 13:

  Total: __/13

  PASS THRESHOLD: 10/13 minimum. All ❌ must be retried.
============================================================
"""
