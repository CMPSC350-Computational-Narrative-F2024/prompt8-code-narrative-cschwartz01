# Initial data representing team members' personal information
team_info = {
    "Alice": {"age": 23, "major": "Computer Science", "minor": "Mathematics"},
    "Bob": {"age": 21, "major": "Physics", "minor": "Astronomy"},
    "Charlie": {"age": 24, "major": "Biology", "minor": "Chemistry"},
    "Dana": {"age": 22, "major": "Psychology", "minor": "Philosophy"},
}

def update_team_info(team_info):
    """Allows the user to add or update personal information for team members."""
    print("=== Update Team Information ===")
    while True:
        name = input("\nEnter the team member's name (or type 'done' to finish): ").strip()
        if name.lower() == 'done':
            break
        age = input(f"Enter {name}'s age: ").strip()
        major = input(f"Enter {name}'s major: ").strip()
        minor = input(f"Enter {name}'s minor: ").strip()

        # Update the team_info dictionary
        team_info[name] = {
            "age": int(age),
            "major": major,
            "minor": minor
        }
        print(f"{name}'s information has been updated.")

def team_report(team_info):
    """Generates a report summarizing the personal information of the team members."""
    print("\n=== Team Information Report ===")
    for name, details in team_info.items():
        print(f"\nName: {name}")
        print(f"Age: {details['age']}")
        print(f"Major: {details['major']}")
        print(f"Minor: {details['minor']}")

def main():
    """Main function to initiate the program."""
    print("Welcome to the Team Information Tool!")
    update_option = input("Would you like to add or update team member information? (yes/no): ").strip().lower()
    if update_option == "yes":
        update_team_info(team_info)
    team_report(team_info)

# Run the main function
main()
