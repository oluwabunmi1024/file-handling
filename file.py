# file_read_write.py

# Open the input file and output file
with open("input.txt", "r") as infile:
    content = infile.read()

# Modify the content (example: convert to uppercase)
modified_content = content.upper()

# Write the modified content to a new file
with open("output.txt", "w") as outfile:
    outfile.write(modified_content)

print("✅ File has been read, modified, and written to output.txt")


# error_handling_lab.py

filename = input("Enter the filename to read: ")

try:
    with open(filename, "r") as f:
        content = f.read()
        print("\nFile content:\n")
        print(content)

except FileNotFoundError:
    print(f"❌ Error: The file '{filename}' does not exist.")
except PermissionError:
    print(f"❌ Error: You don't have permission to read '{filename}'.")
except Exception as e:
    print(f"❌ An unexpected error occurred: {e}")
