print("\n--- 2. Error Handling ---")

def safe_divide(a, b):
    try:
        result = a / b
        return result
    except ZeroDivisionError:
        return "❌ Error: Cannot divide by zero!"
    except TypeError:
        return "❌ Error: Invalid input type!"
    except Exception as e:
        return f"❌ Unexpected error: {e}"

print(f"10 / 2 = {safe_divide(10, 2)}")
print(f"10 / 0 = {safe_divide(10, 0)}")
print(f"'10' / 2 = {safe_divide('10', 2)}")

# Handling file not found
try:
    with open("nonexistent.txt", "r") as f:
        data = f.read()
except FileNotFoundError:
    print("❌ File not found! Creating a new one...")
    with open("nonexistent.txt", "w") as f:
        f.write("New file created.")
except Exception as e:
    print(f"❌ Error: {e}")
