"""
============================================================
  CS50P LECTURE 4 — LIBRARIES
  Post-Lecture Coding Exercises
============================================================
  RULES:
  1. Do NOT look at the lecture while solving these.
  2. If you can't solve it in 10 minutes, mark it ❌ and move on.
  3. Come back to ❌ problems after 24 hours.
  4. You pass this lecture when ALL 12 are ✅.
============================================================
"""

# ─── EXERCISE 1: import Basics ─────────────────────────────
# Import the `math` module.
# Using functions from math, print:
# 1. The value of pi (math.pi)
# 2. Square root of 144
# 3. 2 raised to the power 10
# 4. Ceiling of 4.2
# 5. Floor of 4.8

# YOUR CODE:


# ─── EXERCISE 2: from...import ─────────────────────────────
# Import ONLY the `choice` and `shuffle` functions from `random`.
# Use choice to pick a random element from ["rock", "paper", "scissors"]
# Use shuffle to randomize the order of [1, 2, 3, 4, 5] and print it.

# YOUR CODE:


# ─── EXERCISE 3: random Module Deep Dive ──────────────────
# Write a function `roll_dice(num_dice, sides)` that simulates
# rolling `num_dice` dice, each with `sides` sides.
# Return a dict with: {"rolls": [list of each roll], "total": sum}
# Test: roll_dice(3, 6) might return {"rolls": [4, 2, 6], "total": 12}

# YOUR CODE:


# ─── EXERCISE 4: sys.argv ─────────────────────────────────
# Write a script that reads command line arguments.
# Usage: python this_file.py <name> <age>
# If wrong number of args → print "Usage: python script.py <name> <age>"
# If correct → print "Hello NAME, you are AGE years old."
# Hint: import sys, use sys.argv (it's a list)
# Test by running from terminal with arguments.

# YOUR CODE:


# ─── EXERCISE 5: Your Own Module ──────────────────────────
# Create a SEPARATE file called `mathtools.py` in the same folder.
# In it, write these functions:
#   - square(n) → returns n ** 2
#   - cube(n) → returns n ** 3
#   - is_even(n) → returns True/False
#   - factorial(n) → returns n! using a loop (no math.factorial)
#
# Then in THIS file, import mathtools and test all four functions.
# Note: you'll need to create the mathtools.py file yourself!

# YOUR CODE:


# ─── EXERCISE 6: pip and Third-Party Libraries ───────────
# Install the `cowsay` library: pip install cowsay
# Import it and make a cow say "I am learning Python!"
# Then make a DIFFERENT animal say something.
# (This is just to prove you can install and use third-party packages)

# YOUR CODE:


# ─── EXERCISE 7: json Module ──────────────────────────────
# Create a dictionary with your profile:
#   name, age, college, semester, skills (a list), projects (a list of dicts)
# Convert it to a JSON string with pretty formatting (indent=4).
# Print the JSON string.
# Then convert it BACK to a Python dict and access one nested value.

# YOUR CODE:


# ─── EXERCISE 8: Random Password Generator ───────────────
# Write a function `generate_password(length=12)` that creates
# a random password containing:
#   - At least 2 uppercase letters
#   - At least 2 lowercase letters
#   - At least 2 digits
#   - At least 2 special characters from: !@#$%^&*
# Fill the rest randomly from all character types.
# Shuffle the result so it's not predictable.
# Use the `random` and `string` modules.

# YOUR CODE:


# ─── EXERCISE 9: Statistics Module ────────────────────────
# Import the `statistics` module.
# Given this data:
grades = [78, 92, 85, 90, 88, 76, 95, 89, 91, 82]
# Calculate and print:
#   - Mean
#   - Median
#   - Mode (use [78, 92, 85, 90, 85, 76, 95, 85, 91, 82] for this one)
#   - Standard deviation
# Round each to 2 decimal places.

# YOUR CODE:


# ─── EXERCISE 10: API Preview (requests) ─────────────────
# This is a PREVIEW — install requests: pip install requests
# Fetch a random joke from: https://official-joke-api.appspot.com/random_joke
# Parse the JSON response and print:
#   "Setup: [setup]"
#   "Punchline: [punchline]"
# Wrap it in try/except for connection errors.
# (Don't worry if you don't fully understand requests yet — that's Phase 4)

# YOUR CODE:


# ─── EXERCISE 11: Combining Modules ──────────────────────
# Build a "lucky number" generator that:
# 1. Uses `random` to generate 6 unique numbers between 1-49
# 2. Uses `datetime` to get the current date and time
# 3. Sorts the numbers
# 4. Prints: "Your lucky numbers for [date] are: [numbers]"
# Hint: use random.sample() to get unique numbers

# YOUR CODE:


# ─── EXERCISE 12: The "Can You Build Something?" Test ────
# Build a Quiz Game using a list of dicts as your "database":
# questions = [
#     {"question": "What is Python named after?", "options": ["A snake", "Monty Python", "A Greek god"], "answer": 1},
#     {"question": "What does // do in Python?", "options": ["Division", "Floor division", "Exponent"], "answer": 1},
#     ...add at least 5 more questions
# ]
# Features:
#   - Randomize question order each time (use random.shuffle)
#   - Track score
#   - Show correct answer if they get it wrong
#   - At the end: show score, percentage, and a grade
# All question data should be stored as a list of dicts.

# YOUR CODE:


"""
============================================================
  SCOREBOARD
  Mark each exercise: ✅ (solved) or ❌ (couldn't solve)

  Ex 1:  |  Ex 2:  |  Ex 3:  |  Ex 4:  |  Ex 5:
  Ex 6:  |  Ex 7:  |  Ex 8:  |  Ex 9:  |  Ex 10:
  Ex 11: |  Ex 12:

  Total: __/12

  PASS THRESHOLD: 10/12 minimum. All ❌ must be retried.
============================================================
"""
