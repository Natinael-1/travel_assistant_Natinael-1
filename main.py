#Here is the main python file
import destinationInfo
import hotelsInfo
def main():
    while True:
        print("\n\t\t🙋🙋Welcome to Your Travel Assistant  🙋‍♀️🙋‍♀️")
        print("\t\t===Please what can I help you?===.")
        print("\n\t\t1) Choose destination city\n\t\t2) Search for hotels or get details\n\t\t3) Exit")
        choice = input("\t\tPlease enter your choice: ")
        if choice == "1":
            destinationInfo.displayCityInfo()
        elif choice == "2":
            while True:
                print("\n\t\t====Search for hotels by: =====")
                print("\t\t1) City\n\t\t2) District\n\t\t3) Airport\n\t\t4) Get a hotel detail" \
                "\n\t\t5) Get room detail in hotel\n\t\t6) Back")
                sear_type = input("\t\tInput the search type(should match destination id): ")
                if sear_type == "1":
                    hotelsInfo.hotel_finder("city")
                elif sear_type =="2":
                    hotelsInfo.hotel_finder("district")
                elif sear_type == "3":
                    hotelsInfo.hotel_finder("airport")
                elif sear_type =="4":
                    hotelsInfo.get_sing_hotl()
                elif sear_type == "5":
                    hotelsInfo.get_rooms()
                elif sear_type =="6":
                    break
                else:
                    print("\t\tPlease input valid choice")
                    continue

        elif choice == "3":
            break
        else:
            print("\t\tInvalid choice. Try again!")
            continue
main()

