"""
============================================================
  CS50P LECTURE 9 — ET CETERA
  Post-Lecture Coding Exercises
============================================================
  RULES:
  1. Do NOT look at the lecture while solving these.
  2. If you can't solve it in 10 minutes, mark it ❌ and move on.
  3. Come back to ❌ problems after 24 hours.
  4. You pass this lecture when ALL 15 are ✅.
============================================================
"""

# ─── EXERCISE 1: Sets ─────────────────────────────────────
# Given two lists:
list_a = [1, 2, 3, 4, 5, 3, 2, 1]
list_b = [4, 5, 6, 7, 8, 5, 4]
# Using sets, find and print:
#   1. Unique elements in list_a
#   2. Unique elements in list_b
#   3. Elements in BOTH lists (intersection)
#   4. Elements in EITHER list (union)
#   5. Elements in list_a but NOT in list_b (difference)

# YOUR CODE:


# ─── EXERCISE 2: Global vs Local ─────────────────────────
# start with counter = 0
# Write a function increment() that increases counter by 1.
# First try WITHOUT the `global` keyword — what error do you get?
# Then fix it WITH `global`.
# Then write a COMMENT explaining why using global is generally bad
# and what a better approach would be (hint: pass as parameter, return).

# YOUR CODE:


# ─── EXERCISE 3: Constants ───────────────────────────────
# Define constants: MAX_ATTEMPTS = 3, MIN_PASSWORD_LENGTH = 8
# Write a login system that uses these constants:
#   - Give the user MAX_ATTEMPTS tries to enter the password
#   - Password must be at least MIN_PASSWORD_LENGTH characters
# Explain in a comment: does Python actually enforce constants?

# YOUR CODE:


# ─── EXERCISE 4: Type Hints ──────────────────────────────
# Rewrite these functions WITH proper type hints:
# 1. A function that takes a name (str) and returns a greeting (str)
# 2. A function that takes a list of ints and returns their sum (int)
# 3. A function that takes a dict of str→int and returns the max value key (str)
# 4. A function that takes an optional age (int or None) and returns a message (str)
# Use: str, int, float, list, dict, Optional (from typing)

# YOUR CODE:


# ─── EXERCISE 5: List Comprehensions ─────────────────────
# Solve ALL of these using ONLY list comprehensions (no for loops):
# 1. Squares of 1-10: [1, 4, 9, 16, ..., 100]
# 2. Even numbers from 1-20: [2, 4, 6, ..., 20]
# 3. First letter of each word in "The Quick Brown Fox Jumps": ["T","Q","B","F","J"]
# 4. Flatten [[1,2],[3,4],[5,6]] into [1,2,3,4,5,6]
# 5. Numbers 1-30 that are divisible by 3 AND 5: [15, 30]

# YOUR CODE:


# ─── EXERCISE 6: Dict Comprehensions ─────────────────────
# Solve using dict comprehensions:
# 1. Create a dict of {number: square} for 1-10
#    {1: 1, 2: 4, 3: 9, ...}
# 2. Given words = ["apple", "banana", "cherry", "date"]
#    Create {word: len(word)} → {"apple": 5, "banana": 6, ...}
# 3. Invert a dict: given {"a": 1, "b": 2, "c": 3}
#    Create {1: "a", 2: "b", 3: "c"}

# YOUR CODE:


# ─── EXERCISE 7: enumerate() ─────────────────────────────
# Given:
fruits = ["apple", "banana", "cherry", "date", "elderberry"]
# Use enumerate to print each fruit with its index:
#   "0. apple"
#   "1. banana"  etc.
# Then use enumerate starting from 1:
#   "1. apple"
#   "2. banana"  etc.

# YOUR CODE:


# ─── EXERCISE 8: unpacking and *args/**kwargs ────────────
# 1. Unpack this tuple into 3 variables: point = (3, 4, 5)
# 2. Unpack with * : first, *rest = [1, 2, 3, 4, 5]
# 3. Write a function `sum_all(*args)` that sums ANY number of arguments
# 4. Write a function `build_profile(**kwargs)` that takes any keyword
#    arguments and returns them as a formatted string:
#    build_profile(name="Tejas", age=19, college="BMSCE")
#    → "name: Tejas\nage: 19\ncollege: BMSCE"

# YOUR CODE:


