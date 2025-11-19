#Here is the main python file
import destinationInfo
def main():
    while True:
        print("\n🙋🙋Welcome to Your Travel Assistant  🙋‍♀️🙋‍♀️")
        print("===Please choose what you want below===.")
        print("\n    1) Choose destination")
        print("      2) Exit")
        choice = input("Please enter your choice: ")
        if choice == "1":
            destinationInfo.displayCityInfo()
        elif choice == "2":
            break
        else:
            print("Invalid choice. Try again!")
            continue
main()

