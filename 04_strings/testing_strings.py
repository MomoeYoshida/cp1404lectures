"""
How could you check a filename has the right extension?
How could you check that a phone number has the right area
code for Queensland ('07') at the start?
"""

file_name = input("Text file name: ")
if not file_name.endswith(".txt"):
    print("Let me stop you right there")

phone_number = input("Text phone number: ")
if not phone_number.startswith("07"):
    print("Let me stop you right there")