# ─── EXERCISE 9: map() and filter() ──────────────────────
# Given:
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# Using map():
#   1. Square all numbers → [1, 4, 9, ...]
#   2. Convert all to strings → ["1", "2", ...]
# Using filter():
#   3. Keep only even numbers → [2, 4, 6, ...]
#   4. Keep only numbers > 5 → [6, 7, 8, 9, 10]
# Using map + filter together:
#   5. Square only the even numbers → [4, 16, 36, 64, 100]

# YOUR CODE:


# ─── EXERCISE 10: Lambda Functions ───────────────────────
# Rewrite the map/filter from Exercise 9 using lambda functions
# instead of named functions.
#   Example: list(map(lambda x: x**2, numbers))
# Also:
# Sort this list of tuples by the second element using lambda:
students = [("Tejas", 88), ("Aria", 95), ("Nova", 72), ("Kira", 91)]
# Result: [("Nova", 72), ("Tejas", 88), ("Kira", 91), ("Aria", 95)]

# YOUR CODE:


# ─── EXERCISE 11: Generators ─────────────────────────────
# Write a generator function `countdown(n)` that yields n, n-1, ..., 1.
# Use it in a for loop.
#
# Write another generator `fibonacci_gen()` that yields Fibonacci numbers
# INFINITELY. Use it with a loop that breaks after 15 numbers.
#
# Explain in a comment: why are generators better than lists for large sequences?

# YOUR CODE:


# ─── EXERCISE 12: Docstrings ─────────────────────────────
# Take your BankAccount class from Lecture 8 and add proper docstrings:
#   - Module docstring at the top
#   - Class docstring explaining the class
#   - Method docstrings for each method (include Args and Returns)
# Use the Google docstring style:
# """Short description.
#
# Args:
#     param1: Description.
#     param2: Description.
#
# Returns:
#     Description of return value.
#
# Raises:
#     ErrorType: When this happens.
# """

# YOUR CODE:


# ─── EXERCISE 13: argparse Preview ──────────────────────
# Write a script that uses argparse to accept:
#   --name (required): your name
#   --greeting (optional, default="Hello"): the greeting to use
#   --shout (optional flag): if present, output in uppercase
# Usage: python script.py --name Tejas --greeting "Yo" --shout
# Output: "YO, TEJAS!"

# YOUR CODE:


# ─── EXERCISE 14: Combining Everything ───────────────────
# Write a data processing pipeline using Phase 1 + 9 tools:
# Given raw sales data (list of dicts):
sales = [
    {"product": "Laptop", "price": 999.99, "qty": 5, "region": "North"},
    {"product": "Phone", "price": 699.99, "qty": 12, "region": "South"},
    {"product": "Tablet", "price": 449.99, "qty": 8, "region": "North"},
    {"product": "Laptop", "price": 999.99, "qty": 3, "region": "South"},
    {"product": "Phone", "price": 699.99, "qty": 7, "region": "North"},
    {"product": "Headphones", "price": 199.99, "qty": 20, "region": "East"},
    {"product": "Laptop", "price": 999.99, "qty": 2, "region": "East"},
]
# Using comprehensions, map, filter, and lambda:
#   1. Total revenue per product (price * qty, summed)
#   2. Products with total revenue > $5000
#   3. Revenue by region
#   4. Most sold product (by qty)
#   5. Sorted products by total revenue (descending)

# YOUR CODE:


# ─── EXERCISE 15: The "Can You Build Something?" Test ────
# Build a Contact Manager CLI (the FINAL version) that combines:
# - OOP: Contact class, ContactManager class
# - File I/O: save/load from JSON
# - Error handling: crash-proof
# - Type hints: on all functions and methods
# - Generators: yield contacts matching a search
# - Comprehensions: for filtering and transforming data
# - Docstrings: on every class and public method
# Features:
#   - Add, edit, delete, search contacts
#   - Sort by name, phone, or date added
#   - Export to CSV
#   - Search using generator (yields matching contacts lazily)
#   - Stats: total contacts, most common domain in emails

# YOUR CODE:


"""
============================================================
  SCOREBOARD
  Mark each exercise: ✅ (solved) or ❌ (couldn't solve)

  Ex 1:  |  Ex 2:  |  Ex 3:  |  Ex 4:  |  Ex 5:
  Ex 6:  |  Ex 7:  |  Ex 8:  |  Ex 9:  |  Ex 10:
  Ex 11: |  Ex 12: |  Ex 13: |  Ex 14: |  Ex 15:

  Total: __/15

  PASS THRESHOLD: 12/15 minimum. All ❌ must be retried.
============================================================
"""
