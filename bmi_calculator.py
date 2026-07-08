#!/usr/bin/env python3
"""
BMI Calculator - A simple script to calculate Body Mass Index
and provide health category feedback based on user input.
"""

def calculate_bmi(weight, height):
    """
    Calculate BMI using the formula: BMI = weight (kg) / height (m)^2
    
    Args:
        weight (float): Weight in kilograms
        height (float): Height in meters
    
    Returns:
        float: The calculated BMI value
    """
    if height <= 0:
        raise ValueError("Height must be greater than 0")
    if weight <= 0:
        raise ValueError("Weight must be greater than 0")
    
    bmi = weight / (height ** 2)
    return bmi


def get_bmi_category(bmi):
    """
    Determine the health category based on BMI value
    
    Args:
        bmi (float): The BMI value
    
    Returns:
        str: The health category and feedback
    """
    if bmi < 18.5:
        return "Underweight", "You may need to gain weight. Consider consulting a healthcare provider."
    elif 18.5 <= bmi < 25:
        return "Normal Weight", "Great! You are at a healthy weight. Keep up the good lifestyle!"
    elif 25 <= bmi < 30:
        return "Overweight", "You may want to consider a balanced diet and regular exercise."
    else:
        return "Obese", "Please consult with a healthcare provider for personalized advice."


def main():
    """Main function to run the BMI calculator"""
    print("=" * 50)
    print("Welcome to the BMI Calculator!")
    print("=" * 50)
    
    try:
        # Get user input
        name = input("\nEnter your name: ").strip()
        
        while True:
            try:
                weight = float(input("Enter your weight (in kg): "))
                if weight <= 0:
                    print("Weight must be a positive number. Please try again.")
                    continue
                break
            except ValueError:
                print("Invalid input. Please enter a valid number for weight.")
        
        while True:
            try:
                height = float(input("Enter your height (in meters): "))
                if height <= 0:
                    print("Height must be a positive number. Please try again.")
                    continue
                break
            except ValueError:
                print("Invalid input. Please enter a valid number for height.")
        
        # Calculate BMI
        bmi = calculate_bmi(weight, height)
        category, feedback = get_bmi_category(bmi)
        
        # Display results
        print("\n" + "=" * 50)
        print(f"Hi {name}! Here are your results:")
        print("=" * 50)
        print(f"Weight: {weight} kg")
        print(f"Height: {height} m")
        print(f"BMI: {bmi:.2f}")
        print(f"Category: {category}")
        print(f"Feedback: {feedback}")
        print("=" * 50 + "\n")
        
    except KeyboardInterrupt:
        print("\n\nProgram interrupted by user. Goodbye!")
    except Exception as e:
        print(f"\nAn error occurred: {e}")


if __name__ == "__main__":
    main()
