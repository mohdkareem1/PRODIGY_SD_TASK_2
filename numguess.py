import random

def main():
    print("Welcome to the Number Guessing Game!")
    print("-----------------------------------")
    
    target_number = random.randint(1, 100)  
    attempts = 0
    
    while True:
        guess = int(input("Guess a number between 1 and 100: "))
        attempts += 1
        
        if guess < target_number:
            print("Too low! Try again.")
        elif guess > target_number:
            print("Too high! Try again.")
        else:
            print(f"Congratulations! You guessed the number {target_number} correctly in {attempts} attempts.")
            break

if __name__ == "__main__":
    main()