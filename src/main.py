#!/usr/bin/env python3
"""
Sample Application for GitHub Webhook Testing
This file serves as the main application for action-repo
"""

import sys
from datetime import datetime
from utils import get_current_time, validate_input
from config import APP_NAME, VERSION


def main():
    """Main application entry point"""
    print(f"Welcome to {APP_NAME} v{VERSION}")
    print(f"Application started at: {get_current_time()}")
    
    # Sample functionality
    user_input = input("Enter your name: ")
    
    if validate_input(user_input):
        greet_user(user_input)
    else:
        print("Invalid input provided")
        sys.exit(1)


def greet_user(name):
    """Greet the user with a personalized message"""
    print(f"Hello, {name}!")
    print(f"Today's date is: {datetime.now().strftime('%Y-%m-%d')}")
    
    # Demonstrate some basic operations
    calculate_example()
    
    print(f"Thank you for using {APP_NAME}!")


def calculate_example():
    """Perform sample calculations"""
    numbers = [1, 2, 3, 4, 5]
    total = sum(numbers)
    average = total / len(numbers)
    
    print(f"Sample calculation:")
    print(f"Numbers: {numbers}")
    print(f"Sum: {total}")
    print(f"Average: {average:.2f}")


def add_feature():
    """Sample function for future feature additions"""
    # This function can be expanded when testing webhook events
    print("New feature placeholder")


if __name__ == "__main__":
    main()