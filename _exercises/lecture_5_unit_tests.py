"""
============================================================
  CS50P LECTURE 5 — UNIT TESTS
  Post-Lecture Coding Exercises
============================================================
  RULES:
  1. Do NOT look at the lecture while solving these.
  2. If you can't solve it in 10 minutes, mark it ❌ and move on.
  3. Come back to ❌ problems after 24 hours.
  4. You pass this lecture when ALL 10 are ✅.
============================================================
"""

# ─── EXERCISE 1: Your First assert ────────────────────────
# Write a function `add(a, b)` that returns a + b.
# Below it, write 3 assert statements to test it:
#   assert add(2, 3) == 5
#   assert add(-1, 1) == 0
#   assert add(0, 0) == 0
# If none crash, print "All tests passed!"

# YOUR CODE:


# ─── EXERCISE 2: Write Then Test ──────────────────────────
# Write a function `is_palindrome(word)` that returns True if
# the word reads the same forwards and backwards (case-insensitive).
# Examples: "racecar" → True, "hello" → False, "Madam" → True
# Write at least 5 assert statements to test it.

# YOUR CODE:


# ─── EXERCISE 3: Testing Edge Cases ──────────────────────
# Write a function `divide(a, b)` that returns a / b.
# It should raise ValueError if b is zero.
# Write tests for:
#   - Normal division: divide(10, 2) == 5.0
#   - Decimal result: divide(7, 2) == 3.5
#   - Negative numbers: divide(-6, 3) == -2.0
#   - Zero numerator: divide(0, 5) == 0.0
#   - Zero denominator: should raise ValueError (use try/except to test)

# YOUR CODE:


# ─── EXERCISE 4: Create a Test File ──────────────────────
# Part A: Create a file called `string_utils.py` with these functions:
#   capitalize_words(s) → capitalizes first letter of each word
#     "hello world" → "Hello World"
#   count_words(s) → returns number of words
#     "hello world" → 2
#   reverse_words(s) → reverses word order
#     "hello world" → "world hello"
#
# Part B: Create ANOTHER file called `test_string_utils.py` with
# at least 3 test functions:
#   test_capitalize_words()
#   test_count_words()
#   test_reverse_words()
# Each test function should have at least 3 assert statements.
# Run: pytest test_string_utils.py

# Write both files. Test part goes here as comments/pseudocode:


# ─── EXERCISE 5: Testing with pytest ─────────────────────
# Install pytest if not installed: pip install pytest
# Write a function `fizzbuzz(n)` (from Lecture 1).
# Create a file `test_fizzbuzz.py` with these test functions:
#   test_fizz()       → tests numbers divisible by 3 only
#   test_buzz()       → tests numbers divisible by 5 only
#   test_fizzbuzz()   → tests numbers divisible by both
#   test_neither()    → tests numbers divisible by neither
# Run: pytest test_fizzbuzz.py -v

# YOUR CODE:


# ─── EXERCISE 6: Finding Bugs with Tests ─────────────────
# This function has a BUG. Write tests to find it, then fix it.
def get_grade(score):
    if score >= 90:
        return "A"
    elif score >= 80:
        return "B"
    elif score >= 70:
        return "C"
    elif score > 60:    # <-- there might be a bug here
        return "D"
    else:
        return "F"

# Write tests for: 95, 85, 75, 65, 60, 55, 100, 0
# Which test case reveals the bug? Fix the function.

# YOUR CODE:


# ─── EXERCISE 7: Test a Calculator ───────────────────────
# Write a module `calc.py` with: add, subtract, multiply, divide
# Write `test_calc.py` with at least 12 test cases covering:
#   - Normal operations
#   - Negative numbers
#   - Zero
#   - Floating point
#   - Division by zero (should raise an error)
# Run pytest and make sure all pass.

# YOUR CODE (describe what goes in each file):


# ─── EXERCISE 8: Boolean Testing ─────────────────────────
# Write these functions and test each with at least 4 asserts:
#   is_adult(age)      → True if age >= 18
#   is_valid_email(s)  → True if contains @ and . after @
#   is_strong_password(s) → True if len >= 8 and has digit and has upper

# YOUR CODE:


# ─── EXERCISE 9: Test-Driven Development ─────────────────
# WRITE THE TESTS FIRST (before the function!):
# Create a function `title_case(s)` that converts a string to title case
# BUT with these special rules:
#   - Words like "a", "an", "the", "in", "on", "at" stay lowercase
#   - UNLESS they're the first word
# Example: "the lord of the rings" → "The Lord of the Rings"
#
# Step 1: Write 5+ test cases
# Step 2: THEN write the function to make them pass

# YOUR CODE:


# ─── EXERCISE 10: The "Can You Build Something?" Test ────
# Go back to your Cipher Engine milestone project (or plan for it).
# Write a test file `test_cipher.py` that tests:
#   - Caesar encrypt: known input → known output
#   - Caesar decrypt: reverse of encrypt
#   - Roundtrip: encrypt then decrypt should give original message
#   - Brute force: should find the correct shift
#   - Edge cases: empty string, special characters, numbers in text
# At least 10 test cases total.
# If you haven't built Cipher Engine yet, write the tests first
# (TDD style — the tests define what the functions should do).

# YOUR CODE:


"""
============================================================
  SCOREBOARD
  Mark each exercise: ✅ (solved) or ❌ (couldn't solve)

  Ex 1:  |  Ex 2:  |  Ex 3:  |  Ex 4:  |  Ex 5:
  Ex 6:  |  Ex 7:  |  Ex 8:  |  Ex 9:  |  Ex 10:

  Total: __/10

  PASS THRESHOLD: 8/10 minimum. All ❌ must be retried.
============================================================
"""
