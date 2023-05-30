import random
import string

def generate_password():
    characters = string.ascii_letters + string.digits + "!@#$%*?<>"
    password = [random.choice(string.ascii_lowercase),
                random.choice(string.ascii_uppercase),
                random.choice(string.digits),
                random.choice("!@#$%*?<>" + string.digits)]
    password += random.sample(characters, 4)
    random.shuffle(password)
    return ''.join(password)

# Generate a password
password = generate_password()

# Output the generated password
print("Generated Password: " + password)
