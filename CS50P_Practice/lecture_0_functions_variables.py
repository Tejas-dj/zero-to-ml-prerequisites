"""
============================================================
  CS50P LECTURE 0 — FUNCTIONS, VARIABLES
  Post-Lecture Coding Exercises
============================================================
  RULES:
  1. Do NOT look at the lecture while solving these.
  2. If you can't solve it in 10 minutes, mark it ❌ and move on.
  3. Come back to ❌ problems after 24 hours.
  4. You pass this lecture when ALL 15 are ✅.
============================================================
"""

# ─── EXERCISE 1: Basic I/O ─────────────────────────────────
# Ask the user for their full name.
# Print: "Hello, [NAME]!" where NAME is their input.
# Expected: input "tejas" → output "Hello, Tejas!" (capitalized)

# YOUR CODE:
def ex1():
  name = input(" Type in your name full name:").title().strip()
  print(f"Hello, {name}, this is the first lesson of CS50P")


# ─── EXERCISE 2: String Concatenation ──────────────────────
# Ask for first name and last name separately.
# Print them together as "Last, First" format.
# Expected: first="Tejas", last="Jaiprakash" → "Jaiprakash, Tejas"

# YOUR CODE:
def ex2():
  f1_name = input("Type in your first name:").strip().title()
  f2_name = input("Type in your last name:").strip().title()
  print(f"hello,{f1_name} {f2_name}, this the question 2")


# ─── EXERCISE 3: Type Conversion ───────────────────────────
# Ask the user for their birth year (as input — it comes as a string!)
# Calculate their age in 2026 and print:
# "You are X years old"
# Hint: you'll need to convert the input to a number.

# YOUR CODE:
def ex3():
  x = int(input("Tell us your birth year please: "))
  print(f"So you are {2026-x} years old right?")



# ─── EXERCISE 4: Arithmetic Operators ──────────────────────
# Ask for two numbers from the user.
# Print the result of ALL of these operations:
#   addition, subtraction, multiplication, division,
#   floor division, modulo, and exponentiation
# Format each on its own line like: "5 + 3 = 8"

# YOUR CODE:
def ex4():
  x=int(input("enter one number"))
  y=int(input("enter one number"))
  print(f"Addition of the nos={x+y}")
  print(f"Subtraction of the nos={x-y}")
  print(f"Multiplicaton of the nos={x*y}")
  print(f"Division of the nos={x/y,}")
  print(f"{x} to the power of {y}= {x**y}")




# ─── EXERCISE 5: f-strings ─────────────────────────────────
# Create variables: item = "coffee", price = 4.5678, quantity = 3
# Using a SINGLE f-string, print:
# "3x coffee = $13.70"
# The total must be calculated INSIDE the f-string.
# The price must show exactly 2 decimal places.

# YOUR CODE:
def ex5():
  item = "coffee"
  price = 20.50980
  nos = 33
  print(f"---------Bill amount---------")
  print(f"{item}_____{price} x {nos}   ={price*nos:.2f}")



# ─── EXERCISE 6: String Methods ────────────────────────────
# Given this string (copy it exactly):
# messy = "   hElLo, WoRLd!   "
# Print each of these on a separate line:
# 1. The string with whitespace removed from both ends
# 2. The string in all lowercase
# 3. The string in all uppercase
# 4. The string in title case
# 5. The string with "World" replaced by "Python"

# YOUR CODE:
def ex6():
  messy = "   hElLo, WoRLd!   "
  print(messy.strip())
  print(messy.lower())
  print(messy.upper())
  print(messy.title())
  print(messy.replace("WoRLd", "Pyhton sssssss...."))




# ─── EXERCISE 7: String Slicing ────────────────────────────
# Given:
# word = "PYTHON"
# Using ONLY slicing (no loops, no reversed()), print:
# 1. First 3 characters → "PYT"
# 2. Last 3 characters → "HON"
# 3. Every other character → "PTO"
# 4. The word reversed → "NOHTYP"
# 5. Characters from index 2 to 4 → "THO"

