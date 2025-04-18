import math
import random
import time

def type_text(text, delay=0.04):
    for char in text:
        print(char, end="", flush=True)
        time.sleep(delay)
    print()

while True:
    def calculation_selector():
        math_list = {
            1: "Add",
            2: "Sub",
            3: "Multiply",
            4: "Divide",
            5: "Exponential",
            6: "Square",
            7: "Square Root"
        }
    
        type_text("Choose a calculation to perform:")
        for key, value in math_list.items():
            type_text(f"{key}. {value}")
    
        try:
            while True:
                call = input("\nEnter your choice (number or operation): ").strip().lower()
        
                for key, value in math_list.items():
                    if call == str(key) or call in value.lower():
                        print(f"{value} is on the list")
                        return key, value
                else:
                    print(f"{call} is not on the list")
        except Exception as e:
            type_text(e)
            
    call = calculation_selector()
    
    
    def user_input():
        try:
            while True:
                user_input1 = int(input("\nReal numbers to be calculated: "))
                user_input2 = int(input("Real numbers to be calculated: "))
                return user_input1, user_input2
        except ValueError:
            print("This is Value error")
    
    user_input1, user_input2 = user_input()
    
    def addition():
        if call[1] == "add" or call[0] == 1:
            result = user_input1 + user_input2
            type_text(f"\nThe sum of {user_input1} and {user_input2} is {result}")
            return result
    
    def subtraction():
        if call[1] == "sub" or call[0] == 2:
            result = user_input1 - user_input2
            type_text(f"\nThe subtration of {user_input1} and {user_input2} is {result}")
            return result
    
    def multiplication():
        if call[1] == "multiply" or call[0] == 3:
            result = user_input1 * user_input2
            type_text(f"\nThe multiplication of {user_input1} and {user_input2} is {result}")
            return result
    
    def division():
        if call[1] == "divide" or call[0] == 4:
            result = user_input1 / user_input2
            type_text(f"\nThe division of {user_input1} and {user_input2} is {result}")
            return result
    
    def exponential():
        if call[1] == "exponential" or call[0] == 5:
            result = user_input1 ** user_input2
            type_text(f"\nThe exponential of {user_input1} to {user_input2} is {result}")
            return result
    
    def square():
        if call[1] == "square" or call[0] == 6:
            result1 = user_input1 ** 2
            result2 = user_input2 ** 2
            type_text(f"\nThe square of {user_input1} is {result1}")
            type_text(f"\nThe square of {user_input2} is {result2}")
            return result1, result2
    
    def square_root():
        if call[1] == "square root" or call[0] == 7:
            result1 = math.sqrt(user_input1)
            result2 = math.sqrt(user_input2)
            type_text(f"\nThe square root of {user_input1} is {result1}")
            type_text(f"\nThe square root of {user_input2} is {result2}")
            return result1, result2
    
    def main():
        addition()
        subtraction()
        multiplication()
        division()
        exponential()
        square()
        square_root()
    
    if __name__ == '__main__':
        main()

    play_again_prompt = input("\nDo you want to calculate again (yes/no)\n")
    
<<<<<<< HEAD
    if play_again_prompt != "yes":
        type_text("All calculations are done")
        break
=======
    if play_again_prompt.lower() != "yes":
        type_text("All calculations are done")
        break
>>>>>>> ace0f037d99729f48fc920a055b266f70f95d83e
