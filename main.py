#Here is the main python file
import destinationInfo
import hotelsInfo
def main():
    while True:
        print("\n\t\t🙋🙋Welcome to Your Travel Assistant  🙋‍♀️🙋‍♀️")
        print("\t\t===Please what can I help you?===.")
        print("\n\t\t1) Choose destination")
        
        print("\t\t2) Exit")
        choice = input("\t\tPlease enter your choice: ")
        if choice == "1":
            destinationInfo.displayCityInfo()
            print("\t\t====Search for hotels by: =====")
            while True:
                print("\t\t1) City\n\t\t2) District\n\t\t3) Airport\n\t\t4) Back")
                sear_type = input("\t\tInput the search type: ")
                if sear_type == "1":
                    hotelsInfo.hotel_finder("city")
                elif sear_type =="2":
                    hotelsInfo.hotel_finder("district")
                elif sear_type == "3":
                    hotelsInfo.hotel_finder("airport")
                elif sear_type == "4":
                    break
                else:
                    print("\t\tPlease input valid choice")
                    continue

        elif choice == "2":
            break
        else:
            print("\t\tInvalid choice. Try again!")
            continue
main()

