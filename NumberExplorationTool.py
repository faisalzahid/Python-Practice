# Function to check if a number is prime
def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

# Main function
def number_exploration_tool():
    # Step 1: Gather input
    name = input("Enter your name: ")
    
    # Get three favorite numbers
    num1 = int(input("Enter your first favorite number: "))
    num2 = int(input("Enter your second favorite number: "))
    num3 = int(input("Enter your third favorite number: "))
    
    # Store numbers in a list
    numbers = [num1, num2, num3]
    
    # Step 2: Greet the user
    print(f"\nHello, {name}! Let's explore your favorite numbers:")
    
    # Step 3: Check even/odd and store in a list of tuples
    even_odd_list = [(num, "even" if num % 2 == 0 else "odd") for num in numbers]
    
    # Display if the numbers are even or odd
    for num, even_odd in even_odd_list:
        print(f"The number {num} is {even_odd}.")
    
    # Step 4: Calculate squares and display
    print("\nHere are your numbers and their squares:")
    for num in numbers:
        print(f"The number {num} and its square: ({num}, {num ** 2})")
    
    # Step 5: Calculate and print the sum
    total_sum = sum(numbers)
    print(f"\nAmazing! The sum of your favorite numbers is: {total_sum}")
    
    # Step 6: Check if the sum is a prime number
    if is_prime(total_sum):
        print(f"Wow, {total_sum} is a prime number!")
    else:
        print(f"{total_sum} is not a prime number.")

# Run the tool
number_exploration_tool()
