generations_by_year = {
    
}

def determine_generation(year_of_birth):
    return year_of_birth

def main():
    yob = input()
    generation = determine_generation(yob)
    print(f"You were born in {yob}. That makes you: {generation}.")

if __name__ == "__main__":
    main()
