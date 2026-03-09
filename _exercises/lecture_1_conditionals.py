"""
============================================================
  CS50P LECTURE 1 — CONDITIONALS
  Post-Lecture Coding Exercises
============================================================
  RULES:
  1. Do NOT look at the lecture while solving these.
  2. If you can't solve it in 10 minutes, mark it ❌ and move on.
  3. Come back to ❌ problems after 24 hours.
  4. You pass this lecture when ALL 13 are ✅.
============================================================
"""

# ─── EXERCISE 1: Basic if/else ─────────────────────────────
# Ask the user for a number.
# If it's positive, print "Positive"
# If it's negative, print "Negative"
# If it's zero, print "Zero"

# YOUR CODE:


# ─── EXERCISE 2: elif Chain ────────────────────────────────
# Ask the user for their exam score (0-100).
# Print the grade:
#   90-100 → "A"
#   80-89  → "B"
#   70-79  → "C"
#   60-69  → "D"
#   Below 60 → "F"
# Also handle invalid input: if score > 100 or < 0, print "Invalid score"

# YOUR CODE:


# ─── EXERCISE 3: Logical Operators ─────────────────────────
# Ask for the user's age.
# Ask if they have a license (yes/no).
# They can drive ONLY if age >= 18 AND they have a license.
# Print "You can drive" or "You cannot drive"

# YOUR CODE:


# ─── EXERCISE 4: Nested Conditionals ──────────────────────
# Build a basic login system:
# 1. Ask for username
# 2. Ask for password
# 3. The correct credentials are: username="admin", password="1234"
# 4. If username is wrong → "User not found"
# 5. If username is right but password wrong → "Wrong password"
# 6. If both correct → "Welcome, admin!"

# YOUR CODE:


# ─── EXERCISE 5: or Operator ──────────────────────────────
# Ask the user what day it is (e.g., "Monday").
# If it's Saturday OR Sunday, print "Weekend! 🎉"
# Otherwise print "Weekday. Grind time. 💪"
# Make it case-INSENSITIVE (so "saturday", "SATURDAY", "Saturday" all work)

# YOUR CODE:


# ─── EXERCISE 6: Truthiness ───────────────────────────────
# Without running the code, PREDICT what each prints (True or False).
# Write your prediction as a comment, then verify.
#
# print(bool(0))          → prediction: ???
# print(bool(1))          → prediction: ???
# print(bool(""))         → prediction: ???
# print(bool("hello"))    → prediction: ???
# print(bool([]))         → prediction: ???
# print(bool([1, 2, 3]))  → prediction: ???
# print(bool(None))       → prediction: ???
# print(bool(" "))        → prediction: ???  (tricky!)

# YOUR CODE (predictions first, then verify):


# ─── EXERCISE 7: FizzBuzz (The Classic) ───────────────────
# Write a function fizzbuzz(n) that takes a number and RETURNS:
#   "FizzBuzz" if divisible by BOTH 3 and 5
#   "Fizz"     if divisible by 3 only
#   "Buzz"     if divisible by 5 only
#   The number itself (as a string) if neither
# Test with: 1, 3, 5, 15, 7, 30

# YOUR CODE:


# ─── EXERCISE 8: BMI Calculator ───────────────────────────
# Ask for weight (in kg) and height (in meters).
# Calculate BMI = weight / (height ** 2)
# Print the category:
#   BMI < 18.5     → "Underweight"
#   18.5 ≤ BMI < 25 → "Normal weight"
#   25 ≤ BMI < 30   → "Overweight"
#   BMI ≥ 30        → "Obese"
# Print: "Your BMI is X.X — Category"

# YOUR CODE:


# ─── EXERCISE 9: Rock Paper Scissors ──────────────────────
# Player enters "rock", "paper", or "scissors"
# Computer always picks "rock" (for now — no random yet)
# Determine and print: "You win!", "You lose!", or "It's a tie!"
# Handle invalid input: if player enters something else → "Invalid choice"
# Make it case-insensitive.

# YOUR CODE:


# ─── EXERCISE 10: Leap Year Checker ──────────────────────
# Write a function is_leap_year(year) that RETURNS True or False.
# Rules (this is the REAL algorithm):
#   1. If divisible by 4 → leap year
#   2. BUT if divisible by 100 → NOT a leap year
#   3. BUT if divisible by 400 → IS a leap year
# Test: 2000 → True, 1900 → False, 2024 → True, 2023 → False

# YOUR CODE:


# ─── EXERCISE 11: Ticket Pricing ─────────────────────────
# A movie theater charges:
#   Kids (under 12):     $5
#   Teens (12-17):       $8
#   Adults (18-64):      $12
#   Seniors (65+):       $6
#   Tuesday discount:    50% off for everyone
#
# Ask for age and day of the week.
# Calculate and print the ticket price.
# Use a function that RETURNS the price.

# YOUR CODE:


# ─── EXERCISE 12: Password Strength Checker ──────────────
# Ask for a password. Check and print its strength:
# Rules (check ALL):
#   - At least 8 characters long
#   - Contains at least one digit (0-9)
#   - Contains at least one uppercase letter
#
# If ALL three → "Strong password ✅"
# If TWO of three → "Medium password ⚠️"
# If ONE or NONE → "Weak password ❌"
#
# Hint: you can loop through characters of a string with: for char in password
# Use .isdigit() and .isupper() methods.

# YOUR CODE:


# ─── EXERCISE 13: The "Can You Build Something?" Test ────
# Build a SIMPLE calculator:
# 1. Ask for first number
# 2. Ask for operator (+, -, *, /)
# 3. Ask for second number
# 4. Calculate and print the result
# 5. Handle division by zero: "Error: Cannot divide by zero"
# 6. Handle invalid operator: "Invalid operator"
# Use a function called `calculate(a, op, b)` that RETURNS the result.

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
