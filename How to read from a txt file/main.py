print("Reading the whole file")
print("________________________________________________________________________")
file_path = "readme.txt"

with open(file_path, "r") as file:
    whole_content = file.read()

print(whole_content)


print("Reading line by line:")
print("________________________________________________________________________")

with open(file_path, "r") as file:
    lines = file.readlines()

third_line = lines[2].strip()  # Use strip() to remove newline characters from each line
# Index 2 corresponds to the 3rd line,txt files also count from index 0
print("Third line:", third_line)


print("Reading a part of a line:")
print("________________________________________________________________________")

with open(file_path, "r") as file:
    line = file.readline()

# Assume you want to read the first 22 characters of the line
part_of_line = line[:22]
print(part_of_line)

print("________________________________________________________________________")
print("Reading a part of line 3: ")
with open(file_path, "r") as file:
    lines = file.readlines()

third_line = lines[2].strip()
part_of_line = third_line[:22]
print(part_of_line)
