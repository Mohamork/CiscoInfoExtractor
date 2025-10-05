# CiscoInfoExtractor

A lightweight Python tool that automatically extracts the **model number** and **serial number** from Cisco IOS-XE `show version` command output using regular expressions.

## 📋 Example Input

Example snippet from `show_version.txt`: 

appxk9           None             Smart License    None
securityk9       None             Smart License    None
ipbase           ipbasek9         Smart License    ipbasek9
The current throughput level is unthrottled 
Smart Licensing Status: REGISTERED/AUTHORIZED
**cisco C1111-4P** (1RU) processor with 1401823K/6147K bytes of memory.
Processor board ID **FGL222290LB**
1 Virtual Ethernet interface
6 Gigabit Ethernet interfaces


## 🧠 What It Does

- Reads the `show version` output from a Cisco device.
- Extracts:
  - **Model number** (e.g. `C1111-4P`)
  - **Serial number** (e.g. `FGL222290LB`)
- Uses Python’s built-in `re` module (regular expressions).
- Prints results to the console in a clean, readable format.


## ⚙️ Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/Mohamork/CiscoInfoExtractor.git
   cd CiscoInfoExtractor

## 🚀 Usage 
Make sure your Cisco device’s show version output is saved in a text file (e.g. show_version.txt) and then run:
python ciscoinfoextractor.py

## Example Output 
Serial number: FGL222290LB

Model: C1111-4P

## 🧪 Project Structure
CiscoInfoExtractor/
-- ciscoinfoextractor.py
-- show_version.txt
-- README.md
-- License.md
 
## 👤 Author

Developed by Mohamed Kromah

GitHub: @Mohamork

## 🪪 License

This project is licensed under the MIT License
.
Copyright © 2025 Mohamed Kromah, Norway.
You are free to use, modify, and distribute this software, provided the original license and copyright notice are included.

