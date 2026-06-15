"""
Main file for verfication project
"""
import csv

def load_records() -> dict:
    """loads records from csv file, Returns Dict"""
    records = {}
    with open('file.csv', 'r', encoding='utf-8') as file:
        reader = csv.reader(file)
        for row in reader:
            name = row[0]
            number = row[1]
            records[name] = number
    return records

def store_record(name:str, number:int) -> None:
    """Stores names and their number, Returns None"""
    with open('file.csv', 'a', newline='', encoding='utf-8') as file:
        writer = csv.writer(file)
        writer.writerow([
            name,
            number
        ])

def show_records() -> None:
    """displays all the records in the phone book, Returns None"""
    records = load_records()
    for index, (key, value) in enumerate(records.items()):
        print("========================")
        print(f"{index+1}: {key} - {value}")

def take_user_input(string: str) -> int:
    """Takes user input and check for errors. returns int"""
    try:
        user_input = int(input(string))
    except ValueError:
        print("Enter in numbers (1,2,3)")
    except Exception:
        print("Operation unsuccessful")
    else:
        return user_input

def phone_book() -> None:
    """allows user to see and store records in a phone book, Returns None"""
    print("===== Phone Book =====")
    while True:
        print("========================")
        print("Press: 1 to Store records to the phone book")
        print("Press: 2 to View records from phone book")
        print("Press: 3 to Exit phone book")
        user_input = take_user_input("Enter your Choice: ")
        match user_input:
            case 1:
                print("========================")
                name = input("Enter Name: ")
                number = take_user_input("Enter number: ")
                if isinstance(number, int):
                    store_record(name, number)
                    print("Successfully Saved")
                print("Operation Unsuccessful")
            case 2:
                show_records()
            case 3: 
                print("========================")
                print("Thanks for using phone book")
                break

if __name__ == '__main__':
    phone_book()