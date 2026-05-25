# Writing to a file (using 'with' to auto-close)
filename = "example.txt"
with open(filename, "w") as file:
    file.write("Hello, this is a test file.\n")
    file.write("Line 2: Python is awesome!\n")
print(f"✅ Written to {filename}")

# Reading from a file
print(f"\nReading from {filename}:")
with open(filename, "r") as file:
    content = file.read()
    print(content)
   # ✅ Written to example.txt

# Appending to a file
with open(filename, "a") as file:
    file.write("Line 3: Appended content.\n")
print("✅ Appended to file.")
"""Reading from example.txt:
Hello, this is a test file.
Line 2: Python is awesome!

✅ Appended to file"""

# Reading line by line
print("\nReading line by line:")
with open(filename, "r") as file:
    for line_num, line in enumerate(file, 1):
        print(f"Line {line_num}: {line.strip()}")
"""output:Reading line by line:
Line 1: Hello, this is a test file.
Line 2: Line 2: Python is awesome!
Line 3: Line 3: Appended content.
"""
