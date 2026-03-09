"""
============================================================
  CS50P LECTURE 2 — LOOPS
  Post-Lecture Coding Exercises
============================================================
  RULES:
  1. Do NOT look at the lecture while solving these.
  2. If you can't solve it in 10 minutes, mark it ❌ and move on.
  3. Come back to ❌ problems after 24 hours.
  4. You pass this lecture when ALL 15 are ✅.
============================================================
"""

# ─── EXERCISE 1: Basic for Loop ────────────────────────────
# Print the numbers 1 through 20, each on a new line.
# Then print them all on ONE line separated by spaces.
# Hint: print() has an `end` parameter.

# YOUR CODE:


# ─── EXERCISE 2: Range Mastery ─────────────────────────────
# Using ONLY range(), print:
# 1. Even numbers from 2 to 20
# 2. Odd numbers from 1 to 19
# 3. Countdown from 10 to 1
# 4. Multiples of 5 from 0 to 50

# YOUR CODE:


# ─── EXERCISE 3: while Loop ───────────────────────────────
# Keep asking the user for input until they type "quit".
# Count how many things they entered (not counting "quit").
# At the end, print: "You entered X items before quitting."

# YOUR CODE:


# ─── EXERCISE 4: Accumulator Pattern ──────────────────────
# Write a function `sum_range(start, end)` that RETURNS the sum
# of all integers from start to end (inclusive).
# Do NOT use the built-in sum() function. Use a loop.
# Test: sum_range(1, 10) → 55, sum_range(5, 5) → 5

# YOUR CODE:


# ─── EXERCISE 5: String Iteration ─────────────────────────
# Given a string, count how many vowels (a, e, i, o, u) it contains.
# Make it case-insensitive.
# Write it as a function: count_vowels(text) → returns int
# Test: count_vowels("Hello World") → 3

# YOUR CODE:


# ─── EXERCISE 6: Multiplication Table ─────────────────────
# Ask the user for a number N.
# Print its multiplication table from 1 to 10.
# Format: "N x 1 = N"
#         "N x 2 = 2N"  etc.

# YOUR CODE:


# ─── EXERCISE 7: break and continue ───────────────────────
# Loop through numbers 1 to 50.
# SKIP (continue) any number divisible by 3.
# STOP (break) if you encounter a number divisible by 37.
# Print every number that doesn't get skipped or stopped.

# YOUR CODE:


# ─── EXERCISE 8: Nested Loops ─────────────────────────────
# Print this pattern (for n = 5):
# *
# **
# ***
# ****
# *****
# Ask the user for n, then print the triangle.

# YOUR CODE:


# ─── EXERCISE 9: List Building with Loops ─────────────────
# Write a function that takes a list of numbers and RETURNS
# a NEW list containing only the even numbers.
# Do NOT use list comprehension — use a for loop and .append()
# Test: filter_evens([1, 2, 3, 4, 5, 6, 7, 8]) → [2, 4, 6, 8]

# YOUR CODE:


# ─── EXERCISE 10: Dictionary Iteration ────────────────────
# Given this dict:
scores = {"Tejas": 92, "Aria": 88, "Kira": 95, "Nova": 78, "Zain": 85}
# 1. Print each name and score: "Tejas: 92"
# 2. Find and print the name of the person with the HIGHEST score
# 3. Calculate and print the class average
# Do all of this with loops (no max() or sum() built-ins).

# YOUR CODE:


# ─── EXERCISE 11: Number Guessing Game (v2) ───────────────
# Upgrade the number guesser:
# 1. Generate random number 1-100 (import random, random.randint(1,100))
# 2. Player gets max 7 attempts
# 3. After each wrong guess, tell them "Too high" or "Too low"
# 4. Also tell them how many attempts they have LEFT
# 5. If they guess right → "🎉 Got it in X attempts!"
# 6. If they run out → "💀 Game over. The number was Y."

# YOUR CODE:


# ─── EXERCISE 12: Fibonacci Generator ────────────────────
# Write a function fibonacci(n) that RETURNS a list of the
# first n Fibonacci numbers.
# Fibonacci: 0, 1, 1, 2, 3, 5, 8, 13, 21, ...
# (each number = sum of the two before it)
# Test: fibonacci(8) → [0, 1, 1, 2, 3, 5, 8, 13]

# YOUR CODE:


# ─── EXERCISE 13: Prime Number Checker ────────────────────
# Write a function is_prime(n) that RETURNS True if n is prime.
# A prime number is only divisible by 1 and itself.
# Then print all prime numbers between 2 and 50.
# Hint: if ANY number from 2 to n-1 divides n evenly, it's not prime.

# YOUR CODE:


# ─── EXERCISE 14: Reverse a String (with a loop) ─────────
# Write a function reverse_string(s) that RETURNS the reversed string.
# Do NOT use slicing ([::-1]) or reversed(). Use a loop.
# Test: reverse_string("Python") → "nohtyP"

# YOUR CODE:


# ─── EXERCISE 15: The "Can You Build Something?" Test ────
# Build a number analysis tool:
# Ask the user to keep entering numbers (type "done" to stop).
# After they're done, print:
#   - Count of numbers entered
#   - Sum of all numbers
#   - Average
#   - Highest number
#   - Lowest number
#   - Count of even vs odd numbers
# Do NOT use built-in sum(), max(), min() — calculate everything with loops.

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
