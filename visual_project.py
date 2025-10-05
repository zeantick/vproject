import random
import string

def unit_converter():
    print("\n-- Unit Converter --")
    print("1) Temperature (C <-> F)")
    print("2) Length (m <-> km)")
    choice = input("Choose 1 or 2: ")

    if choice == "1":
        t = float(input("Enter temperature: "))
        u = input("C or F? ").upper()
        if u == "C":
            print(f"{t}°C = {(t * 9/5) + 32:.2f}°F")
        elif u == "F":
            print(f"{t}°F = {(t - 32) * 5/9:.2f}°C")
    elif choice == "2":
        val = float(input("Enter length: "))
        u = input("m or km? ").lower()
        if u == "m":
            print(f"{val} m = {val / 1000} km")
        elif u == "km":
            print(f"{val} km = {val * 1000} m")

def currency_converter():
    print("\n-- Currency Converter --")
    print("(Using fixed rates for example)")
    amount = float(input("Enter amount in EUR: "))
    print(f"{amount} EUR = {amount * 1.08:.2f} USD")
    print(f"{amount} EUR = {amount * 0.86:.2f} GBP")
    print(f"{amount} EUR = {amount * 100:.2f} RUB")

def password_generator():
    print("\n-- Password Generator --")
    length = int(input("Enter password length: "))
    characters = string.ascii_letters + string.digits + "!@#$%^&*()"
    password = "".join(random.choice(characters) for _ in range(length))
    print("Generated password:", password)

def bmi_calculator():
    print("\n-- BMI Calculator --")
    weight = float(input("Enter weight (kg): "))
    height = float(input("Enter height (m): "))
    bmi = weight / (height ** 2)
    print(f"Your BMI: {bmi:.2f}")
    if bmi < 18.5:
        print("Underweight")
    elif bmi < 25:
        print("Normal weight")
    elif bmi < 30:
        print("Overweight")
    else:
        print("Obesity")

def main():
    while True:
        print("\n==== Main Menu ====")
        print("1) Unit Converter")
        print("2) Currency Converter")
        print("3) Password Generator")
        print("4) BMI Calculator")
        print("0) Exit")
        choice = input("Choose: ")
        if choice == "1":
            unit_converter()
        elif choice == "2":
            currency_converter()
        elif choice == "3":
            password_generator()
        elif choice == "4":
            bmi_calculator()
        elif choice == "0":
            print("Bye!")
            break
        else:
            print("Invalid choice!")

if __name__ == "__main__":
    main()
