"""
============================================================
  CS50P LECTURE 7 — REGULAR EXPRESSIONS
  Post-Lecture Coding Exercises
============================================================
  RULES:
  1. Do NOT look at the lecture while solving these.
  2. If you can't solve it in 10 minutes, mark it ❌ and move on.
  3. Come back to ❌ problems after 24 hours.
  4. You pass this lecture when ALL 12 are ✅.
============================================================
"""
import re  # You'll need this for all exercises

# ─── EXERCISE 1: re.search Basics ─────────────────────────
# Write a function `has_digit(text)` that returns True if the
# text contains at least one digit (0-9).
# Use re.search(), not a loop.
# Test: "hello" → False, "hello123" → True, "42" → True, "" → False

# YOUR CODE:


# ─── EXERCISE 2: re.findall ───────────────────────────────
# Given this text:
text = "Call me at 555-1234 or 555-5678. My office is 555-9012."
# Use re.findall() to extract ALL phone numbers.
# Expected: ["555-1234", "555-5678", "555-9012"]

# YOUR CODE:


# ─── EXERCISE 3: Email Validator ──────────────────────────
# Write a function `is_valid_email(email)` that uses regex to check
# if an email is valid. A valid email has:
#   - One or more word characters or dots or hyphens before @
#   - A domain name after @ (word chars and dots)
#   - A TLD (.com, .edu, .org, etc.) that's 2-4 chars
# Pattern: something@something.xx
# Test with: "tejas@gmail.com" ✅, "bad@" ❌, "@missing.com" ❌, "good@bmsce.ac.in" ✅

# YOUR CODE:


# ─── EXERCISE 4: re.sub (Find and Replace) ───────────────
# Given:
messy = "The    spacing   in   this    sentence    is     terrible."
# Use re.sub() to replace all multiple spaces with a single space.
# Expected: "The spacing in this sentence is terrible."

# YOUR CODE:


# ─── EXERCISE 5: Capture Groups ──────────────────────────
# Given this list of full names:
names = ["Tejas Jaiprakash", "Aria Smith", "Kira O'Brien", "Nova Lee"]
# Use regex with capture groups to swap them to "Last, First" format.
# Expected: ["Jaiprakash, Tejas", "Smith, Aria", "O'Brien, Kira", "Lee, Nova"]
# Hint: use re.sub() with groups \1 and \2

# YOUR CODE:


# ─── EXERCISE 6: Date Parser ─────────────────────────────
# Write a function that extracts dates from text.
# It should handle these formats:
#   "03/10/2026"  (MM/DD/YYYY)
#   "2026-03-10"  (YYYY-MM-DD)
#   "March 10, 2026" (Month DD, YYYY)
# Given: "Meeting on 03/10/2026 and deadline is 2026-03-15 and
#         party on March 20, 2026"
# Return a list of all dates found.

# YOUR CODE:


# ─── EXERCISE 7: Password Validator (Regex Version) ──────
# Rewrite the password checker from Lecture 1 using ONLY regex.
# A strong password must match ALL of these patterns:
#   - At least 8 characters: .{8,}
#   - At least one digit: \d
#   - At least one uppercase: [A-Z]
#   - At least one lowercase: [a-z]
#   - At least one special character: [!@#$%^&*]
# Write it as one function using multiple re.search() calls.

# YOUR CODE:


# ─── EXERCISE 8: URL Parser ──────────────────────────────
# Write a function that extracts parts of a URL using regex:
# Given: "https://www.example.com:8080/path/to/page?query=python&lang=en"
# Extract:
#   protocol: "https"
#   domain: "www.example.com"
#   port: "8080" (or None if not present)
#   path: "/path/to/page"
#   query: "query=python&lang=en" (or None)
# Test with URLs that have and don't have ports and queries.

# YOUR CODE:


# ─── EXERCISE 9: Text Censor ─────────────────────────────
# Write a function `censor(text, bad_words)` that replaces
# any occurrence of a bad word with asterisks of the same length.
# It should be case-insensitive but preserve the original case in non-censored parts.
# Use regex with re.sub() and a function as the replacement.
# Example: censor("This is Damn good", ["damn"]) → "This is **** good"

# YOUR CODE:


# ─── EXERCISE 10: Log Parser ─────────────────────────────
# Given this log data (as a multi-line string):
log_data = """
2026-03-10 08:15:23 [INFO] User admin logged in from 192.168.1.100
2026-03-10 08:16:45 [ERROR] Failed to connect to DB at 10.0.0.5:3306
2026-03-10 08:17:02 [INFO] Query completed in 0.045s
2026-03-10 08:18:11 [WARNING] High memory usage: 89%
2026-03-10 09:01:33 [ERROR] Timeout connecting to API at 203.0.113.42:443
2026-03-10 09:02:15 [INFO] User tejas logged in from 192.168.1.105
"""
# Using regex, extract:
#   1. All timestamps
#   2. All log levels (INFO, ERROR, WARNING)
#   3. All IP addresses (with or without ports)
#   4. All usernames that logged in

# YOUR CODE:


# ─── EXERCISE 11: Markdown Link Extractor ────────────────
# Write a function that extracts all markdown links from text.
# Markdown links look like: [link text](url)
# Given: "Check out [Google](https://google.com) and [GitHub](https://github.com)"
# Return: [("Google", "https://google.com"), ("GitHub", "https://github.com")]

# YOUR CODE:


# ─── EXERCISE 12: The "Can You Build Something?" Test ────
# Build a Text Statistics Analyzer:
# Ask the user for a multi-line text input (or read from a file).
# Using regex, analyze and report:
#   1. Word count
#   2. Sentence count (ends with . ! ?)
#   3. Average words per sentence
#   4. Most common words (top 5) — exclude words < 3 chars
#   5. All email addresses found
#   6. All URLs found
#   7. All phone numbers found (XXX-XXX-XXXX or (XXX) XXX-XXXX)
#   8. All hashtags found (#something)
# Print a formatted report.

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
