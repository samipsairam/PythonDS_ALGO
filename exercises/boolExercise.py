from datetime import date

print(type(date.today().year))
birth_year = int(input("What year were you born? "))
print(f"Todays date is {date.today()}")

print(f"Your age is {date.today().year - birth_year}")

