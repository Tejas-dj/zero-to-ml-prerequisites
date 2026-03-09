"""
============================================================
  CS50P LECTURE 3 — EXCEPTIONS
  Post-Lecture Coding Exercises
============================================================
  RULES:
  1. Do NOT look at the lecture while solving these.
  2. If you can't solve it in 10 minutes, mark it ❌ and move on.
  3. Come back to ❌ problems after 24 hours.
  4. You pass this lecture when ALL 12 are ✅.
============================================================
"""

# ─── EXERCISE 1: Basic try/except ──────────────────────────
# Ask the user for a number. If they enter something that's not
# a number, print "That's not a valid number" and ask again.
# Keep asking until they give a valid number.
# Then print: "You entered: X"

# YOUR CODE:


# ─── EXERCISE 2: Specific Exceptions ──────────────────────
# Write code that demonstrates catching DIFFERENT exceptions.
# Create THREE separate try/except blocks that catch:
#   1. ValueError (try converting "hello" to int)
#   2. ZeroDivisionError (try dividing by zero)
#   3. IndexError (try accessing index 10 of a 3-element list)
# For each, print the exception type and message.

# YOUR CODE:


# ─── EXERCISE 3: try/except/else ──────────────────────────
# Ask the user for two numbers and divide the first by the second.
# Use try/except/else:
#   - try: get the inputs and do the division
#   - except ValueError: "Please enter valid numbers"
#   - except ZeroDivisionError: "Cannot divide by zero"
#   - else (no error): print the result

# YOUR CODE:


# ─── EXERCISE 4: try/except/finally ───────────────────────
# Write a function that takes a filename and tries to read it.
# In the `finally` block, print "Attempted to read: [filename]"
# This should print regardless of whether the file exists or not.
# If the file doesn't exist → "File not found: [filename]"
# If it does exist → print its contents
# Test with a file that DOESN'T exist.

# YOUR CODE:


# ─── EXERCISE 5: Raising Exceptions ───────────────────────
# Write a function `set_age(age)` that:
#   - Raises ValueError("Age cannot be negative") if age < 0
#   - Raises ValueError("Age seems unrealistic") if age > 150
#   - Raises TypeError("Age must be a number") if age is not int or float
#   - Returns the age if valid
# Test it with: 25, -5, 200, "twenty"

# YOUR CODE:


# ─── EXERCISE 6: Input Validator Function ─────────────────
# Write a function `get_positive_int(prompt)` that:
#   - Shows the prompt and waits for input
#   - If the input is not a number → print error, ask again
#   - If the number is not positive → print error, ask again
#   - Returns the valid positive integer
# The user should NOT be able to break this function.

# YOUR CODE:


# ─── EXERCISE 7: Safe Division ────────────────────────────
# Write a function `safe_divide(a, b)` that:
#   - Returns the result of a / b
#   - Returns None if b is zero
#   - Returns None if either input isn't a number
# It should NEVER crash. Test with: (10,3), (10,0), ("a",3), (10,"b")

# YOUR CODE:


# ─── EXERCISE 8: Exception Prediction ────────────────────
# Without running the code, PREDICT which exception each raises.
# Write your prediction as a comment, then verify.
#
# int("3.14")                 → prediction: ???
# int(None)                   → prediction: ???
# "hello"[10]                 → prediction: ???
# {"a": 1}["b"]               → prediction: ???
# int("abc")                  → prediction: ???
# 1 + "2"                     → prediction: ???
# [1,2,3].remove(4)           → prediction: ???
# open("nonexistent_file.txt") → prediction: ???

# YOUR CODE (predictions first, then verify):


# ─── EXERCISE 9: Retry Logic ─────────────────────────────
# Write a function that asks for a valid email address.
# A "valid" email must contain exactly ONE "@" and at least one "." after the "@".
# If invalid, show what's wrong and let them retry (max 3 attempts).
# After 3 failed attempts → "Too many invalid attempts."
# If valid → return the email.

# YOUR CODE:


# ─── EXERCISE 10: Defensive Calculator ───────────────────
# Rebuild the calculator from Lecture 1 Exercise 13, but now
# make it COMPLETELY crash-proof:
#   - Handle non-numeric inputs
#   - Handle division by zero
#   - Handle invalid operators
#   - After any error, let the user try again instead of crashing
#   - Add "quit" option to exit

# YOUR CODE:


# ─── EXERCISE 11: Batch Number Processor ─────────────────
# Given this list:
raw_data = ["42", "hello", "3.14", "", "99", "world", "7", "0", "-5"]
#
# Process each item:
#   - Try to convert to a number (int first, then float if int fails)
#   - If successful, add to a "valid" list
#   - If not, add to an "invalid" list
# At the end, print:
#   Valid numbers: [42, 3.14, 99, 7, 0, -5]
#   Invalid items: ["hello", "", "world"]
#   Sum of valid: 146.14

# YOUR CODE:


# ─── EXERCISE 12: The "Can You Build Something?" Test ────
# Build a ROBUST student grade manager:
# 1. Ask "How many students?" — must be a positive integer (retry if invalid)
# 2. For each student, ask name and score (0-100) — validate BOTH
# 3. Store in a dictionary: {name: score}
# 4. Handle ALL possible errors: non-numeric scores, out-of-range scores,
#    empty names, duplicate names
# 5. After all students entered, print the class report:
#    - Each student with their grade letter (A/B/C/D/F)
#    - Class average
#    - Highest and lowest scorers
# The program should be IMPOSSIBLE to crash with bad input.

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
