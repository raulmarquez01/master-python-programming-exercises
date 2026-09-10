import re

def valid_password(password):
    if len(password) < 6 or len(password) > 12:
        return "Invalid password. Please try again"
    if not re.search(r'[a-z]', password):
        return "Invalid password. Please try again"
    if not re.search(r'[0-9]', password):
        return "Invalid password. Please try again"
    if not re.search(r'[A-Z]', password):
        return "Invalid password. Please try again"
    if not re.search(r'[$#@]', password):
        return "Invalid password. Please try again"
    return "Valid password"

print(valid_password("ABd1234@1"))
