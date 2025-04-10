# Basic Python script example
def main():
    # Variable assignment
    name = "Alice"
    age = 30
    height = 165.5
    
    # List of numbers
    numbers = [12, 45, 23, 67, 89, 34]
    
    # Dictionary example
    person = {
        "name": "Bob",
        "age": 35,
        "email": "bob@example.com"
    }
    
    # Calculations
    average = sum(numbers) / len(numbers)
    max_number = max(numbers)
    
    # String formatting
    print(f"Hello {name}! You're {age} years old.")
    print(f"Your height is {height} cm\n")
    
    # List operations
    print(f"Numbers: {numbers}")
    print(f"Average: {average:.2f}")
    print(f"Maximum: {max_number}")
    
    # Dictionary access
    print("\nPerson details:")
    print(f"Name: {person['name']}")
    print(f"Age: {person['age']}")
    print(f"Email: {person['email']}")

if __name__ == "__main__":
    main()