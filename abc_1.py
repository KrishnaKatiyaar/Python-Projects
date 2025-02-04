import re

text = input("Enter text containing email addresses: ")
emails = re.findall(r'[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}', text)

if emails:
    print("Extracted emails:")
    for email in emails:
        print(email)
else:
    print("No valid email addresses found.")
