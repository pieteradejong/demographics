"""
Generations:

Gen Z: born 1997 - (including) 2012
Millennials: 1981 - (including) 1996
Gen X: 1965 - (including) 1980
Boomers: 1946 - (including) 1964
Silent Generation: 1928 - (including) 1945
"""

def determine_generation(yob):
    generation = "Undetermined"
    if not 1928 <= yob <= 2012:
        generation = "Not covered"
    
    elif 1928 < yob <= 1945:
        generation = "Silent Generation"
    elif 1946 < yob <= 1964:
        generation = "Boomers"
    elif 1964 < yob <= 1980:
        generation = "Generation X"
    elif 1981 < yob <= 1996:
        generation = "Millennials"
    elif 1996 < yob <= 2012:
        generation = "Generation Z"
    
    else:
        generation = "We're not sure"
    
    return generation

def main():
    try:
        yob_input = int(input("What is your year of birth? " ))
        generation = determine_generation(yob_input)
        print(f"That makes you part of the generation: {generation}.")
    except ValueError:
        print("Input must be a valid year number.")

if __name__ == "__main__":
    main()
