def calculate_armstrong_sum(number: int) -> int:
    total = 0
    digit_count = len(str(number))

    temp = number
    while temp > 0:
        digit = temp % 10
        total += digit ** digit_count
        temp //= 10

    return total

def start_armstrong_checker():
    user_number = int(input("Enter a number to check if it is an Armstrong number: "))

    armstrong_sum = calculate_armstrong_sum(user_number)

    if user_number == armstrong_sum:
        print(f"\n{user_number} is an Armstrong Number.\n")
    else:
        print(f"\n{user_number} is NOT an Armstrong Number.\n")

start_armstrong_checker()