import re
import random
import string
import hashlib
import requests

def check_password_strength(password):
    length_error=len(password)<8
    digit_error=not re.search(r"\d", password)
    uppercase_error=not re.search(r"[A-Z]", password)
    lowercase_error=not re.search(r"[a-z]", password)
    special_char_error=not re.search(r"[@]", password)

    errors={
        "Too short (minimum 8 characters)": length_error,
        "Missing a digit": digit_error,
        "Missing an uppercase letter": uppercase_error,
        "Missing a lowercase letter": lowercase_error,
        "Missing the @ symbol": special_char_error,
    }

    feedback=[key for key, value in errors.items() if value]
    strength="Strong" if not feedback else "Weak"

    return strength, feedback

def generate_password(length=12):
    if length < 8:
        raise ValueError("Password length must be at least 8 characters")

    lower=random.choice(string.ascii_lowercase)
    upper=random.choice(string.ascii_uppercase)
    digit=random.choice(string.digits)
    special="@"

    remaining_length=length-4
    all_allowed=string.ascii_letters + string.digits
    remaining=[random.choice(all_allowed) for _ in range(remaining_length)]

    password_list=[lower, upper, digit, special]+remaining
    random.shuffle(password_list)
    return ''.join(password_list)

def check_pwned_password(password):
    sha1_password=hashlib.sha1(password.encode()).hexdigest().upper()
    prefix=sha1_password[:5]
    suffix=sha1_password[5:]
    url=f"https://api.pwnedpasswords.com/range/{prefix}"
    response=requests.get(url)
    if response.status_code != 200:
        raise RuntimeError("Error fetching data from Have I Been Pwned API")
    hashes=response.text.splitlines()
    for line in hashes:
        hash_suffix, count=line.split(":")
        if hash_suffix==suffix:
            return True
    return False
