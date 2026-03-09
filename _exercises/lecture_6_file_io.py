"""
============================================================
  CS50P LECTURE 6 — FILE I/O
  Post-Lecture Coding Exercises
============================================================
  RULES:
  1. Do NOT look at the lecture while solving these.
  2. If you can't solve it in 10 minutes, mark it ❌ and move on.
  3. Come back to ❌ problems after 24 hours.
  4. You pass this lecture when ALL 13 are ✅.
============================================================
"""

# ─── EXERCISE 1: Write to a File ──────────────────────────
# Write a program that asks the user for 3 favorite movies.
# Save them to a file called "movies.txt", one per line.
# Then read the file and print what's in it.

# YOUR CODE:


# ─── EXERCISE 2: Append Mode ──────────────────────────────
# Write a program that asks for a new movie and APPENDS it
# to the "movies.txt" file (don't overwrite existing content).
# Then read and print the full file.

# YOUR CODE:


# ─── EXERCISE 3: with Statement ───────────────────────────
# Rewrite Exercise 1 and 2 using the `with` statement.
# Explain in a comment: why is `with` better than manually
# calling .close()?

# YOUR CODE:


# ─── EXERCISE 4: Reading Line by Line ─────────────────────
# Create a file called "numbers.txt" with these numbers (one per line):
# 42, 17, 93, 8, 56, 71, 34, 29, 88, 5
# Read the file and:
#   1. Print each number
#   2. Calculate the sum
#   3. Find the max and min
#   4. Calculate the average
# Handle the case where the file might not exist.

# YOUR CODE:


# ─── EXERCISE 5: CSV Writing ──────────────────────────────
# Create a CSV file called "students.csv" with these columns:
#   name, age, grade, city
# Add at least 5 rows of data (make it up).
# Use the `csv` module's writer.

# YOUR CODE:


# ─── EXERCISE 6: CSV Reading ──────────────────────────────
# Read the "students.csv" file you created above.
# Using csv.DictReader, print each student's info as:
# "Name (age X) from City — Grade: G"
# Then calculate and print the average age.

# YOUR CODE:


# ─── EXERCISE 7: JSON Write ──────────────────────────────
# Create a dictionary representing a playlist:
# {
#   "name": "Coding Vibes",
#   "created": "2026-03-10",
#   "songs": [
#     {"title": "...", "artist": "...", "duration_sec": 240},
#     ...at least 5 songs
#   ]
# }
# Save it to "playlist.json" with pretty formatting (indent=2).

# YOUR CODE:


# ─── EXERCISE 8: JSON Read & Process ─────────────────────
# Read "playlist.json" and print:
#   1. Playlist name
#   2. Number of songs
#   3. Each song as: "Artist — Title (M:SS)"
#      Convert duration_sec to minutes:seconds format
#   4. Total playlist duration in MM:SS format

# YOUR CODE:


# ─── EXERCISE 9: File Search ─────────────────────────────
# Write a function `search_file(filename, keyword)` that:
#   - Opens the file
#   - Searches every line for the keyword (case-insensitive)
#   - Returns a list of tuples: [(line_number, line_text), ...]
#   - If no matches, return an empty list
# Test it on any text file you have.

# YOUR CODE:


# ─── EXERCISE 10: Contact Book with File Persistence ─────
# Upgrade the contact book from Lecture 0's exercises:
# Features:
#   - Add, search, delete contacts (same as before)
#   - NEW: Save all contacts to "contacts.json" on every change
#   - NEW: Load contacts from "contacts.json" on startup
#   - Contacts persist between program runs!
# Handle: file not found (first run), corrupted JSON.

# YOUR CODE:


# ─── EXERCISE 11: Log File Analyzer ──────────────────────
# First, create a fake log file "app.log" with entries like:
#   2026-03-10 08:15:23 INFO  User logged in
#   2026-03-10 08:16:45 ERROR Database connection failed
#   2026-03-10 08:17:02 INFO  Data loaded successfully
#   2026-03-10 08:18:11 WARNING Memory usage high
#   (add at least 15 entries mix of INFO, ERROR, WARNING)
#
# Then write a program that reads it and reports:
#   - Total lines
#   - Count of each level (INFO: X, ERROR: X, WARNING: X)
#   - All ERROR lines printed separately

# YOUR CODE:


# ─── EXERCISE 12: File Splitter ──────────────────────────
# Write a function that takes a large text file and splits it
# into multiple smaller files of N lines each.
# split_file("big_file.txt", lines_per_file=10)
# This should create: big_file_001.txt, big_file_002.txt, etc.
# Test by first creating a file with 35 lines, then splitting by 10.

# YOUR CODE:


# ─── EXERCISE 13: The "Can You Build Something?" Test ────
# Build a Personal Diary / Journal App:
# Features:
#   1. "Write entry" — asks for text, saves with timestamp to diary.json
#   2. "Read all entries" — displays all entries with dates
#   3. "Search entries" — search by keyword across all entries
#   4. "Delete entry" — delete by date/index
#   5. "Export to text" — save all entries as a formatted .txt file
# Data stored as JSON: a list of {"date": "...", "text": "..."} objects.
# The diary should persist between program runs.

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
