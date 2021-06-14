
# username password as input
username = input("What is your username? ")
password = input("What is your password? ")

# password shadow
shadow_pass = '*' * len(password)

print(f"Your username is {username} and the password {shadow_pass} is of {len(password)} long")
