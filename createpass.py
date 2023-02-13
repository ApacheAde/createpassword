import string
import random

def generate_password(length):
    """Generate a random password of specified length"""
    password = ''.join(random.choice(string.ascii_letters + string.digits + string.punctuation) for i in range(length))
    return password

def create_passwords(num_passwords, length):
    """Create multiple random passwords of specified length"""
    for i in range(num_passwords):
        password = generate_password(length)
        print("Password #{}: {}".format(i+1, password))

# Create 10 random passwords, each with a length of 20 characters
create_passwords(10, 20)
