import re

filename = "show_version.txt"
with open (filename, "r") as f:
    show_version = f.read()

serial_pattern = r"^cisco\s(?P<serial_number>\S*\s\S*)"

model_pattern = r"^Processor\s.* ID\s(?P<model_number>\S*)$"

match = re.search(serial_pattern,show_version, re.M)
if match:
    serial = match.group("serial_number") 
match = re.search(model_pattern,show_version,re.M)
if match: 
    model = match.group("model_number")
print()    
print(f"Serial number: {serial}")
print()
print(f"Model: {model}")
print()

