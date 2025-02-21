# Iver John R Monroy
# ITELEC2
# Laboratory #15 -Guided Coding Exercise:
# Variables, Literals, and Case-Sensitivity in Python (with Naming Conversations)

def main():
    total_sum = 0

    while True:
        user_input = input("Enter a number (or 'stop' to finish): ")

        if user_input.strip().lower() == "stop":
            break  

        try:

            number = float(user_input)
            total_sum += number
        except ValueError:
            print("Invalid input. Please enter a numeric value or 'stop'.")

    print("The total sum is:", total_sum)

if __name__ == "__main__":
    main()