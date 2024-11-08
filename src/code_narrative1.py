# code_narrative1.py

def gather_data():
    """Simulates gathering data from multiple sources."""
    data = {
        'team_member_1': {'name': 'Alice', 'age': 21, 'major': 'Computer Science', 'minor': 'Mathematics'},
        'team_member_2': {'name': 'Bob', 'age': 22, 'major': 'Physics', 'minor': 'Philosophy'},
        'team_member_3': {'name': 'Charlie', 'age': 23, 'major': 'Biology', 'minor': 'Chemistry'}
    }
    print("Data gathered from team members.")
    return data

def process_data(data):
    """Processes the gathered data."""
    processed_data = {}
    for member, info in data.items():
        processed_data[member] = {k: (v.upper() if isinstance(v, str) else v) for k, v in info.items()}
    print("Data processed by team members.")
    return processed_data

def combine_data(processed_data):
    """Combines the processed data into a single dataset."""
    combined_data = []
    for info in processed_data.values():
        combined_data.append(info)
    print("Data combined by team members.")
    return combined_data

if __name__ == "__main__":
    def get_user_data():
        """Gets data input from the user."""
        name = input("Enter your name: ")
        age = int(input("Enter your age: "))
        major = input("Enter your college major: ")
        minor = input("Enter your college minor: ")
        user_data = {'name': name, 'age': age, 'major': major, 'minor': minor}
        return user_data

    def main():
        """Main function to orchestrate the collaboration."""
        data = gather_data()
        user_data = get_user_data()
        data['user'] = user_data
        processed_data = process_data(data)
        combined_data = combine_data(processed_data)
        print("Final combined data:", combined_data)

    if __name__ == "__main__":
        main()