# YOUR CODE:
def ex7():
  word = "Python"
  print(word[:3])
  print(word[3:])
  print(word[::2])
  print(word[5::-1])
  print(word[2:5])



# ─── EXERCISE 8: Multiple Assignment ───────────────────────
# In ONE line of code, create three variables:
#   x = 10, y = 20, z = 30
# Then SWAP x and z (also in one line, no temp variable).
# Print all three to prove it worked.

# YOUR CODE:


# ─── EXERCISE 9: Return vs Print ───────────────────────────
# This is the MOST important exercise in this set.
#
# Write TWO functions that both calculate the square of a number:
#   square_print(n)  → PRINTS the result (returns nothing)
#   square_return(n) → RETURNS the result (prints nothing)
#
# Then show WHY this matters:
#   Try to do: result = square_print(5) * 2  → What happens?
#   Then do:   result = square_return(5) * 2 → What happens?
# Print both results and add a comment explaining the difference.

# YOUR CODE:


# ─── EXERCISE 10: Function Parameters ──────────────────────
# Write a function called `greet` that takes two parameters:
#   name (required) and greeting (optional, default = "Hello")
# It should RETURN the string: "[greeting], [name]!"
# Test it:
#   greet("Tejas")           → "Hello, Tejas!"
#   greet("Tejas", "Yo")     → "Yo, Tejas!"
#   greet("Tejas", "Namaste") → "Namaste, Tejas!"

# YOUR CODE:


# ─── EXERCISE 11: Int vs Float Awareness ───────────────────
# Without running the code first, PREDICT what each prints.
# Write your prediction as a comment, THEN uncomment and verify.
# 
# print(type(10))           → prediction: ???
# print(type(10.0))         → prediction: ???
# print(type(10 / 2))       → prediction: ???
# print(type(10 // 2))      → prediction: ???
# print(type("10"))         → prediction: ???
# print(10 == 10.0)         → prediction: ???
# print("10" == 10)         → prediction: ???

# YOUR CODE (predictions first, then verify):


# ─── EXERCISE 12: Input Validation (mini) ──────────────────
# Ask the user for a number.
# If they enter something that ISN'T a number, print "That's not a number!"
# If it IS a number, print "Your number doubled is: X"
# Hint: look up str.isnumeric() or try/except (but you might not know
#       try/except yet — that's fine, use .isnumeric() for now)

# YOUR CODE:


# ─── EXERCISE 13: Multi-line f-string ──────────────────────
# Create a "receipt" using variables and a multi-line f-string.
# Variables: customer_name, item1, price1, item2, price2, tax_rate = 0.08
# The receipt should look like:
# ┌──────────────────────────┐
# │    RECEIPT               │
# │    Customer: Tejas       │
# │    Coffee      $4.50     │
# │    Muffin      $3.25     │
# │    Subtotal:   $7.75     │
# │    Tax (8%):   $0.62     │
# │    Total:      $8.37     │
# └──────────────────────────┘
# (alignment doesn't need to be perfect — focus on the math being right)

# YOUR CODE:


# ─── EXERCISE 14: Nested Function Calls ────────────────────
# Write three functions:
#   celsius_to_fahrenheit(c) → returns (c * 9/5) + 32
#   fahrenheit_to_celsius(f) → returns (f - 32) * 5/9
#   format_temp(value, unit) → returns "XX.X°C" or "XX.X°F"
#
# Then use them TOGETHER in one line:
#   Convert 100°C to Fahrenheit and print it formatted.
#   Convert 72°F to Celsius and print it formatted.

# YOUR CODE:


# ─── EXERCISE 15: The "Can You Build Something?" Test ──────
# Build a SIMPLE tip calculator:
# 1. Ask for the bill amount
# 2. Ask for tip percentage (e.g., 15, 18, 20)
# 3. Ask how many people are splitting the bill
# 4. Calculate and print:
#    - Tip amount
#    - Total bill (with tip)
#    - Amount per person
# All money values should show exactly 2 decimal places.
# Use at least ONE function.

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