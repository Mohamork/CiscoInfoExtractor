""" 
1. Using this show_version.txt file from a Cisco IOS-XE router, extract both the serial number and the model number. You should use regular expressions to accomplish this. These items are contained on the following lines (both the model number and serial number are underlined).
cisco C1111-4P (1RU) processor with 1401823K/6147K bytes of memory.
Processor board ID FGL222290LB


""" 
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
